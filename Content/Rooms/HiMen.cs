using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;
using Content.Items;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Hard, TownRoot.Id)]
    public class HiMen : MonsterBase
    {
        public const string Id = "monster/himen";
        public override string Name => "Хи-мен";
        public override string Identifier => Id;
        protected override decimal Health => 1500;

        protected override decimal GetDamage(User user)
        {
            return 50;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(
                user,
                "Невероятно сильный и невероятно быстрый. А еще у него крутая кошка. Ты хочешь себе эту кошку.",
                buttons
            );
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }

        protected override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo(HiMenCat.Id, 1));
        }
    }
}