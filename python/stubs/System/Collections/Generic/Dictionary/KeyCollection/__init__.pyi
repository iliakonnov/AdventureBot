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

    # properties
    @property
    def Current(self) -> TKey:
        ...

    # methods
    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def MoveNext(self, ) -> System.Boolean:
        ...

