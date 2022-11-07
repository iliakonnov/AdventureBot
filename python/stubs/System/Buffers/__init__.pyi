from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.InteropServices
import System.Buffers

T = typing.TypeVar('T')

class MemoryHandle(System.IDisposable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Pointer(self) -> ptr[None]:
        ...

    # methods
    def __init__(self, pointer: ptr[None], handle: System.Runtime.InteropServices.GCHandle = ..., pinnable: System.Buffers.IPinnable = ..., ):
        ...

    def Dispose(self, ) -> None:
        ...

class IPinnable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Pin(self, elementIndex: int, ) -> System.Buffers.MemoryHandle:
        ...

    @abc.abstractmethod
    def Unpin(self, ) -> None:
        ...

class OperationStatus(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Done: int = ...
    DestinationTooSmall: int = ...
    NeedMoreData: int = ...
    InvalidData: int = ...

class MemoryManager(System.Buffers.IMemoryOwner[T], System.IDisposable, System.Buffers.IPinnable, System.Object, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Memory(self) -> System.Memory[T]:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def GetSpan(self, ) -> System.Span[T]:
        ...

    @abc.abstractmethod
    def Pin(self, elementIndex: int = ..., ) -> System.Buffers.MemoryHandle:
        ...

    @abc.abstractmethod
    def Unpin(self, ) -> None:
        ...

    @typing.overload
    def CreateMemory(self, length: int, ) -> System.Memory[T]:
        ...

    @typing.overload
    def CreateMemory(self, start: int, length: int, ) -> System.Memory[T]:
        ...

    def TryGetArray(self, segment: ref[System.ArraySegment[T]], ) -> bool:
        ...

    def Dispose(self, ) -> None:
        ...

    @abc.abstractmethod
    def Dispose(self, disposing: bool, ) -> None:
        ...

class IMemoryOwner(System.IDisposable, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Memory(self) -> System.Memory[T]:
        ...

    # methods
