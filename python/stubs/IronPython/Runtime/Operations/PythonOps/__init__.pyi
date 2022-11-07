from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.Serialization
import System.Reflection

T = typing.TypeVar('T')

class MultiplySequenceWorker(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T]):
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

    def Invoke(self, self: T, count: int, ) -> T:
        ...

    def BeginInvoke(self, self: T, count: int, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> T:
        ...

