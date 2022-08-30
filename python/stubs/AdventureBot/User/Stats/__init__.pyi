from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import AdventureBot.User
import AdventureBot
import AdventureBot.User.Stats
import System.Collections.Generic


class Statistics(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def MonsterCount(self) -> System.Int32:
        ...

    @property
    def RoomsCount(self) -> System.Int32:
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, user: AdventureBot.User.User, ):
        ...

    @typing.overload
    def RoomTraveled(self, ) -> None:
        ...

class Stats(AdventureBot.ISerializable, AdventureBot.User.Stats.StatsEffect):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def ChangeType(self) -> AdventureBot.User.Stats.ChangeType:
        ...

    @property
    def Effect(self) -> System.Collections.Generic.IReadOnlyDictionary[AdventureBot.User.Stats.StatsProperty, System.Decimal]:
        ...

    # methods
    @typing.overload
    def __init__(self, effect: System.Collections.Generic.IReadOnlyDictionary[AdventureBot.User.Stats.StatsProperty, System.Decimal], ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def Apply(self, effect: AdventureBot.User.Stats.StatsEffect, ) -> AdventureBot.User.Stats.Stats:
        ...

    @typing.overload
    def GetStat(self, property: AdventureBot.User.Stats.StatsProperty, ) -> System.Decimal:
        ...

class ChangeType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Add: System.Int32 = Add
    Set: System.Int32 = Set
    Multiply: System.Int32 = Multiply

class StatsProperty(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Health: System.Int32 = Health
    Intelligence: System.Int32 = Intelligence
    Strength: System.Int32 = Strength
    Mana: System.Int32 = Mana
    Stamina: System.Int32 = Stamina
    Defence: System.Int32 = Defence
    Karma: System.Int32 = Karma

class StatsEffect(AdventureBot.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def ChangeType(self) -> AdventureBot.User.Stats.ChangeType:
        ...

    @property
    def Effect(self) -> System.Collections.Generic.IReadOnlyDictionary[AdventureBot.User.Stats.StatsProperty, System.Decimal]:
        ...

    # methods
    @typing.overload
    def __init__(self, changeType: AdventureBot.User.Stats.ChangeType, effect: System.Collections.Generic.IReadOnlyDictionary[AdventureBot.User.Stats.StatsProperty, System.Decimal], ):
        ...

    @typing.overload
    @staticmethod
    def Compare(props: AdventureBot.StructFlag[AdventureBot.User.Stats.StatsProperty], self: AdventureBot.User.Stats.StatsEffect, other: AdventureBot.User.Stats.StatsEffect, ) -> System.Int32:
        ...

    @typing.overload
    @staticmethod
    def CreateComparer(props: AdventureBot.StructFlag[AdventureBot.User.Stats.StatsProperty], ) -> System.Collections.Generic.IComparer[AdventureBot.User.Stats.StatsEffect]:
        ...

    @typing.overload
    def Clone(self, ) -> AdventureBot.User.Stats.StatsEffect:
        ...

    @typing.overload
    def GetStatOrNull(self, property: AdventureBot.User.Stats.StatsProperty, ) -> System.Nullable[System.Decimal]:
        ...

class UserLevel(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # properties
    @property
    def Level(self) -> System.Int32:
        ...

    @property
    def ExpirenceRequired(self) -> System.Decimal:
        ...

    @property
    def ExpirenceCollected(self) -> System.Decimal:
        ...

    # methods
    @typing.overload
    def __init__(self, user: AdventureBot.User.User, ):
        ...

    @typing.overload
    def __init__(self, level: System.Int32, expirenceRequired: System.Decimal, expirenceCollected: System.Decimal, ):
        ...

    @typing.overload
    def AddXp(self, xp: System.Decimal, ) -> None:
        ...

