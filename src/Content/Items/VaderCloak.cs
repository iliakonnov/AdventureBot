﻿using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items;

[Item(Id)]
public class VaderCloak : ItemBase
{
    public const string Id = "vader/cloak";
    public override StructFlag<BuyGroup> Group => new();
    public override string Name => "Темный плащ";
    public override string Description => string.Empty;
    public override decimal? Price => 80;
    public override string Identifier => Id;

    public override StatsEffect Effect => new(ChangeType.Add, new Dictionary<StatsProperty, decimal>
    {
        {StatsProperty.Defence, 20}
    });

    public override bool CanUse(User user, ItemInfo info)
    {
        return false;
    }
}