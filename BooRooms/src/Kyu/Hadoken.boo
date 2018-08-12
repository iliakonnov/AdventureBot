namespace BooRooms.Kyu

import System
import AdventureBot
import AdventureBot.Room from AdventureBot
import AdventureBot.User from AdventureBot
import AdventureBot.User.Stats from AdventureBot
import AdventureBot.Item from AdventureBot
import AdventureBot.ObjectManager from AdventureBot

[ItemAttribute("ryu/hadoken")]
class Hadoken(ItemBase):
    public override Identifier as string:
        get:
            return "ryu/hadoken"

    public override Group as StructFlag[of BuyGroup]:
        get:
            return StructFlag[of BuyGroup]()

    public override Name as string:
        get:
            return "Хадкен"

    public override Description as string:
        get:
            return ""

    public override Price as Nullable[decimal]:
        get:
            return null

    public override Effect as StatsEffect:
        get:
            return null

    public override def CanUse(user as User, info as ItemInfo) as bool:
        return user.RoomManager.GetRoom() as IMonster != null

    public override def OnUse(user as User, info as ItemInfo) as void:
        monster = user.RoomManager.GetRoom() as IMonster
        if monster == null:
            return

        if user.Info.ChangeStats(StatsProperty.Stamina, -60, false):
            damage = Math.Max(
                user.Info.CurrentStats.GetStat(StatsProperty.Strength),
                user.Info.CurrentStats.GetStat(StatsProperty.Intelligence)
            )
            damage = 2 * damage + 100
            monster.MakeDamage(user, damage)
