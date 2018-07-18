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
            CurrentStats = ApplyItems(new Stats.Stats(BaseStats.Effect));
        }

        private Stats.Stats ApplyItems(StatsEffect stats)
        {
            var result = new Stats.Stats(stats.Effect);
            foreach (var item in _user.ActiveItemsManager.ActiveItems)
            {
                if (item.Item.Effect == null)
                {
                    continue;
                }

                result = result.Apply(item.Item.Effect);
            }

            return result;
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
            var changedBase = BaseStats.Apply(
                new StatsEffect(changeType, new Dictionary<StatsProperty, decimal>
                {
                    {property, value}
                })
            );
            if (value < 0)
            {
                // При понижении статов, нужно проверять с учетом предметов.
                // (базовое здоровье может быть меньше нуля, т.к. предметы тебя спасут)
                var changed = ApplyItems(changedBase);
                var newValue = changed.Effect[property];
                if (!allowLess && newValue < 0)
                {
                    return false;
                }
            }
            else
            {
                // При повышении статов, нужно проверять без учета предметов.
                // (базовое здоровье не может быть больше максимума, но предметы могут повысить за пределы максимума)
                var newValue = changedBase.Effect[property];
                if (!allowMore && newValue > MaxStats.Effect[property])
                {
                    return false;
                }
            }

            BaseStats = changedBase;
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
            return ChangeStats(set ? ChangeType.Set : ChangeType.Add, property, value);
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

        /// <summary>
        ///     Наносит урон с учетом защиты игрока. Убивает при необходимости
        /// </summary>
        /// <param name="value">Какой урон нанесен</param>
        public void MakeDamage(decimal value)
        {
            // Урон (в процентах) в зависмости от защиты: https://www.desmos.com/calculator/xlslvcdbmo

            // График -- гипербола (dmg = k/(def + k) + b) с следующими ограничениями:
            // 1. Урон никогда не может быть меньше 5%, поэтому гипербола сдвинута вверх (b = 0.05)
            // 2. При единичной защите (в самом начале игры), урон должен быть 100% (k=19; http://www.wolframalpha.com/input/?i=1%3Dk%2F(1%2Bk)%2B0.05)

            // Свойства параболы (замеры среднего и медианного значений проводились с шагом 0.001)
            // 1. При защите 100 (максимальная базовая защита), урон составляет примерно 21%
            //
            // 2. Средний урон (защита от 1 до 100) составляет примерно 39%
            // 3. Медианный урон (защита от 1 до 100 с шагом 0.001) составляет примерно 32%
            //
            // 4. Средний урон (защита от 1 до 300 с шагом 0.001) составляет примерно 22.6%
            // 5. Медианный урон (защита от 1 до 300 с шагом 0.001) составляет примерно 16%
            //
            // Необходимо учитывать это при создании монстров!

            value *= -(19m / (CurrentStats.Effect[StatsProperty.Defence] + 19m) + 0.05m);
            ChangeStats(ChangeType.Add, StatsProperty.Health, value, true);
            if (CurrentStats.Effect[StatsProperty.Health] <= 0)
            {
                Kill();
            }
        }
    }
}