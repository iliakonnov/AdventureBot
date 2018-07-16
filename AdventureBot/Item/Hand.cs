using System;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User.Stats;

namespace AdventureBot.Item
{
    [Item("hand")]
    public class Hand : ItemBase<Hand>
    {
        public override void OnLeave(User.User user, ItemInfo info)
        {
            throw new NotImplementedException();
        }

        public override string Name { get; set; } = "Рука";
        public override string Description { get; set; } =
            "Самая обычная рука. У каждого такая есть, а у некторых даже не одна.";

        public override decimal? Price { get; set; } = null;
        public override Flag<BuyGroup> Group { get; set; } = new Flag<BuyGroup>(new BuyGroup[0]);

        public override string Identifier { get; set; } = "hand";
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
                        Text = $"Ты бьешь ужасного монстра, известного как {monsterRoom.Name} своей рукой!"
                    });
                    monsterRoom.MakeDamage(user, user.Info.CurrentStats.Effect[StatsProperty.Strength]);
                }
                else
                {
                    user.MessageManager.SendMessage(new SentMessage
                    {
                        Text = "Ты настолько устал, что монстр не заметил твоего удара"
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