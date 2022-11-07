from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot
import System.Collections.Immutable
import System.Collections.Generic
import System.Collections
import System
import AdventureBot.User
import System.Timers
import Microsoft.Extensions.Configuration

T = typing.TypeVar('T')
TKey = typing.TypeVar('TKey')
TValue = typing.TypeVar('TValue')

class SerializableFlag(AdventureBot.ISerializable, AdventureBot.Flag[T], typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

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
    def __init__(self, values: System.Array[T], ):
        ...

    @typing.overload
    def __init__(self, values: System.Collections.Immutable.ImmutableHashSet[T], ):
        ...

class SerializableList(AdventureBot.ISerializable, System.Collections.Generic.IList[AdventureBot.ISerializable], System.Collections.Generic.ICollection[AdventureBot.ISerializable], System.Collections.Generic.IEnumerable[AdventureBot.ISerializable], System.Collections.IEnumerable, System.Object):
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

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[AdventureBot.ISerializable]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Add(self, item: AdventureBot.ISerializable, ) -> None:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: AdventureBot.ISerializable, ) -> bool:
        ...

    def CopyTo(self, array: System.Array[AdventureBot.ISerializable], arrayIndex: int, ) -> None:
        ...

    def Remove(self, item: AdventureBot.ISerializable, ) -> bool:
        ...

    def IndexOf(self, item: AdventureBot.ISerializable, ) -> int:
        ...

    def Insert(self, index: int, item: AdventureBot.ISerializable, ) -> None:
        ...

    def RemoveAt(self, index: int, ) -> None:
        ...

