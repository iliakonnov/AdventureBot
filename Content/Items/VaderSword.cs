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
    public class VaderSword : ItemBase
    {
        public const string Id = "vader/sword";
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Световой меч";
        public override string Description => "Светится красным";
        public override decimal? Price => 110;
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

            monster.MakeDamage(user, user.Info.CurrentStats.GetStat(StatsProperty.Strength) + 50);
            user.MessageManager.SendMessage(new SentMessage
            {
                Text = "Ты чуть не разрезал монстра пополам"
            });
        }
    }
}