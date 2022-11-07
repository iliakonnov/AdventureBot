from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Collections.Generic
import System.Collections
import System
import System.Collections.Immutable.ImmutableDictionary
import System.Collections.Immutable
import System.Collections.Immutable.ImmutableList
import System.Collections.Immutable.ImmutableDictionary.HashBucket

TKey = typing.TypeVar('TKey')
TValue = typing.TypeVar('TValue')

class Builder(System.Collections.Generic.IDictionary[TKey, TValue], System.Collections.Generic.ICollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IEnumerable, System.Collections.Generic.IReadOnlyDictionary[TKey, TValue], System.Collections.Generic.IReadOnlyCollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IDictionary, System.Collections.ICollection, System.Object, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

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
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Keys(self) -> System.Collections.Generic.IEnumerable[TKey]:
        ...

    @property
    def Keys(self) -> System.Collections.Generic.ICollection[TKey]:
        ...

    @property
    def Values(self) -> System.Collections.Generic.IEnumerable[TValue]:
        ...

    @property
    def Values(self) -> System.Collections.Generic.ICollection[TValue]:
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
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def Version(self) -> int:
        ...

    @property
    def Origin(self) -> System.Collections.Immutable.ImmutableDictionary.MutationInput[TKey, TValue]:
        ...

    @property
    def Root(self) -> System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue]]:
        ...
    @Root.setter
    def Root(self, val: System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue]]):
        ...

    @property
    def Item(self) -> TValue:
        ...
    @Item.setter
    def Item(self, val: TValue):
        ...

    # methods
    def __init__(self, map: System.Collections.Immutable.ImmutableDictionary[TKey, TValue], ):
        ...

    def Add(self, key: System.Object, value: System.Object, ) -> None:
        ...

    def Contains(self, key: System.Object, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.IDictionaryEnumerator:
        ...

    def Remove(self, key: System.Object, ) -> None:
        ...

    def CopyTo(self, array: System.Array, arrayIndex: int, ) -> None:
        ...

    def AddRange(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], ) -> None:
        ...

    def RemoveRange(self, keys: System.Collections.Generic.IEnumerable[TKey], ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.Immutable.ImmutableDictionary.Enumerator[TKey, TValue]:
        ...

    @typing.overload
    def GetValueOrDefault(self, key: TKey, ) -> TValue:
        ...

    @typing.overload
    def GetValueOrDefault(self, key: TKey, defaultValue: TValue, ) -> TValue:
        ...

    def ToImmutable(self, ) -> System.Collections.Immutable.ImmutableDictionary[TKey, TValue]:
        ...

    @typing.overload
    def Add(self, key: TKey, value: TValue, ) -> None:
        ...

    @typing.overload
    def Add(self, item: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> None:
        ...

    def ContainsKey(self, key: TKey, ) -> bool:
        ...

    def ContainsValue(self, value: TValue, ) -> bool:
        ...

    @typing.overload
    def Remove(self, key: TKey, ) -> bool:
        ...

    @typing.overload
    def Remove(self, item: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> bool:
        ...

    def TryGetValue(self, key: TKey, value: ref[TValue], ) -> bool:
        ...

    def TryGetKey(self, equalKey: TKey, actualKey: ref[TKey], ) -> bool:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> bool:
        ...

    def CopyTo(self, array: System.Array[System.Collections.Generic.KeyValuePair[TKey, TValue]], arrayIndex: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[TKey, TValue]]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Apply(self, result: System.Collections.Immutable.ImmutableDictionary.MutationResult[TKey, TValue], ) -> bool:
        ...

class MutationInput(System.ValueType, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Root(self) -> System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue]]:
        ...

    @property
    def Comparers(self) -> System.Collections.Immutable.ImmutableDictionary.Comparers[TKey, TValue]:
        ...

    @property
    def KeyComparer(self) -> System.Collections.Generic.IEqualityComparer[TKey]:
        ...

    @property
    def KeyOnlyComparer(self) -> System.Collections.Generic.IEqualityComparer[System.Collections.Generic.KeyValuePair[TKey, TValue]]:
        ...

    @property
    def ValueComparer(self) -> System.Collections.Generic.IEqualityComparer[TValue]:
        ...

    @property
    def HashBucketComparer(self) -> System.Collections.Generic.IEqualityComparer[System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue]]:
        ...

    # methods
    @typing.overload
    def __init__(self, root: System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue]], comparers: System.Collections.Immutable.ImmutableDictionary.Comparers[TKey, TValue], ):
        ...

    @typing.overload
    def __init__(self, map: System.Collections.Immutable.ImmutableDictionary[TKey, TValue], ):
        ...

