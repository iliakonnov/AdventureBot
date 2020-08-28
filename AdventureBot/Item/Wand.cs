using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User.Stats;

namespace AdventureBot.Item
{
    [Item(Id)]
    public class Wand : ItemBase
    {
        public const string Id = "wand";
        public override string Name => "Волшебная палка";

        public override string Description =>
            "Ты даже не знаешь откуда она взялась. Такое чувство, что она всегда была с тобой";

        public override decimal? Price => null;
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>(BuyGroup.NotSellable);
        public override string Identifier => Id;
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
                monsterRoom.MakeDamage(user, user.Info.CurrentStats.GetStat(StatsProperty.Intelligence));
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