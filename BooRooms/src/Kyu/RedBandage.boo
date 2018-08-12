namespace BooRooms.Kyu

import System
import System.Collections.Generic
import AdventureBot
import AdventureBot.User from AdventureBot
import AdventureBot.User.Stats from AdventureBot
import AdventureBot.Item from AdventureBot
import AdventureBot.ObjectManager from AdventureBot

[ItemAttribute("ryu/red_bandage")]
class Bandage(ItemBase):
    public override Identifier as string:
        get:
            return "ryu/red_bandage"

    public override Group as StructFlag[of BuyGroup]:
        get:
            return StructFlag[of BuyGroup]()

    public override Name as string:
        get:
            return "Красная повязка"

    public override Description as string:
        get:
            return ""

    public override Price as Nullable[decimal]:
        get:
            return null

    public override Effect as StatsEffect:
        get:
            return StatsEffect(ChangeType.Add, Dictionary[of StatsProperty, decimal]() {
                    StatsProperty.Strength: 20,
                    StatsProperty.Intelligence: 20
                }
            )

    public override def CanUse(user as User, info as ItemInfo) as bool:
        return false

    public override def OnUse(user as User, info as ItemInfo) as void:
        return