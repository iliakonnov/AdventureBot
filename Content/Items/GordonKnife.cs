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
    public class GordonKnife : ItemBase
    {
        public const string Id = "gordonRamsey/knife";
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Нож Шефа";
        public override string Description => string.Empty;
        public override decimal? Price => 20;
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

            if (user.Info.ChangeStats(StatsProperty.Stamina, -15))
            {
                monster.MakeDamage(user, user.Info.CurrentStats.GetStat(StatsProperty.Strength) + 15);
            }
            else
            {
                user.MessageManager.SendMessage(new SentMessage
                {
                    Text = "Ты слишком устал"
                });
            }
        }
    }
}