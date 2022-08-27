using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items;

[Item(Id)]
public class HockeyMask : ItemBase
{
    public const string Id = "jason/mask";
    public override StructFlag<BuyGroup> Group => new();
    public override string Name => "Хоккейная маска";
    public override string Description => string.Empty;
    public override decimal? Price => 50;
    public override string Identifier => Id;

    public override StatsEffect Effect => new(ChangeType.Set, new Dictionary<StatsProperty, decimal>
    {
        {StatsProperty.Defence, 15}
    });

    public override bool CanUse(User user, ItemInfo info)
    {
        return false;
    }
}