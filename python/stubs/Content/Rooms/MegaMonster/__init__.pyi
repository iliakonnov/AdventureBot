from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import Content.Rooms.MegaMonster
import AdventureBot
import System.Collections.Generic


class BaseStats(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Artifact: bool
        self.Gold: int
        self.KnowledgeGroup: int
        self.KnowledgeLevel: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def LoadRace(self, ) -> Content.Rooms.MegaMonster.RaceStats:
        ...

class StatsContext(System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Stats: Content.Rooms.MegaMonster.ResultStats
        ...

    # static fields

    # properties
    # methods
    def __init__(self, random: System.Random, roomVariables: AdventureBot.VariableContainer, ):
        ...

    def Dispose(self, ) -> None:
        ...

class Knowledge(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Strength: int = ...
    Intelligence: int = ...

class Place(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    None_: int = ...
    Legs: int = ...
    Body: int = ...
    Head: int = ...

class Generator(System.Object, abc.ABC):
    @typing.overload
    def __init__(self, **kwargs):
        ...

    # static fields

    # properties
    # methods
    @staticmethod
    def GenerateStats(random: System.Random, ) -> Content.Rooms.MegaMonster.ResultStats:
        ...

    @staticmethod
    @typing.overload
    def Mutate(stats: Content.Rooms.MegaMonster.RaceStats, property: int, random: System.Random, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Mutate(stats: Content.Rooms.MegaMonster.RaceStats, random: System.Random, ) -> None:
        ...

    @staticmethod
    @typing.overload
    def Shuffle(value: System.Decimal, random: System.Random, ) -> System.Decimal:
        ...

    @staticmethod
    @typing.overload
    def Shuffle(stats: Content.Rooms.MegaMonster.RaceStats, random: System.Random, ) -> Content.Rooms.MegaMonster.ResultStats:
        ...

    @staticmethod
    def LevelToNum(level: int, few: System.Decimal, medium: System.Decimal, many: System.Decimal, ) -> System.Decimal:
        ...

class MonsterProperty(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Artifact: int = ...
    Gold: int = ...
    KnowledgeGroup: int = ...
    KnowledgeLevel: int = ...
    DefenceLevel: int = ...
    Damage: int = ...
    Health: int = ...

class MutateResult(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Increase: int = ...
    IncreaseMany: int = ...
    Decrease: int = ...
    DecreaseMany: int = ...

class Level(enum.Enum, System.IComparable, System.IFormattable, System.IConvertible, System.Enum):
    Few: int = ...
    Medium: int = ...
    Many: int = ...

class RaceStats(Content.Rooms.MegaMonster.BaseStats):
    @typing.overload
    def __init__(self, **kwargs):
        self.Modifiers: System.Collections.Generic.List[str]
        self.Damage: System.Decimal
        self.Defence: int
        self.DefencedPlaces: int
        self.Health: System.Decimal
        self.Name: str
        self.Artifact: bool
        self.Gold: int
        self.KnowledgeGroup: int
        self.KnowledgeLevel: int
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @typing.overload
    def Modify(self, mutate: int, property: int, ) -> None:
        ...

    @typing.overload
    def Modify(self, before: System.Decimal, after: System.Decimal, property: int, ) -> System.Decimal:
        ...

    def Modifiy(self, before: int, after: int, property: int, ) -> int:
        ...

    @typing.overload
    def Mutate(self, newVal: int, property: int, ) -> None:
        ...

    @typing.overload
    def Mutate(self, newVal: System.Decimal, property: int, ) -> None:
        ...

    @typing.overload
    def Mutate(self, newVal: bool, property: int, ) -> None:
        ...

    @typing.overload
    def Mutate(self, newVal: int, property: int, ) -> None:
        ...

    def ToString(self, ) -> str:
        ...

class ResultStats(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.ArtifactId: str
        self.Damage: System.Decimal
        self.Defence: System.Decimal
        self.DefencedPlaces: int
        self.Gold: System.Decimal
        self.Health: System.Decimal
        self.KnowledgeGroup: int
        self.KnowledgeMinimal: System.Decimal
        self.KnowledgeRequired: System.Decimal
        self.Name: str
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    def Serialize(self, container: AdventureBot.VariableContainer, ) -> None:
        ...

    @staticmethod
    def Deserialize(container: AdventureBot.VariableContainer, ) -> Content.Rooms.MegaMonster.ResultStats:
        ...

    def ToString(self, ) -> str:
        ...

