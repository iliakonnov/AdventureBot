using System;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.User;
using Xunit;

namespace BotTests
{
    public class ItemsTests
    {
        [Theory]
        [InlineData(1)]
        [InlineData(3)]
        public void TestAddMany(int n)
        {
            var user = new User(new UserId(-1, -1));
            Assert.Empty(user.ItemManager.Items);

            for (var i = 0; i < n; i++)
            {
                user.ItemManager.Add(
                    new ItemInfo(new TestItem("test_item"), 1)
                );
            }

            var item = Assert.Single(user.ItemManager.Items);
            Assert.Equal("test_item", item?.Identifier);
            Assert.Equal(n, item?.Count);
        }

        [Theory]
        [InlineData(1)]
        [InlineData(3)]
        public void TestAddManyCount(int n)
        {
            var user = new User(new UserId(-1, -1));
            Assert.Empty(user.ItemManager.Items);

            user.ItemManager.Add(
                new ItemInfo(new TestItem("test_item"), n)
            );

            var item = Assert.Single(user.ItemManager.Items);
            Assert.Equal("test_item", item?.Identifier);
            Assert.Equal(n, item?.Count);
        }

        public static TheoryData<Tuple<int, int>[]> RemoveData => new TheoryData<Tuple<int, int>[]>
        {
            new[]
            {
                new Tuple<int, int>(5, 5) // Completely removes item.
            },
            new[]
            {
                new Tuple<int, int>(5, 5),
                new Tuple<int, int>(3, 3)
            },
            new[]
            {
                new Tuple<int, int>(5, 3) // Leaves 2 items
            },
            new[]
            {
                new Tuple<int, int>(5, 3),
                new Tuple<int, int>(5, 3)
            },
            new[]
            {
                new Tuple<int, int>(5, 3), // Both items together
                new Tuple<int, int>(5, 5)
            }
        };

        [Theory]
        [MemberData(nameof(RemoveData))]
        public void TestRemove(Tuple<int, int>[] objects)
        {
            var user = new User(new UserId(-1, -1));
            Assert.Empty(user.ItemManager.Items);

            // Adds
            for (int i = 0; i < objects.Length; i++)
            {
                for (int j = 0; j < objects[i].Item1; j++)
                {
                    user.ItemManager.Add(
                        new ItemInfo(new TestItem($"test_item #{i}"), 1)
                    );
                }
            }

            // Removes
            for (int i = 0; i < objects.Length; i++)
            {
                for (int j = 0; j < objects[i].Item2; j++)
                {
                    Assert.True(user.ItemManager.Remove(
                        new ItemInfo(new TestItem($"test_item #{i}"), 1)
                    ));
                }
            }

            // Checks
            for (int i = 0; i < objects.Length; i++)
            {
                var neededCount = objects[i].Item1 - objects[i].Item2;
                if (neededCount == 0)
                {
                    Assert.DoesNotContain(user.ItemManager.Items, it => it.Identifier == $"test_item #{i}");
                }
                else
                {
                    var item = Assert.Single(user.ItemManager.Items, it => it.Identifier == $"test_item #{i}");
                    Assert.Equal(neededCount, item?.Count);
                }
            }
        }

        [Theory]
        [MemberData(nameof(RemoveData))]
        public void TestRemoveCount(Tuple<int, int>[] objects)
        {
            var user = new User(new UserId(-1, -1));
            Assert.Empty(user.ItemManager.Items);

            // Adds
            for (int i = 0; i < objects.Length; i++)
            {
                user.ItemManager.Add(
                    new ItemInfo(new TestItem($"test_item #{i}"), objects[i].Item1)
                );
            }

            // Removes
            for (int i = 0; i < objects.Length; i++)
            {
                Assert.True(user.ItemManager.Remove(
                    new ItemInfo(new TestItem("test_item #{i}"), objects[i].Item2)
                ));
            }

            // Checks
            for (int i = 0; i < objects.Length; i++)
            {
                var neededCount = objects[i].Item1 - objects[i].Item2;
                if (neededCount == 0)
                {
                    Assert.DoesNotContain(user.ItemManager.Items, it => it.Identifier == $"test_item #{i}");
                }
                else
                {
                    var item = Assert.Single(user.ItemManager.Items, it => it.Identifier == $"test_item #{i}");
                    Assert.Equal(neededCount, item?.Count);
                }
            }
        }

        [Fact]
        public void RemoveNegative()
        {
            var user = new User(new UserId(-1, -1));
            Assert.Empty(user.ItemManager.Items);

            Assert.False(user.ItemManager.Remove(new ItemInfo(new TestItem("test_item"))));
        }
    }
}