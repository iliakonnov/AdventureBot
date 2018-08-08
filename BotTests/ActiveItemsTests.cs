using System.Collections.Generic;
using System.Collections.ObjectModel;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.User;
using AdventureBot.User.Stats;
using Xunit;

namespace BotTests
{
    public class ActiveItemsTests
    {
        [Fact]
        public void AddBetterTest()
        {
            var user = new User(new UserId(-1, -1));
            Assert.Empty(user.ActiveItemsManager.ActiveItems);

            user.ActiveItemsManager.ActiveLimit = 3;
            user.ActiveItemsManager.ChangeProportion(new StructFlag<StatsProperty>(StatsProperty.Health), 3);

            // Adds item (x3)
            user.ItemManager.Add(
                new ItemInfo(new TestItem
                (
                    "test_health",
                    new StatsEffect(
                        ChangeType.Add,
                        new ReadOnlyDictionary<StatsProperty, decimal>(
                            new Dictionary<StatsProperty, decimal>
                            {
                                {StatsProperty.Health, 1}
                            }
                        )
                    )
                ), 3)
            );

            // Then adds better item (x2)
            user.ItemManager.Add(
                new ItemInfo(new TestItem
                (
                    "better_health",
                    new StatsEffect(
                        ChangeType.Add,
                        new ReadOnlyDictionary<StatsProperty, decimal>(
                            new Dictionary<StatsProperty, decimal>
                            {
                                {StatsProperty.Health, 3}
                            }
                        )
                    )
                ), 2)
            );

            user.ActiveItemsManager.RecalculateActive();

            // Simple item
            var item = Assert.Single(user.ActiveItemsManager.ActiveItems, x => x.Identifier == "test_health");
            Assert.Equal(1, item?.Count);

            // Better item
            var better = Assert.Single(user.ActiveItemsManager.ActiveItems, x => x.Identifier == "better_health");
            Assert.Equal(2, better?.Count);
        }

        [Fact]
        public void AddHealthTest()
        {
            var user = new User(new UserId(-1, -1));
            Assert.Empty(user.ActiveItemsManager.ActiveItems);

            user.ActiveItemsManager.ActiveLimit = 3;
            user.ActiveItemsManager.Proportions = new Dictionary<StructFlag<StatsProperty>, int>
            {
                {new StructFlag<StatsProperty>(StatsProperty.Health), 3}
            };

            // Adds item
            user.ItemManager.Add(
                new ItemInfo(new TestItem
                (
                    "test_health",
                    new StatsEffect(
                        ChangeType.Add,
                        new ReadOnlyDictionary<StatsProperty, decimal>(
                            new Dictionary<StatsProperty, decimal>
                            {
                                {StatsProperty.Health, 1}
                            }
                        )
                    )
                ), 3)
            );

            var item = Assert.Single(user.ActiveItemsManager.ActiveItems);
            Assert.Equal(3, item?.Count);
        }

        [Fact]
        public void AddWorseTest()
        {
            var user = new User(new UserId(-1, -1));
            var mgr = user.ActiveItemsManager;


            Assert.Empty(mgr.ActiveItems);

            user.ActiveItemsManager.ActiveLimit = 3;
            user.ActiveItemsManager.ChangeProportion(new StructFlag<StatsProperty>(StatsProperty.Health), 3);

            // Adds item (x3)
            user.ItemManager.Add(
                new ItemInfo(new TestItem
                (
                    "test_health",
                    new StatsEffect(
                        ChangeType.Add,
                        new ReadOnlyDictionary<StatsProperty, decimal>(
                            new Dictionary<StatsProperty, decimal>
                            {
                                {StatsProperty.Health, 3}
                            }
                        )
                    )
                ), 3)
            );

            // Then adds worse item (x2)
            user.ItemManager.Add(
                new ItemInfo(new TestItem
                (
                    "worse_health",
                    new StatsEffect(
                        ChangeType.Add,
                        new ReadOnlyDictionary<StatsProperty, decimal>(
                            new Dictionary<StatsProperty, decimal>
                            {
                                {StatsProperty.Health, 1}
                            }
                        )
                    )
                ), 2)
            );

            // Simple item
            var item = Assert.Single(mgr.ActiveItems, x => x.Identifier == "test_health");
            Assert.Equal(3, item?.Count);

            // Worse item
            Assert.DoesNotContain(mgr.ActiveItems, x => x.Identifier == "worse_health");
        }

        [Fact]
        public void FirstMultiplyTest()
        {
            var user = new User(new UserId(-1, -1))
            {
                Info =
                {
                    // Initial health is 1
                    BaseStats = new Stats(new Dictionary<StatsProperty, decimal>
                    {
                        {StatsProperty.Health, 1}
                    })
                }
            };
            user.Info.RecalculateStats();

            var mgr = user.ActiveItemsManager;

            Assert.Empty(mgr.ActiveItems);

            user.ActiveItemsManager.ActiveLimit = 3;
            user.ActiveItemsManager.ChangeProportion(new StructFlag<StatsProperty>(StatsProperty.Health), 3);

            // Adds with (+1) effect
            user.ItemManager.Add(
                new ItemInfo(new TestItem
                (
                    "test_health_add",
                    new StatsEffect(
                        ChangeType.Add,
                        new ReadOnlyDictionary<StatsProperty, decimal>(
                            new Dictionary<StatsProperty, decimal>
                            {
                                {StatsProperty.Health, 1}
                            }
                        )
                    )
                ), 1)
            );

            // Then adds item with (*3) effect
            user.ItemManager.Add(
                new ItemInfo(new TestItem
                (
                    "test_health_mul",
                    new StatsEffect(
                        ChangeType.Multiply,
                        new ReadOnlyDictionary<StatsProperty, decimal>(
                            new Dictionary<StatsProperty, decimal>
                            {
                                {StatsProperty.Health, 3}
                            }
                        )
                    )
                ), 1)
            );

            // Both items must be used
            var add = Assert.Single(mgr.ActiveItems, x => x.Identifier == "test_health_add");
            Assert.Equal(1, add?.Count);

            var mul = Assert.Single(mgr.ActiveItems, x => x.Identifier == "test_health_mul");
            Assert.Equal(1, mul?.Count);

            // And result must be equal to 6: (1' + 1) * 3, where 1' is initial health
            Assert.Equal(6, user.Info.CurrentStats.Effect[StatsProperty.Health]);
        }
    }
}