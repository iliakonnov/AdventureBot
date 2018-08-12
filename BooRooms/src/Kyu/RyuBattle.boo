namespace BooRooms.Kyu

import AdventureBot.Room from AdventureBot
import AdventureBot.User from AdventureBot
import AdventureBot.Item from AdventureBot

[Room("ryu/battle")]
class RyuBattle(MonsterBase):
    public Name as string:
        get:
            return "Битва"

    public Identifier as string:
        get:
            return "ryu/battle"

    protected override Health as decimal:
        get:
            return 2000

    protected override def GetDamage(user as User):
        return 90

    protected override def Enter(user as User, buttons as ((string))):
        SendMessage(user, "Голос из ниоткуда прокричал \"FIGHT!\"", buttons)

    protected override def OnRunaway(user as User):
        return true

    protected override def OnWon(user as User):
        user.ItemManager.Add(ItemInfo("ryu/red_bandage", 0))
