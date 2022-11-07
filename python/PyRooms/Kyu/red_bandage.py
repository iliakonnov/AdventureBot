import clr
import clrtype
import attributes

import AdventureBot
import System
from System import Decimal
from AdventureBot import StructFlag
from AdventureBot.Item import ItemInfo, ItemBase, BuyGroup
from AdventureBot.User.Stats import StatsProperty, StatsEffect, ChangeType


class RedBandage(ItemBase, metaclass=clrtype.ClrClass):
    __metaclass__ = clrtype.ClrClass
    _clrclassattribs = [attributes.ObjectManager.Item("ryu/red_bandage")]

    @property
    def Identifier(self) -> System.String:
        return "ryu/red_bandage"

    @property
    def Effect(self) -> StatsEffect:
        return StatsEffect(ChangeType.Add, {
            StatsProperty.Strength: Decimal(20.0),
            StatsProperty.Intelligence: Decimal(20.0),
        })

    @property
    def Name(self) -> System.String:
        return "Красная повязка"

    @property
    def Description(self) -> System.String:
        return ""

    @property
    def Price(self) -> System.Nullable[System.Decimal]:
        return None

    @property
    def Group(self) -> StructFlag[BuyGroup]:
        return StructFlag[BuyGroup]()

    def CanUse(self, user: AdventureBot.User.User, info: AdventureBot.Item.ItemInfo) -> System.Boolean:
        return False
