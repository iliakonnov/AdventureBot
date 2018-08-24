using System;
using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Halls.Items
{
    [Item(Id)]
    public class FighterArmor : ItemBase
    {
        public const string Id = "halls/fighterArmor";

        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Броня истребителя нечисти";
        public override string Description => string.Empty;
        public override decimal? Price => null;
        public override string Identifier => Id;

        public override StatsEffect Effect => new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Defence, 75},
            {StatsProperty.Health, 50}
        });

        public override bool CanUse(User user, ItemInfo info)
        {
            return false;
        }
    }
}