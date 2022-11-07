from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import AdventureBot.Item
import System
import AdventureBot.User.Stats
import AdventureBot
import AdventureBot.User
import AdventureBot.ObjectManager


class ItemBase(AdventureBot.Item.IItem, System.Object, abc.ABC):
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
    def Description(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    @abc.abstractmethod
    def Group(self) -> AdventureBot.StructFlag[int]:
        ...

    # methods
    def __init__(self, ):
        ...

    @abc.abstractmethod
    def CanUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> bool:
        ...

    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    def OnEnter(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    def OnLeave(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    def OnAdd(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, count: int, ) -> None:
        ...

    def OnRemove(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, count: int, ) -> None:
        ...

    def GetItemVariables(self, user: AdventureBot.User.User, ) -> AdventureBot.VariableContainer:
        ...

class IItem(abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    @abc.abstractmethod
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    @abc.abstractmethod
    def Group(self) -> AdventureBot.StructFlag[int]:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Description(self) -> str:
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
    @abc.abstractmethod
    def IsAlwaysActive(self) -> bool:
        ...

    # methods
    @abc.abstractmethod
    def OnUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    @abc.abstractmethod
    def CanUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> bool:
        ...

    @abc.abstractmethod
    def OnEnter(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    @abc.abstractmethod
    def OnLeave(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    @abc.abstractmethod
    def OnAdd(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, count: int, ) -> None:
        ...

    @abc.abstractmethod
    def OnRemove(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, count: int, ) -> None:
        ...

class PetBase(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase, abc.ABC):
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
    def Description(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Price(self) -> System.Nullable[System.Decimal]:
        ...

    @property
    @abc.abstractmethod
    def Group(self) -> AdventureBot.StructFlag[int]:
        ...

    # methods
    def __init__(self, ):
        ...

    def OnAdd(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, count: int, ) -> None:
        ...

class ItemManager(AdventureBot.ObjectManager.IManager[AdventureBot.Item.IItem], AdventureBot.ObjectManager.StorageManager[AdventureBot.Item.IItem, AdventureBot.ObjectManager.ItemAttribute]):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

class BuyGroup(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Market: int = ...
    Guild: int = ...
    Gym: int = ...
    Merchant: int = ...
    NotSellable: int = ...

class IAdventureItem(AdventureBot.Item.IItem, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @abc.abstractmethod
    def OnAdventureEnter(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

    @abc.abstractmethod
    def OnAdventureLeave(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo, ) -> None:
        ...

class Wand(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

class ItemInfo(AdventureBot.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def Count(self) -> int:
        ...
    @Count.setter
    def Count(self, val: int):
        ...

    @property
    def Identifier(self) -> str:
        ...

    @property
    def Item(self) -> AdventureBot.Item.IItem:
        ...

    # methods
    @typing.overload
    def __init__(self, item: AdventureBot.Item.IItem, ):
        ...

    @typing.overload
    def __init__(self, identifier: str, count: int, ):
        ...

    @typing.overload
    def __init__(self, item: AdventureBot.Item.IItem, count: int, ):
        ...

    def CanUse(self, user: AdventureBot.User.User, ) -> bool:
        ...

    def OnUse(self, user: AdventureBot.User.User, ) -> None:
        ...

class Hand(AdventureBot.Item.IItem, AdventureBot.Item.ItemBase):
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

