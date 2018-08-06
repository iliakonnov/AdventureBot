using System;
using System.Collections;
using System.Collections.Generic;
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
        [IgnoreMember] internal User _user;

        [Obsolete("This constructor for serializer only")]
        [UsedImplicitly]
        [SerializationConstructor]
        public ActiveItemsManager(List<ItemInfo> activeItems,
            Dictionary<StructFlag<StatsProperty>, int> activeProportions,
            int activeLimit)
        {
            _activeItems = activeItems;
            _activeProportions = activeProportions;
            ActiveLimit = activeLimit;
        }

        public ActiveItemsManager(User user)
        {
            _user = user;
        }

        /// <summary>
        ///     Текущие активные предметы
        /// </summary>
        [IgnoreMember]
        public IReadOnlyList<ItemInfo> ActiveItems => _activeItems;


        [IgnoreMember]
        public IReadOnlyDictionary<StructFlag<StatsProperty>, int> ActiveProportions => _activeProportions;

        [Key("ActiveProportions")]
        internal Dictionary<StructFlag<StatsProperty>, int> _activeProportions { get; set; } =
            new Dictionary<StructFlag<StatsProperty>, int>();

        [Key(nameof(ActiveLimit))] public int ActiveLimit { get; internal set; } = 3;

        public void ChangeProportion(StructFlag<StatsProperty> property, int count)
        {
            var currentSum = ActiveProportions.Values.Sum();
            var available = ActiveLimit - currentSum;
            var toAdd = Math.Min(count, available); // User cannot add more items than ActiveLimit

            var currentValue = ActiveProportions.GetValueOrDefault(property, 0);

            var newValue = currentValue + toAdd;
            if (newValue <= 0)
            {
                _activeProportions.Remove(property);
            }
            else
            {
                _activeProportions[property] = newValue;
            }

            RecalculateActive();
        }

        public List<StructFlag<StatsProperty>> GetAvailableProportions()
        {
            return _user.ItemManager.Items
                .Select(item => item.Item.Effect)
                .Where(effect => effect != null)
                .Select(effect => new StructFlag<StatsProperty>(effect.Effect.Keys))
                .ToList();
        }

        private IEnumerable<ItemInfo> FindAvailableItems()
        {
            return _user.ItemManager.Items
                .Where(i =>
                    i.Item.Effect != null
                    && i.Item.Effect.Effect.Count != 0
                );
        }

        private IReadOnlyDictionary<StructFlag<StatsProperty>, MustBeOrderedList<ItemInfo>> GroupByStats(
            IEnumerable<ItemInfo> items)
        {
            var result = new Dictionary<StructFlag<StatsProperty>, List<ItemInfo>>();
            foreach (var item in items)
            {
                var combined = new StructFlag<StatsProperty>();
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

        private IDictionary<ChangeType, MustBeOrderedList<ItemInfo>> GroupByChangeType(
            MustBeOrderedList<ItemInfo> items)
        {
            var result = new Dictionary<ChangeType, MustBeOrderedList<ItemInfo>>();

            foreach (var item in items)
            {
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

        private MustBeOrderedList<ItemInfo> TakeBest(int count, MustBeOrderedList<ItemInfo> items)
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
                return StatsEffect.Compare(prop, _user.Info.BaseStats, TakeBest(1, setItems).First().Item.Effect) == 1;
            }

            return false;
        }

        private List<ItemInfo> ActivateItems(StructFlag<StatsProperty> prop, MustBeOrderedList<ItemInfo> items)
        {
            var limit = ActiveProportions[prop];
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
            var bestStats = _user.Info.BaseStats;
            var bestItems = new List<ItemInfo>();
            for (var addCount = 0; addCount < max; addCount++)
            {
                selectedItems = selectedItemsBase.ToList();

                var mulCount = max - addCount;
                selectedItems.AddRange(TakeBest(addCount, groups[ChangeType.Add]));
                selectedItems.AddRange(TakeBest(mulCount, groups[ChangeType.Multiply]));

                var currentStats = UserInfo.ApplyItems(_user.Info.BaseStats, selectedItems);

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
            foreach (var keyValuePair in byStats)
            {
                _activeItems = ActivateItems(keyValuePair.Key, keyValuePair.Value);
            }

            _user.Info.RecalculateStats();
        }

        private class MustBeOrderedList<T> : IOrderedEnumerable<T>, IList<T>
        {
            private readonly IList<T> _listImplementation;

            public MustBeOrderedList(IOrderedEnumerable<T> enumerable)
            {
                _listImplementation = enumerable.ToList();
            }

            public MustBeOrderedList()
            {
                _listImplementation = new List<T>();
            }

            public void Add(T item)
            {
                _listImplementation.Add(item);
            }

            public void Clear()
            {
                _listImplementation.Clear();
            }

            public bool Contains(T item)
            {
                return _listImplementation.Contains(item);
            }

            public void CopyTo(T[] array, int arrayIndex)
            {
                _listImplementation.CopyTo(array, arrayIndex);
            }

            public bool Remove(T item)
            {
                return _listImplementation.Remove(item);
            }

            public int Count => _listImplementation.Count;

            public bool IsReadOnly => _listImplementation.IsReadOnly;

            public int IndexOf(T item)
            {
                return _listImplementation.IndexOf(item);
            }

            public void Insert(int index, T item)
            {
                _listImplementation.Insert(index, item);
            }

            public void RemoveAt(int index)
            {
                _listImplementation.RemoveAt(index);
            }

            public T this[int index]
            {
                get => _listImplementation[index];
                set => _listImplementation[index] = value;
            }

            public IOrderedEnumerable<T> CreateOrderedEnumerable<TKey>(Func<T, TKey> keySelector,
                IComparer<TKey> comparer, bool descending)
            {
                return descending
                    ? _listImplementation.OrderByDescending(keySelector, comparer)
                    : _listImplementation.OrderBy(keySelector, comparer);
            }

            public IEnumerator<T> GetEnumerator()
            {
                return _listImplementation.GetEnumerator();
            }

            IEnumerator IEnumerable.GetEnumerator()
            {
                return ((IEnumerable) _listImplementation).GetEnumerator();
            }
        }
    }
}