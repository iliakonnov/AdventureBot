using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item(Id)]
    public class BeornSkin : ItemBase
    {
        public const string Id = "beorn/skin";
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Шкура беорна";
        public override string Description => "Крепкая";
        public override decimal? Price => null;
        public override string Identifier => Id;

        public override StatsEffect Effect => new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Health, 20},
            {StatsProperty.Defence, 20}
        });

        public override bool CanUse(User user, ItemInfo info)
        {
            return false;
        }
    }
}