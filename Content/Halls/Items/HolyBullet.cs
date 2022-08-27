using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Halls.Items;

[Item(Id)]
public class HolyBullet : ItemBase
{
    public const string Id = "item/holyBullet";
    public override StructFlag<BuyGroup> Group => new();
    public override string Name => "Святая пуля";
    public override string Description => "Не спрашивайте, почему серебро стоит дороже золота в пять раз";
    public override decimal? Price => 5;
    public override string Identifier => Id;
    public override StatsEffect Effect => null;

    public override bool CanUse(User user, ItemInfo info)
    {
        return false;
    }
}