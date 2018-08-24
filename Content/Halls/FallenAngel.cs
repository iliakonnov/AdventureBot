using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Halls
{
    [Available(Id, Difficulity.Any, HallsRoot.Id)]
    public class FallenAngel : EvilMonsterBase
    {
        public const string Id = "halls/fallenAngel";

        public override string Name => "Падший ангел";
        public override string Identifier => Id;
        protected override decimal Health => 120;

        protected override decimal GetDamage(User user)
        {
            return 15;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user,
                "То, что когда-то называлось ангелом, предстало перед тобой в новом обличии. Покрытый голубым пламенем, он жаждет только мести и кровопролития. Массивная серебряная броня покрылась трещинами, крылья уже не пригодны для полета, а меч еще режет только благодаря ярости хозяина. Пора браться за оружие.",
                buttons);
        }

        protected override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo(FallenAngelShard.Id, 1));
        }
    }

    [Item(Id)]
    public class FallenAngelShard : LootBase
    {
        public const string Id = "fallenAngel/armorShard";
        public override string Name => "Осколок брони падшего ангела";
        public override string Description => string.Empty;
        public override string Identifier => Id;
    }
}