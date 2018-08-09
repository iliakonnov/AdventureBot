#if false // Этот файл не должен компилироваться, он только в качестве шаблона

using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item(Id)]
    public class ItemTemplate : ItemBase
    {
        public const string Id = "item/Какой-то уникальный идентификатор";

        // Где предмет можно купить.
        public override StructFlag<BuyGroup> Group =>
            new StructFlag<BuyGroup>(BuyGroup.Guild, BuyGroup.Gym, BuyGroup.Market, BuyGroup.Merchant);

        public override string Name => "Название вещи";
        public override string Description => "Её описание";

        public override decimal? Price => 1234; // Стоимость одной штуки.

        // public override decimal? Price => null;  // Если вещь не продается, то написать так.
        public override string Identifier => Id;

        // Какие эффекты дает предмет, когда активирован
        public override StatsEffect Effect => new StatsEffect(
            // Каким образом он влияет на статы.
            // Если прибавляет, то Add. Если домножает, то Mulitply. Если жестко устанавливает значение, то Set
            ChangeType.Add,

            // На какие статы и насколько он влияет. Всё лишнее нужно просто убрать
            new Dictionary<StatsProperty, decimal>
            {
                {StatsProperty.Defence, 100},
                {StatsProperty.Health, 100},
                {StatsProperty.Intelligence, 100},
                {StatsProperty.Karma, 100},
                {StatsProperty.Mana, 100},
                {StatsProperty.Stamina, 100},
                {StatsProperty.Strength, 100}
            }
        );

        public override bool CanUse(User user, ItemInfo info)
        {
            return false; // Если предмет можно использовать, то true. Если нельзя, то false
        }
    }
}

#endif