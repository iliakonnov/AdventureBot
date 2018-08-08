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
        protected override decimal Health => 1500;

        protected override decimal GetDamage(User user)
        {
            return 50;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(
                user,
                "Этот огромный человекоподобный медведь — когда-то одно из самых опасных существ в Средиземье. Говорят, его когти настолько остры, что можно поцарапаться, просто взглянув на них, но пруфа нет. Пора проверить!",
                buttons
            );
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }

        protected override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo("beorn/skin", 1));
        }
    }
}