from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Collections.Immutable
import System.Collections.Generic
import System.Collections
import System.Collections.Immutable.ImmutableHashSet
import System
import System.Collections.Immutable.ImmutableDictionary

T = typing.TypeVar('T')
TKey = typing.TypeVar('TKey')
TValue = typing.TypeVar('TValue')

class ImmutableHashSet(System.Collections.Immutable.IImmutableSet[T], System.Collections.Generic.IReadOnlyCollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Collections.Generic.IHashKeyCollection[T], System.Collections.Generic.ICollection[T], System.Collections.Generic.ISet[T], System.Collections.ICollection, System.Collections.Immutable.IStrongEnumerable[T, System.Collections.Immutable.ImmutableHashSet.Enumerator[T]], System.Collections.Generic.IReadOnlySet[T], System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def IsEmpty(self) -> System.Boolean:
        ...

    @property
    def KeyComparer(self) -> System.Collections.Generic.IEqualityComparer[T]:
        ...

    # methods
    @typing.overload
    def Clear(self, ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    @typing.overload
    def ToBuilder(self, ) -> System.Collections.Immutable.ImmutableHashSet.Builder[T]:
        ...

    @typing.overload
    def Add(self, item: T, ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    @typing.overload
    def Remove(self, item: T, ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    @typing.overload
    def TryGetValue(self, equalValue: T, actualValue: ref[T], ) -> System.Boolean:
        ...

    @typing.overload
    def Union(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    @typing.overload
    def Intersect(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    @typing.overload
    def Except(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    @typing.overload
    def SymmetricExcept(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    @typing.overload
    def SetEquals(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    def IsProperSubsetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    def IsProperSupersetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    def IsSubsetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    def IsSupersetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    def Overlaps(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    def Contains(self, item: T, ) -> System.Boolean:
        ...

    @typing.overload
    def WithComparer(self, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.Immutable.ImmutableHashSet.Enumerator[T]:
        ...

class ImmutableDictionary(System.Collections.Immutable.IImmutableDictionary[TKey, TValue], System.Collections.Generic.IReadOnlyDictionary[TKey, TValue], System.Collections.Generic.IReadOnlyCollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IEnumerable, System.Collections.Immutable.IImmutableDictionaryInternal[TKey, TValue], System.Collections.Generic.IHashKeyCollection[TKey], System.Collections.Generic.IDictionary[TKey, TValue], System.Collections.Generic.ICollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IDictionary, System.Collections.ICollection, System.Object, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def IsEmpty(self) -> System.Boolean:
        ...

    @property
    def KeyComparer(self) -> System.Collections.Generic.IEqualityComparer[TKey]:
        ...

    @property
    def ValueComparer(self) -> System.Collections.Generic.IEqualityComparer[TValue]:
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

    # methods
    @typing.overload
    def Clear(self, ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    @typing.overload
    def ToBuilder(self, ) -> System.Collections.Immutable.ImmutableDictionary.Builder[TKey, TValue]:
        ...

    @typing.overload
    def Add(self, key: TKey, value: TValue, ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    @typing.overload
    def AddRange(self, pairs: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    @typing.overload
    def SetItem(self, key: TKey, value: TValue, ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    @typing.overload
    def SetItems(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    @typing.overload
    def Remove(self, key: TKey, ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    @typing.overload
    def RemoveRange(self, keys: System.Collections.Generic.IEnumerable[TKey], ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    @typing.overload
    def ContainsKey(self, key: TKey, ) -> System.Boolean:
        ...

    @typing.overload
    def Contains(self, pair: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> System.Boolean:
        ...

    @typing.overload
    def TryGetValue(self, key: TKey, value: ref[TValue], ) -> System.Boolean:
        ...

    @typing.overload
    def TryGetKey(self, equalKey: TKey, actualKey: ref[TKey], ) -> System.Boolean:
        ...

    @typing.overload
    def WithComparers(self, keyComparer: System.Collections.Generic.IEqualityComparer[TKey], valueComparer: System.Collections.Generic.IEqualityComparer[TValue], ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    @typing.overload
    def WithComparers(self, keyComparer: System.Collections.Generic.IEqualityComparer[TKey], ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    @typing.overload
    def ContainsValue(self, value: TValue, ) -> System.Boolean:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.Immutable.ImmutableDictionary.Enumerator[TKey, TValue]:
        ...

class IImmutableSet(System.Collections.Generic.IReadOnlyCollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Clear(self, ) -> System.Collections.Immutable.IImmutableSet:
        ...

    @typing.overload
    @abc.abstractmethod
    def Contains(self, value: T, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def Add(self, value: T, ) -> System.Collections.Immutable.IImmutableSet:
        ...

    @typing.overload
    @abc.abstractmethod
    def Remove(self, value: T, ) -> System.Collections.Immutable.IImmutableSet:
        ...

    @typing.overload
    @abc.abstractmethod
    def TryGetValue(self, equalValue: T, actualValue: ref[T], ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def Intersect(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.IImmutableSet:
        ...

    @typing.overload
    @abc.abstractmethod
    def Except(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.IImmutableSet:
        ...

    @typing.overload
    @abc.abstractmethod
    def SymmetricExcept(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.IImmutableSet:
        ...

    @typing.overload
    @abc.abstractmethod
    def Union(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.IImmutableSet:
        ...

    @typing.overload
    @abc.abstractmethod
    def SetEquals(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def IsProperSubsetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def IsProperSupersetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def IsSubsetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def IsSupersetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def Overlaps(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

class IImmutableDictionary(System.Collections.Generic.IReadOnlyDictionary[TKey, TValue], System.Collections.Generic.IReadOnlyCollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IEnumerable, abc.ABC, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Clear(self, ) -> System.Collections.Immutable.IImmutableDictionary:
        ...

    @typing.overload
    @abc.abstractmethod
    def Add(self, key: TKey, value: TValue, ) -> System.Collections.Immutable.IImmutableDictionary:
        ...

    @typing.overload
    @abc.abstractmethod
    def AddRange(self, pairs: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], ) -> System.Collections.Immutable.IImmutableDictionary:
        ...

    @typing.overload
    @abc.abstractmethod
    def SetItem(self, key: TKey, value: TValue, ) -> System.Collections.Immutable.IImmutableDictionary:
        ...

    @typing.overload
    @abc.abstractmethod
    def SetItems(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], ) -> System.Collections.Immutable.IImmutableDictionary:
        ...

    @typing.overload
    @abc.abstractmethod
    def RemoveRange(self, keys: System.Collections.Generic.IEnumerable[TKey], ) -> System.Collections.Immutable.IImmutableDictionary:
        ...

    @typing.overload
    @abc.abstractmethod
    def Remove(self, key: TKey, ) -> System.Collections.Immutable.IImmutableDictionary:
        ...

    @typing.overload
    @abc.abstractmethod
    def Contains(self, pair: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def TryGetKey(self, equalKey: TKey, actualKey: ref[TKey], ) -> System.Boolean:
        ...

