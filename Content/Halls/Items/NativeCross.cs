using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Halls.Items
{
    [Item(Id)]
    public class NativeCross : ItemBase
    {
        public const string Id = "halls/nativeCross";

        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Нательный крест";
        public override string Description => "Эта штука защитит твою задницу от длительного горения.";
        public override decimal? Price => 150;
        public override string Identifier => Id;
        public override StatsEffect Effect => null;

        public override bool CanUse(User user, ItemInfo info)
        {
            return false;
        }
    }
}