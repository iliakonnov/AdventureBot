using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("tiger/tooth")]
    public class TigerTooth : ItemBase
    {
        public override Flag<BuyGroup> Group => new Flag<BuyGroup>();
        public override string Name => "Клык тигра";
        public override string Description => "Ты с трудом добыл его с невымершого тигра";
        public override decimal? Price => null;
        public override string Identifier => "tiger/tooth";

        public override StatsEffect Effect => new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Strength, 3}
        });

        public override bool CanUse(User user, ItemInfo info)
        {
            return false;
        }
    }
}