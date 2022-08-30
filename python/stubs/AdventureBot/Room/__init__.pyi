from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Room
import System
import AdventureBot
import System.Collections.Generic
import AdventureBot.User
import AdventureBot.Messenger
import AdventureBot.ObjectManager
import System.Runtime.Serialization
import System.Reflection
import AdventureBot.Item


class BossBase(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, AdventureBot.Room.RoomBase, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Identifier(self) -> System.String:
        ...

    @property
    def Routes(self) -> list[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: list[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[System.String, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[System.String, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    @typing.overload
    def MakeDamage(self, user: AdventureBot.User.User, damage: System.Decimal, ) -> None:
        ...

    @typing.overload
    def GetCurrentHealth(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    @typing.overload
    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

    @typing.overload
    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    @typing.overload
    def OnLeave(self, user: AdventureBot.User.User, ) -> System.Boolean:
        ...

class IRoom(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Identifier(self) -> System.String:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def OnReturn(self, user: AdventureBot.User.User, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def OnLeave(self, user: AdventureBot.User.User, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class RootAttribute(AdventureBot.ObjectManager.IdentifiableAttribute):
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

class RootManager(AdventureBot.ObjectManager.IManager[AdventureBot.Room.IRoot], AdventureBot.ObjectManager.StorageManager[AdventureBot.Room.IRoot, AdventureBot.Room.RootAttribute]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

class IRoot(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Identifier(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def RootRoomId(self) -> System.String:
        ...

    # methods
class IMonster(AdventureBot.Room.IRoom, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def MakeDamage(self, user: AdventureBot.User.User, damage: System.Decimal, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def GetCurrentHealth(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

class MonsterBase(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, AdventureBot.Room.RoomBase, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Identifier(self) -> System.String:
        ...

    @property
    def Routes(self) -> list[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: list[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[System.String, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[System.String, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    @typing.overload
    def MakeDamage(self, user: AdventureBot.User.User, damage: System.Decimal, ) -> None:
        ...

    @typing.overload
    def GetCurrentHealth(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    @typing.overload
    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

    @typing.overload
    def OnLeave(self, user: AdventureBot.User.User, ) -> System.Boolean:
        ...

    @typing.overload
    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def MonsterKilled(user: AdventureBot.User.User, monster: AdventureBot.Room.IMonster, ) -> None:
        ...

class RoomAttribute(AdventureBot.ObjectManager.IdentifiableAttribute):
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

class AvailableAttribute(AdventureBot.Room.RoomAttribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Difficulity(self) -> AdventureBot.Room.Difficulity:
        ...

    @property
    def RootId(self) -> System.String:
        ...

    @property
    def Identifier(self) -> System.String:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, identifier: System.String, difficulity: AdventureBot.Room.Difficulity, rootId: System.String, ):
        ...

class MessageReceived(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
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
    def Invoke(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    @typing.overload
    def BeginInvoke(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    @typing.overload
    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class RoomBase(AdventureBot.Room.IRoom, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Identifier(self) -> System.String:
        ...

    @property
    def Routes(self) -> list[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: list[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[System.String, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[System.String, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    @typing.overload
    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    @typing.overload
    def OnLeave(self, user: AdventureBot.User.User, ) -> System.Boolean:
        ...

    @typing.overload
    def GetRoomVariables(self, user: AdventureBot.User.User, ) -> AdventureBot.VariableContainer:
        ...

    @typing.overload
    def OnReturn(self, user: AdventureBot.User.User, ) -> None:
        ...

    @typing.overload
    def GetCurrentRoute(self, user: AdventureBot.User.User, ) -> AdventureBot.Room.MessageReceived:
        ...

    @typing.overload
    def HandleAction(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> System.Boolean:
        ...

    @typing.overload
    def SwitchAction(self, user: AdventureBot.User.User, handler: AdventureBot.Room.MessageReceived, ) -> None:
        ...

    @typing.overload
    def SwitchAndHandle(self, user: AdventureBot.User.User, handler: AdventureBot.Room.MessageReceived, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    @typing.overload
    def HandleButtonAlways(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    @typing.overload
    def GetButtons(self, user: AdventureBot.User.User, ) -> list[list[System.String]]:
        ...

    @typing.overload
    def HandleButton(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> System.Boolean:
        ...

    @typing.overload
    @staticmethod
    def GetItems(user: AdventureBot.User.User, ) -> System.Collections.Generic.IEnumerable[System.String]:
        ...

    @typing.overload
    @staticmethod
    def UseItem(user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> System.Boolean:
        ...

    @typing.overload
    def SendMessage(self, user: AdventureBot.User.User, message: System.String, ) -> None:
        ...

    @typing.overload
    def SendMessage(self, user: AdventureBot.User.User, message: System.String, buttons: list[list[System.String]], ) -> None:
        ...

    @typing.overload
    def SendMessage(self, user: AdventureBot.User.User, message: System.String, intent: System.String, ) -> None:
        ...

    @typing.overload
    def SendMessage(self, user: AdventureBot.User.User, message: System.String, buttons: list[list[System.String]], intent: System.String, ) -> None:
        ...

    @typing.overload
    @staticmethod
    def GetAllItems() -> AdventureBot.Item.ItemManager:
        ...

    @typing.overload
    @staticmethod
    def GetAllRooms() -> AdventureBot.Room.RoomManager:
        ...

class Difficulity(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: System.Int32 = None
    Easy: System.Int32 = Easy
    Medium: System.Int32 = Medium
    Lower: System.Int32 = Lower
    Hard: System.Int32 = Hard
    Upper: System.Int32 = Upper
    Any: System.Int32 = Any

class RoomManager(AdventureBot.ObjectManager.IManager[AdventureBot.Room.IRoom], AdventureBot.ObjectManager.StorageManager[AdventureBot.Room.IRoom, AdventureBot.Room.RoomAttribute]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

class RootRoom(AdventureBot.Room.IRoom, AdventureBot.Room.RoomBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Name(self) -> System.String:
        ...

    @property
    def Identifier(self) -> System.String:
        ...

    @property
    def Routes(self) -> list[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: list[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[System.String, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[System.String, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

    @typing.overload
    def OnLeave(self, user: AdventureBot.User.User, ) -> System.Boolean:
        ...

    @typing.overload
    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    @typing.overload
    def OnReturn(self, user: AdventureBot.User.User, ) -> None:
        ...

