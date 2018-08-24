using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;
using Content.Items;

namespace Content.Halls.Items
{
    [Item(Id)]
    public class Revolver : ItemBase
    {
        public const string Id = "halls/revolver";
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Револьвер «Искупление»";
        public override string Description => string.Empty;
        public override decimal? Price => 600;
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

            decimal damage = 0;
            if (user.ItemManager.Remove(new ItemInfo(HolyBullet.Id, 1)))
            {
                // Holy bullets
                damage = 450;
            }
            else if (user.ItemManager.Remove(new ItemInfo(Bullet.Id, 1)))
            {
                // Normal bullets
                damage = 400;
            }
            else
            {
                user.MessageManager.SendMessage(new SentMessage
                {
                    Text = "У вас нету пуль, как вы собирались стрелять?"
                });
            }

            if (monster is EvilMonsterBase)
            {
                damage *= 1.3M;
            }

            monster.MakeDamage(user, damage);
        }
    }
}