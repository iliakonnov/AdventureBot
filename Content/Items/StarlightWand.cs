using System;
using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items;

[Item(Id)]
public class StarlightWand : ItemBase
{
    public const string Id = "starlight/wand";
    public override StructFlag<BuyGroup> Group => new();
    public override string Name => "Посох Старлайт";
    public override string Description => string.Empty;
    public override decimal? Price => 300;
    public override string Identifier => Id;
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
                user.ItemManager.Add(new ItemInfo(StrongSoul.Id, 1));
                break;
            case 1:
                propText = "интеллект";
                user.ItemManager.Add(new ItemInfo(SmartSoul.Id, 1));
                user.MessageManager.ShownStats |= ShownStats.Intelligence;
                break;
            case 2:
                propText = "защиту";
                user.ItemManager.Add(new ItemInfo(StoneSoul.Id, 1));
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

    public override StructFlag<BuyGroup> Group => new();
    public override string Description => "Ты извлек её из монстра";
    public override decimal? Price => 0;
    public override bool IsAlwaysActive => true;

    public override StatsEffect Effect => new(ChangeType.Add, new Dictionary<StatsProperty, decimal>
    {
        {Property, 1}
    });

    public override bool CanUse(User user, ItemInfo info)
    {
        return false;
    }
}

[Item(Id)]
public class SmartSoul : BaseSoul
{
    public const string Id = "starlight/intelligence";
    public override string Name => "Умная душа монстра";
    public override string Identifier => Id;
    public override StatsProperty Property => StatsProperty.Intelligence;
}

[Item(Id)]
public class StrongSoul : BaseSoul
{
    public const string Id = "starlight/strength";
    public override string Name => "Сильная душа монстра";
    public override string Identifier => Id;
    public override StatsProperty Property => StatsProperty.Strength;
}

[Item(Id)]
public class StoneSoul : BaseSoul
{
    public const string Id = "starlight/defence";
    public override string Name => "Крепкая душа монстра";
    public override string Identifier => Id;
    public override StatsProperty Property => StatsProperty.Defence;
}