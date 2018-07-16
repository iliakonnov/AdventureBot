using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using MessagePack;

namespace AdventureBot.User.Stats
{
    [MessagePackObject(keyAsPropertyName: true)]
    public class Stats : StatsEffect
    {
        private static IReadOnlyDictionary<StatsProperty, decimal> DefaultStats = new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Health, 100},
            {StatsProperty.Mana, 100},
            {StatsProperty.Stamina, 100},
            {StatsProperty.Intelligence, 1},
            {StatsProperty.Strength, 1}
        };

        public static IReadOnlyDictionary<StatsProperty, string> Emojis = new ReadOnlyDictionary<StatsProperty, string>(
            new Dictionary<StatsProperty, string>
            {
                {StatsProperty.Health, "♥️"},
                {StatsProperty.Intelligence, "👓"},
                {StatsProperty.Mana, "🌀"},
                {StatsProperty.Stamina, "⚡️"},
                {StatsProperty.Strength, "💪"}
            }
        );

        [SerializationConstructor]
        public Stats(IReadOnlyDictionary<StatsProperty, decimal> effect) : base(
            ChangeType.Set,
            DefaultStats.ToDictionary(
                kv => kv.Key,
                kv => effect.GetValueOrDefault(kv.Key, kv.Value)
            )
        )
        {
        }

        public Stats() : base(ChangeType.Set, DefaultStats)
        {
        }

        public Stats Apply(StatsEffect effect)
        {
            switch (effect.ChangeType)
            {
                case ChangeType.Add:
                    return new Stats(Effect
                        .ToDictionary(kv => kv.Key, kv => kv.Value + effect.Effect.GetValueOrDefault(kv.Key, 0))
                    );
                case ChangeType.Set:
                    return new Stats(Effect
                        .ToDictionary(kv => kv.Key, kv => effect.Effect.GetValueOrDefault(kv.Key, kv.Value))
                    );
                case ChangeType.Multiply:
                    return new Stats(Effect
                        .ToDictionary(kv => kv.Key, kv => kv.Value * effect.Effect.GetValueOrDefault(kv.Key, 1))
                    );
                default:
                    throw new ArgumentOutOfRangeException();
            }
        }
    }
}