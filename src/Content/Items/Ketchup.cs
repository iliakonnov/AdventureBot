﻿using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items;

[Item(Id)]
public class Ketchup : ItemBase
{
    public const string Id = "sans/ketchup";
    public override StructFlag<BuyGroup> Group => new();
    public override string Name => "Кетчуп";
    public override string Description => "Вкусный кетчуп";
    public override decimal? Price => 180;
    public override string Identifier => Id;
    public override StatsEffect Effect => null;

    public override bool CanUse(User user, ItemInfo info)
    {
        return true;
    }

    public override void OnUse(User user, ItemInfo info)
    {
        if (user.ItemManager.Remove(new ItemInfo(Identifier, 1)))
        {
            user.Info.ChangeStats(StatsProperty.Health, user.Info.MaxStats.GetStat(StatsProperty.Health), true);
        }
    }
}