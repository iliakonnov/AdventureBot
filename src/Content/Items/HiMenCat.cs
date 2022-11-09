using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items;

[Item(Id)]
public class HiMenCat : PetBase
{
    public const string Id = "himen/cat";
    public override StructFlag<BuyGroup> Group => new();
    public override string Name => "Кошка Хи-мена";
    public override string Description => string.Empty;
    public override decimal? Price => 375;
    public override string Identifier => Id;

    public override StatsEffect Effect => new(ChangeType.Add, new Dictionary<StatsProperty, decimal>
    {
        {StatsProperty.Intelligence, 30},
        {StatsProperty.Strength, 30}
    });

    public override bool CanUse(User user, ItemInfo info)
    {
        return false;
    }
}