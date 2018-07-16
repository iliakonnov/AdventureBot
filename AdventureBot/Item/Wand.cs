using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User.Stats;

namespace AdventureBot.Item
{
    [Item("wand")]
    public class Wand : ItemBase
    {
        public override string Name => "Волшебная палка";

        public override string Description =>
            "Ты даже не знаешь откуда она взялась. Такое чувство, что она всегда была с тобой";

        public override decimal? Price => null;
        public override Flag<BuyGroup> Group => new Flag<BuyGroup>(new BuyGroup[0]);

        public override string Identifier => "wand";
        public override StatsEffect Effect => null;

        public override void OnUse(User.User user, ItemInfo info)
        {
            var room = user.RoomManager.GetRoom();
            if (room is IMonster monsterRoom)
            {
                user.MessageManager.SendMessage(new SentMessage
                {
                    Text =
                        $"Ты что-то колдуешь и монстр, скрывающийся под псевдонмом {monsterRoom.Name}, уменьшается в размерах."
                });
                monsterRoom.MakeDamage(user, user.Info.CurrentStats.Effect[StatsProperty.Intelligence]);
            }
            else
            {
                user.MessageManager.SendMessage(new SentMessage
                {
                    Text = "Ты хотел что-нибудь наколдовать, но рядом не было ничего интересного."
                });
            }
        }

        public override bool CanUse(User.User user, ItemInfo info)
        {
            return user.RoomManager.GetRoom() is IMonster;
        }
    }
}