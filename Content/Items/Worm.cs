using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("worms/worm")]
    public class Worm : ItemBase
    {
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>(BuyGroup.Market);
        public override string Name => "Червяк";
        public override string Description => "Маленький, но храбрый";
        public override decimal? Price => 1m;
        public override string Identifier => "worms/worm";
        public override StatsEffect Effect => null;

        public override bool CanUse(User user, ItemInfo info)
        {
            return false;
        }
    }
}