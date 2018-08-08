using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("appletree/notebook")]
    public class Notebook : ItemBase
    {
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Дневник Ньютона";
        public override string Description => string.Empty;
        public override decimal? Price => null;
        public override string Identifier => "appletree/notebook";

        public override StatsEffect Effect => new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Intelligence, 5}
        });

        public override bool CanUse(User user, ItemInfo info)
        {
            return false;
        }
    }
}