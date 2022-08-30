from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Collections
import System.Collections.Generic
import System
import System.Collections.ObjectModel
import System.Collections.Generic.List
import System.Runtime.Serialization
import System.Collections.Generic.Dictionary
import System.Collections.Generic.Queue
import System.Collections.Generic.Stack

T = typing.TypeVar('T')
TKey = typing.TypeVar('TKey')
TValue = typing.TypeVar('TValue')
TOutput = typing.TypeVar('TOutput')

class IEnumerable(System.Collections.IEnumerable, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[T]:
        ...

class IList(System.Collections.Generic.ICollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Item(self) -> T:
        ...
    @abc.abstractmethod
    @Item.setter
    def Item(self, val: T):
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def IndexOf(self, item: T, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def Insert(self, index: System.Int32, item: T, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def RemoveAt(self, index: System.Int32, ) -> None:
        ...

class IReadOnlyDictionary(System.Collections.Generic.IReadOnlyCollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IEnumerable, abc.ABC, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Item(self) -> TValue:
        ...

    @abc.abstractmethod
    @property
    def Keys(self) -> System.Collections.Generic.IEnumerable[TKey]:
        ...

    @abc.abstractmethod
    @property
    def Values(self) -> System.Collections.Generic.IEnumerable[TValue]:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def ContainsKey(self, key: TKey, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def TryGetValue(self, key: TKey, value: ref[TValue], ) -> System.Boolean:
        ...

class IDictionary(System.Collections.Generic.ICollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IEnumerable, abc.ABC, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Item(self) -> TValue:
        ...
    @abc.abstractmethod
    @Item.setter
    def Item(self, val: TValue):
        ...

    @abc.abstractmethod
    @property
    def Keys(self) -> System.Collections.Generic.ICollection[TKey]:
        ...

    @abc.abstractmethod
    @property
    def Values(self) -> System.Collections.Generic.ICollection[TValue]:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def ContainsKey(self, key: TKey, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def Add(self, key: TKey, value: TValue, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Remove(self, key: TKey, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def TryGetValue(self, key: TKey, value: ref[TValue], ) -> System.Boolean:
        ...

class ICollection(System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Count(self) -> System.Int32:
        ...

    @abc.abstractmethod
    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def Add(self, item: T, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Clear(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Contains(self, item: T, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def CopyTo(self, array: list[T], arrayIndex: System.Int32, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Remove(self, item: T, ) -> System.Boolean:
        ...

class KeyValuePair(System.ValueType, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Key(self) -> TKey:
        ...

    @property
    def Value(self) -> TValue:
        ...

    # methods
    @typing.overload
    def __init__(self, key: TKey, value: TValue, ):
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

    @typing.overload
    def Deconstruct(self, key: ref[TKey], value: ref[TValue], ) -> None:
        ...

class IEqualityComparer(abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Equals(self, x: T, y: T, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetHashCode(self, obj: T, ) -> System.Int32:
        ...

class IEnumerator(System.IDisposable, System.Collections.IEnumerator, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Current(self) -> T:
        ...

    # methods
class List(System.Collections.Generic.IList[T], System.Collections.Generic.ICollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Collections.IList, System.Collections.ICollection, System.Collections.Generic.IReadOnlyList[T], System.Collections.Generic.IReadOnlyCollection[T], System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Capacity(self) -> System.Int32:
        ...
    @Capacity.setter
    def Capacity(self, val: System.Int32):
        ...

    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def Item(self) -> T:
        ...
    @Item.setter
    def Item(self, val: T):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, capacity: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[T], ):
        ...

    @typing.overload
    def Add(self, item: T, ) -> None:
        ...

    @typing.overload
    def AddRange(self, collection: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    @typing.overload
    def AsReadOnly(self, ) -> System.Collections.ObjectModel.ReadOnlyCollection[T]:
        ...

    @typing.overload
    def BinarySearch(self, index: System.Int32, count: System.Int32, item: T, comparer: System.Collections.Generic.IComparer[T], ) -> System.Int32:
        ...

    @typing.overload
    def BinarySearch(self, item: T, ) -> System.Int32:
        ...

    @typing.overload
    def BinarySearch(self, item: T, comparer: System.Collections.Generic.IComparer[T], ) -> System.Int32:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, item: T, ) -> System.Boolean:
        ...

    @typing.overload
    def ConvertAll(self, converter: System.Converter[T, TOutput], ) -> System.Collections.Generic.List[TOutput]:
        ...

    @typing.overload
    def CopyTo(self, array: list[T], ) -> None:
        ...

    @typing.overload
    def CopyTo(self, index: System.Int32, array: list[T], arrayIndex: System.Int32, count: System.Int32, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: list[T], arrayIndex: System.Int32, ) -> None:
        ...

    @typing.overload
    def EnsureCapacity(self, capacity: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def Exists(self, match: System.Predicate[T], ) -> System.Boolean:
        ...

    @typing.overload
    def Find(self, match: System.Predicate[T], ) -> T:
        ...

    @typing.overload
    def FindAll(self, match: System.Predicate[T], ) -> System.Collections.Generic.List:
        ...

    @typing.overload
    def FindIndex(self, match: System.Predicate[T], ) -> System.Int32:
        ...

    @typing.overload
    def FindIndex(self, startIndex: System.Int32, match: System.Predicate[T], ) -> System.Int32:
        ...

    @typing.overload
    def FindIndex(self, startIndex: System.Int32, count: System.Int32, match: System.Predicate[T], ) -> System.Int32:
        ...

    @typing.overload
    def FindLast(self, match: System.Predicate[T], ) -> T:
        ...

    @typing.overload
    def FindLastIndex(self, match: System.Predicate[T], ) -> System.Int32:
        ...

    @typing.overload
    def FindLastIndex(self, startIndex: System.Int32, match: System.Predicate[T], ) -> System.Int32:
        ...

    @typing.overload
    def FindLastIndex(self, startIndex: System.Int32, count: System.Int32, match: System.Predicate[T], ) -> System.Int32:
        ...

    @typing.overload
    def ForEach(self, action: System.Action[T], ) -> None:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.Generic.List.Enumerator[T]:
        ...

    @typing.overload
    def GetRange(self, index: System.Int32, count: System.Int32, ) -> System.Collections.Generic.List:
        ...

    @typing.overload
    def IndexOf(self, item: T, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, item: T, index: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def IndexOf(self, item: T, index: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, item: T, ) -> None:
        ...

    @typing.overload
    def InsertRange(self, index: System.Int32, collection: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    @typing.overload
    def LastIndexOf(self, item: T, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, item: T, index: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def LastIndexOf(self, item: T, index: System.Int32, count: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def Remove(self, item: T, ) -> System.Boolean:
        ...

    @typing.overload
    def RemoveAll(self, match: System.Predicate[T], ) -> System.Int32:
        ...

    @typing.overload
    def RemoveAt(self, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def RemoveRange(self, index: System.Int32, count: System.Int32, ) -> None:
        ...

    @typing.overload
    def Reverse(self, ) -> None:
        ...

    @typing.overload
    def Reverse(self, index: System.Int32, count: System.Int32, ) -> None:
        ...

    @typing.overload
    def Sort(self, ) -> None:
        ...

    @typing.overload
    def Sort(self, comparer: System.Collections.Generic.IComparer[T], ) -> None:
        ...

    @typing.overload
    def Sort(self, index: System.Int32, count: System.Int32, comparer: System.Collections.Generic.IComparer[T], ) -> None:
        ...

    @typing.overload
    def Sort(self, comparison: System.Comparison[T], ) -> None:
        ...

    @typing.overload
    def ToArray(self, ) -> list[T]:
        ...

    @typing.overload
    def TrimExcess(self, ) -> None:
        ...

    @typing.overload
    def TrueForAll(self, match: System.Predicate[T], ) -> System.Boolean:
        ...

class Dictionary(System.Collections.Generic.IDictionary[TKey, TValue], System.Collections.Generic.ICollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IEnumerable, System.Collections.IDictionary, System.Collections.ICollection, System.Collections.Generic.IReadOnlyDictionary[TKey, TValue], System.Collections.Generic.IReadOnlyCollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, System.Object, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Comparer(self) -> System.Collections.Generic.IEqualityComparer[TKey]:
        ...

    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def Keys(self) -> System.Collections.Generic.Dictionary.KeyCollection[TKey, TValue]:
        ...

    @property
    def Values(self) -> System.Collections.Generic.Dictionary.ValueCollection[TKey, TValue]:
        ...

    @property
    def Item(self) -> TValue:
        ...
    @Item.setter
    def Item(self, val: TValue):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, capacity: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[TKey], ):
        ...

    @typing.overload
    def __init__(self, capacity: System.Int32, comparer: System.Collections.Generic.IEqualityComparer[TKey], ):
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
    def Add(self, key: TKey, value: TValue, ) -> None:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def ContainsKey(self, key: TKey, ) -> System.Boolean:
        ...

    @typing.overload
    def ContainsValue(self, value: TValue, ) -> System.Boolean:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.Generic.Dictionary.Enumerator[TKey, TValue]:
        ...

    @typing.overload
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def OnDeserialization(self, sender: System.Object, ) -> None:
        ...

    @typing.overload
    def Remove(self, key: TKey, ) -> System.Boolean:
        ...

    @typing.overload
    def Remove(self, key: TKey, value: ref[TValue], ) -> System.Boolean:
        ...

    @typing.overload
    def TryGetValue(self, key: TKey, value: ref[TValue], ) -> System.Boolean:
        ...

    @typing.overload
    def TryAdd(self, key: TKey, value: TValue, ) -> System.Boolean:
        ...

    @typing.overload
    def EnsureCapacity(self, capacity: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def TrimExcess(self, ) -> None:
        ...

    @typing.overload
    def TrimExcess(self, capacity: System.Int32, ) -> None:
        ...

class IReadOnlyList(System.Collections.Generic.IReadOnlyCollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Item(self) -> T:
        ...

    # methods
class IReadOnlyCollection(System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Count(self) -> System.Int32:
        ...

    # methods
class Queue(System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[T], System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, capacity: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[T], ):
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: list[T], arrayIndex: System.Int32, ) -> None:
        ...

    @typing.overload
    def Enqueue(self, item: T, ) -> None:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.Generic.Queue.Enumerator[T]:
        ...

    @typing.overload
    def Dequeue(self, ) -> T:
        ...

    @typing.overload
    def TryDequeue(self, result: ref[T], ) -> System.Boolean:
        ...

    @typing.overload
    def Peek(self, ) -> T:
        ...

    @typing.overload
    def TryPeek(self, result: ref[T], ) -> System.Boolean:
        ...

    @typing.overload
    def Contains(self, item: T, ) -> System.Boolean:
        ...

    @typing.overload
    def ToArray(self, ) -> list[T]:
        ...

    @typing.overload
    def TrimExcess(self, ) -> None:
        ...

    @typing.overload
    def EnsureCapacity(self, capacity: System.Int32, ) -> System.Int32:
        ...

class Stack(System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[T], System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, capacity: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[T], ):
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, item: T, ) -> System.Boolean:
        ...

    @typing.overload
    def CopyTo(self, array: list[T], arrayIndex: System.Int32, ) -> None:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.Generic.Stack.Enumerator[T]:
        ...

    @typing.overload
    def TrimExcess(self, ) -> None:
        ...

    @typing.overload
    def Peek(self, ) -> T:
        ...

    @typing.overload
    def TryPeek(self, result: ref[T], ) -> System.Boolean:
        ...

    @typing.overload
    def Pop(self, ) -> T:
        ...

    @typing.overload
    def TryPop(self, result: ref[T], ) -> System.Boolean:
        ...

    @typing.overload
    def Push(self, item: T, ) -> None:
        ...

    @typing.overload
    def EnsureCapacity(self, capacity: System.Int32, ) -> System.Int32:
        ...

    @typing.overload
    def ToArray(self, ) -> list[T]:
        ...

class IComparer(abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Compare(self, x: T, y: T, ) -> System.Int32:
        ...

class ISet(System.Collections.Generic.ICollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Add(self, item: T, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def UnionWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def IntersectWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def ExceptWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def SymmetricExceptWith(self, other: System.Collections.Generic.IEnumerable[T], ) -> None:
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
    def IsProperSupersetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def IsProperSubsetOf(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def Overlaps(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def SetEquals(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

class IReadOnlySet(System.Collections.Generic.IReadOnlyCollection[T], System.Collections.Generic.IEnumerable[T], System.Collections.IEnumerable, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Contains(self, item: T, ) -> System.Boolean:
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

    @typing.overload
    @abc.abstractmethod
    def SetEquals(self, other: System.Collections.Generic.IEnumerable[T], ) -> System.Boolean:
        ...

