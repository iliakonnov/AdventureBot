using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item(Id)]
    public class Chainsword : ItemBase
    {
        public const string Id = "spacemarine/chainsword";
        public override string Name => "Цепной меч";
        public override string Description => "Cамый распространенный вид цепного оружия";
        public override decimal? Price => 225;
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Identifier => Id;
        public override StatsEffect Effect => null;

        public override void OnUse(User user, ItemInfo info)
        {
            var room = user.RoomManager.GetRoom();
            if (room is IMonster monsterRoom)
            {
                var bleeding = (int?) (Serializable.Int) GetItemVariables(user).Get("bleeding") ?? 0;

                if (bleeding != 0)
                {
                    user.MessageManager.SendMessage(new SentMessage
                    {
                        Text = "У монстра не хватает конечностей и он истекает кровью"
                    });

                    monsterRoom.MakeDamage(user, 10m * bleeding);
                }

                if (user.Info.ChangeStats(StatsProperty.Stamina, -10))
                {
                    user.MessageManager.SendMessage(new SentMessage
                    {
                        Text =
                            "Цепной меч издает сердитое жужжание, перерастающее в пронзительный визг, когда цепь начинает вгрызаться в врага."
                    });
                    monsterRoom.MakeDamage(user, user.Info.CurrentStats.GetStat(StatsProperty.Strength) + 80);
                    GetItemVariables(user).Set("bleeding", new Serializable.Int(bleeding + 1));
                }
                else
                {
                    user.MessageManager.SendMessage(new SentMessage
                    {
                        Text = "Ты не смог поднять массивный меч."
                    });
                }
            }
            else
            {
                user.MessageManager.SendMessage(new SentMessage
                {
                    Text = "Ты хотел кого-нибудь ударить, но не смог найти подходящих монстров."
                });
            }
        }

        public override bool CanUse(User user, ItemInfo info)
        {
            return user.RoomManager.GetRoom() is IMonster;
        }

        public override void OnEnter(User user, ItemInfo info)
        {
            GetItemVariables(user).Set("bleeding", new Serializable.Int(0));
        }

        public override void OnLeave(User user, ItemInfo info)
        {
            GetItemVariables(user).Set("bleeding", new Serializable.Int(0));
        }
    }
}