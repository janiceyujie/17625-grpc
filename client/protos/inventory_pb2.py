# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/inventory.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16protos/inventory.proto\x12\x02\x41\x33\"f\n\x04\x42ook\x12\x0c\n\x04ISBN\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x18\n\x05genre\x18\x04 \x01(\x0e\x32\t.A3.Genre\x12\x17\n\x0fpublishing_year\x18\x05 \x01(\x05\"i\n\rInventoryItem\x12\x15\n\rinventory_num\x18\x01 \x01(\x05\x12\x18\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x08.A3.BookH\x00\x12\x1a\n\x06status\x18\x03 \x01(\x0e\x32\n.A3.StatusB\x0b\n\titem_type*:\n\x05Genre\x12\x0b\n\x07\x46ICTION\x10\x00\x12\x0b\n\x07MYSTERY\x10\x01\x12\x0b\n\x07HISTORY\x10\x02\x12\n\n\x06POETRY\x10\x03*\"\n\x06Status\x12\r\n\tAVAILABLE\x10\x00\x12\t\n\x05TAKEN\x10\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.inventory_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GENRE._serialized_start=241
  _GENRE._serialized_end=299
  _STATUS._serialized_start=301
  _STATUS._serialized_end=335
  _BOOK._serialized_start=30
  _BOOK._serialized_end=132
  _INVENTORYITEM._serialized_start=134
  _INVENTORYITEM._serialized_end=239
# @@protoc_insertion_point(module_scope)
