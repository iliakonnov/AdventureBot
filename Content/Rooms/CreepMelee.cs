using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("monster/CreepMelee", Difficulity.Easy)]
    public class MonsterTemplate : MonsterBase
    {
        public const string Id = "monster/CreepMelee";
        public override string Name => "Крип-мечник";
        public override string Identifier => Id;
        protected override decimal Health => 45;

        protected override decimal GetDamage(User user)
        {
            return 15;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "Неотъемлемая часть любой РПГ. Ты им смерть - они тебе деньги", buttons);
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }

        protected override void OnWon(User user)
        {
            user.Info.Gold += 45;
        }
    }
}