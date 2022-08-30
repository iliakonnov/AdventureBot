from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import Microsoft.Extensions.Configuration
import AdventureBot
import System.Collections.Immutable
import System.Collections.Generic
import System.Collections
import AdventureBot.User

T = typing.TypeVar('T')
TKey = typing.TypeVar('TKey')
TValue = typing.TypeVar('TValue')

class Configuration(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Config(self) -> Microsoft.Extensions.Configuration.IConfigurationRoot:
        ...

    # methods
class DebugHelpers(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @staticmethod
    def Serialize(obj: T, ) -> list[System.Byte]:
        ...

    @typing.overload
    @staticmethod
    def SerializeJson(obj: T, ) -> System.String:
        ...

    @typing.overload
    @staticmethod
    def Dump(obj: T, output: System.String, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def DumpJson(obj: T, output: System.String, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def LoadJson(input: System.String, ) -> T:
        ...

    @typing.overload
    @staticmethod
    def LoadBinary(input: System.String, ) -> T:
        ...

    @typing.overload
    @staticmethod
    def Deserialize(data: list[System.Byte], ) -> T:
        ...

    @typing.overload
    @staticmethod
    def DeserializeJson(json: System.String, ) -> T:
        ...

    @typing.overload
    @staticmethod
    def LoadUser(messenger_id: System.Int32, user_id: System.Int64, ) -> AdventureBot.BadWrapDisposable[AdventureBot.UserContext]:
        ...

class BadWrapDisposable(System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Item: T
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, item: T, ):
        ...

class DecimalExtensions(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @staticmethod
    def Format(dec: System.Decimal, precision: System.Int32, ) -> System.String:
        ...

class StructFlag(AdventureBot.Flag[T], typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Values(self) -> System.Collections.Immutable.ImmutableHashSet[T]:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, value: T, ):
        ...

    @typing.overload
    def __init__(self, values: System.Collections.Generic.IEnumerable[T], ):
        ...

    @typing.overload
    def __init__(self, values: list[T], ):
        ...

    @typing.overload
    def __init__(self, values: System.Collections.Immutable.ImmutableHashSet[T], ):
        ...

class SerializableFlag(AdventureBot.ISerializable, AdventureBot.Flag[T], typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Values(self) -> System.Collections.Immutable.ImmutableHashSet[T]:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, value: T, ):
        ...

    @typing.overload
    def __init__(self, values: System.Collections.Generic.IEnumerable[T], ):
        ...

    @typing.overload
    def __init__(self, values: list[T], ):
        ...

    @typing.overload
    def __init__(self, values: System.Collections.Immutable.ImmutableHashSet[T], ):
        ...

class Flag(System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Values(self) -> System.Collections.Immutable.ImmutableHashSet[T]:
        ...

    # methods
    @typing.overload
    def Intersects(self, other: AdventureBot.Flag, ) -> System.Boolean:
        ...

    @typing.overload
    def Equals(self, obj: System.Object, ) -> System.Boolean:
        ...

    @typing.overload
    def GetHashCode(self, ) -> System.Int32:
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class GlobalVariables(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Variables(self) -> AdventureBot.VariableContainer:
        ...

    # methods
class ListExtensions(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @staticmethod
    def Shuffle(list: System.Collections.Generic.IList[T], rng: System.Random, ) -> None:
        ...

class ReadOnlyDictionaryExtensions(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @staticmethod
    def GetValueOrDefault(dictionary: System.Collections.Generic.IReadOnlyDictionary[TKey, TValue], key: TKey, value: TValue, ) -> TValue:
        ...

class NullableDictionary(System.Collections.Generic.IDictionary[TKey, TValue], System.Collections.Generic.ICollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IEnumerable, System.Object, typing.Generic[TKey, TValue]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Item(self) -> TValue:
        ...
    @Item.setter
    def Item(self, val: TValue):
        ...

    @property
    def Keys(self) -> System.Collections.Generic.ICollection[TKey]:
        ...

    @property
    def Values(self) -> System.Collections.Generic.ICollection[TValue]:
        ...

    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[TKey], ):
        ...

    @typing.overload
    def ContainsKey(self, key: TKey, ) -> System.Boolean:
        ...

    @typing.overload
    def Add(self, key: TKey, value: TValue, ) -> None:
        ...

    @typing.overload
    def Remove(self, key: TKey, ) -> System.Boolean:
        ...

    @typing.overload
    def TryGetValue(self, key: TKey, value: ref[TValue], ) -> System.Boolean:
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[TKey, TValue]]:
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
    def CopyTo(self, array: list[System.Collections.Generic.KeyValuePair[TKey, TValue]], arrayIndex: System.Int32, ) -> None:
        ...

    @typing.overload
    def Remove(self, item: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> System.Boolean:
        ...

class ISerializable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class Serializable(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
class SerializableList(AdventureBot.ISerializable, System.Collections.Generic.IList[AdventureBot.ISerializable], System.Collections.Generic.ICollection[AdventureBot.ISerializable], System.Collections.Generic.IEnumerable[AdventureBot.ISerializable], System.Collections.IEnumerable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def IsReadOnly(self) -> System.Boolean:
        ...

    @property
    def Item(self) -> AdventureBot.ISerializable:
        ...
    @Item.setter
    def Item(self, val: AdventureBot.ISerializable):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, listImplementation: System.Collections.Generic.List[AdventureBot.ISerializable], ):
        ...

    @typing.overload
    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[AdventureBot.ISerializable]:
        ...

    @typing.overload
    def Add(self, item: AdventureBot.ISerializable, ) -> None:
        ...

    @typing.overload
    def Clear(self, ) -> None:
        ...

    @typing.overload
    def Contains(self, item: AdventureBot.ISerializable, ) -> System.Boolean:
        ...

    @typing.overload
    def CopyTo(self, array: list[AdventureBot.ISerializable], arrayIndex: System.Int32, ) -> None:
        ...

    @typing.overload
    def Remove(self, item: AdventureBot.ISerializable, ) -> System.Boolean:
        ...

    @typing.overload
    def IndexOf(self, item: AdventureBot.ISerializable, ) -> System.Int32:
        ...

    @typing.overload
    def Insert(self, index: System.Int32, item: AdventureBot.ISerializable, ) -> None:
        ...

    @typing.overload
    def RemoveAt(self, index: System.Int32, ) -> None:
        ...

class Singleton(System.Object, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Instance(self) -> T:
        ...

    # methods
class TopParam(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Rooms: System.Int32 = Rooms
    Monsters: System.Int32 = Monsters
    Gold: System.Int32 = Gold
    Level: System.Int32 = Level

class TopPlayers(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @staticmethod
    def GetTop(param: AdventureBot.TopParam, count: System.Int32, ) -> System.Collections.Generic.IEnumerable[System.ValueTuple[AdventureBot.UserId, AdventureBot.User.DatabaseVariables]]:
        ...

class UserContext(System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def User(self) -> AdventureBot.User.User:
        ...

    # methods
    @typing.overload
    def __init__(self, userId: AdventureBot.UserId, ):
        ...

    @typing.overload
    def __init__(self, userId: AdventureBot.UserId, chatId: AdventureBot.ChatId, ):
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

class UserId(AdventureBot.ISerializable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.Messenger: System.Int32
        self.Id: System.Int64
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, messenger: System.Int32, id: System.Int64, ):
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class ChatId(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.Messenger: System.Int32
        self.Id: System.Int64
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, messenger: System.Int32, id: System.Int64, ):
        ...

    @typing.overload
    def ToString(self, ) -> System.String:
        ...

class VariableContainer(AdventureBot.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, variables: System.Collections.Generic.Dictionary[System.String, AdventureBot.ISerializable], ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def Get(self, key: System.String, ) -> AdventureBot.ISerializable:
        ...

    @typing.overload
    def Get(self, key: System.String, ) -> T:
        ...

    @typing.overload
    def Keys(self, ) -> System.Collections.Generic.IEnumerable[System.String]:
        ...

    @typing.overload
    def Set(self, key: System.String, value: AdventureBot.ISerializable, ) -> None:
        ...

    @typing.overload
    def Remove(self, key: System.String, ) -> None:
        ...

