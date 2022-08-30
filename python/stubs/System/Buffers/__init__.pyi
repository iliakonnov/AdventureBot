from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.Serialization
import System.Reflection
import System.Runtime.InteropServices
import System.Buffers

T = typing.TypeVar('T')
TArg = typing.TypeVar('TArg')

class SpanAction(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T, TArg]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, span: System.Span[T], arg: TArg, ) -> None:
        ...

    @typing.overload
    def BeginInvoke(self, span: System.Span[T], arg: TArg, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class OperationStatus(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Done: System.Int32 = Done
    DestinationTooSmall: System.Int32 = DestinationTooSmall
    NeedMoreData: System.Int32 = NeedMoreData
    InvalidData: System.Int32 = InvalidData

class MemoryHandle(System.IDisposable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Pointer(self) -> ptr[None]:
        ...

    # methods
    @typing.overload
    def __init__(self, pointer: ptr[None], handle: System.Runtime.InteropServices.GCHandle, pinnable: System.Buffers.IPinnable, ):
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

class IPinnable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Pin(self, elementIndex: System.Int32, ) -> System.Buffers.MemoryHandle:
        ...

    @typing.overload
    @abc.abstractmethod
    def Unpin(self, ) -> None:
        ...

