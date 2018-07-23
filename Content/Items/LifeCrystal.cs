using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("lifecrystal/shard")]
    public class LifeCrystalShard : ItemBase
    {
        public override Flag<BuyGroup> Group => new Flag<BuyGroup>(BuyGroup.Merchant);
        public override string Name => "Осколок кристалла жизни";
        public override string Description => "Собери четыре";
        public override decimal? Price => 750;
        public override string Identifier => "lifecrystal/shard";
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
                user.ItemManager.Add(new ItemInfo("item/lifecrystal", 1));
            }
        }
    }

    [Item("item/lifecrystal")]
    public class LifeCrystal : ItemBase
    {
        public override Flag<BuyGroup> Group => new Flag<BuyGroup>();
        public override string Name => "Кристалла жизни";
        public override string Description => "Просто активируй";
        public override decimal? Price => null;
        public override string Identifier => "item/lifecrystal";
        public override StatsEffect Effect => null;

        public override bool CanUse(User user, ItemInfo info)
        {
            return true;
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
}