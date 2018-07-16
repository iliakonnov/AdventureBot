using System;
using System.Collections.Generic;
using MessagePack;

namespace AdventureBot.User.Stats
{
    public enum ChangeType
    {
        Add,
        Set,
        Multiply
    }

    public enum StatsProperty
    {
        Health,
        Intelligence,
        Strength,
        Mana,
        Stamina,
        Defence
    }

    [MessagePackObject(true)]
    public class StatsEffect
    {
        [SerializationConstructor]
        public StatsEffect(ChangeType changeType, IReadOnlyDictionary<StatsProperty, decimal> effect)
        {
            ChangeType = changeType;
            Effect = effect;
        }

        public ChangeType ChangeType { get; }

        public IReadOnlyDictionary<StatsProperty, decimal> Effect { get; }

        public static int Compare(Flag<StatsProperty> props, Stats userStats, StatsEffect self, StatsEffect other)
        {
            var result = 0m;
            var selfAffected = userStats.Apply(self);
            var otherAffected = userStats.Apply(other);
            foreach (var property in props.Values)
                result += otherAffected.Effect.GetValueOrDefault(property, 0) -
                          selfAffected.Effect.GetValueOrDefault(property, 0);

            return Math.Sign(result);
        }

        public static IComparer<StatsEffect> CreateComparer(Flag<StatsProperty> props, Stats userStats)
        {
            return Comparer<StatsEffect>.Create((a, b) => Compare(props, userStats, a, b));
        }
    }
}