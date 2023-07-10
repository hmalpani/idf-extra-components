# SPDX-FileCopyrightText: 2022 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: Unlicense OR CC0-1.0
import http.server
import multiprocessing
import os
import socket
import ssl
from typing import Callable

import pexpect
import pytest
from pytest_embedded import Dut
from RangeHTTPServer import RangeRequestHandler

server_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'server_certs/ca_cert.pem')
key_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'server_certs/server_key.pem')
enc_bin_name = 'pre_encrypted_ota_secure.bin'


def get_my_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def https_request_handler() -> Callable[...,http.server.BaseHTTPRequestHandler]:
    """
    Returns a request handler class that handles broken pipe exception
    """
    class RequestHandler(RangeRequestHandler):
        def finish(self) -> None:
            try:
                if not self.wfile.closed:
                    self.wfile.flush()
                    self.wfile.close()
            except socket.error:
                pass
            self.rfile.close()

        def handle(self) -> None:
            try:
                RangeRequestHandler.handle(self)
            except socket.error:
                pass

    return RequestHandler


def start_https_server(ota_image_dir: str, server_ip: str, server_port: int) -> None:
    os.chdir(ota_image_dir)
    requestHandler = https_request_handler()
    httpd = http.server.HTTPServer((server_ip, server_port), requestHandler)

    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   keyfile=key_file,
                                   certfile=server_file, server_side=True)
    httpd.serve_forever()


@pytest.mark.esp32
@pytest.mark.ethernet
def test_examples_protocol_pre_encrypted_ota_example(dut: Dut) -> None:
    server_port = 8001
    host_ip = get_my_ip()
    # Start server
    thread1 = multiprocessing.Process(target=start_https_server, args=(dut.app.binary_path, host_ip, server_port))
    thread1.daemon = True
    thread1.start()
    try:
        dut.expect('Loaded app from partition at offset', timeout=30)
        try:
            ip_address = dut.expect(r'IPv4 address: (\d+\.\d+\.\d+\.\d+)[^\d]', timeout=30)[1].decode()
            print('Connected to AP/Ethernet with IP: {}'.format(ip_address))
        except pexpect.exceptions.TIMEOUT:
            raise ValueError('ENV_TEST_FAILURE: Cannot connect to AP/Ethernet')

        dut.expect('Starting Pre Encrypted OTA example', timeout=30)
        print('writing to device: {}'.format('https://' + host_ip + ':' + str(server_port) + '/' + enc_bin_name))
        dut.write('https://' + host_ip + ':' + str(server_port) + '/' + enc_bin_name)
        dut.expect('Magic Verified', timeout=30)
        dut.expect('Reading RSA private key', timeout=30)
        dut.expect('upgrade successful. Rebooting', timeout=60)
        # after reboot
        dut.expect('Loaded app from partition at offset', timeout=30)
    finally:
        thread1.terminate()