class Comparers(System.Collections.Generic.IEqualityComparer[System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue]], System.Collections.Generic.IEqualityComparer[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Object, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Default: System.Collections.Immutable.ImmutableDictionary.Comparers = ...

    # properties
    @property
    def KeyComparer(self) -> System.Collections.Generic.IEqualityComparer[TKey]:
        ...

    @property
    def KeyOnlyComparer(self) -> System.Collections.Generic.IEqualityComparer[System.Collections.Generic.KeyValuePair[TKey, TValue]]:
        ...

    @property
    def ValueComparer(self) -> System.Collections.Generic.IEqualityComparer[TValue]:
        ...

    @property
    def HashBucketEqualityComparer(self) -> System.Collections.Generic.IEqualityComparer[System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue]]:
        ...

    # methods
    def __init__(self, keyComparer: System.Collections.Generic.IEqualityComparer[TKey], valueComparer: System.Collections.Generic.IEqualityComparer[TValue], ):
        ...

    def Equals(self, x: System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue], y: System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue], ) -> bool:
        ...

    def GetHashCode(self, obj: System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue], ) -> int:
        ...

    def Equals(self, x: System.Collections.Generic.KeyValuePair[TKey, TValue], y: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> bool:
        ...

    def GetHashCode(self, obj: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> int:
        ...

    @staticmethod
    def Get(keyComparer: System.Collections.Generic.IEqualityComparer[TKey], valueComparer: System.Collections.Generic.IEqualityComparer[TValue], ) -> System.Collections.Immutable.ImmutableDictionary.Comparers:
        ...

    def WithValueComparer(self, valueComparer: System.Collections.Generic.IEqualityComparer[TValue], ) -> System.Collections.Immutable.ImmutableDictionary.Comparers:
        ...

class Enumerator(System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.IDisposable, System.Collections.IEnumerator, System.ValueType, typing.Generic[TKey, TValue]):
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

    # methods
    def __init__(self, root: System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue]], builder: System.Collections.Immutable.ImmutableDictionary.Builder[TKey, TValue] = ..., ):
        ...

    def MoveNext(self, ) -> bool:
        ...

    def Reset(self, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

    def ThrowIfChanged(self, ) -> None:
        ...

class HashBucket(System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IEnumerable, System.ValueType, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def IsEmpty(self) -> bool:
        ...

    @property
    def FirstValue(self) -> System.Collections.Generic.KeyValuePair[TKey, TValue]:
        ...

    @property
    def AdditionalElements(self) -> System.Collections.Immutable.ImmutableList.Node[System.Collections.Generic.KeyValuePair[TKey, TValue]]:
        ...

    # methods
    def __init__(self, firstElement: System.Collections.Generic.KeyValuePair[TKey, TValue], additionalElements: System.Collections.Immutable.ImmutableList.Node[System.Collections.Generic.KeyValuePair[TKey, TValue]] = ..., ):
        ...

    def GetEnumerator(self, ) -> System.Collections.Immutable.ImmutableDictionary.HashBucket.Enumerator[TKey, TValue]:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[TKey, TValue]]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def Add(self, key: TKey, value: TValue, keyOnlyComparer: System.Collections.Generic.IEqualityComparer[System.Collections.Generic.KeyValuePair[TKey, TValue]], valueComparer: System.Collections.Generic.IEqualityComparer[TValue], behavior: int, result: ref[int], ) -> System.Collections.Immutable.ImmutableDictionary.HashBucket:
        ...

    def Remove(self, key: TKey, keyOnlyComparer: System.Collections.Generic.IEqualityComparer[System.Collections.Generic.KeyValuePair[TKey, TValue]], result: ref[int], ) -> System.Collections.Immutable.ImmutableDictionary.HashBucket:
        ...

    def TryGetValue(self, key: TKey, comparers: System.Collections.Immutable.ImmutableDictionary.Comparers[TKey, TValue], value: ref[TValue], ) -> bool:
        ...

    def TryGetKey(self, equalKey: TKey, comparers: System.Collections.Immutable.ImmutableDictionary.Comparers[TKey, TValue], actualKey: ref[TKey], ) -> bool:
        ...

    def Freeze(self, ) -> None:
        ...

class OperationResult(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum, typing.Generic[TKey, TValue]):
    AppliedWithoutSizeChange: int = ...
    SizeChanged: int = ...
    NoChangeRequired: int = ...

class KeyCollisionBehavior(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum, typing.Generic[TKey, TValue]):
    SetValue: int = ...
    Skip: int = ...
    ThrowIfValueDifferent: int = ...
    ThrowAlways: int = ...

class MutationResult(System.ValueType, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Root(self) -> System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue]]:
        ...

    @property
    def CountAdjustment(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, unchangedInput: System.Collections.Immutable.ImmutableDictionary.MutationInput[TKey, TValue], ):
        ...

    @typing.overload
    def __init__(self, root: System.Collections.Immutable.SortedInt32KeyNode[System.Collections.Immutable.ImmutableDictionary.HashBucket[TKey, TValue]], countAdjustment: int, ):
        ...

    def Finalize(self, priorMap: System.Collections.Immutable.ImmutableDictionary[TKey, TValue], ) -> System.Collections.Immutable.ImmutableDictionary[TKey, TValue]:
        ...

