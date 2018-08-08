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
        protected override decimal Health => 200;

        protected override decimal GetDamage(User user)
        {
            return 15;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "Эта свинина настолько жирная, что уже натягивает свои леопардовые лосины!", buttons);
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }

        protected override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo("gordonRamsey/knife", 1));
        }
    }
}