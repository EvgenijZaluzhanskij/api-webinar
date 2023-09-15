from google.api import annotations_pb2 as _annotations_pb2
from google.api import http_pb2 as _http_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUsersRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetUsersResponse(_message.Message):
    __slots__ = ["users"]
    class User(_message.Message):
        __slots__ = ["user_id", "user_name"]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        user_id: int
        user_name: str
        def __init__(self, user_id: _Optional[int] = ..., user_name: _Optional[str] = ...) -> None: ...
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[GetUsersResponse.User]
    def __init__(self, users: _Optional[_Iterable[_Union[GetUsersResponse.User, _Mapping]]] = ...) -> None: ...
