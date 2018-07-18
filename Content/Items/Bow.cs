using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("legolas/bow")]
    public class Bow : ItemBase
    {
        public override Flag<BuyGroup> Group => new Flag<BuyGroup>();
        public override string Name => "Эльфийский лук";
        public override string Description => "Этому луку стрелы не нужны!";
        public override decimal? Price => null;
        public override string Identifier => "legolas/bow";
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