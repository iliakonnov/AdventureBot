using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("monster/camper", Difficulity.Medium)]
    public class Camper : MonsterBase
    {
        public override string Name => "Кэмпер";
        public override string Identifier => "monster/camper";
        public override decimal Health => 70;

        public override decimal GetDamage(User user)
        {
            return 70;
        }

        public override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "Сидел за ящиками, падла. Задай ему жару!", buttons);
        }

        public override bool OnRunaway(User user)
        {
            return true;
        }

        public override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo("camper/awp", 1));
        }
    }
}