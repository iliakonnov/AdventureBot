using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;
using Content.Items;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Medium)]
    public class Tiger : MonsterBase
    {
        public const string Id = "monster/tiger";
        public override string Name => "Саблезубый тигр";
        public override string Identifier => Id;
        protected override decimal Health => 75;

        protected override decimal GetDamage(User user)
        {
            return 10;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "Разве они не вымерли?", buttons);
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }

        protected override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo(TigerTooth.Id, 1));
        }
    }
}