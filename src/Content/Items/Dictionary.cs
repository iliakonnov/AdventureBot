using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items;

[Item(Id)]
public class DictionaryDahl : ItemBase
{
    public const string Id = "grammar/dictionary_dahl";
    public override StructFlag<BuyGroup> Group => new();
    public override string Name => "Словарь Даля";

    public override string Description =>
        "Говорят, что кто-то даже пытался себя убить этим словарем. Что ж, слово действительно может ранить.";

    public override decimal? Price => 10;
    public override string Identifier => Id;

    public override StatsEffect Effect => new(ChangeType.Add, new Dictionary<StatsProperty, decimal>
    {
        {StatsProperty.Intelligence, 12}
    });

    public override bool CanUse(User user, ItemInfo info)
    {
        return false;
    }
}

[Item(Id)]
public class DictionaryOzhegov : ItemBase
{
    public const string Id = "grammar/dictionary_ozhegov";
    public override StructFlag<BuyGroup> Group => new();
    public override string Name => "Словарь Ожегова";
    public override string Description => string.Empty;
    public override decimal? Price => 5;
    public override string Identifier => Id;

    public override StatsEffect Effect => new(ChangeType.Add, new Dictionary<StatsProperty, decimal>
    {
        {StatsProperty.Intelligence, 12}
    });

    public override bool CanUse(User user, ItemInfo info)
    {
        return false;
    }
}