from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.Serialization
import System.Reflection
import System.Collections.Generic

T = typing.TypeVar('T')

class HandleUnicodeError(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: System.Object
        self._methodBase: System.Object
        self._methodPtr: System.IntPtr
        self._methodPtrAux: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    def Invoke(self, data: ref[System.ReadOnlySpan[T]], start: int, end: int, reason: str, ) -> None:
        ...

    def BeginInvoke(self, data: ref[System.ReadOnlySpan[T]], start: int, end: int, reason: str, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, data: ref[System.ReadOnlySpan[T]], result: System.IAsyncResult, ) -> None:
        ...

class ParseBytesErrorHandler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: System.Object
        self._methodBase: System.Object
        self._methodPtr: System.IntPtr
        self._methodPtrAux: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    def Invoke(self, data: ref[System.ReadOnlySpan[T]], start: int, end: int, reason: str, ) -> System.Collections.Generic.IReadOnlyList[int]:
        ...

    def BeginInvoke(self, data: ref[System.ReadOnlySpan[T]], start: int, end: int, reason: str, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, data: ref[System.ReadOnlySpan[T]], result: System.IAsyncResult, ) -> System.Collections.Generic.IReadOnlyList[int]:
        ...

class ParseStringErrorHandler(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: System.Object
        self._methodBase: System.Object
        self._methodPtr: System.IntPtr
        self._methodPtrAux: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    def Invoke(self, data: ref[System.ReadOnlySpan[T]], start: int, end: int, reason: str, ) -> System.Collections.Generic.IReadOnlyList[str]:
        ...

    def BeginInvoke(self, data: ref[System.ReadOnlySpan[T]], start: int, end: int, reason: str, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, data: ref[System.ReadOnlySpan[T]], result: System.IAsyncResult, ) -> System.Collections.Generic.IReadOnlyList[str]:
        ...

