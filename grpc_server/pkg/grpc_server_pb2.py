# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_server.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import http_pb2 as google_dot_api_dot_http__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11grpc_server.proto\x12\x0bgrpc_server\x1a\x1cgoogle/api/annotations.proto\x1a\x15google/api/http.proto\"\x11\n\x0fGetUsersRequest\"\x8c\x01\n\x10GetUsersResponse\x12\x38\n\x05users\x18\x01 \x03(\x0b\x32\".grpc_server.GetUsersResponse.UserR\x05users\x1a>\n\x04User\x12\x18\n\x07user_id\x18\x01 \x01(\x03R\x07user_id\x12\x1c\n\tuser_name\x18\x02 \x01(\tR\tuser_name2r\n\x10MyAwesomeService\x12^\n\x08GetUsers\x12\x1c.grpc_server.GetUsersRequest\x1a\x1d.grpc_server.GetUsersResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\n/api/users:\x01*b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_server_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MYAWESOMESERVICE.methods_by_name['GetUsers']._options = None
  _MYAWESOMESERVICE.methods_by_name['GetUsers']._serialized_options = b'\202\323\344\223\002\017\022\n/api/users:\001*'
  _globals['_GETUSERSREQUEST']._serialized_start=87
  _globals['_GETUSERSREQUEST']._serialized_end=104
  _globals['_GETUSERSRESPONSE']._serialized_start=107
  _globals['_GETUSERSRESPONSE']._serialized_end=247
  _globals['_GETUSERSRESPONSE_USER']._serialized_start=185
  _globals['_GETUSERSRESPONSE_USER']._serialized_end=247
  _globals['_MYAWESOMESERVICE']._serialized_start=249
  _globals['_MYAWESOMESERVICE']._serialized_end=363
# @@protoc_insertion_point(module_scope)