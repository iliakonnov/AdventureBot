using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item(Id)]
    public class MercuryFulminate : ItemBase
    {
        public const string Id = "item/MercuryFulminate";
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>(BuyGroup.Market, BuyGroup.Merchant);
        public override string Name => "Пакетик гремучей ртути";

        public override string Description =>
            "Эту смесь мне дал мой старый знакомый Уолтер Уайт. Просто кинь кристалл на землю и беги!";

        public override decimal? Price => 100;
        public override string Identifier => Id;
        public override StatsEffect Effect => null;
        public override bool CanUse(User user, ItemInfo info)
        {
            return user.RoomManager.GetRoom() is IMonster;
        }

        public override void OnUse(User user, ItemInfo info)
        {
            if (!CanUse(user, info))
            {
                return;
            }

            if (!user.ItemManager.Remove(new ItemInfo(Identifier, 1)))
            {
                return;
            }

            user.Info.MakeDamage(user.Info.CurrentStats.GetStat(StatsProperty.Health) / 2);
            user.RoomManager.Leave();
        }
    }
}