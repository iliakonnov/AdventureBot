using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("monster/beorn", Difficulity.Hard)]
    public class Beorn : MonsterBase
    {
        public override string Name => "Беорн";
        public override string Identifier => "monster/beorn";
        public override decimal Health => 1500;

        public override decimal GetDamage(User user)
        {
            return 50;
        }

        public override void Enter(User user, string[][] buttons)
        {
            SendMessage(
                user,
                "Этот огромный человекоподобный медведь — когда-то одно из самых опасных существ в Средиземье. Говорят, его когти настолько остры, что можно поцарапаться, просто взглянув на них, но пруфа нет. Пора проверить!",
                buttons
            );
        }

        public override bool OnRunaway(User user)
        {
            return true;
        }

        public override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo("beorn/skin", 1));
        }
    }
}