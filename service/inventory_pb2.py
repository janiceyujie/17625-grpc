# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventory.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finventory.proto\"\x88\x01\n\x04\x42ook\x12\x0c\n\x04ISBN\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x17\n\x0fpublishing_year\x18\x04 \x01(\x05\":\n\x05Genre\x12\x0b\n\x07\x46ICTION\x10\x00\x12\x0b\n\x07MYSTERY\x10\x01\x12\x0b\n\x07HISTORY\x10\x02\x12\n\n\x06POETRY\x10\x03\"n\n\rInventoryItem\x12\x15\n\rinventory_num\x18\x01 \x01(\x05\x12\x15\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x05.BookH\x00\"\"\n\x06Status\x12\r\n\tAVAILABLE\x10\x00\x12\t\n\x05TAKEN\x10\x01\x42\x0b\n\titem_typeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventory_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOK._serialized_start=20
  _BOOK._serialized_end=156
  _BOOK_GENRE._serialized_start=98
  _BOOK_GENRE._serialized_end=156
  _INVENTORYITEM._serialized_start=158
  _INVENTORYITEM._serialized_end=268
  _INVENTORYITEM_STATUS._serialized_start=221
  _INVENTORYITEM_STATUS._serialized_end=255
# @@protoc_insertion_point(module_scope)
