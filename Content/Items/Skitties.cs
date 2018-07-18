using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("skitties/candy")]
    public class Skitties : ItemBase
    {
        public override Flag<BuyGroup> Group => new Flag<BuyGroup>();
        public override string Name => "Конфета \"Skitties\"";
        public override string Description => string.Empty;
        public override decimal? Price => 50;
        public override string Identifier => "skitties/candy";
        public override StatsEffect Effect => null;

        public override bool CanUse(User user, ItemInfo info)
        {
            return true;
        }

        public override void OnUse(User user, ItemInfo info)
        {
            if (user.ItemManager.Remove(new ItemInfo(Identifier, 1)))
            {
                user.Info.ChangeStats(StatsProperty.Health, 25);
            }
        }
    }
}