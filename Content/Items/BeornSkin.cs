using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("beorn/skin")]
    public class BeornSkin : ItemBase
    {
        public override Flag<BuyGroup> Group => new Flag<BuyGroup>();
        public override string Name => "Шкура беорна";
        public override string Description => "Крепкая";
        public override decimal? Price => null;
        public override string Identifier => "beorn/skin";

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