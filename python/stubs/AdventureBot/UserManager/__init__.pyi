from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.ObjectManager
import System
import AdventureBot
import AdventureBot.UserManager
import AdventureBot.User
import AdventureBot.UserManager.DatabaseConnection
import System.Collections.Generic
import Microsoft.Data.Sqlite

T = typing.TypeVar('T')

class MigratorAttribute(AdventureBot.ObjectManager.IdentifiableAttribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Identifier(self) -> str:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    def __init__(self, version: int, ):
        ...

class Flusher(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def Init() -> None:
        ...

    @staticmethod
    def Flush() -> None:
        ...

class Cache(AdventureBot.Singleton[AdventureBot.UserManager.Cache]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def Get(self, id: AdventureBot.UserId, ) -> AdventureBot.User.User:
        ...

    def Put(self, user: AdventureBot.User.User, ) -> None:
        ...

    def RemoveOldeset(self, ) -> None:
        ...

    def FlushAll(self, ) -> None:
        ...

class UserProxy(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, id: AdventureBot.UserId, ):
        ...

    @staticmethod
    def GetLoadedUser(id: AdventureBot.UserId, ) -> AdventureBot.UserManager.UserProxy:
        ...

    @staticmethod
    def Get(id: AdventureBot.UserId, ) -> AdventureBot.User.User:
        ...

    @staticmethod
    @typing.overload
    def GetUnsafe(id: AdventureBot.UserId, ) -> AdventureBot.User.User:
        ...

    @typing.overload
    def GetUnsafe(self, ) -> AdventureBot.User.User:
        ...

    @staticmethod
    def Save(user: AdventureBot.User.User, ) -> None:
        ...

    def Acquire(self, ) -> AdventureBot.User.User:
        ...

    def GetUser(self, ) -> AdventureBot.User.User:
        ...

    def Release(self, user: AdventureBot.User.User, ) -> None:
        ...

class MigratorManager(AdventureBot.ObjectManager.IManager[AdventureBot.UserManager.IMigrator], AdventureBot.ObjectManager.StorageManager[AdventureBot.UserManager.IMigrator, AdventureBot.UserManager.MigratorAttribute]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

class UserData(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Data(self) -> System.Array[int]:
        ...

    @property
    def Id(self) -> AdventureBot.UserId:
        ...

    @property
    def Version(self) -> int:
        ...

    @property
    def Variables(self) -> AdventureBot.User.DatabaseVariables:
        ...

    # methods
    @typing.overload
    def __init__(self, id: AdventureBot.UserId, data: System.Array[int], variables: AdventureBot.User.DatabaseVariables, version: int, ):
        ...

    @typing.overload
    def __init__(self, id: AdventureBot.UserId, ):
        ...

    @staticmethod
    def Serialize(user: AdventureBot.User.User, ) -> AdventureBot.UserManager.UserData:
        ...

    def Deserialize(self, ) -> AdventureBot.User.User:
        ...

    def Migrate(self, user: System.Object, ) -> System.Object:
        ...

class DatabaseConnection(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def QueryHelper(callback: AdventureBot.UserManager.DatabaseConnection.QueryCallback[T], ) -> T:
        ...

    @staticmethod
    def GetUsersList(messengerId: System.Nullable[int] = ..., ) -> System.Collections.Generic.List[AdventureBot.UserId]:
        ...

    @staticmethod
    def QueryUsers(order: System.Collections.Generic.List[System.ValueTuple[AdventureBot.User.DbColumnAttribute, bool]], filter: System.Collections.Generic.List[System.ValueTuple[AdventureBot.User.DbColumnAttribute, str, System.Object]], limit: System.Nullable[int], ) -> System.Collections.Generic.List[AdventureBot.UserManager.UserData]:
        ...

    @staticmethod
    def LoadUserData(id: AdventureBot.UserId, ) -> AdventureBot.UserManager.UserData:
        ...

    @staticmethod
    def SaveUsers(users: System.Collections.Generic.IEnumerable[AdventureBot.UserManager.UserData], ) -> None:
        ...

    @staticmethod
    def InitailizeTables(command: Microsoft.Data.Sqlite.SqliteCommand, ) -> AdventureBot.UserManager.DatabaseConnection.Void:
        ...

class IMigrator(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Migrate(self, user: System.Object, ) -> System.Object:
        ...

