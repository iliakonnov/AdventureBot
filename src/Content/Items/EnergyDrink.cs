using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items;

[Item(Id)]
public class EnergyDrink : ItemBase
{
    public const string Id = "item/energy";
    public override StructFlag<BuyGroup> Group => new(BuyGroup.Market);
    public override string Name => "Энергетик";
    public override string Description => "Для тех, кто хочет жить опасно";
    public override decimal? Price => 100;
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
            user.Info.ChangeStats(StatsProperty.Stamina, user.Info.MaxStats.GetStat(StatsProperty.Stamina));
        }
    }
}