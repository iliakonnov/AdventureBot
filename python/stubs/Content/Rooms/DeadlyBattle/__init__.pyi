from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Item
import Content.Rooms.DeadlyBattle
import AdventureBot.User.Stats
import System
import AdventureBot
import AdventureBot.User
import AdventureBot.Room
import System.Collections.Generic
import AdventureBot.Room.BetterRoom


class Cigar(AdventureBot.Item.IItem, Content.Rooms.DeadlyBattle.LootBase):
    @typing.overload
    def __init__(self, **kwargs):
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
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def Damage(self) -> System.Decimal:
        ...

    @property
    def AddDamage(self) -> bool:
        ...

    @property
    def Description(self) -> str:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
        ...

    @property
    def IsAlwaysActive(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

class LootBase(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Description(self) -> str:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
        ...

    @property
    @abc.abstractmethod
    def Damage(self) -> System.Decimal:
        ...

    @property
    @abc.abstractmethod
    def AddDamage(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def Identifier(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    @property
    def IsAlwaysActive(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    # methods
    def __init__(self, ):
        ...

    def CanUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> bool:
        ...

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class KungLao(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Rooms.DeadlyBattle.TournamentMonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
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
    def Loot(self) -> str:
        ...

    @property
    def Health(self) -> System.Decimal:
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

class JohnnyCage(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Rooms.DeadlyBattle.TournamentMonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
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
    def Loot(self) -> str:
        ...

    @property
    def Health(self) -> System.Decimal:
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

class SharpHat(AdventureBot.Item.IItem, Content.Rooms.DeadlyBattle.LootBase):
    @typing.overload
    def __init__(self, **kwargs):
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
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def Damage(self) -> System.Decimal:
        ...

    @property
    def AddDamage(self) -> bool:
        ...

    @property
    def Description(self) -> str:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
        ...

    @property
    def IsAlwaysActive(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

class Nunchaku(AdventureBot.Item.IItem, Content.Rooms.DeadlyBattle.LootBase):
    @typing.overload
    def __init__(self, **kwargs):
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
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def Damage(self) -> System.Decimal:
        ...

    @property
    def AddDamage(self) -> bool:
        ...

    @property
    def Description(self) -> str:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
        ...

    @property
    def IsAlwaysActive(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

class SubZero(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Rooms.DeadlyBattle.TournamentMonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
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
    def Loot(self) -> str:
        ...

    @property
    def Health(self) -> System.Decimal:
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

class Scorpio(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Rooms.DeadlyBattle.TournamentMonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
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
    def Loot(self) -> str:
        ...

    @property
    def Health(self) -> System.Decimal:
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

class Jax(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Rooms.DeadlyBattle.TournamentMonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
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
    def Loot(self) -> str:
        ...

    @property
    def Health(self) -> System.Decimal:
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

class TournamentMonsterBase(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, AdventureBot.Room.MonsterBase, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Loot(self) -> str:
        ...

    @property
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

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class LiuKang(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Rooms.DeadlyBattle.TournamentMonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
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
    def Loot(self) -> str:
        ...

    @property
    def Health(self) -> System.Decimal:
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

class BlueMask(AdventureBot.Item.IItem, Content.Rooms.DeadlyBattle.LootBase):
    @typing.overload
    def __init__(self, **kwargs):
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
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def Damage(self) -> System.Decimal:
        ...

    @property
    def AddDamage(self) -> bool:
        ...

    @property
    def Description(self) -> str:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
        ...

    @property
    def IsAlwaysActive(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

class Harpoon(AdventureBot.Item.IItem, Content.Rooms.DeadlyBattle.LootBase):
    @typing.overload
    def __init__(self, **kwargs):
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
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def Damage(self) -> System.Decimal:
        ...

    @property
    def AddDamage(self) -> bool:
        ...

    @property
    def Description(self) -> str:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
        ...

    @property
    def IsAlwaysActive(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

class Tournament(AdventureBot.Room.IRoom, AdventureBot.Room.BetterRoom.BetterRoomBase[Content.Rooms.DeadlyBattle.Tournament]):
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

    def OnReturn(self, user: AdventureBot.User.User, ) -> None:
        ...

    def BeginBattle(self, user: AdventureBot.User.User, ) -> None:
        ...

class ShaoKahn(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, AdventureBot.Room.MonsterBase):
    @typing.overload
    def __init__(self, **kwargs):
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
    def Health(self) -> System.Decimal:
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

    def GetDamage(self, user: AdventureBot.User.User, ) -> System.Decimal:
        ...

    def Enter(self, user: AdventureBot.User.User, buttons: System.Array[System.Array[str]], ) -> None:
        ...

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class Hammer(AdventureBot.Item.IItem, Content.Rooms.DeadlyBattle.LootBase):
    @typing.overload
    def __init__(self, **kwargs):
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
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def Damage(self) -> System.Decimal:
        ...

    @property
    def AddDamage(self) -> bool:
        ...

    @property
    def Description(self) -> str:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
        ...

    @property
    def IsAlwaysActive(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

class Sunglasses(AdventureBot.Item.IItem, Content.Rooms.DeadlyBattle.LootBase):
    @typing.overload
    def __init__(self, **kwargs):
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
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def Damage(self) -> System.Decimal:
        ...

    @property
    def AddDamage(self) -> bool:
        ...

    @property
    def Description(self) -> str:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
        ...

    @property
    def IsAlwaysActive(self) -> bool:
        ...

    # methods
    def __init__(self, ):
        ...

