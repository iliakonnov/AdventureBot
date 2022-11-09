﻿using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items;

[Item(Id)]
public class Notebook : ItemBase
{
    public const string Id = "appletree/notebook";
    public override StructFlag<BuyGroup> Group => new();
    public override string Name => "Дневник Ньютона";
    public override string Description => string.Empty;
    public override decimal? Price => 5;
    public override string Identifier => Id;

    public override StatsEffect Effect => new(ChangeType.Add, new Dictionary<StatsProperty, decimal>
    {
        {StatsProperty.Intelligence, 5}
    });

    public override bool CanUse(User user, ItemInfo info)
    {
        return false;
    }
}