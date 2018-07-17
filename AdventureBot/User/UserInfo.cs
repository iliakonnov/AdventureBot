using System.Collections.Generic;
using System.Collections.ObjectModel;
using AdventureBot.Analysis;
using AdventureBot.User.Stats;
using MessagePack;

namespace AdventureBot.User
{
    [MessagePackObject(true)]
    public class UserInfo
    {
        [SerializationConstructor]
        public UserInfo(bool dead, UserId userId, Stats.Stats baseStats, Stats.Stats currentStats)
        {
            Dead = dead;
            UserId = userId;
            BaseStats = baseStats;
            CurrentStats = currentStats;
        }

        public UserInfo(UserId userId, User user)
        {
            Dead = true;
            MaxStats = new Stats.Stats(new ReadOnlyDictionary<StatsProperty, decimal>(
                new Dictionary<StatsProperty, decimal>
                {
                    {StatsProperty.Health, 100},
                    {StatsProperty.Mana, 100},
                    {StatsProperty.Stamina, 100},
                    {StatsProperty.Intelligence, 100},
                    {StatsProperty.Strength, 100}
                }
            ));
            BaseStats = new Stats.Stats(new ReadOnlyDictionary<StatsProperty, decimal>(
                new Dictionary<StatsProperty, decimal>
                {
                    {StatsProperty.Health, MaxStats.Effect[StatsProperty.Health]},
                    {StatsProperty.Mana, MaxStats.Effect[StatsProperty.Mana]},
                    {StatsProperty.Stamina, MaxStats.Effect[StatsProperty.Stamina]},
                    {StatsProperty.Intelligence, 1},
                    {StatsProperty.Strength, 1}
                }
            ));
            UserId = userId;
            _user = user;
            RecalculateStats();
        }

        [IgnoreMember] internal User _user { get; set; }

        public bool Dead { get; internal set; }

        public decimal Gold { get; set; }

        public decimal SellMultiplier { get; } = 0.75m;

        public UserId UserId { get; }

        /// <summary>
        ///     Характеристики без эффектов от предметов
        /// </summary>
        public Stats.Stats BaseStats { get; internal set; }

        /// <summary>
        ///     Характеристики с учетом эффектов от активных вещей
        /// </summary>
        public Stats.Stats CurrentStats { get; private set; }

        /// <summary>
        ///     Максимально возможные характеристики (базовые). Характеристики с эффектами от бонусов могут быть больше.
        /// </summary>
        public Stats.Stats MaxStats { get; set; }

        /// <summary>
        ///     Перерасчитывает <see cref="CurrentStats" />, учитывая текущие активные предметы.
        /// </summary>
        internal void RecalculateStats()
        {
            CurrentStats = new Stats.Stats(BaseStats.Effect);
            foreach (var item in _user.ActiveItemsManager.ActiveItems)
            {
                if (item.Item.Effect == null)
                {
                    continue;
                }

                CurrentStats = CurrentStats.Apply(item.Item.Effect);
            }
        }

        /// <summary>
        ///     Уменьшает количество золота игрока.
        ///     Не позволяет количеству золота стать отрицательным. Если золота не хвататет, то ничего не меняет.
        /// </summary>
        /// <param name="value">На сколько именно нужно уменьшить</param>
        /// <returns>Достаточно ли золота было у игрока.</returns>
        public bool TryDecreaseGold(decimal value)
        {
            if (Gold < value)
            {
                return false;
            }

            Gold -= value;
            return true;
        }

        private bool ChangeStats(ChangeType changeType, StatsProperty property, decimal value, bool allowLess = false,
            bool allowMore = false)
        {
            var changed = BaseStats.Apply(
                new StatsEffect(changeType, new Dictionary<StatsProperty, decimal>
                {
                    {property, value}
                })
            );
            var newValue = changed.Effect[property];
            if (
                !allowLess && newValue < 0
                || !allowMore && newValue > MaxStats.Effect[property])
            {
                return false;
            }

            BaseStats = changed;
            RecalculateStats();
            return true;
        }

        /// <summary>
        ///     Изменяет указанную характеристику героя. Не позволяет стать характеристике больше максимума или меньше нуля.
        /// </summary>
        /// <param name="property">Какую характеристку следует изменить</param>
        /// <param name="value">На сколько надо изменить. Отрицательное для того, чтобы уменьшить</param>
        /// <param name="set">Необходимо жестко установить новое значение (true) или прибавить к текущему</param>
        public bool ChangeStats(StatsProperty property, decimal value, bool set = false)
        {
            var changeType = set ? ChangeType.Set : ChangeType.Add;

            if (property == StatsProperty.Health)
            {
                // Special case
                var result = ChangeStats(changeType, StatsProperty.Health, value, true);
                if (BaseStats.Effect[StatsProperty.Health] <= 0)
                {
                    Kill();
                }

                return result;
            }

            return ChangeStats(changeType, property, value);
        }

        /// <summary>
        ///     Просто напросто убивает игрока
        /// </summary>
        public void Kill()
        {
            Events.Dead(_user);
            ChangeStats(ChangeType.Set, StatsProperty.Health, 0);
            Dead = true;
            _user.RoomManager.Go("_root", false);
        }
    }
}