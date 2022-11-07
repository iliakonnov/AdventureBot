from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Collections.Generic
import System.Collections
import System
import System.Collections.Generic.Stack
import System.Collections.ObjectModel
import System.Collections.Generic.List
import System.Collections.Generic.Queue
import System.Runtime.Serialization
import System.Collections.Generic.HashSet
import System.Collections.Generic.Dictionary

T = typing.TypeVar('T')
TOutput = typing.TypeVar('TOutput')
TKey = typing.TypeVar('TKey')
TValue = typing.TypeVar('TValue')

class IEqualityComparer(abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Equals(self, x: T, y: T, ) -> bool:
        ...

    @abc.abstractmethod
    def GetHashCode(self, obj: T, ) -> int:
        ...

class ISet(System.Collections.Generic.ICollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Add(self, item: T, ) -> bool:
        ...

    @abc.abstractmethod
    def UnionWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    @abc.abstractmethod
    def IntersectWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    @abc.abstractmethod
    def ExceptWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    @abc.abstractmethod
    def SymmetricExceptWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    @abc.abstractmethod
    def IsSubsetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    @abc.abstractmethod
    def IsSupersetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    @abc.abstractmethod
    def IsProperSupersetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    @abc.abstractmethod
    def IsProperSubsetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    @abc.abstractmethod
    def Overlaps(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    @abc.abstractmethod
    def SetEquals(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

class IReadOnlySet(System.Collections.Generic.IReadOnlyCollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Contains(self, item: T, ) -> bool:
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

    @abc.abstractmethod
    def SetEquals(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

class IReadOnlyCollection(System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Count(self) -> int:
        ...

    # methods
class ICollection(System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Count(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def IsReadOnly(self) -> bool:
        ...

    # methods
    @abc.abstractmethod
    def Add(self, item: T, ) -> None:
        ...

    @abc.abstractmethod
    def Clear(self, ) -> None:
        ...

    @abc.abstractmethod
    def Contains(self, item: T, ) -> bool:
        ...

    @abc.abstractmethod
    def CopyTo(self, array: System.Array[T], arrayIndex: int, ) -> None:
        ...

    @abc.abstractmethod
    def Remove(self, item: T, ) -> bool:
        ...

class Stack(System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[T], System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, capacity: int, ):
        ...

    @typing.overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[T], ):
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: T, ) -> bool:
        ...

    def CopyTo(self, array: System.Array[T], arrayIndex: int, ) -> None:
        ...

    def CopyTo(self, array: System.Array, arrayIndex: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.Stack.Enumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def TrimExcess(self, ) -> None:
        ...

    def Peek(self, ) -> T:
        ...

    def TryPeek(self, result: ref[T], ) -> bool:
        ...

    def Pop(self, ) -> T:
        ...

    def TryPop(self, result: ref[T], ) -> bool:
        ...

    def Push(self, item: T, ) -> None:
        ...

    def PushWithResize(self, item: T, ) -> None:
        ...

    def EnsureCapacity(self, capacity: int, ) -> int:
        ...

    def Grow(self, capacity: int, ) -> None:
        ...

    def ToArray(self, ) -> System.Array[T]:
        ...

    def ThrowForEmptyStack(self, ) -> None:
        ...

class List(System.Collections.Generic.IList[T], System.Collections.Generic.ICollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Collections.IList, System.Collections.ICollection, System.Collections.Generic.IReadOnlyList[T], System.Collections.Generic.IReadOnlyCollection[T], System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self._items: System.Array[T]
        self._size: int
        ...

    # static fields

    # properties
    @property
    def Capacity(self) -> int:
        ...
    @Capacity.setter
    def Capacity(self, val: int):
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def IsReadOnly(self) -> bool:
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

    @property
    def Item(self) -> T:
        ...
    @Item.setter
    def Item(self, val: T):
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, capacity: int, ):
        ...

    @typing.overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[T], ):
        ...

    @staticmethod
    def IsCompatibleObject(value: System.Object, ) -> bool:
        ...

    def Add(self, item: T, ) -> None:
        ...

    def AddWithResize(self, item: T, ) -> None:
        ...

    def Add(self, item: System.Object, ) -> int:
        ...

    def AddRange(self, collection: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    def AsReadOnly(self, ) -> System.Collections.ObjectModel.ReadOnlyCollection[T]:
        ...

    @typing.overload
    def BinarySearch(self, index: int, count: int, item: T, comparer: System.Collections.Generic.IComparer[T], ) -> int:
        ...

    @typing.overload
    def BinarySearch(self, item: T, ) -> int:
        ...

    @typing.overload
    def BinarySearch(self, item: T, comparer: System.Collections.Generic.IComparer[T], ) -> int:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: T, ) -> bool:
        ...

    def Contains(self, item: System.Object, ) -> bool:
        ...

    def ConvertAll(self, converter: System.Converter[T, TOutput], ) -> System.Collections.Generic.List[TOutput]:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[T], ) -> None:
        ...

    @typing.overload
    def CopyTo(self, index: int, array: System.Array[T], arrayIndex: int, count: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[T], arrayIndex: int, ) -> None:
        ...

    def CopyTo(self, array: System.Array, arrayIndex: int, ) -> None:
        ...

    def EnsureCapacity(self, capacity: int, ) -> int:
        ...

    def Grow(self, capacity: int, ) -> None:
        ...

    def Exists(self, match: System.Predicate[T], ) -> bool:
        ...

    def Find(self, match: System.Predicate[T], ) -> T:
        ...

    def FindAll(self, match: System.Predicate[T], ) -> System.Collections.Generic.List:
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

    def ForEach(self, action: System.Action[T], ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.List.Enumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetRange(self, index: int, count: int, ) -> System.Collections.Generic.List:
        ...

    @typing.overload
    def IndexOf(self, item: T, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, item: T, index: int, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, item: T, index: int, count: int, ) -> int:
        ...

    def IndexOf(self, item: System.Object, ) -> int:
        ...

    def Insert(self, index: int, item: T, ) -> None:
        ...

    def Insert(self, index: int, item: System.Object, ) -> None:
        ...

    def InsertRange(self, index: int, collection: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    @typing.overload
    def LastIndexOf(self, item: T, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, item: T, index: int, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, item: T, index: int, count: int, ) -> int:
        ...

    def Remove(self, item: T, ) -> bool:
        ...

    def Remove(self, item: System.Object, ) -> None:
        ...

    def RemoveAll(self, match: System.Predicate[T], ) -> int:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def RemoveRange(self, index: int, count: int, ) -> None:
        ...

    @typing.overload
    def Reverse(self, ) -> None:
        ...

    @typing.overload
    def Reverse(self, index: int, count: int, ) -> None:
        ...

    @typing.overload
    def Sort(self, ) -> None:
        ...

    @typing.overload
    def Sort(self, comparer: System.Collections.Generic.IComparer[T], ) -> None:
        ...

    @typing.overload
    def Sort(self, index: int, count: int, comparer: System.Collections.Generic.IComparer[T], ) -> None:
        ...

    @typing.overload
    def Sort(self, comparison: System.Comparison[T], ) -> None:
        ...

    def ToArray(self, ) -> System.Array[T]:
        ...

    def TrimExcess(self, ) -> None:
        ...

    def TrueForAll(self, match: System.Predicate[T], ) -> bool:
        ...

class IComparer(abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Compare(self, x: T, y: T, ) -> int:
        ...

class IList(System.Collections.Generic.ICollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Item(self) -> T:
        ...
    @Item.setter
    @abc.abstractmethod
    def Item(self, val: T):
        ...

    # methods
    @abc.abstractmethod
    def IndexOf(self, item: T, ) -> int:
        ...

    @abc.abstractmethod
    def Insert(self, index: int, item: T, ) -> None:
        ...

    @abc.abstractmethod
    def RemoveAt(self, index: int, ) -> None:
        ...

class Queue(System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[T], System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Count(self) -> int:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, capacity: int, ):
        ...

    @typing.overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[T], ):
        ...

    def Clear(self, ) -> None:
        ...

    def CopyTo(self, array: System.Array[T], arrayIndex: int, ) -> None:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def Enqueue(self, item: T, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.Queue.Enumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Dequeue(self, ) -> T:
        ...

    def TryDequeue(self, result: ref[T], ) -> bool:
        ...

    def Peek(self, ) -> T:
        ...

    def TryPeek(self, result: ref[T], ) -> bool:
        ...

    def Contains(self, item: T, ) -> bool:
        ...

    def ToArray(self, ) -> System.Array[T]:
        ...

    def SetCapacity(self, capacity: int, ) -> None:
        ...

    def MoveNext(self, index: ref[int], ) -> None:
        ...

    def ThrowForEmptyQueue(self, ) -> None:
        ...

    def TrimExcess(self, ) -> None:
        ...

    def EnsureCapacity(self, capacity: int, ) -> int:
        ...

    def Grow(self, capacity: int, ) -> None:
        ...

class KeyValuePair(System.ValueType, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Key(self) -> TKey:
        ...

    @property
    def Value(self) -> TValue:
        ...

    # methods
    def __init__(self, key: TKey, value: TValue, ):
        ...

    def ToString(self, ) -> str:
        ...

    def Deconstruct(self, key: ref[TKey], value: ref[TValue], ) -> None:
        ...

class HashSet(System.Collections.Generic.ICollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Collections.Generic.ISet[T], System.Collections.Generic.IReadOnlyCollection[T], System.Collections.Generic.IReadOnlySet[T], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, System.Object, typing.Generic[T]):
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
    def Comparer(self) -> System.Collections.Generic.IEqualityComparer[T]:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[T], ):
        ...

    @typing.overload
    def __init__(self, capacity: int, ):
        ...

    @typing.overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[T], ):
        ...

    @typing.overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[T], comparer: System.Collections.Generic.IEqualityComparer[T], ):
        ...

    @typing.overload
    def __init__(self, capacity: int, comparer: System.Collections.Generic.IEqualityComparer[T], ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def ConstructFrom(self, source: System.Collections.Generic.HashSet, ) -> None:
        ...

    def Add(self, item: T, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: T, ) -> bool:
        ...

    def FindItemIndex(self, item: T, ) -> int:
        ...

    def GetBucketRef(self, hashCode: int, ) -> ref[int]:
        ...

    def Remove(self, item: T, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.HashSet.Enumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[T]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def OnDeserialization(self, sender: System.Object, ) -> None:
        ...

    def Add(self, item: T, ) -> bool:
        ...

    def TryGetValue(self, equalValue: T, actualValue: ref[T], ) -> bool:
        ...

    def UnionWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    def IntersectWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    def ExceptWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    def SymmetricExceptWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    def IsSubsetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    def IsProperSubsetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    def IsSupersetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    def IsProperSupersetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    def Overlaps(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    def SetEquals(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[T], ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[T], arrayIndex: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array[T], arrayIndex: int, count: int, ) -> None:
        ...

    def RemoveWhere(self, match: System.Predicate[T], ) -> int:
        ...

    def EnsureCapacity(self, capacity: int, ) -> int:
        ...

    @typing.overload
    def Resize(self, ) -> None:
        ...

    @typing.overload
    def Resize(self, newSize: int, forceNewHashCodes: bool, ) -> None:
        ...

    def TrimExcess(self, ) -> None:
        ...

    @staticmethod
    def CreateSetComparer() -> System.Collections.Generic.IEqualityComparer[System.Collections.Generic.HashSet]:
        ...

    def Initialize(self, capacity: int, ) -> int:
        ...

    def AddIfNotPresent(self, value: T, location: ref[int], ) -> bool:
        ...

    def ContainsAllElements(self, other: System.Collections.Generic.IEnumerable[T], ) -> bool:
        ...

    def IsSubsetOfHashSetWithSameComparer(self, other: System.Collections.Generic.HashSet, ) -> bool:
        ...

    def IntersectWithHashSetWithSameComparer(self, other: System.Collections.Generic.HashSet, ) -> None:
        ...

    def IntersectWithEnumerable(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    def SymmetricExceptWithUniqueHashSet(self, other: System.Collections.Generic.HashSet, ) -> None:
        ...

    def SymmetricExceptWithEnumerable(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    def CheckUniqueAndUnfoundElements(self, other: System.Collections.Generic.IEnumerable[T], returnIfUnfound: bool, ) -> System.ValueTuple[int, int]:
        ...

    @staticmethod
    def EqualityComparersAreEqual(set1: System.Collections.Generic.HashSet, set2: System.Collections.Generic.HashSet, ) -> bool:
        ...

class IReadOnlyList(System.Collections.Generic.IReadOnlyCollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Item(self) -> T:
        ...

    # methods
class IDictionary(System.Collections.Generic.ICollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IEnumerable, abc.ABC, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Item(self) -> TValue:
        ...
    @Item.setter
    @abc.abstractmethod
    def Item(self, val: TValue):
        ...

    @property
    @abc.abstractmethod
    def Keys(self) -> System.Collections.Generic.ICollection[TKey]:
        ...

    @property
    @abc.abstractmethod
    def Values(self) -> System.Collections.Generic.ICollection[TValue]:
        ...

    # methods
    @abc.abstractmethod
    def ContainsKey(self, key: TKey, ) -> bool:
        ...

    @abc.abstractmethod
    def Add(self, key: TKey, value: TValue, ) -> None:
        ...

    @abc.abstractmethod
    def Remove(self, key: TKey, ) -> bool:
        ...

    @abc.abstractmethod
    def TryGetValue(self, key: TKey, value: ref[TValue], ) -> bool:
        ...

class IReadOnlyDictionary(System.Collections.Generic.IReadOnlyCollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IEnumerable, abc.ABC, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Item(self) -> TValue:
        ...

    @property
    @abc.abstractmethod
    def Keys(self) -> System.Collections.Generic.IEnumerable[TKey]:
        ...

    @property
    @abc.abstractmethod
    def Values(self) -> System.Collections.Generic.IEnumerable[TValue]:
        ...

    # methods
    @abc.abstractmethod
    def ContainsKey(self, key: TKey, ) -> bool:
        ...

    @abc.abstractmethod
    def TryGetValue(self, key: TKey, value: ref[TValue], ) -> bool:
        ...

class IEnumerator(System.IDisposable, System.Collections.IEnumerator, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Current(self) -> T:
        ...

    # methods
class IEnumerable(System.Collections.IEnumerable, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[T]:
        ...

class Dictionary(System.Collections.Generic.IDictionary[TKey, TValue], System.Collections.Generic.ICollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IEnumerable, System.Collections.IDictionary, System.Collections.ICollection, System.Collections.Generic.IReadOnlyDictionary[TKey, TValue], System.Collections.Generic.IReadOnlyCollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, System.Object, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Comparer(self) -> System.Collections.Generic.IEqualityComparer[TKey]:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def Keys(self) -> System.Collections.Generic.Dictionary.KeyCollection[TKey, TValue]:
        ...

    @property
    def Keys(self) -> System.Collections.Generic.ICollection[TKey]:
        ...

    @property
    def Keys(self) -> System.Collections.Generic.IEnumerable[TKey]:
        ...

    @property
    def Values(self) -> System.Collections.Generic.Dictionary.ValueCollection[TKey, TValue]:
        ...

    @property
    def Values(self) -> System.Collections.Generic.ICollection[TValue]:
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

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
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

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, capacity: int, ):
        ...

    @typing.overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[TKey], ):
        ...

    @typing.overload
    def __init__(self, capacity: int, comparer: System.Collections.Generic.IEqualityComparer[TKey], ):
        ...

    @typing.overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[TKey, TValue], ):
        ...

    @typing.overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[TKey, TValue], comparer: System.Collections.Generic.IEqualityComparer[TKey], ):
        ...

    @typing.overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], ):
        ...

    @typing.overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], comparer: System.Collections.Generic.IEqualityComparer[TKey], ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def AddRange(self, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], ) -> None:
        ...

    def Add(self, key: TKey, value: TValue, ) -> None:
        ...

    def Add(self, keyValuePair: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> None:
        ...

    def Contains(self, keyValuePair: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> bool:
        ...

    def Remove(self, keyValuePair: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> bool:
        ...

    def Clear(self, ) -> None:
        ...

    def ContainsKey(self, key: TKey, ) -> bool:
        ...

    def ContainsValue(self, value: TValue, ) -> bool:
        ...

    def CopyTo(self, array: System.Array[System.Collections.Generic.KeyValuePair[TKey, TValue]], index: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.Dictionary.Enumerator[TKey, TValue]:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[TKey, TValue]]:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def FindValue(self, key: TKey, ) -> ref[TValue]:
        ...

    def Initialize(self, capacity: int, ) -> int:
        ...

    def TryInsert(self, key: TKey, value: TValue, behavior: int, ) -> bool:
        ...

    def OnDeserialization(self, sender: System.Object, ) -> None:
        ...

    @typing.overload
    def Resize(self, ) -> None:
        ...

    @typing.overload
    def Resize(self, newSize: int, forceNewHashCodes: bool, ) -> None:
        ...

    @typing.overload
    def Remove(self, key: TKey, ) -> bool:
        ...

    @typing.overload
    def Remove(self, key: TKey, value: ref[TValue], ) -> bool:
        ...

    def TryGetValue(self, key: TKey, value: ref[TValue], ) -> bool:
        ...

    def TryAdd(self, key: TKey, value: TValue, ) -> bool:
        ...

    def CopyTo(self, array: System.Array[System.Collections.Generic.KeyValuePair[TKey, TValue]], index: int, ) -> None:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def EnsureCapacity(self, capacity: int, ) -> int:
        ...

    @typing.overload
    def TrimExcess(self, ) -> None:
        ...

    @typing.overload
    def TrimExcess(self, capacity: int, ) -> None:
        ...

    def CopyEntries(self, entries: System.Array[System.Collections.Generic.Dictionary.Entry[TKey, TValue]], count: int, ) -> None:
        ...

    @staticmethod
    def IsCompatibleKey(key: System.Object, ) -> bool:
        ...

    def Add(self, key: System.Object, value: System.Object, ) -> None:
        ...

    def Contains(self, key: System.Object, ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.IDictionaryEnumerator:
        ...

    def Remove(self, key: System.Object, ) -> None:
        ...

    def GetBucket(self, hashCode: int, ) -> ref[int]:
        ...

