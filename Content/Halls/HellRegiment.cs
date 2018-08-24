using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Halls
{
    [Available(Id, Difficulity.Any, HallsRoot.Id)]
    public class HellRegiment : EvilMonsterBase
    {
        public const string Id = "halls/HellRegiment";
        public override string Name => "Адский полк";
        public override string Identifier => Id;
        protected override decimal Health => 100 * 10;
        protected override decimal GetDamage(User user)
        {
            return 20 * 10;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "Один демон-солдат - это плохо, десять - еще хуже.", buttons);
        }

        protected override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo(DemonicEssence.Id, 10));
        }
    }
}