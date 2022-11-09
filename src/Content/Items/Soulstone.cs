﻿using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;
using Content.Rooms;

namespace Content.Items;

[Item(Id)]
public class Soulstone : ItemBase
{
    public const string Id = "portal/soulstone";

    public override StructFlag<BuyGroup> Group => new();
    public override string Name => "Камень Души";
    public override string Description => string.Empty;
    public override decimal? Price => null;
    public override string Identifier => Id;
    public override StatsEffect Effect => null;

    public override bool CanUse(User user, ItemInfo info)
    {
        return info.Count >= 6;
    }

    public override void OnAdd(User user, ItemInfo info, int count)
    {
        if (info.Count >= 6)
        {
            user.RoomManager.Go(Thanos.Id);
        }
    }

    public override void OnUse(User user, ItemInfo info)
    {
        if (info.Count < 6)
        {
            return;
        }

        user.RoomManager.Go(Thanos.Id);
    }
}