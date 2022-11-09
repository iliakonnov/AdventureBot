from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Item
import Content.Items
import AdventureBot
import System
import AdventureBot.User.Stats
import AdventureBot.User


class StoneSoul(AdventureBot.Item.IItem, Content.Items.BaseSoul):
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
    def Property(self) -> int:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
        ...

    @property
    def Description(self) -> str:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def IsAlwaysActive(self) -> bool:
        ...

    @property
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    # methods
    def __init__(self, ):
        ...

class Bow(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class StarlightWand(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class Slippers(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class DungeonsAndDragons(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class SmartSoul(AdventureBot.Item.IItem, Content.Items.BaseSoul):
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
    def Property(self) -> int:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
        ...

    @property
    def Description(self) -> str:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def IsAlwaysActive(self) -> bool:
        ...

    @property
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    # methods
    def __init__(self, ):
        ...

class DictionaryDahl(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class ElderWand(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class HiMenCat(AdventureBot.Item.IItem, AdventureBot.Item.PetBase):
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

class StarkSuit(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class Cheat(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class ActivatedGolemHeart(AdventureBot.Item.IItem, AdventureBot.Item.IAdventureItem, AdventureBot.Item.ItemBase):
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

    def OnAdventureEnter(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    def OnAdd(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, count: int, ) -> None:
        ...

    def OnAdventureLeave(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class Soulstone(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

    def OnAdd(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, count: int, ) -> None:
        ...

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class LifeCrystal(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class Ketchup(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class LifeCrystalShard(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class GolemHeart(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class BeornSkin(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class VaderCloak(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class GordonKnife(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class ActivatedStarkSuit(AdventureBot.Item.IItem, AdventureBot.Item.IAdventureItem, AdventureBot.Item.ItemBase):
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

    def OnAdventureEnter(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    def OnAdd(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, count: int, ) -> None:
        ...

    def OnAdventureLeave(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class Narzan(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class Chainsword(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
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

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    def CanUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> bool:
        ...

    def OnEnter(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    def OnLeave(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class VaderRespirator(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class StrongSoul(AdventureBot.Item.IItem, Content.Items.BaseSoul):
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
    def Property(self) -> int:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
        ...

    @property
    def Description(self) -> str:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def IsAlwaysActive(self) -> bool:
        ...

    @property
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    # methods
    def __init__(self, ):
        ...

class InfinityGlove(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class MercuryFulminate(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class Notebook(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class HockeyMask(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class EnergyDrink(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class VaderSword(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class Skitties(AdventureBot.Item.IItem, AdventureBot.Item.IAdventureItem, AdventureBot.Item.ItemBase):
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

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    def OnAdventureEnter(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    def OnAdventureLeave(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class Worm(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class DictionaryOzhegov(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class Awp(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class Bullet(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class TigerTooth(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class BaseSoul(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Property(self) -> int:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[int]:
        ...

    @property
    def Description(self) -> str:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def IsAlwaysActive(self) -> bool:
        ...

    @property
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    @property
    @abc.abstractmethod
    def Identifier(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    # methods
    def __init__(self, ):
        ...

    def CanUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> bool:
        ...

class AnimeBadge(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

