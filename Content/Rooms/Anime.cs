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
        public override decimal Health => 150;

        public override decimal GetDamage(User user)
        {
            return 15;
        }

        public override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "— Это не просто мультики! Это искусство!", buttons);
        }

        public override bool OnRunaway(User user)
        {
            return true;
        }

        public override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo("anime/badge", 1));
        }
    }
}