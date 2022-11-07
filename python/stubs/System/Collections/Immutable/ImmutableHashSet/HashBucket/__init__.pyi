from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Collections.Generic
import System
import System.Collections
import System.Collections.Immutable.ImmutableHashSet

T = typing.TypeVar('T')

class Enumerator(System.Collections.Generic.IEnumerator[T], System.IDisposable, System.Collections.IEnumerator, System.ValueType, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...

    @property
    def Current(self) -> T:
        ...

    # methods
    def __init__(self, bucket: System.Collections.Immutable.ImmutableHashSet.HashBucket[T], ):
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    def ThrowIfDisposed(self, ) -> None:
        ...

