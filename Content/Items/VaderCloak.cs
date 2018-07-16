using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("vader/cloak")]
    public class VaderCloak : ItemBase
    {
        public override Flag<BuyGroup> Group => new Flag<BuyGroup>();
        public override string Name => "Темный плащ";
        public override string Description => string.Empty;
        public override decimal? Price => null;
        public override string Identifier => "vader/cloak";

        public override StatsEffect Effect => new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Defence, 20}
        });

        public override bool CanUse(User user, ItemInfo info)
        {
            return false;
        }
    }
}