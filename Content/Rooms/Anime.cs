using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("monster/anime", Difficulity.Medium)]
    public class Anime : MonsterBase
    {
        public override string Name => "Анимешник";
        public override string Identifier => "monster/anime";
        protected override decimal Health => 150;

        protected override decimal GetDamage(User user)
        {
            return 15;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "— Это не просто мультики! Это искусство!", buttons);
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }

        protected override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo("anime/badge", 1));
        }
    }
}