using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("anime/badge")]
    public class AnimeBadge : ItemBase
    {
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Значок \"I ❤️ 宮崎 駿\"";
        public override string Description => "";
        public override decimal? Price => 12;
        public override string Identifier => "anime/badge";

        public override StatsEffect Effect => new StatsEffect(ChangeType.Set, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Intelligence, 1}
        });

        public override bool CanUse(User user, ItemInfo info)
        {
            return false;
        }
    }
}
