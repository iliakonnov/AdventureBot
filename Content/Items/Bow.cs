using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item(Id)]
    public class Bow : ItemBase
    {
        public const string Id = "legolas/bow";
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Эльфийский лук";
        public override string Description => "Этому луку стрелы не нужны!";
        public override decimal? Price => 350;
        public override string Identifier => Id;
        public override StatsEffect Effect => null;

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

            monster.MakeDamage(user, 300);
        }
    }
}
