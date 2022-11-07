from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections
import System.Runtime.Serialization
import System.Collections.Hashtable


class IEnumerator(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Current(self) -> System.Object:
        ...

    # methods
    @abc.abstractmethod
    def MoveNext(self, ) -> bool:
        ...

    @abc.abstractmethod
    def Reset(self, ) -> None:
        ...

class IEnumerable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class IStructuralComparable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def CompareTo(self, other: System.Object, comparer: System.Collections.IComparer, ) -> int:
        ...

class IDictionaryEnumerator(System.Collections.IEnumerator, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Key(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def Value(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def Entry(self) -> System.Collections.DictionaryEntry:
        ...

    # methods
class IDictionary(System.Collections.ICollection, System.Collections.IEnumerable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Item(self) -> System.Object:
        ...
    @Item.setter
    @abc.abstractmethod
    def Item(self, val: System.Object):
        ...

    @property
    @abc.abstractmethod
    def Keys(self) -> System.Collections.ICollection:
        ...

    @property
    @abc.abstractmethod
    def Values(self) -> System.Collections.ICollection:
        ...

    @property
    @abc.abstractmethod
    def IsReadOnly(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def IsFixedSize(self) -> bool:
        ...

    # methods
    @abc.abstractmethod
    def Contains(self, key: System.Object, ) -> bool:
        ...

    @abc.abstractmethod
    def Add(self, key: System.Object, value: System.Object, ) -> None:
        ...

    @abc.abstractmethod
    def Clear(self, ) -> None:
        ...

    @abc.abstractmethod
    def GetEnumerator(self, ) -> System.Collections.IDictionaryEnumerator:
        ...

    @abc.abstractmethod
    def Remove(self, key: System.Object, ) -> None:
        ...

class IList(System.Collections.ICollection, System.Collections.IEnumerable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Item(self) -> System.Object:
        ...
    @Item.setter
    @abc.abstractmethod
    def Item(self, val: System.Object):
        ...

    @property
    @abc.abstractmethod
    def IsReadOnly(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def IsFixedSize(self) -> bool:
        ...

    # methods
    @abc.abstractmethod
    def Add(self, value: System.Object, ) -> int:
        ...

    @abc.abstractmethod
    def Contains(self, value: System.Object, ) -> bool:
        ...

    @abc.abstractmethod
    def Clear(self, ) -> None:
        ...

    @abc.abstractmethod
    def IndexOf(self, value: System.Object, ) -> int:
        ...

    @abc.abstractmethod
    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    @abc.abstractmethod
    def Remove(self, value: System.Object, ) -> None:
        ...

    @abc.abstractmethod
    def RemoveAt(self, index: int, ) -> None:
        ...

class ReadOnlyCollectionBase(System.Collections.ICollection, System.Collections.IEnumerable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def InnerList(self) -> System.Collections.ArrayList:
        ...

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
    def __init__(self, ):
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class IEqualityComparer(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Equals(self, x: System.Object, y: System.Object, ) -> bool:
        ...

    @abc.abstractmethod
    def GetHashCode(self, obj: System.Object, ) -> int:
        ...

class IComparer(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Compare(self, x: System.Object, y: System.Object, ) -> int:
        ...

class BitArray(System.Collections.ICollection, System.Collections.IEnumerable, System.ICloneable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Item(self) -> bool:
        ...
    @Item.setter
    def Item(self, val: bool):
        ...

    @property
    def Length(self) -> int:
        ...
    @Length.setter
    def Length(self, val: int):
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
    def IsReadOnly(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, length: int, ):
        ...

    @typing.overload
    def __init__(self, length: int, defaultValue: bool, ):
        ...

    @typing.overload
    def __init__(self, bytes: System.Array[int], ):
        ...

    @typing.overload
    def __init__(self, values: System.Array[bool], ):
        ...

    @typing.overload
    def __init__(self, values: System.Array[int], ):
        ...

    @typing.overload
    def __init__(self, bits: System.Collections.BitArray, ):
        ...

    def Get(self, index: int, ) -> bool:
        ...

    def Set(self, index: int, value: bool, ) -> None:
        ...

    def SetAll(self, value: bool, ) -> None:
        ...

    def And(self, value: System.Collections.BitArray, ) -> System.Collections.BitArray:
        ...

    def Or(self, value: System.Collections.BitArray, ) -> System.Collections.BitArray:
        ...

    def Xor(self, value: System.Collections.BitArray, ) -> System.Collections.BitArray:
        ...

    def Not(self, ) -> System.Collections.BitArray:
        ...

    def RightShift(self, count: int, ) -> System.Collections.BitArray:
        ...

    def LeftShift(self, count: int, ) -> System.Collections.BitArray:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def Clone(self, ) -> System.Object:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @staticmethod
    def GetInt32ArrayLengthFromBitLength(n: int, ) -> int:
        ...

    @staticmethod
    def GetInt32ArrayLengthFromByteLength(n: int, ) -> int:
        ...

    @staticmethod
    def GetByteArrayLengthFromBitLength(n: int, ) -> int:
        ...

    @staticmethod
    def Div32Rem(number: int, remainder: ref[int], ) -> int:
        ...

    @staticmethod
    def Div4Rem(number: int, remainder: ref[int], ) -> int:
        ...

    @staticmethod
    def ThrowArgumentOutOfRangeException(index: int, ) -> None:
        ...

class Hashtable(System.Collections.IDictionary, System.Collections.ICollection, System.Collections.IEnumerable, System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, System.ICloneable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def hcp(self) -> System.Collections.IHashCodeProvider:
        ...
    @hcp.setter
    def hcp(self, val: System.Collections.IHashCodeProvider):
        ...

    @property
    def comparer(self) -> System.Collections.IComparer:
        ...
    @comparer.setter
    def comparer(self, val: System.Collections.IComparer):
        ...

    @property
    def EqualityComparer(self) -> System.Collections.IEqualityComparer:
        ...

    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
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
    def Count(self) -> int:
        ...

    # methods
    @typing.overload
    def __init__(self, trash: bool, ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, capacity: int, ):
        ...

    @typing.overload
    def __init__(self, capacity: int, loadFactor: float, ):
        ...

    @typing.overload
    def __init__(self, capacity: int, loadFactor: float, equalityComparer: System.Collections.IEqualityComparer, ):
        ...

    @typing.overload
    def __init__(self, hcp: System.Collections.IHashCodeProvider, comparer: System.Collections.IComparer, ):
        ...

    @typing.overload
    def __init__(self, equalityComparer: System.Collections.IEqualityComparer, ):
        ...

    @typing.overload
    def __init__(self, capacity: int, hcp: System.Collections.IHashCodeProvider, comparer: System.Collections.IComparer, ):
        ...

    @typing.overload
    def __init__(self, capacity: int, equalityComparer: System.Collections.IEqualityComparer, ):
        ...

    @typing.overload
    def __init__(self, d: System.Collections.IDictionary, ):
        ...

    @typing.overload
    def __init__(self, d: System.Collections.IDictionary, loadFactor: float, ):
        ...

    @typing.overload
    def __init__(self, d: System.Collections.IDictionary, hcp: System.Collections.IHashCodeProvider, comparer: System.Collections.IComparer, ):
        ...

    @typing.overload
    def __init__(self, d: System.Collections.IDictionary, equalityComparer: System.Collections.IEqualityComparer, ):
        ...

    @typing.overload
    def __init__(self, capacity: int, loadFactor: float, hcp: System.Collections.IHashCodeProvider, comparer: System.Collections.IComparer, ):
        ...

    @typing.overload
    def __init__(self, d: System.Collections.IDictionary, loadFactor: float, hcp: System.Collections.IHashCodeProvider, comparer: System.Collections.IComparer, ):
        ...

    @typing.overload
    def __init__(self, d: System.Collections.IDictionary, loadFactor: float, equalityComparer: System.Collections.IEqualityComparer, ):
        ...

    @typing.overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ):
        ...

    def InitHash(self, key: System.Object, hashsize: int, seed: ref[int], incr: ref[int], ) -> int:
        ...

    def Add(self, key: System.Object, value: System.Object, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Clone(self, ) -> System.Object:
        ...

    def Contains(self, key: System.Object, ) -> bool:
        ...

    def ContainsKey(self, key: System.Object, ) -> bool:
        ...

    def ContainsValue(self, value: System.Object, ) -> bool:
        ...

    def CopyKeys(self, array: System.Array, arrayIndex: int, ) -> None:
        ...

    def CopyEntries(self, array: System.Array, arrayIndex: int, ) -> None:
        ...

    def CopyTo(self, array: System.Array, arrayIndex: int, ) -> None:
        ...

    def ToKeyValuePairsArray(self, ) -> System.Array[System.Collections.KeyValuePairs]:
        ...

    def CopyValues(self, array: System.Array, arrayIndex: int, ) -> None:
        ...

    def expand(self, ) -> None:
        ...

    @typing.overload
    def rehash(self, ) -> None:
        ...

    @typing.overload
    def rehash(self, newsize: int, ) -> None:
        ...

    def UpdateVersion(self, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Collections.IDictionaryEnumerator:
        ...

    def GetHash(self, key: System.Object, ) -> int:
        ...

    def KeyEquals(self, item: System.Object, key: System.Object, ) -> bool:
        ...

    def Insert(self, key: System.Object, nvalue: System.Object, add: bool, ) -> None:
        ...

    def putEntry(self, newBuckets: System.Array[System.Collections.Hashtable.bucket], key: System.Object, nvalue: System.Object, hashcode: int, ) -> None:
        ...

    def Remove(self, key: System.Object, ) -> None:
        ...

    @staticmethod
    def Synchronized(table: System.Collections.Hashtable, ) -> System.Collections.Hashtable:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    def OnDeserialization(self, sender: System.Object, ) -> None:
        ...

class IHashCodeProvider(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def GetHashCode(self, obj: System.Object, ) -> int:
        ...

class SortedList(System.Collections.IDictionary, System.Collections.ICollection, System.Collections.IEnumerable, System.ICloneable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
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
    def Keys(self) -> System.Collections.ICollection:
        ...

    @property
    def Values(self) -> System.Collections.ICollection:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
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
    def __init__(self, initialCapacity: int, ):
        ...

    @typing.overload
    def __init__(self, comparer: System.Collections.IComparer, ):
        ...

    @typing.overload
    def __init__(self, comparer: System.Collections.IComparer, capacity: int, ):
        ...

    @typing.overload
    def __init__(self, d: System.Collections.IDictionary, ):
        ...

    @typing.overload
    def __init__(self, d: System.Collections.IDictionary, comparer: System.Collections.IComparer, ):
        ...

    def Add(self, key: System.Object, value: System.Object, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Clone(self, ) -> System.Object:
        ...

    def Contains(self, key: System.Object, ) -> bool:
        ...

    def ContainsKey(self, key: System.Object, ) -> bool:
        ...

    def ContainsValue(self, value: System.Object, ) -> bool:
        ...

    def CopyTo(self, array: System.Array, arrayIndex: int, ) -> None:
        ...

    def ToKeyValuePairsArray(self, ) -> System.Array[System.Collections.KeyValuePairs]:
        ...

    def EnsureCapacity(self, min: int, ) -> None:
        ...

    def GetByIndex(self, index: int, ) -> System.Object:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def GetEnumerator(self, ) -> System.Collections.IDictionaryEnumerator:
        ...

    def GetKey(self, index: int, ) -> System.Object:
        ...

    def GetKeyList(self, ) -> System.Collections.IList:
        ...

    def GetValueList(self, ) -> System.Collections.IList:
        ...

    def IndexOfKey(self, key: System.Object, ) -> int:
        ...

    def IndexOfValue(self, value: System.Object, ) -> int:
        ...

    def Insert(self, index: int, key: System.Object, value: System.Object, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def Remove(self, key: System.Object, ) -> None:
        ...

    def SetByIndex(self, index: int, value: System.Object, ) -> None:
        ...

    @staticmethod
    def Synchronized(list: System.Collections.SortedList, ) -> System.Collections.SortedList:
        ...

    def TrimToSize(self, ) -> None:
        ...

class CollectionBase(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def InnerList(self) -> System.Collections.ArrayList:
        ...

    @property
    def List(self) -> System.Collections.IList:
        ...

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
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
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

    def OnInsert(self, index: int, value: System.Object, ) -> None:
        ...

    def OnSet(self, index: int, oldValue: System.Object, newValue: System.Object, ) -> None:
        ...

    def OnClear(self, ) -> None:
        ...

    def OnRemove(self, index: int, value: System.Object, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

    def Contains(self, value: System.Object, ) -> bool:
        ...

    def Add(self, value: System.Object, ) -> int:
        ...

    def Remove(self, value: System.Object, ) -> None:
        ...

    def IndexOf(self, value: System.Object, ) -> int:
        ...

    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def OnValidate(self, value: System.Object, ) -> None:
        ...

    def OnSetComplete(self, index: int, oldValue: System.Object, newValue: System.Object, ) -> None:
        ...

    def OnInsertComplete(self, index: int, value: System.Object, ) -> None:
        ...

    def OnClearComplete(self, ) -> None:
        ...

    def OnRemoveComplete(self, index: int, value: System.Object, ) -> None:
        ...

class ArrayList(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.ICloneable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
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
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
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
    def __init__(self, c: System.Collections.ICollection, ):
        ...

    @staticmethod
    def Adapter(list: System.Collections.IList, ) -> System.Collections.ArrayList:
        ...

    def Add(self, value: System.Object, ) -> int:
        ...

    def AddRange(self, c: System.Collections.ICollection, ) -> None:
        ...

    @typing.overload
    def BinarySearch(self, index: int, count: int, value: System.Object, comparer: System.Collections.IComparer, ) -> int:
        ...

    @typing.overload
    def BinarySearch(self, value: System.Object, ) -> int:
        ...

    @typing.overload
    def BinarySearch(self, value: System.Object, comparer: System.Collections.IComparer, ) -> int:
        ...

    def Clear(self, ) -> None:
        ...

    def Clone(self, ) -> System.Object:
        ...

    def Contains(self, item: System.Object, ) -> bool:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, arrayIndex: int, ) -> None:
        ...

    @typing.overload
    def CopyTo(self, index: int, array: System.Array, arrayIndex: int, count: int, ) -> None:
        ...

    def EnsureCapacity(self, min: int, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def FixedSize(list: System.Collections.IList, ) -> System.Collections.IList:
        ...

    @staticmethod
    @typing.overload
    def FixedSize(list: System.Collections.ArrayList, ) -> System.Collections.ArrayList:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    def GetEnumerator(self, index: int, count: int, ) -> System.Collections.IEnumerator:
        ...

    @typing.overload
    def IndexOf(self, value: System.Object, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, value: System.Object, startIndex: int, ) -> int:
        ...

    @typing.overload
    def IndexOf(self, value: System.Object, startIndex: int, count: int, ) -> int:
        ...

    def Insert(self, index: int, value: System.Object, ) -> None:
        ...

    def InsertRange(self, index: int, c: System.Collections.ICollection, ) -> None:
        ...

    @typing.overload
    def LastIndexOf(self, value: System.Object, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, value: System.Object, startIndex: int, ) -> int:
        ...

    @typing.overload
    def LastIndexOf(self, value: System.Object, startIndex: int, count: int, ) -> int:
        ...

    @staticmethod
    @typing.overload
    def ReadOnly(list: System.Collections.IList, ) -> System.Collections.IList:
        ...

    @staticmethod
    @typing.overload
    def ReadOnly(list: System.Collections.ArrayList, ) -> System.Collections.ArrayList:
        ...

    def Remove(self, obj: System.Object, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

    def RemoveRange(self, index: int, count: int, ) -> None:
        ...

    @staticmethod
    def Repeat(value: System.Object, count: int, ) -> System.Collections.ArrayList:
        ...

    @typing.overload
    def Reverse(self, ) -> None:
        ...

    @typing.overload
    def Reverse(self, index: int, count: int, ) -> None:
        ...

    def SetRange(self, index: int, c: System.Collections.ICollection, ) -> None:
        ...

    def GetRange(self, index: int, count: int, ) -> System.Collections.ArrayList:
        ...

    @typing.overload
    def Sort(self, ) -> None:
        ...

    @typing.overload
    def Sort(self, comparer: System.Collections.IComparer, ) -> None:
        ...

    @typing.overload
    def Sort(self, index: int, count: int, comparer: System.Collections.IComparer, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Synchronized(list: System.Collections.IList, ) -> System.Collections.IList:
        ...

    @staticmethod
    @typing.overload
    def Synchronized(list: System.Collections.ArrayList, ) -> System.Collections.ArrayList:
        ...

    @typing.overload
    def ToArray(self, ) -> System.Array[System.Object]:
        ...

    @typing.overload
    def ToArray(self, type: System.Type, ) -> System.Array:
        ...

    def TrimToSize(self, ) -> None:
        ...

class ICollection(System.Collections.IEnumerable, abc.ABC):
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
    def SyncRoot(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def IsSynchronized(self) -> bool:
        ...

    # methods
    @abc.abstractmethod
    def CopyTo(self, array: System.Array, index: int, ) -> None:
        ...

class DictionaryEntry(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Key(self) -> System.Object:
        ...
    @Key.setter
    def Key(self, val: System.Object):
        ...

    @property
    def Value(self) -> System.Object:
        ...
    @Value.setter
    def Value(self, val: System.Object):
        ...

    # methods
    def __init__(self, key: System.Object, value: System.Object, ):
        ...

    def Deconstruct(self, key: ref[System.Object], value: ref[System.Object], ) -> None:
        ...

class IStructuralEquatable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Equals(self, other: System.Object, comparer: System.Collections.IEqualityComparer, ) -> bool:
        ...

    @abc.abstractmethod
    def GetHashCode(self, comparer: System.Collections.IEqualityComparer, ) -> int:
        ...

