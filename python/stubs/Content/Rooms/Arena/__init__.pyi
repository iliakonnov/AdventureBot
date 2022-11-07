from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Item
import AdventureBot
import System
import AdventureBot.User.Stats
import AdventureBot.User
import AdventureBot.Messenger
import AdventureBot.Room
import AdventureBot.Room.BetterRoom
import Content.Rooms.Arena
import System.Collections.Generic


class Medallion(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Description(self) -> str:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    @property
    def IsAlwaysActive(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

    def CanUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> bool:
        ...

    def OnMessage(self, user: AdventureBot.User.User, message: AdventureBot.Messenger.ReceivedMessage, ) -> None:
        ...

    def EnsureSingle(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> bool:
        ...

    def GetGladiators(self, ) -> AdventureBot.SerializableList:
        ...

    def OnAdd(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, count: int, ) -> None:
        ...

    def OnRemove(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, count: int, ) -> None:
        ...

    def OnReset(self, user: AdventureBot.User.User, ) -> None:
        ...

class Arena(AdventureBot.Room.IRoom, AdventureBot.Room.BetterRoom.BetterRoomBase[Content.Rooms.Arena.Arena]):
    @typing.overload
    def __init__(self, **kwargs):
        self._actions: System.Collections.Generic.Dictionary[System.Type, AdventureBot.Room.BetterRoom.ActionBase]
        self._rootAction: AdventureBot.Room.BetterRoom.ActionBase
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def actions(self) -> System.Array[System.Type]:
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

class Battle(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, AdventureBot.Room.BetterRoom.BetterRoomBase[Content.Rooms.Arena.Battle]):
    @typing.overload
    def __init__(self, **kwargs):
        self._actions: System.Collections.Generic.Dictionary[System.Type, AdventureBot.Room.BetterRoom.ActionBase]
        self._rootAction: AdventureBot.Room.BetterRoom.ActionBase
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Name(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def actions(self) -> System.Array[System.Type]:
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

    def OnLeave(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def MakeDamage(self, user: AdventureBot.User.User, damage: System.Decimal, ) -> None:
        ...

    def GetCurrentHealth(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    @staticmethod
    def BeginBattle(user: AdventureBot.User.User, enemy: AdventureBot.User.User, firstTurn: bool, ) -> None:
        ...

    def Win(self, winner: AdventureBot.User.User, loser: AdventureBot.User.User, ) -> None:
        ...

    def Lose(self, winner: AdventureBot.User.User, loser: AdventureBot.User.User, ) -> None:
        ...

    def GetActions(self, user: AdventureBot.User.User, ) -> System.Array[System.Array[str]]:
        ...

