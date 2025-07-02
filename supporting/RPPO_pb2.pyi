from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OriginData(_message.Message):
    __slots__ = ("host", "last_visit_time", "origins")
    HOST_FIELD_NUMBER: _ClassVar[int]
    LAST_VISIT_TIME_FIELD_NUMBER: _ClassVar[int]
    ORIGINS_FIELD_NUMBER: _ClassVar[int]
    host: str
    last_visit_time: int
    origins: _containers.RepeatedCompositeFieldContainer[OriginStat]
    def __init__(self, host: _Optional[str] = ..., last_visit_time: _Optional[int] = ..., origins: _Optional[_Iterable[_Union[OriginStat, _Mapping]]] = ...) -> None: ...

class OriginStat(_message.Message):
    __slots__ = ("origin", "number_of_hits", "number_of_misses", "consecutive_misses", "average_position", "always_access_network", "accessed_network")
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_HITS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_MISSES_FIELD_NUMBER: _ClassVar[int]
    CONSECUTIVE_MISSES_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_POSITION_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACCESS_NETWORK_FIELD_NUMBER: _ClassVar[int]
    ACCESSED_NETWORK_FIELD_NUMBER: _ClassVar[int]
    origin: str
    number_of_hits: int
    number_of_misses: int
    consecutive_misses: int
    average_position: float
    always_access_network: bool
    accessed_network: bool
    def __init__(self, origin: _Optional[str] = ..., number_of_hits: _Optional[int] = ..., number_of_misses: _Optional[int] = ..., consecutive_misses: _Optional[int] = ..., average_position: _Optional[float] = ..., always_access_network: bool = ..., accessed_network: bool = ...) -> None: ...
