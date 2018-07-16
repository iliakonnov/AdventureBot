using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Linq;
using AdventureBot.Item;
using AdventureBot.User.Stats;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot.User
{
    [MessagePackObject]
    public class ActiveItemsManager
    {
        [IgnoreMember] internal User _user;

        /// <summary>
        /// Текущие активные предметы
        /// </summary>
        [IgnoreMember]
        public IReadOnlyList<ItemInfo> ActiveItems => _activeItems;

        [Key("ActiveItems")] private List<ItemInfo> _activeItems = new List<ItemInfo>();

        // TODO: Сделать его internal, в Public -- Только IReadOnly
        [Key(nameof(ActiveProportions))]
        public Dictionary<Flag<StatsProperty>, int> ActiveProportions { get; internal set; } =
            new Dictionary<Flag<StatsProperty>, int>();

        [Key(nameof(ActiveLimit))] public int ActiveLimit { get; internal set; }

        [Obsolete("This constructor for serializer only")]
        [UsedImplicitly]
        [SerializationConstructor]
        public ActiveItemsManager(List<ItemInfo> activeItems, Dictionary<Flag<StatsProperty>, int> activeProportions,
            int activeLimit)
        {
            _activeItems = activeItems;
            ActiveProportions = activeProportions;
            ActiveLimit = activeLimit;
        }

        public ActiveItemsManager(User user)
        {
            _user = user;
        }

        public void ChangeProportion(Flag<StatsProperty> property, int count)
        {
            var currentSum = ActiveProportions.Values.Sum();
            var available = ActiveLimit - currentSum;
            var toAdd = Math.Min(count, available); // User cannot add more items than ActiveLimit

            var currentValue = ActiveProportions.GetValueOrDefault(property, 0);

            var newValue = currentValue + toAdd;
            if (newValue <= 0)
            {
                ActiveProportions.Remove(property);
            }
            else
            {
                ActiveProportions[property] = newValue;
            }

            RecalculateActive();
        }

        internal void RecalculateActive()
        {
            var items = _user.ItemManager.Items
                .Where(i => i.Item.Effect != null) // Only items that have any effect
                .Select(i => new
                {
                    Item = i,
                    Affects = new StructFlag<StatsProperty>(i.Item.Effect.Effect.Keys) // See what stats this item affects
                })
                .Where(i => ActiveProportions.ContainsKey(i.Affects)) // Only effects that needed
                .GroupBy(i => i.Affects) // Group so we can sort each group by corresponding stats
                .Select(g => new
                {
                    g.Key,
                    Items = g
                        .OrderBy(i => i.Item.Item.Effect,
                            StatsEffect.CreateComparer(g.Key, _user.Info.BaseStats)) // Order items
                        .Select(i => i.Item) // Anonymous class not needed anymore
                });

            var remains = new Dictionary<Flag<StatsProperty>, int>(ActiveProportions);

            var result = new List<ItemInfo>();
            foreach (var group in items)
            {
                foreach (var item in group.Items)
                {
                    var taken = Math.Min(remains[group.Key], item.Count);
                    if (taken == 0) continue;

                    remains[group.Key] -= taken;
                    var added = item.Clone();
                    added.Count = taken;
                    result.Add(added);
                }
            }

            _activeItems = result;
            _user.Info.RecalculateStats();
        }
    }
}