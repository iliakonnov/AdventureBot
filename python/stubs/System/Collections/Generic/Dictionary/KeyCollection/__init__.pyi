from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Collections.Generic
import System
import System.Collections

TKey = typing.TypeVar('TKey')
TValue = typing.TypeVar('TValue')

class Enumerator(System.Collections.Generic.IEnumerator[TKey], System.IDisposable, System.Collections.IEnumerator, System.ValueType, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> TKey:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, dictionary: System.Collections.Generic.Dictionary[TKey, TValue], ):
        ...

    def Dispose(self, ) -> None:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

