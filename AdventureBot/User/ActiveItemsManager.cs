using System;
using System.Collections.Generic;
using System.Diagnostics;
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
        [Key("ActiveItems")] private List<ItemInfo> _activeItems = new List<ItemInfo>();
        [IgnoreMember] internal User User;

        [Obsolete("This constructor for serializer only")]
        [UsedImplicitly]
        [SerializationConstructor]
        public ActiveItemsManager(List<ItemInfo> activeItems,
            Dictionary<StructFlag<StatsProperty>, int> activeProportions,
            int activeLimit)
        {
            _activeItems = activeItems;
            Proportions = activeProportions;
            ActiveLimit = activeLimit;
        }

        public ActiveItemsManager(User user)
        {
            User = user;
        }

        /// <summary>
        ///     Текущие активные предметы
        /// </summary>
        [IgnoreMember]
        public IReadOnlyList<ItemInfo> ActiveItems => _activeItems;


        [IgnoreMember] public IReadOnlyDictionary<StructFlag<StatsProperty>, int> ActiveProportions => Proportions;

        [Key("ActiveProportions")]
        internal Dictionary<StructFlag<StatsProperty>, int> Proportions { get; set; } =
            new Dictionary<StructFlag<StatsProperty>, int>();

        [Key(nameof(ActiveLimit))] public int ActiveLimit { get; internal set; } = 3;

        public void ChangeProportion(StructFlag<StatsProperty> property, int count)
        {
            var currentSum = ActiveProportions.Values.Sum();
            var available = ActiveLimit - currentSum;
            var toAdd = Math.Min(count, available); // User cannot add more items than ActiveLimit

            var currentValue = ActiveProportions.GetValueOrDefault(property);

            var newValue = currentValue + toAdd;
            if (newValue <= 0)
            {
                Proportions.Remove(property);
            }
            else
            {
                Proportions[property] = newValue;
            }

            RecalculateActive();
        }

        public List<StructFlag<StatsProperty>> GetAvailableProportions()
        {
            return FindAvailableItems()
                .Select(info => new StructFlag<StatsProperty>(info.Item.Effect.Effect.Keys))
                .ToList();
        }

        private IEnumerable<ItemInfo> FindAvailableItems()
        {
            return User.ItemManager.Items
                .Where(i =>
                    !i.Item.IsAlwaysActive
                    && i.Item.Effect != null
                    && i.Item.Effect.Effect.Count != 0
                );
        }

        private static IReadOnlyDictionary<StructFlag<StatsProperty>, MustBeOrderedList<ItemInfo>> GroupByStats(
            IEnumerable<ItemInfo> items)
        {
            var result = new Dictionary<StructFlag<StatsProperty>, List<ItemInfo>>();
            foreach (var item in items)
            {
                var combined = new StructFlag<StatsProperty>();
                Debug.Assert(item.Item.Effect != null, "item.Item.Effect != null");
                foreach (var effectKey in item.Item.Effect.Effect.Keys)
                {
                    combined = new StructFlag<StatsProperty>(combined.Values.Add(effectKey));
                }

                if (result.TryGetValue(combined, out var list))
                {
                    list.Add(item);
                }
                else
                {
                    result[combined] = new List<ItemInfo> {item};
                }
            }

            return result.ToDictionary(
                kv => kv.Key,
                kv => new MustBeOrderedList<ItemInfo>(kv.Value
                    .OrderBy(i => i.Item.Effect, StatsEffect.CreateComparer(kv.Key)))
            );
        }

        private static IDictionary<ChangeType, MustBeOrderedList<ItemInfo>> GroupByChangeType(
            MustBeOrderedList<ItemInfo> items)
        {
            var result = new Dictionary<ChangeType, MustBeOrderedList<ItemInfo>>();

            foreach (var item in items)
            {
                Debug.Assert(item.Item.Effect != null, "item.Item.Effect != null");
                if (result.TryGetValue(item.Item.Effect.ChangeType, out var list))
                {
                    list.Add(item);
                }
                else
                {
                    result[item.Item.Effect.ChangeType] = new MustBeOrderedList<ItemInfo> {item};
                }
            }

            return result;
        }

        private static MustBeOrderedList<ItemInfo> TakeBest(int count, MustBeOrderedList<ItemInfo> items)
        {
            var result = new MustBeOrderedList<ItemInfo>();
            foreach (var item in items)
            {
                if (item.Count >= count)
                {
                    result.Add(new ItemInfo(item.Item, count));
                    break;
                }

                result.Add(item);
                count -= item.Count;
            }

            return result;
        }

        private bool DetectUseSet(StructFlag<StatsProperty> prop,
            IDictionary<ChangeType, MustBeOrderedList<ItemInfo>> items)
        {
            if (items.TryGetValue(ChangeType.Set, out var setItems))
            {
                // Returns is best "set" item better than BaseStats
                return StatsEffect.Compare(prop, User.Info.BaseStats, TakeBest(1, setItems).First().Item.Effect) == 1;
            }

            return false;
        }

        private List<ItemInfo> ActivateItems(StructFlag<StatsProperty> prop, MustBeOrderedList<ItemInfo> items)
        {
            if (!ActiveProportions.TryGetValue(prop, out var limit))
            {
                return new List<ItemInfo>();
            }

            var groups = GroupByChangeType(items);
            var useSet = DetectUseSet(prop, groups);

            var max = limit;
            if (useSet)
            {
                max--;
            }

            var selectedItems = new List<ItemInfo>();
            if (useSet)
            {
                selectedItems.AddRange(TakeBest(1, groups[ChangeType.Set]));
            }

            if (!groups.ContainsKey(ChangeType.Add) && !groups.ContainsKey(ChangeType.Multiply))
            {
                // No multiplication and addition. Only set, maybe.
                // So just do nothing, because DetectUseSet() will handle set.
                return selectedItems;
            }

            if (!groups.ContainsKey(ChangeType.Add))
            {
                // Only multiplication (and set, maybe)
                selectedItems.AddRange(TakeBest(max, groups[ChangeType.Multiply]));
                return selectedItems;
            }

            if (!groups.ContainsKey(ChangeType.Multiply))
            {
                // Only addition (and set, maybe)
                selectedItems.AddRange(TakeBest(max, groups[ChangeType.Add]));
                return selectedItems;
            }

            // Both multiplication and addition (and set, maybe)
            /*
             * Наилучшая комбинация будет если сначала складывать, а потом умножать, т.к. (x + a) * b > (x * b) + a
             * Этот алгоритм сначала пробует взять максимальное количество умножения,
             * потом в каждой итерации добавляет одно сложение. В конце концов пробует только сложения.
             * Работает за O(N^2), где N -- max (ActiveProportions[prop])
             */
            var selectedItemsBase = selectedItems.ToList();
            var bestStats = User.Info.BaseStats;
            var bestItems = new List<ItemInfo>();
            for (var addCount = 0; addCount < max; addCount++)
            {
                selectedItems = selectedItemsBase.ToList();

                var mulCount = max - addCount;
                selectedItems.AddRange(TakeBest(addCount, groups[ChangeType.Add]));
                selectedItems.AddRange(TakeBest(mulCount, groups[ChangeType.Multiply]));

                var currentStats = UserInfo.ApplyItems(User.Info.BaseStats, selectedItems);

                if (StatsEffect.Compare(prop, bestStats, currentStats) == 1)
                {
                    bestStats = currentStats;
                    bestItems = selectedItems.ToList();
                }
            }

            return bestItems;
        }

        internal void RecalculateActive()
        {
            var items = FindAvailableItems();
            var byStats = GroupByStats(items);
            _activeItems = User.ItemManager.Items.Where(i => i.Item.IsAlwaysActive).ToList();
            foreach (var keyValuePair in byStats)
            {
                _activeItems.AddRange(ActivateItems(keyValuePair.Key, keyValuePair.Value));
            }

            User.Info.RecalculateStats();
        }
    }
}