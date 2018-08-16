using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;
using Content.Items;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Medium)]
    public class GordonRamsey : MonsterBase
    {
        public const string Id = "monster/gordonRamsey";
        public override string Name => "Гордон Рамзи";
        public override string Identifier => Id;
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
            user.ItemManager.Add(new ItemInfo(GordonKnife.Id, 1));
        }
    }
}