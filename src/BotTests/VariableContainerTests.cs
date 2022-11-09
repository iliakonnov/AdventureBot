using AdventureBot;
using Xunit;

namespace BotTests;

public class VariableContainerTests
{
    [Fact]
    public void GetNotexistingTest()
    {
        var container = new VariableContainer();
        Assert.Empty(container.Keys());

        Assert.Null(container.Get("key"));
    }

    [Fact]
    public void NestedTest()
    {
        var containerA = new VariableContainer();
        Assert.Empty(containerA.Keys());

        var containerB = new VariableContainer();
        Assert.Empty(containerB.Keys());

        var containerC = new VariableContainer();
        Assert.Empty(containerC.Keys());

        containerC.Set("test_c", new Serializable.Bool(true));

        containerB.Set("test_b", new Serializable.String("test"));
        containerB.Set("nested_c", containerC);

        containerA.Set("test_a", new Serializable.Int(1));
        containerA.Set("nested_b", containerB);

        Assert.Equal(1, (int) containerA.Get<Serializable.Int>("test_a"));

        var nestedB = containerA.Get<VariableContainer>("nested_b");
        Assert.NotNull(nestedB);

        Assert.Equal("test", nestedB.Get<Serializable.String>("test_b"));

        var nestedC = containerB.Get<VariableContainer>("nested_c");
        Assert.NotNull(nestedC);

        Assert.Equal(true, (bool) nestedC.Get<Serializable.Bool>("test_c"));
    }

    [Fact]
    public void PlainTest()
    {
        var container = new VariableContainer();
        Assert.Empty(container.Keys());

        container.Set("test_variable", new Serializable.Int(1));
        Assert.Single(container.Keys(), "test_variable");

        var value = container.Get<Serializable.Int>("test_variable");
        Assert.Equal(1, (int) value);
    }
}