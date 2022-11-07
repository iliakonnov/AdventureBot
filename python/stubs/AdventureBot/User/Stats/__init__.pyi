from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import AdventureBot.User
import AdventureBot
import AdventureBot.User.Stats
import System.Collections.Generic


class ChangeType(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Add: int = ...
    Set: int = ...
    Multiply: int = ...

class Statistics(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.User: AdventureBot.User.User
        ...

    # static fields

    # properties
    @property
    def MonsterCount(self) -> int:
        ...
    @MonsterCount.setter
    def MonsterCount(self, val: int):
        ...

    @property
    def RoomsCount(self) -> int:
        ...
    @RoomsCount.setter
    def RoomsCount(self, val: int):
        ...

    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    def __init__(self, user: AdventureBot.User.User, ):
        ...

    def RoomTraveled(self, ) -> None:
        ...

    def MonsterKilled(self, ) -> None:
        ...

    def GoldChanged(self, ) -> None:
        ...

class StatsProperty(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Health: int = ...
    Intelligence: int = ...
    Strength: int = ...
    Mana: int = ...
    Stamina: int = ...
    Defence: int = ...
    Karma: int = ...

class Stats(AdventureBot.ISerializable, AdventureBot.User.Stats.StatsEffect):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields
    DefaultStats: System.Collections.Generic.IReadOnlyDictionary[int, System.Decimal] = ...
    Emojis: System.Collections.Generic.IReadOnlyDictionary[int, str] = ...

    # properties
    @property
    def ChangeType(self) -> int:
        ...

    @property
    def Effect(self) -> System.Collections.Generic.IReadOnlyDictionary[int, System.Decimal]:
        ...

    # methods
    @typing.overload
    def __init__(self, effect: System.Collections.Generic.IReadOnlyDictionary[int, System.Decimal], ):
        ...

    @typing.overload
    def __init__(self, ):
        ...

    def Apply(self, effect: AdventureBot.User.Stats.StatsEffect, ) -> AdventureBot.User.Stats.Stats:
        ...

    def GetStat(self, property: int, ) -> System.Decimal:
        ...

class StatsEffect(AdventureBot.ISerializable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    @property
    def ChangeType(self) -> int:
        ...

    @property
    def Effect(self) -> System.Collections.Generic.IReadOnlyDictionary[int, System.Decimal]:
        ...

    # methods
    def __init__(self, changeType: int, effect: System.Collections.Generic.IReadOnlyDictionary[int, System.Decimal], ):
        ...

    @staticmethod
    def Compare(props: AdventureBot.StructFlag[int], self: AdventureBot.User.Stats.StatsEffect, other: AdventureBot.User.Stats.StatsEffect, ) -> int:
        ...

    @staticmethod
    def CreateComparer(props: AdventureBot.StructFlag[int], ) -> System.Collections.Generic.IComparer[AdventureBot.User.Stats.StatsEffect]:
        ...

    def Clone(self, ) -> AdventureBot.User.Stats.StatsEffect:
        ...

    def GetStatOrNull(self, property: int, ) -> System.Nullable[System.Decimal]:
        ...

class UserLevel(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.User: AdventureBot.User.User
        ...

    # static fields

    # properties
    @property
    def Level(self) -> int:
        ...
    @Level.setter
    def Level(self, val: int):
        ...

    @property
    def ExpirenceRequired(self) -> System.Decimal:
        ...
    @ExpirenceRequired.setter
    def ExpirenceRequired(self, val: System.Decimal):
        ...

    @property
    def ExpirenceCollected(self) -> System.Decimal:
        ...
    @ExpirenceCollected.setter
    def ExpirenceCollected(self, val: System.Decimal):
        ...

    # methods
    @typing.overload
    def __init__(self, user: AdventureBot.User.User, ):
        ...

    @typing.overload
    def __init__(self, level: int, expirenceRequired: System.Decimal, expirenceCollected: System.Decimal, ):
        ...

    def AddXp(self, xp: System.Decimal, ) -> None:
        ...

