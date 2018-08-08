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
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Хоккейная маска";
        public override string Description => string.Empty;
        public override decimal? Price => null;
        public override string Identifier => "jason/mask";

        public override StatsEffect Effect => new StatsEffect(ChangeType.Set, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Defence, 15}
        });

        public override bool CanUse(User user, ItemInfo info)
        {
            return false;
        }
    }
}