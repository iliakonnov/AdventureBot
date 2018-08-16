using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item(Id)]
    public class Slippers : ItemBase
    {
        public const string Id = "item/slippers";
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>(BuyGroup.Merchant);
        public override string Name => "Мягкие тапочки";
        public override string Description => "Теплые и тихие";
        public override decimal? Price => 300;
        public override string Identifier => Id;
        public override StatsEffect Effect => null;

        public override bool CanUse(User user, ItemInfo info)
        {
            return false;
        }
    }
}