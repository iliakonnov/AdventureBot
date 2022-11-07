from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import AdventureBot
import System.Collections.Generic
import AdventureBot.Room.BossBase
import AdventureBot.Room


class Attacker(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.DamageDealed: System.Decimal
        self.UserId: AdventureBot.UserId
        ...

    # static fields

    # properties
    # methods
    def __init__(self, ):
        ...

    @staticmethod
    def Load(list: AdventureBot.SerializableList, ) -> System.Collections.Generic.List[AdventureBot.Room.BossBase.Attacker]:
        ...

    @staticmethod
    def Save(attackers: System.Collections.Generic.IEnumerable[AdventureBot.Room.BossBase.Attacker], ) -> AdventureBot.SerializableList:
        ...

class Variables(System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Attackers: System.Collections.Generic.List[AdventureBot.Room.BossBase.Attacker]
        self.Gold: System.Decimal
        self.Health: System.Decimal
        self.TotalDamage: System.Decimal
        ...

    # static fields

    # properties
    # methods
    def __init__(self, boss: AdventureBot.Room.BossBase, ):
        ...

    def Dispose(self, ) -> None:
        ...

    def Save(self, ) -> None:
        ...

    def Remove(self, ) -> None:
        ...

