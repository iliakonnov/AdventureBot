using System.Collections.Generic;
using AdventureBot;
using AdventureBot.User.Stats;
using Xunit;

namespace BotTests;

public class StatsTests
{
    [Fact]
    public void ApplyAddTest()
    {
        var stats = new Stats();
        var effect = new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Health, 5}
        });
        var applied = stats.Apply(effect);
        Assert.Equal(stats.Effect[StatsProperty.Health],
            applied.Effect[StatsProperty.Health] - effect.Effect[StatsProperty.Health]);
    }

    [Fact]
    public void ApplyMultiplyTest()
    {
        var stats = new Stats();
        var effect = new StatsEffect(ChangeType.Multiply, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Health, 5}
        });
        var applied = stats.Apply(effect);
        Assert.Equal(stats.Effect[StatsProperty.Health],
            applied.Effect[StatsProperty.Health] / effect.Effect[StatsProperty.Health]);
    }

    [Fact]
    public void ApplySetTest()
    {
        var stats = new Stats();
        var effect = new StatsEffect(ChangeType.Set, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Health, 5}
        });
        var applied = stats.Apply(effect);
        Assert.Equal(effect.Effect[StatsProperty.Health], applied.Effect[StatsProperty.Health]);
    }

    [Fact]
    public void CompareDifferent()
    {
        var props = new StructFlag<StatsProperty>(StatsProperty.Health);

        var comparer = StatsEffect.CreateComparer(props);

        // Bigger
        var a = new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Health, 5}
        });

        // Smaller
        var b = new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Health, 3}
        });

        // Bigger first
        Assert.Equal(-1, comparer.Compare(a, b));
        Assert.Equal(-1, StatsEffect.Compare(props, a, b));

        // Smaller first
        Assert.Equal(1, comparer.Compare(b, a));
        Assert.Equal(1, StatsEffect.Compare(props, b, a));
    }

    [Fact]
    public void CompareDifferentProperties()
    {
        // Bigger by health, smaller by mana, equal by intelligence
        var a = new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Health, 5},
            {StatsProperty.Mana, 3},
            {StatsProperty.Intelligence, 1}
        });

        // Smaller by health, bigger by mana, equal by intelligence
        var b = new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Health, 3},
            {StatsProperty.Mana, 5},
            {StatsProperty.Intelligence, 1}
        });

        var health = new StructFlag<StatsProperty>(StatsProperty.Health);
        Assert.Equal(-1, StatsEffect.Compare(health, a, b));

        var mana = new StructFlag<StatsProperty>(StatsProperty.Mana);
        Assert.Equal(1, StatsEffect.Compare(mana, a, b));

        var intelligence = new StructFlag<StatsProperty>(StatsProperty.Intelligence);
        Assert.Equal(0, StatsEffect.Compare(intelligence, a, b));
    }

    [Fact]
    public void CompareSame()
    {
        var props = new StructFlag<StatsProperty>(StatsProperty.Health);

        var comparer = StatsEffect.CreateComparer(props);

        var a = new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Health, 5}
        });
        var b = new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Health, 5}
        });

        Assert.Equal(0, comparer.Compare(a, b));
        Assert.Equal(0, StatsEffect.Compare(props, a, b));
    }
}