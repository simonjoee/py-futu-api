# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Common.proto',
  package='Common',
  syntax='proto2',
  serialized_pb=_b('\n\x0c\x43ommon.proto\x12\x06\x43ommon\",\n\x08PacketID\x12\x0e\n\x06\x63onnID\x18\x01 \x02(\x04\x12\x10\n\x08serialNo\x18\x02 \x02(\r*w\n\x07RetType\x12\x13\n\x0fRetType_Succeed\x10\x00\x12\x1b\n\x0eRetType_Failed\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1c\n\x0fRetType_TimeOut\x10\x9c\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1c\n\x0fRetType_Unknown\x10\xf0\xfc\xff\xff\xff\xff\xff\xff\xff\x01*\x83\x01\n\rPacketEncAlgo\x12\x1b\n\x17PacketEncAlgo_FTAES_ECB\x10\x00\x12\x1f\n\x12PacketEncAlgo_None\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x19\n\x15PacketEncAlgo_AES_ECB\x10\x01\x12\x19\n\x15PacketEncAlgo_AES_CBC\x10\x02')
)

_RETTYPE = _descriptor.EnumDescriptor(
  name='RetType',
  full_name='Common.RetType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RetType_Succeed', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RetType_Failed', index=1, number=-1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RetType_TimeOut', index=2, number=-100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RetType_Unknown', index=3, number=-400,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=70,
  serialized_end=189,
)
_sym_db.RegisterEnumDescriptor(_RETTYPE)

RetType = enum_type_wrapper.EnumTypeWrapper(_RETTYPE)
_PACKETENCALGO = _descriptor.EnumDescriptor(
  name='PacketEncAlgo',
  full_name='Common.PacketEncAlgo',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PacketEncAlgo_FTAES_ECB', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PacketEncAlgo_None', index=1, number=-1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PacketEncAlgo_AES_ECB', index=2, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PacketEncAlgo_AES_CBC', index=3, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=192,
  serialized_end=323,
)
_sym_db.RegisterEnumDescriptor(_PACKETENCALGO)

PacketEncAlgo = enum_type_wrapper.EnumTypeWrapper(_PACKETENCALGO)
RetType_Succeed = 0
RetType_Failed = -1
RetType_TimeOut = -100
RetType_Unknown = -400
PacketEncAlgo_FTAES_ECB = 0
PacketEncAlgo_None = -1
PacketEncAlgo_AES_ECB = 1
PacketEncAlgo_AES_CBC = 2



_PACKETID = _descriptor.Descriptor(
  name='PacketID',
  full_name='Common.PacketID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connID', full_name='Common.PacketID.connID', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialNo', full_name='Common.PacketID.serialNo', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=68,
)

DESCRIPTOR.message_types_by_name['PacketID'] = _PACKETID
DESCRIPTOR.enum_types_by_name['RetType'] = _RETTYPE
DESCRIPTOR.enum_types_by_name['PacketEncAlgo'] = _PACKETENCALGO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PacketID = _reflection.GeneratedProtocolMessageType('PacketID', (_message.Message,), dict(
  DESCRIPTOR = _PACKETID,
  __module__ = 'Common_pb2'
  # @@protoc_insertion_point(class_scope:Common.PacketID)
  ))
_sym_db.RegisterMessage(PacketID)


# @@protoc_insertion_point(module_scope)
