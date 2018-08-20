using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item(Id)]
    public class Narzan : ItemBase
    {
        public const string Id = "wedding/narzan";
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Бутылка нарзани";

        public override string Description =>
            "Она появилась в твоём рюкзаке после пьянки с твоими грузинскими друзьями. Отлично помогает от похмелья";

        public override decimal? Price => 80;
        public override string Identifier => Id;
        public override StatsEffect Effect => null;

        public override bool CanUse(User user, ItemInfo info)
        {
            return user.Info.BaseStats.GetStat(StatsProperty.Health) !=
                   user.Info.MaxStats.GetStat(StatsProperty.Health);
        }

        public override void OnUse(User user, ItemInfo info)
        {
            if (user.ItemManager.Remove(new ItemInfo(Identifier, 1)))
            {
                user.Info.ChangeStats(StatsProperty.Health, user.Info.MaxStats.GetStat(StatsProperty.Health), true);
            }
        }
    }
}