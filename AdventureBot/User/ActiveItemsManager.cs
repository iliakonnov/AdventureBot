using System;
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
        public ActiveItemsManager(List<ItemInfo> activeItems, Dictionary<Flag<StatsProperty>, int> activeProportions,
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


        [IgnoreMember] public IReadOnlyDictionary<Flag<StatsProperty>, int> ActiveProportions => _activeProportions;

        [Key("ActiveProportions")]
        internal Dictionary<Flag<StatsProperty>, int> _activeProportions { get; set; } =
            new Dictionary<Flag<StatsProperty>, int>();

        [Key(nameof(ActiveLimit))] public int ActiveLimit { get; internal set; } = 3;

        public void ChangeProportion(Flag<StatsProperty> property, int count)
        {
            var currentSum = ActiveProportions.Values.Sum();
            var available = ActiveLimit - currentSum;
            var toAdd = Math.Min(count, available); // User cannot add more items than ActiveLimit

            var currentValue = ActiveProportions.GetValueOrDefault(property, 0);

            var newValue = currentValue + toAdd;
            if (newValue <= 0)
                _activeProportions.Remove(property);
            else
                _activeProportions[property] = newValue;

            RecalculateActive();
        }

        public List<Flag<StatsProperty>> GetAvailableProportions()
        {
            return _user.ItemManager.Items
                .Select(item => item.Item.Effect)
                .Where(effect => effect != null)
                .Select(effect => new Flag<StatsProperty>(effect.Effect.Keys))
                .ToList();
        }

        internal void RecalculateActive()
        {
            var items = _user.ItemManager.Items
                .Where(i => i.Item.Effect != null) // Only items that have any effect
                .Select(i => new
                {
                    Item = i,
                    Affects =
                        new StructFlag<StatsProperty>(i.Item.Effect.Effect.Keys) // See what stats this item affects
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

            var remains = new Dictionary<Flag<StatsProperty>, int>(_activeProportions);

            var result = new List<ItemInfo>();
            foreach (var group in items)
            foreach (var item in group.Items)
            {
                var taken = Math.Min(remains[group.Key], item.Count);
                if (taken == 0) continue;

                remains[group.Key] -= taken;
                var added = item.Clone();
                added.Count = taken;
                result.Add(added);
            }

            _activeItems = result;
            _user.Info.RecalculateStats();
        }
    }
}