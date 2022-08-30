from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Collections.Generic
import System.Collections
import System
import System.Collections.Generic.Dictionary.KeyCollection
import System.Collections.Generic.Dictionary.ValueCollection

TKey = typing.TypeVar('TKey')
TValue = typing.TypeVar('TValue')

class KeyCollection(System.Collections.Generic.ICollection[TKey], System.Collections.Generic.IEnumerable[TKey], System.Collections.IEnumerable, System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[TKey], System.Object, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def __init__(self, dictionary: System.Collections.Generic.Dictionary[TKey, TValue], ):
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.Generic.Dictionary.KeyCollection.Enumerator[TKey, TValue]:
        ...

    @typing.overload
    def CopyTo(self, array: list[TKey], index: System.Int32, ) -> None:
        ...

class ValueCollection(System.Collections.Generic.ICollection[TValue], System.Collections.Generic.IEnumerable[TValue], System.Collections.IEnumerable, System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[TValue], System.Object, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def __init__(self, dictionary: System.Collections.Generic.Dictionary[TKey, TValue], ):
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.Generic.Dictionary.ValueCollection.Enumerator[TKey, TValue]:
        ...

    @typing.overload
    def CopyTo(self, array: list[TValue], index: System.Int32, ) -> None:
        ...

class Enumerator(System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.IDisposable, System.Collections.IEnumerator, System.Collections.IDictionaryEnumerator, System.ValueType, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Current(self) -> System.Collections.Generic.KeyValuePair[TKey, TValue]:
        ...

    # methods
    @typing.overload
    def MoveNext(self, ) -> System.Boolean:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

