# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: network_ctrl.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import constants_pb2 as constants__pb2
import network_constants_pb2 as network__constants__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12network_ctrl.proto\x1a\x0f\x63onstants.proto\x1a\x17network_constants.proto\".\n\x0c\x43mdCtrlReset\x12\x1e\n\x08net_type\x18\x01 \x01(\x0e\x32\x0c.NetworkType\"/\n\rRespCtrlReset\x12\x1e\n\x08net_type\x18\x01 \x01(\x0e\x32\x0c.NetworkType\"/\n\rCmdCtrlReprov\x12\x1e\n\x08net_type\x18\x01 \x01(\x0e\x32\x0c.NetworkType\"0\n\x0eRespCtrlReprov\x12\x1e\n\x08net_type\x18\x01 \x01(\x0e\x32\x0c.NetworkType\"\x86\x02\n\x12NetworkCtrlPayload\x12 \n\x03msg\x18\x01 \x01(\x0e\x32\x13.NetworkCtrlMsgType\x12\x17\n\x06status\x18\x02 \x01(\x0e\x32\x07.Status\x12\'\n\x0e\x63md_ctrl_reset\x18\x0b \x01(\x0b\x32\r.CmdCtrlResetH\x00\x12)\n\x0fresp_ctrl_reset\x18\x0c \x01(\x0b\x32\x0e.RespCtrlResetH\x00\x12)\n\x0f\x63md_ctrl_reprov\x18\r \x01(\x0b\x32\x0e.CmdCtrlReprovH\x00\x12+\n\x10resp_ctrl_reprov\x18\x0e \x01(\x0b\x32\x0f.RespCtrlReprovH\x00\x42\t\n\x07payload*\x86\x01\n\x12NetworkCtrlMsgType\x12\x14\n\x10TypeCtrlReserved\x10\x00\x12\x14\n\x10TypeCmdCtrlReset\x10\x01\x12\x15\n\x11TypeRespCtrlReset\x10\x02\x12\x15\n\x11TypeCmdCtrlReprov\x10\x03\x12\x16\n\x12TypeRespCtrlReprov\x10\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'network_ctrl_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NETWORKCTRLMSGTYPE._serialized_start=526
  _NETWORKCTRLMSGTYPE._serialized_end=660
  _CMDCTRLRESET._serialized_start=64
  _CMDCTRLRESET._serialized_end=110
  _RESPCTRLRESET._serialized_start=112
  _RESPCTRLRESET._serialized_end=159
  _CMDCTRLREPROV._serialized_start=161
  _CMDCTRLREPROV._serialized_end=208
  _RESPCTRLREPROV._serialized_start=210
  _RESPCTRLREPROV._serialized_end=258
  _NETWORKCTRLPAYLOAD._serialized_start=261
  _NETWORKCTRLPAYLOAD._serialized_end=523
# @@protoc_insertion_point(module_scope)
