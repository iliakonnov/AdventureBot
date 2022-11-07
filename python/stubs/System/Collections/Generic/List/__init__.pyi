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

    # static fields

    # properties
    @property
    def Current(self) -> T:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    # methods
    def __init__(self, list: System.Collections.Generic.List[T], ):
        ...

    def Dispose(self, ) -> None:
        ...

    def MoveNext(self, ) -> bool:
        ...

    def MoveNextRare(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

