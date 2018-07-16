using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content
{
    [Available("monster/hedgehog")]
    public class Hedgehog : MonsterBase
    {
        public override string Name => "Злой ёж";
        public override string Identifier => "monster/hedgehog";
        public override decimal Health => 30;
        
        public override decimal GetDamage(User user)
        {
            return 5;
        }

        public override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "Вы встречаете самого настоящего ежа. Удивительно!", buttons);
        }

        public override bool OnRunaway(User user)
        {
            return true;
        }
    }
}