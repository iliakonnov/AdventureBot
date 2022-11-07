from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Runtime.Serialization
import System.Reflection

TKey = typing.TypeVar('TKey')
TRow = typing.TypeVar('TRow')

class ComparisonBySelector(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[TKey, TRow]):
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

    def Invoke(self, key: TKey, row: TRow, ) -> int:
        ...

