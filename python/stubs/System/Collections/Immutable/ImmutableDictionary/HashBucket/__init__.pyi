from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Collections.Generic
import System
import System.Collections
import System.Collections.Immutable.ImmutableDictionary

TKey = typing.TypeVar('TKey')
TValue = typing.TypeVar('TValue')

class Enumerator(System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.IDisposable, System.Collections.IEnumerator, System.ValueType, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Object:
        ...

    @property
    def Current(self) -> System.Collections.Generic.KeyValuePair[TKey, TValue]:
        ...

    # methods
    def __init__(self, bucket: System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue], ):
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

