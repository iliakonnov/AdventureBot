from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Room
import System.Collections.Generic
import System
import AdventureBot.Room.BetterRoom
import AdventureBot
import AdventureBot.User
import AdventureBot.Messenger

TAction = typing.TypeVar('TAction')
T = typing.TypeVar('T')

class BetterRoomBase(AdventureBot.Room.IRoom, AdventureBot.Room.RoomBase, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self._actions: System.Collections.Generic.Dictionary[System.Type, AdventureBot.Room.BetterRoom.ActionBase]
        self._rootAction: AdventureBot.Room.BetterRoom.ActionBase
        ...

    # static fields

    # properties
    @property
    def actions(self) -> System.Array[System.Type]:
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

    def _build(self, self: System.Type, ) -> None:
        ...

    @typing.overload
    def SwitchAction(self, user: AdventureBot.User.User, action: System.Type, ) -> None:
        ...

    @typing.overload
    def SwitchAction(self, user: AdventureBot.User.User, ) -> None:
        ...

    @typing.overload
    def GetAction(self, ) -> TAction:
        ...

    @typing.overload
    def GetAction(self, action: System.Type, ) -> AdventureBot.Room.BetterRoom.ActionBase:
        ...

    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class ButtonAttribute(AdventureBot.Room.BetterRoom.MessageHandlerAttribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Text(self) -> str:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    def __init__(self, text: str, ):
        ...

class BetterRoomBase(AdventureBot.Room.IRoom, AdventureBot.Room.BetterRoom.BetterRoomBase, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self._actions: System.Collections.Generic.Dictionary[System.Type, AdventureBot.Room.BetterRoom.ActionBase]
        self._rootAction: AdventureBot.Room.BetterRoom.ActionBase
        ...

    # static fields

    # properties
    @property
    def actions(self) -> System.Array[System.Type]:
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

    def SwitchAction(self, user: AdventureBot.User.User, ) -> None:
        ...

    @typing.overload
    def GetAction(self, ) -> TAction:
        ...

    @typing.overload
    def GetAction(self, action: System.Type, ) -> AdventureBot.Room.BetterRoom.ActionBase[T]:
        ...

class ActionBase(AdventureBot.Room.BetterRoom.ActionBase, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]
        self.Room: AdventureBot.Room.BetterRoom.BetterRoomBase
        ...

    # static fields

    # properties
    @property
    def Room(self) -> T:
        ...

    # methods
    def __init__(self, room: T, ):
        ...

class ActionAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Index(self) -> System.Nullable[int]:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, index: int, ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

class MessageHandlerAttribute(System.Attribute):
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

class ActionBase(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Collections.Generic.Dictionary[str, AdventureBot.Room.MessageReceived]
        self.Room: AdventureBot.Room.BetterRoom.BetterRoomBase
        ...

    # static fields

    # properties
    # methods
    def __init__(self, room: AdventureBot.Room.BetterRoom.BetterRoomBase, ):
        ...

    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class FallbackAttribute(AdventureBot.Room.BetterRoom.MessageHandlerAttribute):
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

