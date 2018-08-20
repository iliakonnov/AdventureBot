using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Upper)]
    public class FirstBoss : BossBase
    {
        public const string Id = "boss/firstBoss";
        public override string Name => "Первый босс во всем городе";
        public override string Identifier => Id;
        protected override decimal InitialGold => 1_000;
        protected override decimal Health => 500;
        protected override decimal GetDamage(User user)
        {
            return 35;
        }
    }
}