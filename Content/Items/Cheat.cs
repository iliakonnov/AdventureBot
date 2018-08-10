#if DEBUG

using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("item/cheat")]
    public class Cheat : ItemBase
    {
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Отладочный предмет";
        public override string Description => "Его у вас быть не должно.";
        public override decimal? Price => short.MaxValue;
        public override string Identifier => "item/cheat";

        public override StatsEffect Effect => new StatsEffect(ChangeType.Set, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Health, 300},
            {StatsProperty.Defence, 300},
            {StatsProperty.Intelligence, 300},
            {StatsProperty.Mana, 300},
            {StatsProperty.Stamina, 300},
            {StatsProperty.Strength, 300}
        });

        public override bool CanUse(User user, ItemInfo info)
        {
            return false;
        }
    }
}

#endif