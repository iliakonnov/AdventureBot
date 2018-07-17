using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("vader/sword")]
    public class VaderSword : ItemBase
    {
        public override Flag<BuyGroup> Group => new Flag<BuyGroup>();
        public override string Name => "Световой меч";
        public override string Description => "Светится красным";
        public override decimal? Price => null;
        public override string Identifier => "vader/sword";
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

            monster.MakeDamage(user, user.Info.CurrentStats.Effect[StatsProperty.Strength] + 50);
            user.MessageManager.SendMessage(new SentMessage
            {
                Text = "Ты чуть не разрезал монстра пополам"
            });
        }
    }
}