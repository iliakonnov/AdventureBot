using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("monster/hedgehog", Difficulity.Easy)]
    public class Hedgehog : MonsterBase
    {
        public override string Name => "Злой ёж";
        public override string Identifier => "monster/hedgehog";
        protected override decimal Health => 30;

        protected override decimal GetDamage(User user)
        {
            return 5;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "Вы встречаете самого настоящего ежа. Удивительно!", buttons);
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }

        protected override void OnWon(User user)
        {
        }
    }
}