using System;
using System.Collections.Generic;
using MessagePack;

namespace AdventureBot.User.Stats;

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
    Defence,
    Karma
}

[MessagePackObject(true)]
public class StatsEffect : ISerializable
{
    [SerializationConstructor]
    public StatsEffect(ChangeType changeType, IReadOnlyDictionary<StatsProperty, decimal> effect)
    {
        ChangeType = changeType;
        Effect = effect;
    }

    public ChangeType ChangeType { get; }

    public IReadOnlyDictionary<StatsProperty, decimal> Effect { get; }

    public static int Compare(StructFlag<StatsProperty> props, StatsEffect self, StatsEffect other)
    {
        var result = 0m;
        foreach (var property in props.Values)
        {
            result += other.Effect.GetValueOrDefault(property) - self.Effect.GetValueOrDefault(property);
        }

        return Math.Sign(result);
    }

    public static IComparer<StatsEffect> CreateComparer(StructFlag<StatsProperty> props)
    {
        return Comparer<StatsEffect>.Create((a, b) => Compare(props, a, b));
    }

    public StatsEffect Clone()
    {
        return new StatsEffect(ChangeType, Effect);
    }

    public decimal? GetStatOrNull(StatsProperty property)
    {
        return Effect.TryGetValue(property, out var result)
            ? result
            : null;
    }
}