using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Halls
{
    [Available(Id, Difficulity.Any, HallsRoot.Id)]
    public class Ghoul : EvilMonsterBase
    {
        public const string Id = "halls/ghoul";
        public override string Name => "Вурдалак";
        public override string Identifier => Id;
        protected override decimal Health => 50;
        protected override decimal GetDamage(User user)
        {
            return 15;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "Вечный обитатель Чертогов. Мерзкий, злобный и очень слабый.", buttons);
        }

        protected override void OnWon(User user)
        {
            user.Info.Gold += 30;
        }
    }
}