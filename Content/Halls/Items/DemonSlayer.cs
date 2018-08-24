using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Halls.Items
{
    [Item(Id)]
    public class DemonSlayer : ItemBase
    {
        public const string Id = "halls/demonSlayer";
        
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Убийца демонов";
        public override string Description => string.Empty;
        public override decimal? Price => null;
        public override string Identifier => Id;
        public override StatsEffect Effect => null;
        
        public override bool CanUse(User user, ItemInfo info)
        {
            return user.RoomManager.GetRoom() is EvilMonsterBase;
        }

        public override void OnUse(User user, ItemInfo info)
        {
            if (!(user.RoomManager.GetRoom() is MonsterBase monster))
            {
                return;
            }

            var damage = user.Info.CurrentStats.GetStat(StatsProperty.Strength);
            damage += 90;

            if (monster is EvilMonsterBase)
            {
                damage *= 1.7M;
            }
            
            monster.MakeDamage(user, damage);
        }
    }
}