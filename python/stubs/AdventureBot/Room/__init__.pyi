from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Room
import System
import AdventureBot.ObjectManager
import AdventureBot
import System.Collections.Generic
import AdventureBot.User
import AdventureBot.Messenger
import AdventureBot.Item
import System.Runtime.Serialization
import System.Reflection


class AvailableAttribute(AdventureBot.Room.RoomAttribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Difficulity(self) -> int:
        ...

    @property
    def RootId(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    def __init__(self, identifier: str, difficulity: int, rootId: str, ):
        ...

class IRoot(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Identifier(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def RootRoomId(self) -> str:
        ...

    # methods
class RoomManager(AdventureBot.ObjectManager.IManager[AdventureBot.Room.IRoom], AdventureBot.ObjectManager.StorageManager[AdventureBot.Room.IRoom, AdventureBot.Room.RoomAttribute]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

class RoomBase(AdventureBot.Room.IRoom, System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def GetRoomVariables(self, user: AdventureBot.User.User, ) -> AdventureBot.VariableContainer:
        ...

    @abc.abstractmethod
    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def OnLeave(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def UpdateCounter(self, containerName: str, diff: int, ) -> int:
        ...

    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

    def OnReturn(self, user: AdventureBot.User.User, ) -> None:
        ...

    def GetCurrentRoute(self, user: AdventureBot.User.User, ) -> AdventureBot.Room.MessageReceived:
        ...

    def GetRouteIdx(self, user: AdventureBot.User.User, ) -> System.Nullable[int]:
        ...

    def HandleAction(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> bool:
        ...

    def SwitchAction(self, user: AdventureBot.User.User, handler: AdventureBot.Room.MessageReceived, ) -> None:
        ...

    def SwitchAndHandle(self, user: AdventureBot.User.User, handler: AdventureBot.Room.MessageReceived, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def GetCurrentButtons(self, user: AdventureBot.User.User, ) -> System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]:
        ...

    def HandleButtonAlways(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def GetButtons(self, user: AdventureBot.User.User, ) -> System.Array[System.Array[str]]:
        ...

    def HandleButton(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> bool:
        ...

    @staticmethod
    def GetItems(user: AdventureBot.User.User, ) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    def UseItem(user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> bool:
        ...

    @typing.overload
    def SendMessage(self, user: AdventureBot.User.User, message: str, ) -> None:
        ...

    @typing.overload
    def SendMessage(self, user: AdventureBot.User.User, message: str, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    @typing.overload
    def SendMessage(self, user: AdventureBot.User.User, message: str, intent: str, ) -> None:
        ...

    @typing.overload
    def SendMessage(self, user: AdventureBot.User.User, message: str, buttons: System.Array[System.Array[str]], intent: str, ) -> None:
        ...

    @staticmethod
    def GetAllItems() -> AdventureBot.Item.ItemManager:
        ...

    @staticmethod
    def GetAllRooms() -> AdventureBot.Room.RoomManager:
        ...

class MessageReceived(System.ICloneable, System.Runtime.Serialization.ISerializable, System.MulticastDelegate):
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

    def Invoke(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def BeginInvoke(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, callback: System.AsyncCallback, object: System.Object, ) -> System.IAsyncResult:
        ...

    def EndInvoke(self, result: System.IAsyncResult, ) -> None:
        ...

class BossBase(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, AdventureBot.Room.RoomBase, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def InitialGold(self) -> System.Decimal:
        ...

    @property
    @abc.abstractmethod
    def Health(self) -> System.Decimal:
        ...

    @property
    def GlobalVariablesKey(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def MakeDamage(self, user: AdventureBot.User.User, damage: System.Decimal, ) -> None:
        ...

    def GetCurrentHealth(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def OnLeave(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def GetActions(self, user: AdventureBot.User.User, ) -> System.Array[System.Array[str]]:
        ...

class IRoom(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Identifier(self) -> str:
        ...

    # methods
    @abc.abstractmethod
    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

    @abc.abstractmethod
    def OnReturn(self, user: AdventureBot.User.User, ) -> None:
        ...

    @abc.abstractmethod
    def OnLeave(self, user: AdventureBot.User.User, ) -> bool:
        ...

    @abc.abstractmethod
    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class RoomAttribute(AdventureBot.ObjectManager.IdentifiableAttribute):
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

class RootAttribute(AdventureBot.ObjectManager.IdentifiableAttribute):
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

class Difficulity(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Easy: int = ...
    Medium: int = ...
    Lower: int = ...
    Hard: int = ...
    Upper: int = ...
    Any: int = ...

class RootManager(AdventureBot.ObjectManager.IManager[AdventureBot.Room.IRoot], AdventureBot.ObjectManager.StorageManager[AdventureBot.Room.IRoot, AdventureBot.Room.RootAttribute]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

class IMonster(AdventureBot.Room.IRoom, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def MakeDamage(self, user: AdventureBot.User.User, damage: System.Decimal, ) -> None:
        ...

    @abc.abstractmethod
    def GetCurrentHealth(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

class RootRoom(AdventureBot.Room.IRoom, AdventureBot.Room.RoomBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

    def NewGame(self, user: AdventureBot.User.User, message: str = ..., ) -> None:
        ...

    def OnLeave(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def ConfirmRestart(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def OnReturn(self, user: AdventureBot.User.User, ) -> None:
        ...

class MonsterBase(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, AdventureBot.Room.RoomBase, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Health(self) -> System.Decimal:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Identifier(self) -> str:
        ...

    @property
    def Routes(self) -> System.Array[AdventureBot.Room.MessageReceived]:
        ...
    @Routes.setter
    def Routes(self, val: System.Array[AdventureBot.Room.MessageReceived]):
        ...

    @property
    def Buttons(self) -> AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]:
        ...
    @Buttons.setter
    def Buttons(self, val: AdventureBot.NullableDictionary[AdventureBot.Room.MessageReceived, System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]]):
        ...

    # methods
    def __init__(self, ):
        ...

    def MakeDamage(self, user: AdventureBot.User.User, damage: System.Decimal, ) -> None:
        ...

    def OnEnter(self, user: AdventureBot.User.User, ) -> None:
        ...

    @abc.abstractmethod
    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    @abc.abstractmethod
    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    @abc.abstractmethod
    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    @abc.abstractmethod
    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

    def GetCurrentHealth(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def OnLeave(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    @staticmethod
    def MonsterKilled(user: AdventureBot.User.User, monster: AdventureBot.Room.IMonster, ) -> None:
        ...

    def NotHandled(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def FinishTurn(self, user: AdventureBot.User.User, ) -> None:
        ...

    def GetActions(self, user: AdventureBot.User.User, ) -> System.Array[System.Array[str]]:
        ...

