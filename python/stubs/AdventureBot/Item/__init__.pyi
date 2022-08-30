from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Item
import System
import AdventureBot
import AdventureBot.User.Stats
import AdventureBot.User
import AdventureBot.ObjectManager


class Hand(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Name(self) -> System.String:
        ...

    @property
    def Description(self) -> System.String:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[AdventureBot.Item.BuyGroup]:
        ...

    @property
    def Identifier(self) -> System.String:
        ...

    @property
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    @property
    def IsAlwaysActive(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    @typing.overload
    def CanUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> System.Boolean:
        ...

class IAdventureItem(AdventureBot.Item.IItem, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    @abc.abstractmethod
    def OnAdventureEnter(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def OnAdventureLeave(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class BuyGroup(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Market: System.Int32 = Market
    Guild: System.Int32 = Guild
    Gym: System.Int32 = Gym
    Merchant: System.Int32 = Merchant
    NotSellable: System.Int32 = NotSellable

class IItem(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @abc.abstractmethod
    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @abc.abstractmethod
    @property
    def Group(self) -> AdventureBot.StructFlag[AdventureBot.Item.BuyGroup]:
        ...

    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Description(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Identifier(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    @abc.abstractmethod
    @property
    def IsAlwaysActive(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    @abc.abstractmethod
    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def CanUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> System.Boolean:
        ...

    @typing.overload
    @abc.abstractmethod
    def OnEnter(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def OnLeave(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def OnAdd(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, count: System.Int32, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def OnRemove(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, count: System.Int32, ) -> None:
        ...

class ItemBase(AdventureBot.Item.IItem, System.Object, abc.ABC):
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
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    @property
    def IsAlwaysActive(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Description(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @abc.abstractmethod
    @property
    def Group(self) -> AdventureBot.StructFlag[AdventureBot.Item.BuyGroup]:
        ...

    # methods
    @typing.overload
    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    @typing.overload
    @abc.abstractmethod
    def CanUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> System.Boolean:
        ...

    @typing.overload
    def OnEnter(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    @typing.overload
    def OnLeave(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    @typing.overload
    def OnAdd(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, count: System.Int32, ) -> None:
        ...

    @typing.overload
    def OnRemove(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, count: System.Int32, ) -> None:
        ...

class ItemInfo(AdventureBot.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Count(self) -> System.Int32:
        ...

    @property
    def Identifier(self) -> System.String:
        ...

    @property
    def Item(self) -> AdventureBot.Item.IItem:
        ...

    # methods
    @typing.overload
    def __init__(self, item: AdventureBot.Item.IItem, ):
        ...

    @typing.overload
    def __init__(self, identifier: System.String, count: System.Int32, ):
        ...

    @typing.overload
    def __init__(self, item: AdventureBot.Item.IItem, count: System.Int32, ):
        ...

    @typing.overload
    def CanUse(self, user: AdventureBot.User.User, ) -> System.Boolean:
        ...

    @typing.overload
    def OnUse(self, user: AdventureBot.User.User, ) -> None:
        ...

class ItemManager(AdventureBot.ObjectManager.IManager[AdventureBot.Item.IItem], AdventureBot.ObjectManager.StorageManager[AdventureBot.Item.IItem, AdventureBot.ObjectManager.ItemAttribute]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

class PetBase(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase, abc.ABC):
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
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    @property
    def IsAlwaysActive(self) -> System.Boolean:
        ...

    @abc.abstractmethod
    @property
    def Name(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Description(self) -> System.String:
        ...

    @abc.abstractmethod
    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @abc.abstractmethod
    @property
    def Group(self) -> AdventureBot.StructFlag[AdventureBot.Item.BuyGroup]:
        ...

    # methods
    @typing.overload
    def OnAdd(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, count: System.Int32, ) -> None:
        ...

class Wand(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Name(self) -> System.String:
        ...

    @property
    def Description(self) -> System.String:
        ...

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    def Group(self) -> AdventureBot.StructFlag[AdventureBot.Item.BuyGroup]:
        ...

    @property
    def Identifier(self) -> System.String:
        ...

    @property
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        ...

    @property
    def IsAlwaysActive(self) -> System.Boolean:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    @typing.overload
    def CanUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> System.Boolean:
        ...

