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

    # static fields

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    def __init__(self, dictionary: System.Collections.Generic.Dictionary[TKey, TValue], ):
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.Dictionary.KeyCollection.Enumerator[TKey, TValue]:
        ...

    def CopyTo(self, array: System.Array[TKey], index: int, ) -> None:
        ...

    def Add(self, item: TKey, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: TKey, ) -> bool:
        ...

    def Remove(self, item: TKey, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[TKey]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

class ValueCollection(System.Collections.Generic.ICollection[TValue], System.Collections.Generic.IEnumerable[TValue], System.Collections.IEnumerable, System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[TValue], System.Object, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    def __init__(self, dictionary: System.Collections.Generic.Dictionary[TKey, TValue], ):
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.Dictionary.ValueCollection.Enumerator[TKey, TValue]:
        ...

    def CopyTo(self, array: System.Array[TValue], index: int, ) -> None:
        ...

    def Add(self, item: TValue, ) -> None:
        ...

    def Remove(self, item: TValue, ) -> bool:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: TValue, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[TValue]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

class Entry(System.ValueType, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        self.hashCode: int
        self.next: int
        self.key: TKey
        self.value: TValue
        ...

    # static fields

    # properties
    # methods
class Enumerator(System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.IDisposable, System.Collections.IEnumerator, System.Collections.IDictionaryEnumerator, System.ValueType, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Current(self) -> System.Collections.Generic.KeyValuePair[TKey, TValue]:
        ...

    @property
    def Current(self) -> System.Object:
        ...

    @property
    def Entry(self) -> System.Collections.DictionaryEntry:
        ...

    @property
    def Key(self) -> System.Object:
        ...

    @property
    def Value(self) -> System.Object:
        ...

    # methods
    def __init__(self, dictionary: System.Collections.Generic.Dictionary[TKey, TValue], getEnumeratorRetType: int, ):
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Dispose(self, ) -> None:
        ...

    def Reset(self, ) -> None:
        ...

