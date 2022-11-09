using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items;

[Item(Id)]
public class Bullet : ItemBase
{
    public const string Id = "item/bullet";
    public override StructFlag<BuyGroup> Group => new(BuyGroup.Market);
    public override string Name => "Пуля";
    public override string Description => "Обычная универсальная пуля";
    public override decimal? Price => 3;
    public override string Identifier => Id;
    public override StatsEffect Effect => null;

    public override bool CanUse(User user, ItemInfo info)
    {
        return false;
    }
}