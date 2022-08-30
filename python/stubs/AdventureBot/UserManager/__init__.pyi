from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot
import AdventureBot.UserManager
import AdventureBot.User
import System
import System.Collections.Generic
import AdventureBot.ObjectManager


class Cache(AdventureBot.Singleton[AdventureBot.UserManager.Cache]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def Get(self, id: AdventureBot.UserId, ) -> AdventureBot.User.User:
        ...

    @typing.overload
    def Put(self, user: AdventureBot.User.User, ) -> None:
        ...

    @typing.overload
    def FlushAll(self, ) -> None:
        ...

class DatabaseConnection(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @staticmethod
    def GetUsersList(messengerId: System.Nullable[System.Int32], ) -> System.Collections.Generic.List[AdventureBot.UserId]:
        ...

    @typing.overload
    @staticmethod
    def QueryUsers(order: System.Collections.Generic.List[System.ValueTuple[AdventureBot.User.DbColumnAttribute, System.Boolean]], filter: System.Collections.Generic.List[System.ValueTuple[AdventureBot.User.DbColumnAttribute, System.String, System.Object]], limit: System.Nullable[System.Int32], ) -> System.Collections.Generic.List[AdventureBot.UserManager.UserData]:
        ...

    @typing.overload
    @staticmethod
    def LoadUserData(id: AdventureBot.UserId, ) -> AdventureBot.UserManager.UserData:
        ...

    @typing.overload
    @staticmethod
    def SaveUsers(users: System.Collections.Generic.IEnumerable[AdventureBot.UserManager.UserData], ) -> None:
        ...

class Flusher(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @staticmethod
    def Init() -> None:
        ...

class MigratorAttribute(AdventureBot.ObjectManager.IdentifiableAttribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Identifier(self) -> System.String:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, version: System.Int32, ):
        ...

class IMigrator(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Migrate(self, user: System.Object, ) -> System.Object:
        ...

class MigratorManager(AdventureBot.ObjectManager.IManager[AdventureBot.UserManager.IMigrator], AdventureBot.ObjectManager.StorageManager[AdventureBot.UserManager.IMigrator, AdventureBot.UserManager.MigratorAttribute]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

class UserData(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Data(self) -> list[System.Byte]:
        ...

    @property
    def Id(self) -> AdventureBot.UserId:
        ...

    @property
    def Version(self) -> System.Int32:
        ...

    @property
    def Variables(self) -> AdventureBot.User.DatabaseVariables:
        ...

    # methods
    @typing.overload
    def __init__(self, id: AdventureBot.UserId, data: list[System.Byte], variables: AdventureBot.User.DatabaseVariables, version: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, id: AdventureBot.UserId, ):
        ...

    @typing.overload
    @staticmethod
    def Serialize(user: AdventureBot.User.User, ) -> AdventureBot.UserManager.UserData:
        ...

    @typing.overload
    def Deserialize(self, ) -> AdventureBot.User.User:
        ...

class UserProxy(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @staticmethod
    def Get(id: AdventureBot.UserId, ) -> AdventureBot.User.User:
        ...

    @typing.overload
    @staticmethod
    def GetUnsafe(id: AdventureBot.UserId, ) -> AdventureBot.User.User:
        ...

    @typing.overload
    @staticmethod
    def Save(user: AdventureBot.User.User, ) -> None:
        ...

    @typing.overload
    def Acquire(self, ) -> AdventureBot.User.User:
        ...

    @typing.overload
    def GetUnsafe(self, ) -> AdventureBot.User.User:
        ...

    @typing.overload
    def Release(self, user: AdventureBot.User.User, ) -> None:
        ...

