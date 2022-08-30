from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections.Generic
import AdventureBot.Room
import AdventureBot.User
import AdventureBot.Messenger
import AdventureBot.Room.BetterRoom
import AdventureBot

T = typing.TypeVar('T')
TAction = typing.TypeVar('TAction')

class ActionBase(System.Object, abc.ABC, typing.Generic[T]):
    @typing.overload
    def __init__(self, **kwargs):
        self.Buttons: System.Collections.Generic.Dictionary[System.String, AdventureBot.Room.MessageReceived]
        ...

    # properties
    # methods
    @typing.overload
    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

class ActionAttribute(System.Attribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Index(self) -> System.Nullable[System.Int32]:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, index: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

class MessageHandlerAttribute(System.Attribute):
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

class ButtonAttribute(AdventureBot.Room.BetterRoom.MessageHandlerAttribute):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Text(self) -> System.String:
        ...

    @property
    def TypeId(self) -> System.Object:
        ...

    # methods
    @typing.overload
    def __init__(self, text: System.String, ):
        ...

class FallbackAttribute(AdventureBot.Room.BetterRoom.MessageHandlerAttribute):
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

class BetterRoomBase(AdventureBot.Room.IRoom, AdventureBot.Room.RoomBase, abc.ABC, typing.Generic[T]):
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
    def SwitchAction(self, user: AdventureBot.User.User, action: System.Type, ) -> None:
        ...

    @typing.overload
    def SwitchAction(self, user: AdventureBot.User.User, ) -> None:
        ...

    @typing.overload
    def GetAction(self, ) -> TAction:
        ...

    @typing.overload
    def GetAction(self, action: System.Type, ) -> AdventureBot.Room.BetterRoom.ActionBase[T]:
        ...

    @typing.overload
    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

