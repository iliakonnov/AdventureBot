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
        public override decimal Health => 1000;

        public override decimal GetDamage(User user)
        {
            return user.Random.Next(40, 50);
        }

        public override void Enter(User user, string[][] buttons)
        {
            SendMessage(user,
                "Перед тобой стоит солдат в тяжелой броне с двухглавым орлом на груди и мечом-пилой в руке", buttons);
            SendMessage(user, "— Славься Император!", buttons);
        }

        public override bool OnRunaway(User user)
        {
            return true;
        }

        public override void OnWon(User user)
        {
            SendMessage(user, "Победив космодесантника, ты подобрал *цепной меч*");
            user.ItemManager.Add(new ItemInfo("spacemarine/chainsword", 1));
        }
    }
}