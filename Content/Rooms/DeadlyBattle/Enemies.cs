using AdventureBot.Room;

namespace Content.Rooms.DeadlyBattle
{
    [Room(Id)]
    public class KungLao : TournamentMonsterBase
    {
        public const string Id = "tournament/KungLao";
        public override string Name => "Кунг Лао";
        public override string Identifier => Id;
        protected override string Loot => SharpHat.Id;
    }

    [Room(Id)]
    public class SubZero : TournamentMonsterBase
    {
        public const string Id = "tournament/SubZero";
        public override string Name => "Саб-Зиро";
        public override string Identifier => Id;
        protected override string Loot => BlueMask.Id;
    }

    [Room(Id)]
    public class Scorpio : TournamentMonsterBase
    {
        public const string Id = "tournament/Scorpio";
        public override string Name => "Скорпион";
        public override string Identifier => Id;
        protected override string Loot => Harpoon.Id;
    }

    [Room(Id)]
    public class LiuKang : TournamentMonsterBase
    {
        public const string Id = "tournament/LiuKang";
        public override string Name => "Лю Канг";
        public override string Identifier => Id;
        protected override string Loot => Nunchaku.Id;
    }

    [Room(Id)]
    public class JohnnyCage : TournamentMonsterBase
    {
        public const string Id = "tournament/JohnnyCage";
        public override string Name => "Джонни Кейдж";
        public override string Identifier => Id;
        protected override string Loot => Sunglasses.Id;
    }

    [Room(Id)]
    public class Jax : TournamentMonsterBase
    {
        public const string Id = "tournament/Jax";
        public override string Name => "Джакс";
        public override string Identifier => Id;
        protected override string Loot => Cigar.Id;
    }
}