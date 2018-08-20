using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item(Id)]
    public class InfinityGlove : ItemBase
    {
        public const string Id = "thanos/glove";

        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Перчатка Бесконечности";
        public override string Description => string.Empty;
        public override decimal? Price => 160000;
        public override string Identifier => Id;

        public override StatsEffect Effect => new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Defence, 150},
            {StatsProperty.Health, 200},
            {StatsProperty.Karma, -70}
        });

        public override bool IsAlwaysActive => true;

        public override bool CanUse(User user, ItemInfo info)
        {
            return user.RoomManager.GetRoom() is IMonster;
        }

        public override void OnUse(User user, ItemInfo info)
        {
            if (!(user.RoomManager.GetRoom() is IMonster monster))
            {
                return;
            }

            monster.MakeDamage(user, 250);
        }
    }
}