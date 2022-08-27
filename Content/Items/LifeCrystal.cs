using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items;

[Item(Id)]
public class LifeCrystalShard : ItemBase
{
    public const string Id = "lifecrystal/shard";
    public override StructFlag<BuyGroup> Group => new(BuyGroup.Merchant);
    public override string Name => "Осколок кристалла жизни";
    public override string Description => "Собери четыре";
    public override decimal? Price => 750;
    public override string Identifier => Id;
    public override StatsEffect Effect => null;

    public override bool CanUse(User user, ItemInfo info)
    {
        var shards = user.ItemManager.Get(Identifier);
        return shards != null && shards.Count >= 4;
    }

    public override void OnUse(User user, ItemInfo info)
    {
        if (user.ItemManager.Remove(new ItemInfo(Identifier, 4)))
        {
            user.ItemManager.Add(new ItemInfo(LifeCrystal.Id, 1));
        }
    }
}

[Item(Id)]
public class LifeCrystal : ItemBase
{
    public const string Id = "item/lifecrystal";
    public override StructFlag<BuyGroup> Group => new();
    public override string Name => "Кристалл жизни";
    public override string Description => "Просто активируй";
    public override decimal? Price => null;
    public override string Identifier => Id;
    public override StatsEffect Effect => null;

    public override bool CanUse(User user, ItemInfo info)
    {
        return !(user.RoomManager.GetRoom() is IMonster);
    }

    public override void OnUse(User user, ItemInfo info)
    {
        if (user.ItemManager.Remove(new ItemInfo(Identifier, 1)))
        {
            user.Info.MaxStats = user.Info.MaxStats.Apply(new StatsEffect(ChangeType.Add,
                new Dictionary<StatsProperty, decimal>
                {
                    {StatsProperty.Health, 50}
                }));
        }
    }
}