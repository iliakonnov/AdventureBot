from __future__ import annotations
import typing, abc, enum
from stubhelper import *

import System
import System.Collections.Generic
import AdventureBot.Room.BossBase
import AdventureBot.Room
import AdventureBot


class Variables(System.IDisposable, System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.Attackers: System.Collections.Generic.List[AdventureBot.Room.BossBase.Attacker]
        self.Gold: System.Decimal
        self.Health: System.Decimal
        self.TotalDamage: System.Decimal
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, boss: AdventureBot.Room.BossBase, ):
        ...

    @typing.overload
    def Dispose(self, ) -> None:
        ...

    @typing.overload
    def Save(self, ) -> None:
        ...

    @typing.overload
    def Remove(self, ) -> None:
        ...

class Attacker(System.Object):
    @typing.overload
    def __init__(self, **kwargs):
        self.DamageDealed: System.Decimal
        self.UserId: AdventureBot.UserId
        ...

    # properties
    # methods
    @typing.overload
    def __init__(self, ):
        ...

    @typing.overload
    @staticmethod
    def Load(list: AdventureBot.SerializableList, ) -> System.Collections.Generic.List[AdventureBot.Room.BossBase.Attacker]:
        ...

    @typing.overload
    @staticmethod
    def Save(attackers: System.Collections.Generic.IEnumerable[AdventureBot.Room.BossBase.Attacker], ) -> AdventureBot.SerializableList:
        ...

