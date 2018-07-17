using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("monster/gordonRamsey", Difficulity.Medium)]
    public class GordonRamsey : MonsterBase
    {
        public override string Name => "Гордон Рамзи";
        public override string Identifier => "monster/gordonRamsey";
        public override decimal Health => 200;

        public override decimal GetDamage(User user)
        {
            return 15;
        }

        public override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "Эта свинина настолько жирная, что уже натягивает свои леопардовые лосины!", buttons);
        }

        public override bool OnRunaway(User user)
        {
            return true;
        }

        public override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo("gordonRamsey/knife", 1));
        }
    }
}