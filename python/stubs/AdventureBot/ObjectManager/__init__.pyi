from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.ObjectManager
import System
import System.Runtime.Serialization
import System.Reflection
import System.Collections.Generic
import AdventureBot.ObjectManager.StorageManager
import AdventureBot

T = typing.TypeVar('T')
TAttribute = typing.TypeVar('TAttribute')
TObj = typing.TypeVar('TObj')
TMgr = typing.TypeVar('TMgr')

class IdentifiableAttribute(AdventureBot.ObjectManager.GameObjectAttribute):
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
    def __init__(self, identifier: str, ):
        ...

class MessengerAttribute(AdventureBot.ObjectManager.GameObjectAttribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    def __init__(self, ):
        ...

class Create(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self._target: System.Object
        self._methodBase: System.Object
        self._methodPtr: System.IntPtr
        self._methodPtrAux: System.IntPtr
        ...

    # static fields

    # properties
    @property
    def Target(self) -> System.Object:
        ...

    @property
    def Method(self) -> System.Reflection.MethodInfo:
        ...

    # methods
    def __init__(self, object: System.Object, method: System.IntPtr, ):
        ...

    def Invoke(self, ) -> T:
        ...

    def BeginInvoke(self, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> T:
        ...

class StorageManager(AdventureBot.ObjectManager.IManager[T], System.Object, typing.Generic[T, TAttribute]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def Register(self, attribute: AdventureBot.ObjectManager.GameObjectAttribute, creator: AdventureBot.ObjectManager.Create[T], ) -> None:
        ...

    def InitializeAll(self, ) -> None:
        ...

    def Get(self, identifier: str, ) -> T:
        ...

    def Items(self, ) -> System.Collections.Generic.IEnumerable[AdventureBot.ObjectManager.StorageManager.Item[T, TAttribute]]:
        ...

    def Keys(self, ) -> System.Collections.Generic.IEnumerable[str]:
        ...

    def Contains(self, identifier: str, ) -> bool:
        ...

class ObjectManager(AdventureBot.ObjectManager.IObjectManager, AdventureBot.Singleton[AdventureBot.ObjectManager.ObjectManager], typing.Generic[TObj]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @typing.overload
    def Register(self, attribute: AdventureBot.ObjectManager.GameObjectAttribute, creator: AdventureBot.ObjectManager.Create[System.Object], ) -> None:
        ...

    @typing.overload
    def Register(self, attribute: AdventureBot.ObjectManager.GameObjectAttribute, ) -> None:
        ...

    @typing.overload
    def RegisterManager(self, manager: TMgr, ) -> None:
        ...

    @typing.overload
    def RegisterManager(self, ) -> None:
        ...

    def Get(self, ) -> TMgr:
        ...

class IManager(abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def Register(self, attribute: AdventureBot.ObjectManager.GameObjectAttribute, creator: AdventureBot.ObjectManager.Create[T], ) -> None:
        ...

class GameObjectAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    def __init__(self, ):
        ...

class ItemAttribute(AdventureBot.ObjectManager.IdentifiableAttribute):
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
    def __init__(self, identifier: str, ):
        ...

