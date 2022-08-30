from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System.Collections
import System
import System.Runtime.Serialization


class IEnumerable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class ICollection(System.Collections.IEnumerable, abc.ABC):
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
    def SyncRoot(self) -> System.Object:
        ...

    @abc.abstractmethod
    @property
    def IsSynchronized(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def CopyTo(self, array: System.Array, index: System.Int32, ) -> None:
        ...

class IEnumerator(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Current(self) -> System.Object:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def MoveNext(self, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def Reset(self, ) -> None:
        ...

class IList(System.Collections.ICollection, System.Collections.IEnumerable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Item(self) -> System.Object:
        ...
    @abc.abstractmethod
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @abc.abstractmethod
    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def IsFixedSize(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def Add(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def Contains(self, value: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def Clear(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def IndexOf(self, value: System.Object, ) -> System.Int32:
        ...

    @typing.overload
    @abc.abstractmethod
    def Insert(self, index: System.Int32, value: System.Object, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Remove(self, value: System.Object, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def RemoveAt(self, index: System.Int32, ) -> None:
        ...

class IStructuralEquatable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Equals(self, other: System.Object, comparer: System.Collections.IEqualityComparer, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetHashCode(self, comparer: System.Collections.IEqualityComparer, ) -> System.Int32:
        ...

class IStructuralComparable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def CompareTo(self, other: System.Object, comparer: System.Collections.IComparer, ) -> System.Int32:
        ...

class IDictionary(System.Collections.ICollection, System.Collections.IEnumerable, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Item(self) -> System.Object:
        ...
    @abc.abstractmethod
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @abc.abstractmethod
    @property
    def Keys(self) -> System.Collections.ICollection:
        ...

    @abc.abstractmethod
    @property
    def Values(self) -> System.Collections.ICollection:
        ...

    @abc.abstractmethod
    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def IsFixedSize(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def Contains(self, key: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def Add(self, key: System.Object, value: System.Object, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def Clear(self, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetEnumerator(self, ) -> System.Collections.IDictionaryEnumerator:
        ...

    @typing.overload
    @abc.abstractmethod
    def Remove(self, key: System.Object, ) -> None:
        ...

class IComparer(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Compare(self, x: System.Object, y: System.Object, ) -> System.Int32:
        ...

class IEqualityComparer(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Equals(self, x: System.Object, y: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetHashCode(self, obj: System.Object, ) -> System.Int32:
        ...

class IDictionaryEnumerator(System.Collections.IEnumerator, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Key(self) -> System.Object:
        ...

    @abc.abstractmethod
    @property
    def Value(self) -> System.Object:
        ...

    @abc.abstractmethod
    @property
    def Entry(self) -> System.Collections.DictionaryEntry:
        ...

    # methods
class DictionaryEntry(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        ...

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
    @typing.overload
    def __init__(self, key: System.Object, value: System.Object, ):
        ...

    @typing.overload
    def Deconstruct(self, key: ref[System.Object], value: ref[System.Object], ) -> None:
        ...

class ReadOnlyCollectionBase(System.Collections.ICollection, System.Collections.IEnumerable, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

class Hashtable(System.Collections.IDictionary, System.Collections.ICollection, System.Collections.IEnumerable, System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, System.ICloneable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Item(self) -> System.Object:
        ...
    @Item.setter
    def Item(self, val: System.Object):
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def IsFixedSize(self) -> System.Boolean:
        ...

    @property
    def IsSynchronized(self) -> System.Boolean:
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
    def __init__(self, capacity: System.Int32, loadFactor: System.Single, ):
        ...

    @typing.overload
    def __init__(self, capacity: System.Int32, loadFactor: System.Single, equalityComparer: System.Collections.IEqualityComparer, ):
        ...

    @typing.overload
    def __init__(self, hcp: System.Collections.IHashCodeProvider, comparer: System.Collections.IComparer, ):
        ...

    @typing.overload
    def __init__(self, equalityComparer: System.Collections.IEqualityComparer, ):
        ...

    @typing.overload
    def __init__(self, capacity: System.Int32, hcp: System.Collections.IHashCodeProvider, comparer: System.Collections.IComparer, ):
        ...

    @typing.overload
    def __init__(self, capacity: System.Int32, equalityComparer: System.Collections.IEqualityComparer, ):
        ...

    @typing.overload
    def __init__(self, d: System.Collections.IDictionary, ):
        ...

    @typing.overload
    def __init__(self, d: System.Collections.IDictionary, loadFactor: System.Single, ):
        ...

    @typing.overload
    def __init__(self, d: System.Collections.IDictionary, hcp: System.Collections.IHashCodeProvider, comparer: System.Collections.IComparer, ):
        ...

    @typing.overload
    def __init__(self, d: System.Collections.IDictionary, equalityComparer: System.Collections.IEqualityComparer, ):
        ...

    @typing.overload
    def __init__(self, capacity: System.Int32, loadFactor: System.Single, hcp: System.Collections.IHashCodeProvider, comparer: System.Collections.IComparer, ):
        ...

    @typing.overload
    def __init__(self, d: System.Collections.IDictionary, loadFactor: System.Single, hcp: System.Collections.IHashCodeProvider, comparer: System.Collections.IComparer, ):
        ...

    @typing.overload
    def __init__(self, d: System.Collections.IDictionary, loadFactor: System.Single, equalityComparer: System.Collections.IEqualityComparer, ):
        ...

    @typing.overload
    def Clone(self, ) -> System.Object:
        ...

    @typing.overload
    def Add(self, key: System.Object, value: System.Object, ) -> None:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, key: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def ContainsKey(self, key: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def ContainsValue(self, value: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def CopyTo(self, array: System.Array, arrayIndex: System.Int32, ) -> None:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IDictionaryEnumerator:
        ...

    @typing.overload
    def Remove(self, key: System.Object, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def Synchronized(table: System.Collections.Hashtable, ) -> System.Collections.Hashtable:
        ...

    @typing.overload
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext, ) -> None:
        ...

    @typing.overload
    def OnDeserialization(self, sender: System.Object, ) -> None:
        ...

class IHashCodeProvider(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def GetHashCode(self, obj: System.Object, ) -> System.Int32:
        ...

class CollectionBase(System.Collections.IList, System.Collections.ICollection, System.Collections.IEnumerable, System.Object, abc.ABC):
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

    # methods
    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def RemoveAt(self, index: System.Int32, ) -> None:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

