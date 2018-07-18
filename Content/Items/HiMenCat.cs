using System;
using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("himen/cat")]
    public class HiMenCat : PetBase
    {
        public override Flag<BuyGroup> Group => new Flag<BuyGroup>();
        public override string Name => "Кошка Хи-мена";
        public override string Description => string.Empty;
        public override decimal? Price => null;
        public override string Identifier => "himen/cat";
        public override StatsEffect Effect => new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Intelligence, 30},
            {StatsProperty.Strength, 30}
        });
        public override bool CanUse(User user, ItemInfo info)
        {
            return false;
        }
    }
}