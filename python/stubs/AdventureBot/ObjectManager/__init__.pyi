from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import AdventureBot.ObjectManager
import System.Runtime.Serialization
import System.Reflection
import AdventureBot
import System.Collections.Generic
import AdventureBot.ObjectManager.StorageManager

T = typing.TypeVar('T')
TObj = typing.TypeVar('TObj')
TMgr = typing.TypeVar('TMgr')
TAttribute = typing.TypeVar('TAttribute')

class GameObjectAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

class IdentifiableAttribute(AdventureBot.ObjectManager.GameObjectAttribute):
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
    def __init__(self, identifier: System.String, ):
        ...

class ItemAttribute(AdventureBot.ObjectManager.IdentifiableAttribute):
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
    def __init__(self, identifier: System.String, ):
        ...

class MessengerAttribute(AdventureBot.ObjectManager.GameObjectAttribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

class Create(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    @typing.overload
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    @typing.overload
    def Invoke(self, ) -> T:
        ...

    @typing.overload
    def BeginInvoke(self, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> T:
        ...

class IManager(abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def Register(self, attribute: AdventureBot.ObjectManager.GameObjectAttribute, creator: AdventureBot.ObjectManager.Create[T], ) -> None:
        ...

class ObjectManager(AdventureBot.ObjectManager.IObjectManager, AdventureBot.Singleton[AdventureBot.ObjectManager.ObjectManager], typing.Generic[TObj]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def Register(self, attribute: AdventureBot.ObjectManager.GameObjectAttribute, creator: AdventureBot.ObjectManager.Create[System.Object], ) -> None:
        ...

    @typing.overload
    def RegisterManager(self, manager: TMgr, ) -> None:
        ...

    @typing.overload
    def RegisterManager(self, ) -> None:
        ...

    @typing.overload
    def Get(self, ) -> TMgr:
        ...

    @typing.overload
    def Register(self, attribute: AdventureBot.ObjectManager.GameObjectAttribute, ) -> None:
        ...

class StorageManager(AdventureBot.ObjectManager.IManager[T], System.Object, typing.Generic[T, TAttribute]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def Register(self, attribute: AdventureBot.ObjectManager.GameObjectAttribute, creator: AdventureBot.ObjectManager.Create[T], ) -> None:
        ...

    @typing.overload
    def Get(self, identifier: System.String, ) -> T:
        ...

    @typing.overload
    def Items(self, ) -> System.Collections.Generic.IEnumerable[AdventureBot.ObjectManager.StorageManager.Item[T, TAttribute]]:
        ...

    @typing.overload
    def Keys(self, ) -> System.Collections.Generic.IEnumerable[System.String]:
        ...

    @typing.overload
    def Contains(self, identifier: System.String, ) -> System.Boolean:
        ...

