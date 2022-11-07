from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Room
import Content.Quests
import Content.Halls
import System
import AdventureBot
import System.Collections.Generic
import AdventureBot.User
import AdventureBot.Item
import AdventureBot.User.Stats
import AdventureBot.Room.BetterRoom


class FallenAngel(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, Content.Halls.EvilMonsterBase):
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

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class FallenAngelShard(AdventureBot.Item.IItem, Content.Halls.LootBase):
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
    def Description(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
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

class Recipe(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Gold(self) -> System.Decimal:
        ...

    @property
    def Input(self) -> System.Collections.Generic.Dictionary[str, int]:
        ...

    @property
    def Output(self) -> str:
        ...

    # methods
    def __init__(self, gold: System.Decimal, output: str, input: System.Collections.Generic.Dictionary[str, int], ):
        ...

class IEvilWeapon(AdventureBot.Item.IItem, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def DamageMultiplier(self) -> System.Decimal:
        ...

    # methods
class DemonGeneral(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, Content.Halls.EvilMonsterBase):
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

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class ObsidianPlate(AdventureBot.Item.IItem, Content.Halls.LootBase):
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
    def Description(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
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

class Weaponsmith(AdventureBot.Room.IRoom, AdventureBot.Room.BetterRoom.BetterRoomBase[Content.Halls.Weaponsmith]):
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

    def GetWeapons(self, ) -> System.Array[System.Array[str]]:
        ...

    def GetStock(self, ) -> System.Array[System.Array[str]]:
        ...

class DemonSolider(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, Content.Halls.EvilMonsterBase):
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

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class DemonicEssence(AdventureBot.Item.IItem, Content.Halls.LootBase):
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
    def Description(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
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

class DemonOutcast(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, Content.Halls.EvilMonsterBase):
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

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class OutcastChain(AdventureBot.Item.IItem, Content.Halls.IEvilWeapon, Content.Halls.LootBase):
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
    def Description(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def DamageMultiplier(self) -> System.Decimal:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
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

class ObsidianGolem(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, Content.Halls.EvilMonsterBase):
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

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class Ghoul(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, Content.Halls.EvilMonsterBase):
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

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class Halls(AdventureBot.Room.IRoom, AdventureBot.Room.BetterRoom.BetterRoomBase[Content.Halls.Halls]):
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

    def Explore(self, user: AdventureBot.User.User, ) -> None:
        ...

class HallsRoot(AdventureBot.Room.IRoot, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    Id: str = ...

    # properties
    @property
    def Identifier(self) -> str:
        ...

    @property
    def RootRoomId(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

class EvilMonsterBase(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, AdventureBot.Room.MonsterBase, abc.ABC):
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

    def OnRunaway(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def ForceRun(self, user: AdventureBot.User.User, ) -> None:
        ...

class DemonGeneralHorns(AdventureBot.Item.IItem, Content.Halls.LootBase):
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
    def Description(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
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

class HellRegiment(AdventureBot.Room.IRoom, AdventureBot.Room.IMonster, Content.Quests.IQuestMonster, Content.Halls.EvilMonsterBase):
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

    def OnWon(self, user: AdventureBot.User.User, ) -> None:
        ...

class LootBase(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
        ...

    @property
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    @property
    @abc.abstractmethod
    def Identifier(self) -> str:
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
    def Description(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

    def CanUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> bool:
        ...

