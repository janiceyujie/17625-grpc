# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/InventoryService.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import inventory_pb2 as protos_dot_inventory__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dprotos/InventoryService.proto\x12\x02\x41\x33\x1a\x16protos/inventory.proto\",\n\x0b\x63reateReply\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1e\n\x0egetBookRequest\x12\x0c\n\x04ISBN\x18\x01 \x01(\t\"E\n\x0cgetBookReply\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x16\n\x04\x62ook\x18\x03 \x01(\x0b\x32\x08.A3.Book2p\n\x10InventoryService\x12)\n\nCreateBook\x12\x08.A3.Book\x1a\x0f.A3.createReply\"\x00\x12\x31\n\x07GetBook\x12\x12.A3.getBookRequest\x1a\x10.A3.getBookReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.InventoryService_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEREPLY._serialized_start=61
  _CREATEREPLY._serialized_end=105
  _GETBOOKREQUEST._serialized_start=107
  _GETBOOKREQUEST._serialized_end=137
  _GETBOOKREPLY._serialized_start=139
  _GETBOOKREPLY._serialized_end=208
  _INVENTORYSERVICE._serialized_start=210
  _INVENTORYSERVICE._serialized_end=322
# @@protoc_insertion_point(module_scope)