using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("monster/SpaceMarine", Difficulity.Hard)]
    public class SpaceMarine : MonsterBase
    {
        public override string Name => "Космодесантник";
        public override string Identifier => "monster/SpaceMarine";
        protected override decimal Health => 1000;

        protected override decimal GetDamage(User user)
        {
            return user.Random.Next(40, 50);
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user,
                "Перед тобой стоит солдат в тяжелой броне с двухглавым орлом на груди и мечом-пилой в руке", buttons);
            SendMessage(user, "— Славься Император!", buttons);
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }

        protected override void OnWon(User user)
        {
            SendMessage(user, "Победив космодесантника, ты подобрал *цепной меч*");
            user.ItemManager.Add(new ItemInfo("spacemarine/chainsword", 1));
        }
    }
}