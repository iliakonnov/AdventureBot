using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("monster/tiger", Difficulity.Medium)]
    public class Tiger : MonsterBase
    {
        public override string Name => "Саблезубый тигр";
        public override string Identifier => "monster/tiger";
        public override decimal Health => 75;

        public override decimal GetDamage(User user)
        {
            return 10;
        }

        public override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "Разве они не вымерли?", buttons);
        }

        public override bool OnRunaway(User user)
        {
            return true;
        }

        public override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo("tiger/tooth", 1));
        }
    }
}