from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Collections.Generic
import System.Collections
import System
import System.Collections.Immutable.ImmutableDictionary
import System.Collections.Immutable

TKey = typing.TypeVar('TKey')
TValue = typing.TypeVar('TValue')

class Builder(System.Collections.Generic.IDictionary[TKey, TValue], System.Collections.Generic.ICollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IEnumerable, System.Collections.Generic.IReadOnlyDictionary[TKey, TValue], System.Collections.Generic.IReadOnlyCollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IDictionary, System.Collections.ICollection, System.Object, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def KeyComparer(self) -> System.Collections.Generic.IEqualityComparer[TKey]:
        ...
    @KeyComparer.setter
    def KeyComparer(self, val: System.Collections.Generic.IEqualityComparer[TKey]):
        ...

    @property
    def ValueComparer(self) -> System.Collections.Generic.IEqualityComparer[TValue]:
        ...
    @ValueComparer.setter
    def ValueComparer(self, val: System.Collections.Generic.IEqualityComparer[TValue]):
        ...

    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def Keys(self) -> System.Collections.Generic.IEnumerable[TKey]:
        ...

    @property
    def Values(self) -> System.Collections.Generic.IEnumerable[TValue]:
        ...

    @property
    def Item(self) -> TValue:
        ...
    @Item.setter
    def Item(self, val: TValue):
        ...

    # methods
    @typing.overload
    def AddRange(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], ) -> None:
        ...

    @typing.overload
    def RemoveRange(self, keys: System.Collections.Generic.IEnumerable[TKey], ) -> None:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.Immutable.ImmutableDictionary.Enumerator[TKey, TValue]:
        ...

    @typing.overload
    def GetValueOrDefault(self, key: TKey, ) -> TValue:
        ...

    @typing.overload
    def GetValueOrDefault(self, key: TKey, defaultValue: TValue, ) -> TValue:
        ...

    @typing.overload
    def ToImmutable(self, ) -> System.Collections.Immutable.ImmutableDictionary[TKey, TValue]:
        ...

    @typing.overload
    def Add(self, key: TKey, value: TValue, ) -> None:
        ...

    @typing.overload
    def ContainsKey(self, key: TKey, ) -> System.Boolean:
        ...

    @typing.overload
    def ContainsValue(self, value: TValue, ) -> System.Boolean:
        ...

    @typing.overload
    def Remove(self, key: TKey, ) -> System.Boolean:
        ...

    @typing.overload
    def TryGetValue(self, key: TKey, value: ref[TValue], ) -> System.Boolean:
        ...

    @typing.overload
    def TryGetKey(self, equalKey: TKey, actualKey: ref[TKey], ) -> System.Boolean:
        ...

    @typing.overload
    def Add(self, item: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> None:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, item: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> System.Boolean:
        ...

    @typing.overload
    def Remove(self, item: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> System.Boolean:
        ...

class Enumerator(System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.IDisposable, System.Collections.IEnumerator, System.ValueType, typing.Generic[TKey, TValue]):
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
    def Reset(self, ) -> None:
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

