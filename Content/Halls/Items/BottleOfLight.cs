using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Halls.Items;

[Item(Id)]
public class BottleOfLight : ItemBase
{
    public const string Id = "halls/bottleOfLight";
    public override StructFlag<BuyGroup> Group => new();
    public override string Name => "Флакон божественного света";
    public override string Description => "Для демонов это как перцовым баллончиком в глаза.";
    public override decimal? Price => 50;
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
            monster.ForceRun(user);
        }
    }
}