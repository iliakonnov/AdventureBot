using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("monster/stormtrooper", Difficulity.Lower)]
    public class Stormtrooper : MonsterBase
    {
        public override string Name => "Штурмовик";
        public override string Identifier => "monster/stormtrooper";
        protected override decimal Health => 40;

        protected override decimal GetDamage(User user)
        {
            return user.Random.NextDouble() > 0.35
                ? 10
                : 0;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user,
                "Солдат Новой Империи, покрытый белой пластмассовой броней, наводит на тебя свое лазерное оружие. Вернее, это он так думает.",
                buttons);
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }

        protected override void OnWon(User user)
        {
            user.Info.Gold += 25;
        }
    }
}