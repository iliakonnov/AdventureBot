import clr

import attributes
import clrtype

import AdventureBot
import System
from AdventureBot import StructFlag
from AdventureBot.Item import ItemInfo, ItemBase, BuyGroup
from AdventureBot.Room import IMonster
from AdventureBot.User import User
from AdventureBot.User.Stats import StatsProperty


class Hadoken(ItemBase, metaclass=clrtype.ClrClass):
    __metaclass__ = clrtype.ClrClass
    _clrclassattribs = [attributes.ObjectManager.Item("ryu/hadoken")]

    @property
    def Identifier(self) -> System.String:
        return "ryu/hadoken"

    @property
    def Name(self) -> System.String:
        return "Хадкен"

    @property
    def Description(self) -> System.String:
        return ""

    @property
    def Effect(self) -> AdventureBot.User.Stats.StatsEffect:
        return None

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        return None

    @property
    def Group(self) -> StructFlag[BuyGroup]:
        return StructFlag[BuyGroup]()

    def CanUse(self, user: User, info: ItemInfo) -> System.Boolean:
        return isinstance(user.RoomManager.GetRoom(), IMonster)

    def OnUse(self, user: User, info: ItemInfo) -> None:
        try:
            monster = clr.Convert(user.RoomManager.GetRoom(), IMonster)  # type: IMonster
        except TypeError:
            return

        if user.Info.ChangeStats(StatsProperty.Stamina, -60, False):
            damage = max(
                user.Info.CurrentStats.GetStat(StatsProperty.Strength),
                user.Info.CurrentStats.GetStat(StatsProperty.Intelligence),
            )
            damage = 2 * damage + 100
            monster.MakeDamage(user, damage)
