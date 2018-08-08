using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User.Stats;

namespace AdventureBot.Item
{
    [Item("hand")]
    public class Hand : ItemBase
    {
        public override string Name => "Рука";

        public override string Description =>
            "Самая обычная рука. У каждого такая есть, а у некторых даже не одна.";

        public override decimal? Price => null;
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>(new BuyGroup[0]);

        public override string Identifier => "hand";
        public override StatsEffect Effect => null;

        public override void OnUse(User.User user, ItemInfo info)
        {
            var room = user.RoomManager.GetRoom();
            if (room is IMonster monsterRoom)
            {
                user.MessageManager.SendMessage(new SentMessage
                {
                    Text = $"Ты бьешь ужасного монстра, известного как {monsterRoom.Name} своей рукой!"
                });
                monsterRoom.MakeDamage(user, user.Info.CurrentStats.Effect[StatsProperty.Strength]);
            }
            else
            {
                user.MessageManager.SendMessage(new SentMessage
                {
                    Text = "Ты хотел кого-нибудь ударить, но не смог найти подходящих монстров."
                });
            }
        }

        public override bool CanUse(User.User user, ItemInfo info)
        {
            return user.RoomManager.GetRoom() is IMonster;
        }
    }
}