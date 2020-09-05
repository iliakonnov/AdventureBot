using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using MessagePack;

namespace AdventureBot.User.Stats
{
    [MessagePackObject(true)]
    public class Stats : StatsEffect
    {
        public static readonly IReadOnlyDictionary<StatsProperty, decimal> DefaultStats =
            new Dictionary<StatsProperty, decimal>
            {
                {StatsProperty.Health, 100},
                {StatsProperty.Mana, 100},
                {StatsProperty.Stamina, 100},
                {StatsProperty.Intelligence, 10},
                {StatsProperty.Strength, 10},
                {StatsProperty.Defence, 10},
                {StatsProperty.Karma, 0}
            };

        public static readonly IReadOnlyDictionary<StatsProperty, string> Emojis =
            new ReadOnlyDictionary<StatsProperty, string>(
                new Dictionary<StatsProperty, string>
                {
                    {StatsProperty.Health, "♥️"},
                    {StatsProperty.Intelligence, "👓"},
                    {StatsProperty.Mana, "🌀"},
                    {StatsProperty.Stamina, "⚡️"},
                    {StatsProperty.Strength, "💪"},
                    {StatsProperty.Defence, "🛡️"},
                    {StatsProperty.Karma, "☯"}
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
                    return new Stats(DefaultStats
                        .ToDictionary(kv => kv.Key, kv => GetStat(kv.Key) + effect.Effect.GetValueOrDefault(kv.Key))
                    );
                case ChangeType.Set:
                    return new Stats(DefaultStats
                        .ToDictionary(kv => kv.Key, kv => effect.Effect.GetValueOrDefault(kv.Key, GetStat(kv.Key)))
                    );
                case ChangeType.Multiply:
                    return new Stats(DefaultStats
                        .ToDictionary(kv => kv.Key, kv => GetStat(kv.Key) * effect.Effect.GetValueOrDefault(kv.Key, 1))
                    );
                default:
                    throw new ArgumentOutOfRangeException();
            }
        }

        public decimal GetStat(StatsProperty property)
        {
            return GetStatOrNull(property) ?? DefaultStats[property];
        }
    }
}