using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;
using Content.Items;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Hard)]
    public class SpaceMarine : MonsterBase
    {
        public const string Id = "monster/SpaceMarine";
        public override string Name => "Космодесантник";
        public override string Identifier => Id;
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
            SendMessage(user, "Победив космодесантника, ты подобрал <b>цепной меч</b>");
            user.ItemManager.Add(new ItemInfo(Chainsword.Id, 1));
        }
    }
}