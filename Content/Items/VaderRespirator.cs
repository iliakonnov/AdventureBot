using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item(Id)]
    public class VaderRespirator : ItemBase
    {
        public const string Id = "Когда-то её носил великий человек";
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Респираторная маска";
        public override string Description => string.Empty;
        public override decimal? Price => 40;
        public override string Identifier => Id;

        public override StatsEffect Effect => new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Defence, 10}
        });

        public override bool CanUse(User user, ItemInfo info)
        {
            return false;
        }
    }
}
