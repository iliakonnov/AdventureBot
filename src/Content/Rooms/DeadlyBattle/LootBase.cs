using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Rooms.DeadlyBattle;

public abstract class LootBase : ItemBase
{
    public override string Description => null;
    public override StructFlag<BuyGroup> Group => new();
    public abstract decimal Damage { get; }
    public abstract bool AddDamage { get; }

    public override bool CanUse(User user, ItemInfo info)
    {
        return Damage != 0;
    }

    public override void OnUse(User user, ItemInfo info)
    {
        var room = user.RoomManager.GetRoom();
        if (!(room is IMonster monsterRoom))
        {
            return;
        }

        if (AddDamage)
        {
            monsterRoom.MakeDamage(user, user.Info.CurrentStats.GetStat(StatsProperty.Strength) + Damage);
        }
        else
        {
            monsterRoom.MakeDamage(user, Damage);
        }
    }
}