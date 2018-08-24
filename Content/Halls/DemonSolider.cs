using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Halls
{
    [Available(Id, Difficulity.Any, HallsRoot.Id)]
    public class DemonSolider : EvilMonsterBase
    {
        public const string Id = "halls/DemonSolider";
        public override string Name => "Демон-солдат";
        public override string Identifier => Id;
        protected override decimal Health => 100;

        protected override decimal GetDamage(User user)
        {
            return 20;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user,
                "Существа, созданные только для убийства. Отсутствие массивной брони с лихвой восполняется бесконечной яростью и кривыми широкими лезвиями, На твоем месте я бы поскорее нанес первый и последний смертельный удар, чем ждал бы ответного.",
                buttons);
        }

        protected override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo(DemonicEssence.Id, 1));
        }
    }
    
    [Item(Id)]
    public class DemonicEssence : LootBase
    {
        public const string Id = "DemonSolider/Essence";
        public override string Name => "Демоническая сущность";
        public override string Description => string.Empty;
        public override string Identifier => Id;
    }
}