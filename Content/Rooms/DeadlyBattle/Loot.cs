using System.Collections.Generic;
using AdventureBot.ObjectManager;
using AdventureBot.User.Stats;

namespace Content.Rooms.DeadlyBattle
{
    [Item(Id)]
    public class SharpHat : LootBase
    {
        public const string Id = "tournament/sharp_hat";

        public override string Name => "Острая шляпа";
        public override string Identifier => Id;
        public override StatsEffect Effect => null;
        public override decimal? Price => 20;
        public override decimal Damage => 50;
        public override bool AddDamage => false;
    }

    [Item(Id)]
    public class BlueMask : LootBase
    {
        public const string Id = "tournament/blue_mask";

        public override string Name => "Синяя маска";
        public override string Identifier => Id;

        public override StatsEffect Effect => new StatsEffect(ChangeType.Add,
            new Dictionary<StatsProperty, decimal>
            {
                {StatsProperty.Defence, 10}
            }
        );

        public override decimal? Price => 15;
        public override decimal Damage => 0;
        public override bool AddDamage => false;
    }

    [Item(Id)]
    public class Harpoon : LootBase
    {
        public const string Id = "tournament/harpoon";

        public override string Name => "Гарпун";
        public override string Identifier => Id;
        public override StatsEffect Effect => null;
        public override decimal? Price => 10;
        public override decimal Damage => 25;
        public override bool AddDamage => false;
    }

    [Item(Id)]
    public class Nunchaku : LootBase
    {
        public const string Id = "tournament/nunchaku";

        public override string Name => "Нунчаки";
        public override string Identifier => Id;
        public override StatsEffect Effect => null;
        public override decimal? Price => 25;
        public override decimal Damage => 35;
        public override bool AddDamage => true;
    }

    [Item(Id)]
    public class Sunglasses : LootBase
    {
        public const string Id = "tournament/sunglasses";

        public override string Name => "Солнечные очки";
        public override string Identifier => Id;
        public override StatsEffect Effect => null;
        public override decimal? Price => 5;
        public override decimal Damage => 0;
        public override bool AddDamage => false;
    }

    [Item(Id)]
    public class Cigar : LootBase
    {
        public const string Id = "tournament/cigar";

        public override string Name => "Сигара";
        public override string Identifier => Id;
        public override StatsEffect Effect => null;
        public override decimal? Price => 8;
        public override decimal Damage => 15;
        public override bool AddDamage => false;
    }

    [Item(Id)]
    public class Hammer : LootBase
    {
        public const string Id = "tournament/hammer";

        public override string Name => "Молот Шао Кана";
        public override string Identifier => Id;
        public override StatsEffect Effect => null;
        public override decimal? Price => 9999;
        public override decimal Damage => 200;
        public override bool AddDamage => true;
    }
}