using System;
using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("starlight/wand")]
    public class StarlightWand : ItemBase
    {
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Посох Старлайт";
        public override string Description => string.Empty;
        public override decimal? Price => null;
        public override string Identifier => "starlight/wand";
        public override StatsEffect Effect => null;

        public override bool CanUse(User user, ItemInfo info)
        {
            if (!(user.RoomManager.GetRoom() is IMonster monster))
            {
                return false;
            }

            return monster.GetCurrentHealth(user) <= 30;
        }

        public override void OnUse(User user, ItemInfo info)
        {
            if (!(user.RoomManager.GetRoom() is IMonster monster))
            {
                return;
            }

            if (monster.GetCurrentHealth(user) > 30)
            {
                return;
            }

            var rnd = user.Random.Next(0, 3);
            string propText;
            switch (rnd)
            {
                case 0:
                    propText = "силу";
                    user.MessageManager.ShownStats |= ShownStats.Strength;
                    user.ItemManager.Add(new ItemInfo("starlight/strength", 1));
                    break;
                case 1:
                    propText = "интеллект";
                    user.ItemManager.Add(new ItemInfo("starlight/intelligence", 1));
                    user.MessageManager.ShownStats |= ShownStats.Intelligence;
                    break;
                case 2:
                    propText = "защиту";
                    user.ItemManager.Add(new ItemInfo("starlight/defence", 1));
                    user.MessageManager.ShownStats |= ShownStats.Defence;
                    break;
                default:
                    throw new ArgumentOutOfRangeException(nameof(rnd));
            }

            user.MessageManager.SendMessage(new SentMessage
            {
                Text = $"Вы поглощаете {propText} монстра!"
            });
            monster.MakeDamage(user, 1_000_000);
        }
    }

    public abstract class BaseSoul : ItemBase
    {
        public abstract StatsProperty Property { get; }

        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Description => "Ты извлек её из монстра";
        public override decimal? Price => 0;
        public override bool IsAlwaysActive => true;

        public override StatsEffect Effect => new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
        {
            {Property, 1}
        });

        public override bool CanUse(User user, ItemInfo info)
        {
            return false;
        }
    }

    [Item("starlight/intelligence")]
    public class SmartSoul : BaseSoul
    {
        public override string Name => "Умная душа монстра";
        public override string Identifier => "starlight/intelligence";
        public override StatsProperty Property => StatsProperty.Intelligence;
    }

    [Item("starlight/strength")]
    public class StrongSoul : BaseSoul
    {
        public override string Name => "Сильная душа монстра";
        public override string Identifier => "starlight/strength";
        public override StatsProperty Property => StatsProperty.Strength;
    }

    [Item("starlight/defence")]
    public class StoneSoul : BaseSoul
    {
        public override string Name => "Крепкая душа монстра";
        public override string Identifier => "starlight/defence";
        public override StatsProperty Property => StatsProperty.Defence;
    }
}