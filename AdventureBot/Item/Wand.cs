using System;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User.Stats;

namespace AdventureBot.Item
{
    [Item("wand")]
    public class Wand : ItemBase<Wand>
    {
        public override void OnLeave(User.User user, ItemInfo info)
        {
            throw new NotImplementedException();
        }

        public override string Name { get; set; } = "Волшебная палка";

        public override string Description { get; set; } =
            "Ты даже не знаешь откуда она взялась. Такое чувство, что она всегда была с тобой";

        public override decimal? Price { get; set; } = null;
        public override Flag<BuyGroup> Group { get; set; } = new Flag<BuyGroup>(new BuyGroup[0]);

        public override string Identifier { get; set; } = "wand";
        public override StatsEffect Effect { get; set; } = null;

        public override void OnUse(User.User user, ItemInfo info)
        {
            var room = user.RoomManager.GetRoom();
            if (room is IMonster monsterRoom)
            {
                if (user.Info.ChangeStats(StatsProperty.Mana, -5))
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
                        Text = "У тебя не хватило маны даже на маленькое заклинание"
                    });
                }
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

        public override void OnMessage(User.User user, ItemInfo info)
        {
        }

        public override void OnEnter(User.User user, ItemInfo info)
        {
        }
    }
}