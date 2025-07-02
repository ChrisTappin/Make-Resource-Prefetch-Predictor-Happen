from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RedirectData(_message.Message):
    __slots__ = ("primary_key", "last_visit_time", "redirect_endpoints")
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    LAST_VISIT_TIME_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    primary_key: str
    last_visit_time: int
    redirect_endpoints: _containers.RepeatedCompositeFieldContainer[RedirectStat]
    def __init__(self, primary_key: _Optional[str] = ..., last_visit_time: _Optional[int] = ..., redirect_endpoints: _Optional[_Iterable[_Union[RedirectStat, _Mapping]]] = ...) -> None: ...

class RedirectStat(_message.Message):
    __slots__ = ("url", "number_of_hits", "number_of_misses", "consecutive_misses", "url_scheme", "url_port")
    URL_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_HITS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_MISSES_FIELD_NUMBER: _ClassVar[int]
    CONSECUTIVE_MISSES_FIELD_NUMBER: _ClassVar[int]
    URL_SCHEME_FIELD_NUMBER: _ClassVar[int]
    URL_PORT_FIELD_NUMBER: _ClassVar[int]
    url: str
    number_of_hits: int
    number_of_misses: int
    consecutive_misses: int
    url_scheme: str
    url_port: int
    def __init__(self, url: _Optional[str] = ..., number_of_hits: _Optional[int] = ..., number_of_misses: _Optional[int] = ..., consecutive_misses: _Optional[int] = ..., url_scheme: _Optional[str] = ..., url_port: _Optional[int] = ...) -> None: ...
