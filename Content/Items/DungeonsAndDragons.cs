using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("geek/d&d")]
    public class DungeonsAndDragons : ItemBase
    {
        public override Flag<BuyGroup> Group => new Flag<BuyGroup>();
        public override string Name => "Dungeons and Dragons";
        public override string Description => string.Empty;
        public override decimal? Price => null;
        public override string Identifier => "geek/d&d";

        public override StatsEffect Effect => new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Intelligence, 10}
        });

        public override bool CanUse(User user, ItemInfo info)
        {
            return false;
        }
    }
}