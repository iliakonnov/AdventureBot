﻿using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("wedding/narzan")]
    public class Narzan : ItemBase
    {
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Бутылка нарзани";

        public override string Description =>
            "Она появилась в твоём рюкзаке после пьянки с твоими грузинскими друзьями. Отлично помогает от похмелья";

        public override decimal? Price => 80;
        public override string Identifier => "wedding/narzan";
        public override StatsEffect Effect => null;

        public override bool CanUse(User user, ItemInfo info)
        {
            return user.Info.BaseStats.GetStat(StatsProperty.Health) !=
                   user.Info.MaxStats.GetStat(StatsProperty.Health);
        }

        public override void OnUse(User user, ItemInfo info)
        {
            user.Info.ChangeStats(StatsProperty.Health, user.Info.MaxStats.GetStat(StatsProperty.Health), true);
        }
    }
}
