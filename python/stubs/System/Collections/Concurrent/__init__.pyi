from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Collections.Generic
import System.Collections
import System
import System.Collections.Concurrent.ConcurrentDictionary
import System.Collections.ObjectModel

TKey = typing.TypeVar('TKey')
TValue = typing.TypeVar('TValue')
TArg = typing.TypeVar('TArg')

class ConcurrentDictionary(System.Collections.Generic.IDictionary[TKey, TValue], System.Collections.Generic.ICollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IEnumerable, System.Collections.IDictionary, System.Collections.ICollection, System.Collections.Generic.IReadOnlyDictionary[TKey, TValue], System.Collections.Generic.IReadOnlyCollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Object, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Item(self) -> TValue:
        ...
    @Item.setter
    def Item(self, val: TValue):
        ...

    @property
    def Comparer(self) -> System.Collections.Generic.IEqualityComparer[TKey]:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsEmpty(self) -> bool:
        ...

    @property
    def Keys(self) -> System.Collections.Generic.ICollection[TKey]:
        ...

    @property
    def Keys(self) -> System.Collections.Generic.IEnumerable[TKey]:
        ...

    @property
    def Values(self) -> System.Collections.Generic.ICollection[TValue]:
        ...

    @property
    def Values(self) -> System.Collections.Generic.IEnumerable[TValue]:
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
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def DefaultConcurrencyLevel(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, concurrencyLevel: int, capacity: int, ):
        ...

    @typing.overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], ):
        ...

    @typing.overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[TKey], ):
        ...

    @typing.overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], comparer: System.Collections.Generic.IEqualityComparer[TKey], ):
        ...

    @typing.overload
    def __init__(self, concurrencyLevel: int, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], comparer: System.Collections.Generic.IEqualityComparer[TKey], ):
        ...

    @typing.overload
    def __init__(self, concurrencyLevel: int, capacity: int, comparer: System.Collections.Generic.IEqualityComparer[TKey], ):
        ...

    @typing.overload
    def __init__(self, concurrencyLevel: int, capacity: int, growLockArray: bool, comparer: System.Collections.Generic.IEqualityComparer[TKey], ):
        ...

    @staticmethod
    def IsValueWriteAtomic() -> bool:
        ...

    def InitializeFromCollection(self, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], ) -> None:
        ...

    def TryAdd(self, key: TKey, value: TValue, ) -> bool:
        ...

    def ContainsKey(self, key: TKey, ) -> bool:
        ...

    @typing.overload
    def TryRemove(self, key: TKey, value: ref[TValue], ) -> bool:
        ...

    @typing.overload
    def TryRemove(self, item: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> bool:
        ...

    def TryRemoveInternal(self, key: TKey, value: ref[TValue], matchValue: bool, oldValue: TValue, ) -> bool:
        ...

    def TryGetValue(self, key: TKey, value: ref[TValue], ) -> bool:
        ...

    def TryGetValueInternal(self, key: TKey, hashcode: int, value: ref[TValue], ) -> bool:
        ...

    def TryUpdate(self, key: TKey, newValue: TValue, comparisonValue: TValue, ) -> bool:
        ...

    def TryUpdateInternal(self, key: TKey, nullableHashcode: System.Nullable[int], newValue: TValue, comparisonValue: TValue, ) -> bool:
        ...

    def Clear(self, ) -> None:
        ...

    def CopyTo(self, array: System.Array[System.Collections.Generic.KeyValuePair[TKey, TValue]], index: int, ) -> None:
        ...

    def ToArray(self, ) -> System.Array[System.Collections.Generic.KeyValuePair[TKey, TValue]]:
        ...

    def CopyToPairs(self, array: System.Array[System.Collections.Generic.KeyValuePair[TKey, TValue]], index: int, ) -> None:
        ...

    def CopyToEntries(self, array: System.Array[System.Collections.DictionaryEntry], index: int, ) -> None:
        ...

    def CopyToObjects(self, array: System.Array[System.Object], index: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[TKey, TValue]]:
        ...

    def TryAddInternal(self, key: TKey, nullableHashcode: System.Nullable[int], value: TValue, updateIfExists: bool, acquireLock: bool, resultingValue: ref[TValue], ) -> bool:
        ...

    @staticmethod
    def ThrowKeyNotFoundException(key: TKey, ) -> None:
        ...

    def GetCountInternal(self, ) -> int:
        ...

    @typing.overload
    def GetOrAdd(self, key: TKey, valueFactory: System.Func[TKey, TValue], ) -> TValue:
        ...

    @typing.overload
    def GetOrAdd(self, key: TKey, valueFactory: System.Func[TKey, TArg, TValue], factoryArgument: TArg, ) -> TValue:
        ...

    @typing.overload
    def GetOrAdd(self, key: TKey, value: TValue, ) -> TValue:
        ...

    @typing.overload
    def AddOrUpdate(self, key: TKey, addValueFactory: System.Func[TKey, TArg, TValue], updateValueFactory: System.Func[TKey, TValue, TArg, TValue], factoryArgument: TArg, ) -> TValue:
        ...

    @typing.overload
    def AddOrUpdate(self, key: TKey, addValueFactory: System.Func[TKey, TValue], updateValueFactory: System.Func[TKey, TValue, TValue], ) -> TValue:
        ...

    @typing.overload
    def AddOrUpdate(self, key: TKey, addValue: TValue, updateValueFactory: System.Func[TKey, TValue, TValue], ) -> TValue:
        ...

    def Add(self, key: TKey, value: TValue, ) -> None:
        ...

    def Remove(self, key: TKey, ) -> bool:
        ...

    def Add(self, keyValuePair: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> None:
        ...

    def Contains(self, keyValuePair: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> bool:
        ...

    def Remove(self, keyValuePair: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Add(self, key: System.Object, value: System.Object, ) -> None:
        ...

    def Contains(self, key: System.Object, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.IDictionaryEnumerator:
        ...

    def Remove(self, key: System.Object, ) -> None:
        ...

    @staticmethod
    def ThrowIfInvalidObjectValue(value: System.Object, ) -> None:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def AreAllBucketsEmpty(self, ) -> bool:
        ...

    def GrowTable(self, tables: System.Collections.Concurrent.ConcurrentDictionary.Tables[TKey, TValue], ) -> None:
        ...

    def AcquireAllLocks(self, locksAcquired: ref[int], ) -> None:
        ...

    def AcquireLocks(self, fromInclusive: int, toExclusive: int, locksAcquired: ref[int], ) -> None:
        ...

    def ReleaseLocks(self, fromInclusive: int, toExclusive: int, ) -> None:
        ...

    def GetKeys(self, ) -> System.Collections.ObjectModel.ReadOnlyCollection[TKey]:
        ...

    def GetValues(self, ) -> System.Collections.ObjectModel.ReadOnlyCollection[TValue]:
        ...

