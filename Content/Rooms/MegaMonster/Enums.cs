using System;

namespace Content.Rooms.MegaMonster
{
    public enum Level
    {
        Few,
        Medium,
        Many
    }

    public enum Knowledge
    {
        Strength,
        Intelligence
    }

    [Flags]
    public enum Place
    {
        None = 0,
        Legs = 1 << 0,
        Body = 1 << 1,
        Head = 1 << 2
    }

    public enum MonsterProperty
    {
        Artifact,
        Gold,
        KnowledgeGroup,
        KnowledgeLevel,
        DefenceLevel,
        Damage,
        Health
    }

    public enum MutateResult
    {
        Increase,
        IncreaseMany,
        Decrease,
        DecreaseMany
    }
}