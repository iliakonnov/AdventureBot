using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("jason/mask")]
    public class HockeyMask : ItemBase
    {
        public override Flag<BuyGroup> Group => new Flag<BuyGroup>();
        public override string Name => "Хоккейная маска";
        public override string Description => string.Empty;
        public override decimal? Price => null;
        public override string Identifier => "jason/mask";

        // TODO: Defence
        public override StatsEffect Effect => new StatsEffect(ChangeType.Set, new Dictionary<StatsProperty, decimal>());

        public override bool CanUse(User user, ItemInfo info)
        {
            return false;
        }
    }
}