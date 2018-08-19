﻿using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("voldemort/wand")]
    public class ElderWand : ItemBase
    {
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Бузиная палочка";
        public override string Description => string.Empty;
        public override decimal? Price => 350;
        public override string Identifier => "voldemort/wand";
        public override StatsEffect Effect => null;

        public override bool CanUse(User user, ItemInfo info)
        {
            return true;
        }

        public override void OnUse(User user, ItemInfo info)
        {
            user.MessageManager.SendMessage(new SentMessage
            {
                Text = "Эта палочка испугала всех вокруг и ты попытался убежать."
            });
            user.RoomManager.Leave();
        }
    }
}
