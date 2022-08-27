using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Halls.Items;

[Item(Id)]
public class HolyBomb : ItemBase
{
    public const string Id = "halls/HolyBomb";
    public override StructFlag<BuyGroup> Group => new();
    public override string Name => "Святая бомба";
    public override string Description => "А-а-аллилуйя!";
    public override decimal? Price => 250;
    public override string Identifier => Id;
    public override StatsEffect Effect => null;

    public override bool CanUse(User user, ItemInfo info)
    {
        return user.RoomManager.GetRoom() is EvilMonsterBase;
    }

    public override void OnUse(User user, ItemInfo info)
    {
        if (!(user.RoomManager.GetRoom() is EvilMonsterBase monster))
        {
            return;
        }

        if (user.ItemManager.Remove(new ItemInfo(Identifier, 1)))
        {
            monster.MakeDamage(user, 1000);
        }
    }
}