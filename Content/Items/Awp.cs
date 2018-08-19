﻿using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("camper/awp")]
    public class Awp : ItemBase
    {
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "AWP";
        public override string Description => string.Empty;
        public override decimal? Price => 25;
        public override string Identifier => "camper/awp";
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

            var bullets = user.ItemManager.Get("item/bullet")?.Count;
            if (bullets == null)
            {
                user.MessageManager.SendMessage(new SentMessage
                {
                    Text = "Ты попытался выстрелить, но оказалось, что у тебя нету патронов"
                });
                return;
            }

            if (!user.ItemManager.Remove(new ItemInfo("item/bullet", 1)))
            {
                user.MessageManager.SendMessage(new SentMessage
                {
                    Text = "Почему-то тебе не хватило патронов. Странно."
                });
                return;
            }

            monster.MakeDamage(user, 150m);
            user.MessageManager.SendMessage(new SentMessage
            {
                Text = "Ты всадил пулю в монстра"
            });
        }
    }
}
