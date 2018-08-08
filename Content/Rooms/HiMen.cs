using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("monster/himen", Difficulity.Hard)]
    public class HiMen : MonsterBase
    {
        public override string Name => "Хи-мен";
        public override string Identifier => "monster/himen";
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
            user.ItemManager.Add(new ItemInfo("himen/cat", 1));
        }
    }
}