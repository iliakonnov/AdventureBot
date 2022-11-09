from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Item
import AdventureBot
import System
import AdventureBot.User.Stats
import AdventureBot.User


class NativeCross(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class HolyBomb(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class Revolver(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class BottleOfLight(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class FighterArmor(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class DemonSlayer(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class HolyBullet(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

