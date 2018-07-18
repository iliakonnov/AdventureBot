using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("monster/legolas", Difficulity.Hard)]
    public class Legolas : MonsterBase
    {
        public override string Name => "Леголас";
        public override string Identifier => "monster/legolas";
        public override decimal Health => 500;

        public override decimal GetDamage(User user)
        {
            return 70;
        }

        public override void Enter(User user, string[][] buttons)
        {
            SendMessage(user,
                "Никогда не промахивается и может глушить эль галлонами не пьянея.  Стрела пролетела в миллиметре от твоей макушки.");
            SendMessage(user, "— Это был предупредительный выстрел!", buttons);
        }

        public override bool OnRunaway(User user)
        {
            return true;
        }

        public override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo("legolas/bow", 1));
        }
    }
}