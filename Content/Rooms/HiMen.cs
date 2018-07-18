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
        public override decimal Health => 1500;

        public override decimal GetDamage(User user)
        {
            return 50;
        }

        public override void Enter(User user, string[][] buttons)
        {
            SendMessage(
                user,
                "Невероятно сильный и невероятно быстрый. А еще у него крутая кошка. Ты хочешь себе эту кошку.",
                buttons
            );
        }

        public override bool OnRunaway(User user)
        {
            return true;
        }

        public override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo("himen/cat", 1));
        }
    }
}