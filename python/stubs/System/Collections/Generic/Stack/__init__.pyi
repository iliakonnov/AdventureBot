from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Collections.Generic
import System
import System.Collections

T = typing.TypeVar('T')

class Enumerator(System.Collections.Generic.IEnumerator[T], System.IDisposable, System.Collections.IEnumerator, System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Current(self) -> T:
        ...

    # methods
    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def MoveNext(self, ) -> System.Boolean:
        ...

