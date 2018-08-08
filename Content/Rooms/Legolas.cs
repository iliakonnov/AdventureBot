using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("monster/legolas", Difficulity.Hard)]
    public class Legolas : MonsterBase
    {
        public override string Name => "Леголас";
        public override string Identifier => "monster/legolas";
        protected override decimal Health => 500;

        protected override decimal GetDamage(User user)
        {
            return 70;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user,
                "Никогда не промахивается и может глушить эль галлонами не пьянея.  Стрела пролетела в миллиметре от твоей макушки.");
            SendMessage(user, "— Это был предупредительный выстрел!", buttons);
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }

        protected override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo("legolas/bow", 1));
        }
    }
}