from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Collections.Immutable
import System.Collections.Generic
import System.Collections
import System.Collections.Immutable.ImmutableHashSet
import System
import System.Collections.Immutable.ImmutableDictionary
import System.Collections.Immutable.ImmutableList

T = typing.TypeVar('T')
TKey = typing.TypeVar('TKey')
TValue = typing.TypeVar('TValue')
TOutput = typing.TypeVar('TOutput')

class ImmutableHashSet(System.Collections.Immutable.IImmutableSet[T], System.Collections.Generic.IReadOnlyCollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Collections.Generic.IHashKeyCollection[T], System.Collections.Generic.ICollection[T], System.Collections.Generic.ISet[T], System.Collections.ICollection, System.Collections.Immutable.IStrongEnumerable[T, System.Collections.Immutable.ImmutableHashSet.Enumerator[T]], System.Collections.Generic.IReadOnlySet[T], System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Empty: System.Collections.Immutable.ImmutableHashSet = ...

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def IsEmpty(self) -> bool:
        ...

    @property
    def KeyComparer(self) -> System.Collections.Generic.IEqualityComparer[T]:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def Root(self) -> System.Collections.Immutable.IBinaryTree:
        ...

    @property
    def Origin(self) -> System.Collections.Immutable.ImmutableHashSet.MutationInput[T]:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ):
        ...

    @typing.overload
    def __init__(self, root: System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableHashSet.HashBucket[T]], equalityComparer: System.Collections.Generic.IEqualityComparer[T], count: int, ):
        ...

    def Clear(self, ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    def Clear(self, ) -> System.Collections.Immutable.IImmutableSet[T]:
        ...

    def ToBuilder(self, ) -> System.Collections.Immutable.ImmutableHashSet.Builder[T]:
        ...

    @typing.overload
    def Add(self, item: T, ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    @staticmethod
    @typing.overload
    def Add(item: T, origin: System.Collections.Immutable.ImmutableHashSet.MutationInput[T], ) -> System.Collections.Immutable.ImmutableHashSet.MutationResult[T]:
        ...

    @typing.overload
    def Remove(self, item: T, ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    @staticmethod
    @typing.overload
    def Remove(item: T, origin: System.Collections.Immutable.ImmutableHashSet.MutationInput[T], ) -> System.Collections.Immutable.ImmutableHashSet.MutationResult[T]:
        ...

    def TryGetValue(self, equalValue: T, actualValue: ref[T], ) -> bool:
        ...

    @typing.overload
    def Union(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    @staticmethod
    @typing.overload
    def Union(other: System.Collections.Generic.IEnumerable[T], origin: System.Collections.Immutable.ImmutableHashSet.MutationInput[T], ) -> System.Collections.Immutable.ImmutableHashSet.MutationResult[T]:
        ...

    @typing.overload
    def Union(self, items: System.Collections.Generic.IEnumerable[T], avoidWithComparer: bool, ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    @typing.overload
    def Intersect(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    @staticmethod
    @typing.overload
    def Intersect(other: System.Collections.Generic.IEnumerable[T], origin: System.Collections.Immutable.ImmutableHashSet.MutationInput[T], ) -> System.Collections.Immutable.ImmutableHashSet.MutationResult[T]:
        ...

    @typing.overload
    def Except(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    @staticmethod
    @typing.overload
    def Except(other: System.Collections.Generic.IEnumerable[T], equalityComparer: System.Collections.Generic.IEqualityComparer[T], hashBucketEqualityComparer: System.Collections.Generic.IEqualityComparer[System.Collections.Immutable.ImmutableHashSet.HashBucket[T]], root: System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableHashSet.HashBucket[T]], ) -> System.Collections.Immutable.ImmutableHashSet.MutationResult[T]:
        ...

    @typing.overload
    def SymmetricExcept(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    @staticmethod
    @typing.overload
    def SymmetricExcept(other: System.Collections.Generic.IEnumerable[T], origin: System.Collections.Immutable.ImmutableHashSet.MutationInput[T], ) -> System.Collections.Immutable.ImmutableHashSet.MutationResult[T]:
        ...

    @typing.overload
    def SetEquals(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def SetEquals(other: System.Collections.Generic.IEnumerable[T], origin: System.Collections.Immutable.ImmutableHashSet.MutationInput[T], ) -> bool:
        ...

    @typing.overload
    def IsProperSubsetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsProperSubsetOf(other: System.Collections.Generic.IEnumerable[T], origin: System.Collections.Immutable.ImmutableHashSet.MutationInput[T], ) -> bool:
        ...

    @typing.overload
    def IsProperSupersetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsProperSupersetOf(other: System.Collections.Generic.IEnumerable[T], origin: System.Collections.Immutable.ImmutableHashSet.MutationInput[T], ) -> bool:
        ...

    @typing.overload
    def IsSubsetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsSubsetOf(other: System.Collections.Generic.IEnumerable[T], origin: System.Collections.Immutable.ImmutableHashSet.MutationInput[T], ) -> bool:
        ...

    @typing.overload
    def IsSupersetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def IsSupersetOf(other: System.Collections.Generic.IEnumerable[T], origin: System.Collections.Immutable.ImmutableHashSet.MutationInput[T], ) -> bool:
        ...

    @typing.overload
    def Overlaps(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Overlaps(other: System.Collections.Generic.IEnumerable[T], origin: System.Collections.Immutable.ImmutableHashSet.MutationInput[T], ) -> bool:
        ...

    def Add(self, item: T, ) -> System.Collections.Immutable.IImmutableSet[T]:
        ...

    def Remove(self, item: T, ) -> System.Collections.Immutable.IImmutableSet[T]:
        ...

    def Union(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.IImmutableSet[T]:
        ...

    def Intersect(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.IImmutableSet[T]:
        ...

    def Except(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.IImmutableSet[T]:
        ...

    def SymmetricExcept(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.IImmutableSet[T]:
        ...

    @typing.overload
    def Contains(self, item: T, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Contains(item: T, origin: System.Collections.Immutable.ImmutableHashSet.MutationInput[T], ) -> bool:
        ...

    def WithComparer(self, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    def Add(self, item: T, ) -> bool:
        ...

    def ExceptWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    def IntersectWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    def SymmetricExceptWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    def UnionWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    def CopyTo(self, array: System.Array[T], arrayIndex: int, ) -> None:
        ...

    def Add(self, item: T, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Remove(self, item: T, ) -> bool:
        ...

    def CopyTo(self, array: System.Array, arrayIndex: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.Immutable.ImmutableHashSet.Enumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @staticmethod
    def UpdateRoot(root: System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableHashSet.HashBucket[T]], hashCode: int, hashBucketEqualityComparer: System.Collections.Generic.IEqualityComparer[System.Collections.Immutable.ImmutableHashSet.HashBucket[T]], newBucket: System.Collections.Immutable.ImmutableHashSet.HashBucket[T], ) -> System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableHashSet.HashBucket[T]]:
        ...

    @staticmethod
    @typing.overload
    def Wrap(root: System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableHashSet.HashBucket[T]], equalityComparer: System.Collections.Generic.IEqualityComparer[T], count: int, ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    @typing.overload
    def Wrap(self, root: System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableHashSet.HashBucket[T]], adjustedCountIfDifferentRoot: int, ) -> System.Collections.Immutable.ImmutableHashSet:
        ...

    @staticmethod
    def GetHashBucketEqualityComparer(valueComparer: System.Collections.Generic.IEqualityComparer[T], ) -> System.Collections.Generic.IEqualityComparer[System.Collections.Immutable.ImmutableHashSet.HashBucket[T]]:
        ...

class ImmutableDictionary(System.Collections.Immutable.IImmutableDictionary[TKey, TValue], System.Collections.Generic.IReadOnlyDictionary[TKey, TValue], System.Collections.Generic.IReadOnlyCollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IEnumerable, System.Collections.Immutable.IImmutableDictionaryInternal[TKey, TValue], System.Collections.Generic.IHashKeyCollection[TKey], System.Collections.Generic.IDictionary[TKey, TValue], System.Collections.Generic.ICollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IDictionary, System.Collections.ICollection, System.Object, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Empty: System.Collections.Immutable.ImmutableDictionary = ...

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def IsEmpty(self) -> bool:
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
    def Keys(self) -> System.Collections.Generic.ICollection[TKey]:
        ...

    @property
    def Values(self) -> System.Collections.Generic.ICollection[TValue]:
        ...

    @property
    def Origin(self) -> System.Collections.Immutable.ImmutableDictionary.MutationInput[TKey, TValue]:
        ...

    @property
    def Item(self) -> TValue:
        ...

    @property
    def Item(self) -> TValue:
        ...
    @Item.setter
    def Item(self, val: TValue):
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Keys(self) -> System.Collections.ICollection:
        ...

    @property
    def Values(self) -> System.Collections.ICollection:
        ...

    @property
    def Root(self) -> System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue]]:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, root: System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue]], comparers: System.Collections.Immutable.ImmutableDictionary.Comparers[TKey, TValue], count: int, ):
        ...

    @typing.overload
    def __init__(self, comparers: System.Collections.Immutable.ImmutableDictionary.Comparers[TKey, TValue] = ..., ):
        ...

    def Clear(self, ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    def Clear(self, ) -> System.Collections.Immutable.IImmutableDictionary[TKey, TValue]:
        ...

    def ToBuilder(self, ) -> System.Collections.Immutable.ImmutableDictionary.Builder[TKey, TValue]:
        ...

    @typing.overload
    def Add(self, key: TKey, value: TValue, ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    @staticmethod
    @typing.overload
    def Add(key: TKey, value: TValue, behavior: int, origin: System.Collections.Immutable.ImmutableDictionary.MutationInput[TKey, TValue], ) -> System.Collections.Immutable.ImmutableDictionary.MutationResult[TKey, TValue]:
        ...

    @typing.overload
    def AddRange(self, pairs: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    @staticmethod
    @typing.overload
    def AddRange(items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], origin: System.Collections.Immutable.ImmutableDictionary.MutationInput[TKey, TValue], collisionBehavior: int = ..., ) -> System.Collections.Immutable.ImmutableDictionary.MutationResult[TKey, TValue]:
        ...

    @typing.overload
    def AddRange(self, pairs: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], avoidToHashMap: bool, ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    def SetItem(self, key: TKey, value: TValue, ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    def SetItems(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    @typing.overload
    def Remove(self, key: TKey, ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    @staticmethod
    @typing.overload
    def Remove(key: TKey, origin: System.Collections.Immutable.ImmutableDictionary.MutationInput[TKey, TValue], ) -> System.Collections.Immutable.ImmutableDictionary.MutationResult[TKey, TValue]:
        ...

    def RemoveRange(self, keys: System.Collections.Generic.IEnumerable[TKey], ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    @typing.overload
    def ContainsKey(self, key: TKey, ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def ContainsKey(key: TKey, origin: System.Collections.Immutable.ImmutableDictionary.MutationInput[TKey, TValue], ) -> bool:
        ...

    @typing.overload
    def Contains(self, pair: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def Contains(keyValuePair: System.Collections.Generic.KeyValuePair[TKey, TValue], origin: System.Collections.Immutable.ImmutableDictionary.MutationInput[TKey, TValue], ) -> bool:
        ...

    @typing.overload
    def TryGetValue(self, key: TKey, value: ref[TValue], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryGetValue(key: TKey, origin: System.Collections.Immutable.ImmutableDictionary.MutationInput[TKey, TValue], value: ref[TValue], ) -> bool:
        ...

    @typing.overload
    def TryGetKey(self, equalKey: TKey, actualKey: ref[TKey], ) -> bool:
        ...

    @staticmethod
    @typing.overload
    def TryGetKey(equalKey: TKey, origin: System.Collections.Immutable.ImmutableDictionary.MutationInput[TKey, TValue], actualKey: ref[TKey], ) -> bool:
        ...

    @typing.overload
    def WithComparers(self, keyComparer: System.Collections.Generic.IEqualityComparer[TKey], valueComparer: System.Collections.Generic.IEqualityComparer[TValue], ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    @typing.overload
    def WithComparers(self, keyComparer: System.Collections.Generic.IEqualityComparer[TKey], ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    def ContainsValue(self, value: TValue, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.Immutable.ImmutableDictionary.Enumerator[TKey, TValue]:
        ...

    def Add(self, key: TKey, value: TValue, ) -> System.Collections.Immutable.IImmutableDictionary[TKey, TValue]:
        ...

    def SetItem(self, key: TKey, value: TValue, ) -> System.Collections.Immutable.IImmutableDictionary[TKey, TValue]:
        ...

    def SetItems(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], ) -> System.Collections.Immutable.IImmutableDictionary[TKey, TValue]:
        ...

    def AddRange(self, pairs: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], ) -> System.Collections.Immutable.IImmutableDictionary[TKey, TValue]:
        ...

    def RemoveRange(self, keys: System.Collections.Generic.IEnumerable[TKey], ) -> System.Collections.Immutable.IImmutableDictionary[TKey, TValue]:
        ...

    def Remove(self, key: TKey, ) -> System.Collections.Immutable.IImmutableDictionary[TKey, TValue]:
        ...

    def Add(self, key: TKey, value: TValue, ) -> None:
        ...

    def Remove(self, key: TKey, ) -> bool:
        ...

    def Add(self, item: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Remove(self, item: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> bool:
        ...

    def CopyTo(self, array: System.Array[System.Collections.Generic.KeyValuePair[TKey, TValue]], arrayIndex: int, ) -> None:
        ...

    def Add(self, key: System.Object, value: System.Object, ) -> None:
        ...

    def Contains(self, key: System.Object, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.IDictionaryEnumerator:
        ...

    def Remove(self, key: System.Object, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def CopyTo(self, array: System.Array, arrayIndex: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[TKey, TValue]]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @staticmethod
    def EmptyWithComparers(comparers: System.Collections.Immutable.ImmutableDictionary.Comparers[TKey, TValue], ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    @staticmethod
    def TryCastToImmutableMap(sequence: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], other: ref[System.Collections.Immutable.ImmutableDictionary], ) -> bool:
        ...

    @staticmethod
    def UpdateRoot(root: System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue]], hashCode: int, newBucket: System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue], hashBucketComparer: System.Collections.Generic.IEqualityComparer[System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue]], ) -> System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue]]:
        ...

    @staticmethod
    @typing.overload
    def Wrap(root: System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue]], comparers: System.Collections.Immutable.ImmutableDictionary.Comparers[TKey, TValue], count: int, ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

    @typing.overload
    def Wrap(self, root: System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue]], adjustedCountIfDifferentRoot: int, ) -> System.Collections.Immutable.ImmutableDictionary:
        ...

class IImmutableDictionary(System.Collections.Generic.IReadOnlyDictionary[TKey, TValue], System.Collections.Generic.IReadOnlyCollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IEnumerable, abc.ABC, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Clear(self, ) -> System.Collections.Immutable.IImmutableDictionary:
        ...

    @abc.abstractmethod
    def Add(self, key: TKey, value: TValue, ) -> System.Collections.Immutable.IImmutableDictionary:
        ...

    @abc.abstractmethod
    def AddRange(self, pairs: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], ) -> System.Collections.Immutable.IImmutableDictionary:
        ...

    @abc.abstractmethod
    def SetItem(self, key: TKey, value: TValue, ) -> System.Collections.Immutable.IImmutableDictionary:
        ...

    @abc.abstractmethod
    def SetItems(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], ) -> System.Collections.Immutable.IImmutableDictionary:
        ...

    @abc.abstractmethod
    def RemoveRange(self, keys: System.Collections.Generic.IEnumerable[TKey], ) -> System.Collections.Immutable.IImmutableDictionary:
        ...

    @abc.abstractmethod
    def Remove(self, key: TKey, ) -> System.Collections.Immutable.IImmutableDictionary:
        ...

    @abc.abstractmethod
    def Contains(self, pair: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> bool:
        ...

    @abc.abstractmethod
    def TryGetKey(self, equalKey: TKey, actualKey: ref[TKey], ) -> bool:
        ...

class IImmutableSet(System.Collections.Generic.IReadOnlyCollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Clear(self, ) -> System.Collections.Immutable.IImmutableSet:
        ...

    @abc.abstractmethod
    def Contains(self, value: T, ) -> bool:
        ...

    @abc.abstractmethod
    def Add(self, value: T, ) -> System.Collections.Immutable.IImmutableSet:
        ...

    @abc.abstractmethod
    def Remove(self, value: T, ) -> System.Collections.Immutable.IImmutableSet:
        ...

    @abc.abstractmethod
    def TryGetValue(self, equalValue: T, actualValue: ref[T], ) -> bool:
        ...

    @abc.abstractmethod
    def Intersect(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.IImmutableSet:
        ...

    @abc.abstractmethod
    def Except(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.IImmutableSet:
        ...

    @abc.abstractmethod
    def SymmetricExcept(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.IImmutableSet:
        ...

    @abc.abstractmethod
    def Union(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.IImmutableSet:
        ...

    @abc.abstractmethod
    def SetEquals(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    @abc.abstractmethod
    def IsProperSubsetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    @abc.abstractmethod
    def IsProperSupersetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    @abc.abstractmethod
    def IsSubsetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    @abc.abstractmethod
    def IsSupersetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    @abc.abstractmethod
    def Overlaps(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

class ImmutableList(System.Collections.Immutable.IImmutableList[T], System.Collections.Generic.IReadOnlyList[T], System.Collections.Generic.IReadOnlyCollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Collections.Generic.IList[T], System.Collections.Generic.ICollection[T], System.Collections.IList, System.Collections.ICollection, System.Collections.Immutable.IOrderedCollection[T], System.Collections.Immutable.IImmutableListQueries[T], System.Collections.Immutable.IStrongEnumerable[T, System.Collections.Immutable.ImmutableList.Enumerator[T]], System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Empty: System.Collections.Immutable.ImmutableList = ...

    # properties
    @property
    def IsEmpty(self) -> bool:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def Item(self) -> T:
        ...

    @property
    def Item(self) -> T:
        ...

    @property
    def Item(self) -> T:
        ...
    @Item.setter
    def Item(self, val: T):
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Root(self) -> System.Collections.Immutable.ImmutableList.Node[T]:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, root: System.Collections.Immutable.ImmutableList.Node[T], ):
        ...

    def GetEnumerator(self, ) -> System.Collections.Immutable.ImmutableList.Enumerator[T]:
        ...

    @staticmethod
    def WrapNode(root: System.Collections.Immutable.ImmutableList.Node[T], ) -> System.Collections.Immutable.ImmutableList:
        ...

    @staticmethod
    def TryCastToImmutableList(sequence: System.Collections.Generic.IEnumerable[T], other: ref[System.Collections.Immutable.ImmutableList], ) -> bool:
        ...

    @staticmethod
    def IsCompatibleObject(value: System.Object, ) -> bool:
        ...

    def Wrap(self, root: System.Collections.Immutable.ImmutableList.Node[T], ) -> System.Collections.Immutable.ImmutableList:
        ...

    @staticmethod
    def CreateRange(items: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.ImmutableList:
        ...

    def Clear(self, ) -> System.Collections.Immutable.ImmutableList:
        ...

    @typing.overload
    def BinarySearch(self, item: T, ) -> int:
        ...

    @typing.overload
    def BinarySearch(self, item: T, comparer: System.Collections.Generic.IComparer[T], ) -> int:
        ...

    @typing.overload
    def BinarySearch(self, index: int, count: int, item: T, comparer: System.Collections.Generic.IComparer[T], ) -> int:
        ...

    def Clear(self, ) -> System.Collections.Immutable.IImmutableList[T]:
        ...

    def ItemRef(self, index: int, ) -> ref[T]:
        ...

    def ToBuilder(self, ) -> System.Collections.Immutable.ImmutableList.Builder[T]:
        ...

    def Add(self, value: T, ) -> System.Collections.Immutable.ImmutableList:
        ...

    def AddRange(self, items: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.ImmutableList:
        ...

    def Insert(self, index: int, item: T, ) -> System.Collections.Immutable.ImmutableList:
        ...

    def InsertRange(self, index: int, items: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.ImmutableList:
        ...

    @typing.overload
    def Remove(self, value: T, ) -> System.Collections.Immutable.ImmutableList:
        ...

    @typing.overload
    def Remove(self, value: T, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> System.Collections.Immutable.ImmutableList:
        ...

    @typing.overload
    def RemoveRange(self, index: int, count: int, ) -> System.Collections.Immutable.ImmutableList:
        ...

    @typing.overload
    def RemoveRange(self, items: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.ImmutableList:
        ...

    @typing.overload
    def RemoveRange(self, items: System.Collections.Generic.IEnumerable[T], equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> System.Collections.Immutable.ImmutableList:
        ...

    def RemoveAt(self, index: int, ) -> System.Collections.Immutable.ImmutableList:
        ...

    def RemoveAll(self, match: System.Predicate[T], ) -> System.Collections.Immutable.ImmutableList:
        ...

    def SetItem(self, index: int, value: T, ) -> System.Collections.Immutable.ImmutableList:
        ...

    @typing.overload
    def Replace(self, oldValue: T, newValue: T, ) -> System.Collections.Immutable.ImmutableList:
        ...

    @typing.overload
    def Replace(self, oldValue: T, newValue: T, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> System.Collections.Immutable.ImmutableList:
        ...

    @typing.overload
    def Reverse(self, ) -> System.Collections.Immutable.ImmutableList:
        ...

    @typing.overload
    def Reverse(self, index: int, count: int, ) -> System.Collections.Immutable.ImmutableList:
        ...

    @typing.overload
    def Sort(self, ) -> System.Collections.Immutable.ImmutableList:
        ...

    @typing.overload
    def Sort(self, comparison: System.Comparison[T], ) -> System.Collections.Immutable.ImmutableList:
        ...

    @typing.overload
    def Sort(self, comparer: System.Collections.Generic.IComparer[T], ) -> System.Collections.Immutable.ImmutableList:
        ...

    @typing.overload
    def Sort(self, index: int, count: int, comparer: System.Collections.Generic.IComparer[T], ) -> System.Collections.Immutable.ImmutableList:
        ...

    def ForEach(self, action: System.Action[T], ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[T], ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[T], arrayIndex: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, index: int, array: System.Array[T], arrayIndex: int, count: int, ) -> None:
        ...

    def GetRange(self, index: int, count: int, ) -> System.Collections.Immutable.ImmutableList:
        ...

    def ConvertAll(self, converter: System.Func[T, TOutput], ) -> System.Collections.Immutable.ImmutableList[TOutput]:
        ...

    def Exists(self, match: System.Predicate[T], ) -> bool:
        ...

    def Find(self, match: System.Predicate[T], ) -> T:
        ...

    def FindAll(self, match: System.Predicate[T], ) -> System.Collections.Immutable.ImmutableList:
        ...

    @typing.overload
    def FindIndex(self, match: System.Predicate[T], ) -> int:
        ...

    @typing.overload
    def FindIndex(self, startIndex: int, match: System.Predicate[T], ) -> int:
        ...

    @typing.overload
    def FindIndex(self, startIndex: int, count: int, match: System.Predicate[T], ) -> int:
        ...

    def FindLast(self, match: System.Predicate[T], ) -> T:
        ...

    @typing.overload
    def FindLastIndex(self, match: System.Predicate[T], ) -> int:
        ...

    @typing.overload
    def FindLastIndex(self, startIndex: int, match: System.Predicate[T], ) -> int:
        ...

    @typing.overload
    def FindLastIndex(self, startIndex: int, count: int, match: System.Predicate[T], ) -> int:
        ...

    @typing.overload
    def IndexOf(self, item: T, index: int, count: int, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> int:
        ...

    @typing.overload
    def IndexOf(self, value: T, ) -> int:
        ...

    def LastIndexOf(self, item: T, index: int, count: int, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> int:
        ...

    def TrueForAll(self, match: System.Predicate[T], ) -> bool:
        ...

    def Contains(self, value: T, ) -> bool:
        ...

    def Add(self, value: T, ) -> System.Collections.Immutable.IImmutableList[T]:
        ...

    def AddRange(self, items: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.IImmutableList[T]:
        ...

    def Insert(self, index: int, item: T, ) -> System.Collections.Immutable.IImmutableList[T]:
        ...

    def InsertRange(self, index: int, items: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.IImmutableList[T]:
        ...

    def Remove(self, value: T, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> System.Collections.Immutable.IImmutableList[T]:
        ...

    def RemoveAll(self, match: System.Predicate[T], ) -> System.Collections.Immutable.IImmutableList[T]:
        ...

    @typing.overload
    def RemoveRange(self, items: System.Collections.Generic.IEnumerable[T], equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> System.Collections.Immutable.IImmutableList[T]:
        ...

    @typing.overload
    def RemoveRange(self, index: int, count: int, ) -> System.Collections.Immutable.IImmutableList[T]:
        ...

    def RemoveAt(self, index: int, ) -> System.Collections.Immutable.IImmutableList[T]:
        ...

    def SetItem(self, index: int, value: T, ) -> System.Collections.Immutable.IImmutableList[T]:
        ...

    def Replace(self, oldValue: T, newValue: T, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> System.Collections.Immutable.IImmutableList[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Insert(self, index: int, item: T, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def Add(self, item: T, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Remove(self, item: T, ) -> bool:
        ...

    def CopyTo(self, array: System.Array, arrayIndex: int, ) -> None:
        ...

    def Add(self, value: System.Object, ) -> int:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, value: System.Object, ) -> bool:
        ...

    def IndexOf(self, value: System.Object, ) -> int:
        ...

    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    def Remove(self, value: System.Object, ) -> None:
        ...

class IImmutableList(System.Collections.Generic.IReadOnlyList[T], System.Collections.Generic.IReadOnlyCollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Clear(self, ) -> System.Collections.Immutable.IImmutableList:
        ...

    @abc.abstractmethod
    def IndexOf(self, item: T, index: int, count: int, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> int:
        ...

    @abc.abstractmethod
    def LastIndexOf(self, item: T, index: int, count: int, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> int:
        ...

    @abc.abstractmethod
    def Add(self, value: T, ) -> System.Collections.Immutable.IImmutableList:
        ...

    @abc.abstractmethod
    def AddRange(self, items: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.IImmutableList:
        ...

    @abc.abstractmethod
    def Insert(self, index: int, element: T, ) -> System.Collections.Immutable.IImmutableList:
        ...

    @abc.abstractmethod
    def InsertRange(self, index: int, items: System.Collections.Generic.IEnumerable[T], ) -> System.Collections.Immutable.IImmutableList:
        ...

    @abc.abstractmethod
    def Remove(self, value: T, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> System.Collections.Immutable.IImmutableList:
        ...

    @abc.abstractmethod
    def RemoveAll(self, match: System.Predicate[T], ) -> System.Collections.Immutable.IImmutableList:
        ...

    @abc.abstractmethod
    @typing.overload
    def RemoveRange(self, items: System.Collections.Generic.IEnumerable[T], equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> System.Collections.Immutable.IImmutableList:
        ...

    @abc.abstractmethod
    @typing.overload
    def RemoveRange(self, index: int, count: int, ) -> System.Collections.Immutable.IImmutableList:
        ...

    @abc.abstractmethod
    def RemoveAt(self, index: int, ) -> System.Collections.Immutable.IImmutableList:
        ...

    @abc.abstractmethod
    def SetItem(self, index: int, value: T, ) -> System.Collections.Immutable.IImmutableList:
        ...

    @abc.abstractmethod
    def Replace(self, oldValue: T, newValue: T, equalityComparer: System.Collections.Generic.IEqualityComparer[T], ) -> System.Collections.Immutable.IImmutableList:
        ...

