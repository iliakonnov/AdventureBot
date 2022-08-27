using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items;

[Item(Id)]
public class TigerTooth : ItemBase
{
    public const string Id = "tiger/tooth";
    public override StructFlag<BuyGroup> Group => new();
    public override string Name => "Клык тигра";
    public override string Description => "Ты с трудом добыл его с невымершого тигра";
    public override decimal? Price => 4;
    public override string Identifier => Id;

    public override StatsEffect Effect => new(ChangeType.Add, new Dictionary<StatsProperty, decimal>
    {
        {StatsProperty.Strength, 3}
    });

    public override bool CanUse(User user, ItemInfo info)
    {
        return false;
    }
}