class Singleton(System.Object, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Instance(self) -> T:
        ...

    # methods
    def __init__(self, ):
        ...

class TopParam(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Rooms: int = ...
    Monsters: int = ...
    Gold: int = ...
    Level: int = ...

class ReadOnlyDictionaryExtensions(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def GetValueOrDefault(dictionary: System.Collections.Generic.IReadOnlyDictionary[TKey, TValue], key: TKey, value: TValue = ..., ) -> TValue:
        ...

class VariableContainer(AdventureBot.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @typing.overload
    def __init__(self, variables: System.Collections.Generic.Dictionary[str, AdventureBot.ISerializable], ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def Get(self, key: str, ) -> AdventureBot.ISerializable:
        ...

    @typing.overload
    def Get(self, key: str, ) -> T:
        ...

    def Keys(self, ) -> System.Collections.Generic.IEnumerable[str]:
        ...

    def Set(self, key: str, value: AdventureBot.ISerializable, ) -> None:
        ...

    def Remove(self, key: str, ) -> None:
        ...

class Serializable(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
class DebugHelpers(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def Serialize(obj: T, ) -> System.Array[int]:
        ...

    @staticmethod
    def SerializeJson(obj: T, ) -> str:
        ...

    @staticmethod
    def Dump(obj: T, output: str, ) -> None:
        ...

    @staticmethod
    def DumpJson(obj: T, output: str, ) -> None:
        ...

    @staticmethod
    def LoadJson(input: str, ) -> T:
        ...

    @staticmethod
    def LoadBinary(input: str, ) -> T:
        ...

    @staticmethod
    def Deserialize(data: System.Array[int], ) -> T:
        ...

    @staticmethod
    def DeserializeJson(json: str, ) -> T:
        ...

    @staticmethod
    def LoadUser(messengerId: int, userId: int, ) -> AdventureBot.BadWrapDisposable[AdventureBot.UserContext]:
        ...

class TopPlayers(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def GetTop(param: int, count: int, ) -> System.Collections.Generic.IEnumerable[System.ValueTuple[AdventureBot.UserId, AdventureBot.User.DatabaseVariables]]:
        ...

class UserContext(System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def User(self) -> AdventureBot.User.User:
        ...
    @User.setter
    def User(self, val: AdventureBot.User.User):
        ...

    # methods
    @typing.overload
    def __init__(self, userId: AdventureBot.UserId, ):
        ...

    @typing.overload
    def __init__(self, userId: AdventureBot.UserId, chatId: AdventureBot.ChatId, ):
        ...

    def Dispose(self, ) -> None:
        ...

    def LoadUser(self, userId: AdventureBot.UserId, ) -> None:
        ...

    def Unlink(self, ) -> bool:
        ...

    def InitializeTimer(self, ) -> None:
        ...

    @staticmethod
    def TimerOnElapsed(sender: System.Object, e: System.Timers.ElapsedEventArgs, ) -> None:
        ...

class UserId(AdventureBot.ISerializable, System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.Messenger: int
        self.Id: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, messenger: int, id: int, ):
        ...

    def ToString(self, ) -> str:
        ...

class GlobalVariables(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Variables(self) -> AdventureBot.VariableContainer:
        ...

    # methods
    @staticmethod
    def Flush() -> None:
        ...

class Flag(System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

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
    def __init__(self, values: System.Array[T], ):
        ...

    @typing.overload
    def __init__(self, values: System.Collections.Immutable.ImmutableHashSet[T], ):
        ...

    def Intersects(self, other: AdventureBot.Flag, ) -> bool:
        ...

    def Equals(self, obj: System.Object, ) -> bool:
        ...

    def GetHashCode(self, ) -> int:
        ...

    def ToString(self, ) -> str:
        ...

class NullableDictionary(System.Collections.Generic.IDictionary[TKey, TValue], System.Collections.Generic.ICollection[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[TKey, TValue]], System.Collections.IEnumerable, System.Object, typing.Generic[TKey, TValue]):
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
    def Keys(self) -> System.Collections.Generic.ICollection[TKey]:
        ...

    @property
    def Values(self) -> System.Collections.Generic.ICollection[TValue]:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[TKey], ):
        ...

    def ContainsKey(self, key: TKey, ) -> bool:
        ...

    @typing.overload
    def Add(self, key: TKey, value: TValue, ) -> None:
        ...

    @typing.overload
    def Add(self, item: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> None:
        ...

    @typing.overload
    def Remove(self, key: TKey, ) -> bool:
        ...

    @typing.overload
    def Remove(self, item: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> bool:
        ...

    def TryGetValue(self, key: TKey, value: ref[TValue], ) -> bool:
        ...

    def GetEnumerator(self, ) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[TKey, TValue]]:
        ...

    def GetEnumerator(self, ) -> System.Collections.IEnumerator:
        ...

    def Clear(self, ) -> None:
        ...

    def Contains(self, item: System.Collections.Generic.KeyValuePair[TKey, TValue], ) -> bool:
        ...

    def CopyTo(self, array: System.Array[System.Collections.Generic.KeyValuePair[TKey, TValue]], arrayIndex: int, ) -> None:
        ...

class DecimalExtensions(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def Format(dec: System.Decimal, precision: int = ..., ) -> str:
        ...

class StructFlag(AdventureBot.Flag[T], typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

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
    def __init__(self, values: System.Array[T], ):
        ...

    @typing.overload
    def __init__(self, values: System.Collections.Immutable.ImmutableHashSet[T], ):
        ...

class Configuration(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Config(self) -> Microsoft.Extensions.Configuration.IConfigurationRoot:
        ...

    # methods
class ListExtensions(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def Shuffle(list: System.Collections.Generic.IList[T], rng: System.Random, ) -> None:
        ...

class ISerializable(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
class BadWrapDisposable(System.IDisposable, System.Object, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Item: T
        ...

    # static fields

    # properties
    # methods
    def __init__(self, item: T, ):
        ...

    def Finalize(self, ) -> None:
        ...

    def Dispose(self, ) -> None:
        ...

class ChatId(System.ValueType):
    @typing.overload
    def __init__(self, **kwargs):
        self.Messenger: int
        self.Id: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, messenger: int, id: int, ):
        ...

    def ToString(self, ) -> str:
        ...

