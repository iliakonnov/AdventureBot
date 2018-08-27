using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.NameGenerator;
using AdventureBot.User.Stats;
using MessagePack;

namespace AdventureBot.User
{
    [MessagePackObject(true)]
    public class UserInfo
    {
        [SerializationConstructor]
        public UserInfo(bool dead, UserId userId, Stats.Stats baseStats, Stats.Stats currentStats, string _name,
            Statistics statistics, UserLevel level)
        {
            Dead = dead;
            UserId = userId;
            BaseStats = baseStats;
            CurrentStats = currentStats;
            this._name = _name;
            Statistics = statistics;
            Level = level;
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
                    {StatsProperty.Strength, 100},
                    {StatsProperty.Defence, 100},
                    {StatsProperty.Karma, 100}
                }
            ));
            MinStats = new Stats.Stats(new ReadOnlyDictionary<StatsProperty, decimal>(
                new Dictionary<StatsProperty, decimal>
                {
                    {StatsProperty.Health, 0},
                    {StatsProperty.Mana, 0},
                    {StatsProperty.Stamina, 0},
                    {StatsProperty.Intelligence, 0},
                    {StatsProperty.Strength, 0},
                    {StatsProperty.Defence, 0},
                    {StatsProperty.Karma, -100}
                }
            ));
            BaseStats = new Stats.Stats(Stats.Stats.DefaultStats);
            UserId = userId;
            User = user;
            _name = Generator.Generate(User.Random);
            Statistics = new Statistics(user);
            Level = new UserLevel(user);
            RecalculateStats();
        }

        [IgnoreMember] internal User User { get; set; }

        public bool Dead { get; internal set; }

        public decimal Gold
        {
            get => User.DatabaseVariables.Gold;
            set
            {
                if (User != null)
                {
                    User.DatabaseVariables.Gold = value;
                }

                Statistics.GoldChanged();
            }
        }

        public decimal SellMultiplier { get; } = 0.75m;

        public UserId UserId { get; }

        private string _name;

        [IgnoreMember]
        public string Name
        {
            get
            {
                var modifiers = new List<string>();
                if (Dead)
                {
                    modifiers.Add("[Мертв]");
                }
                else if (DateTime.Now - User.MessageManager.LastMessageRecived > TimeSpan.FromDays(7))
                {
                    modifiers.Add("[Спит]");
                }

                if (UserId.Messenger == 3) // Api messenger
                {
                    modifiers.Add("[Бот]");
                }

                return modifiers.Count == 0
                    ? _name
                    : $"{_name} <b>{string.Join(" ", modifiers)}</b>";
            }
            set => _name = value;
        }

        public Statistics Statistics { get; }

        public UserLevel Level { get; }

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
        ///     Минимально возможные характеристики (базовые).
        /// </summary>
        public Stats.Stats MinStats { get; set; }

        /// <summary>
        ///     Перерасчитывает <see cref="CurrentStats" />, учитывая текущие активные предметы.
        /// </summary>
        internal void RecalculateStats()
        {
            CurrentStats = ApplyItems(new Stats.Stats(BaseStats.Effect), User.ActiveItemsManager.ActiveItems);
        }

        internal static Stats.Stats ApplyItems(StatsEffect stats, IEnumerable<ItemInfo> activeItems)
        {
            var result = new Stats.Stats(stats.Effect);
            foreach (var item in activeItems)
            {
                if (item.Item.Effect == null)
                {
                    continue;
                }

                for (var i = 0; i < item.Count; i++)
                {
                    result = result.Apply(item.Item.Effect);
                }
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

        private bool ChangeStats(ChangeType changeType, StatsProperty property, decimal value, bool allowLess = false)
        {
            var changedBase = BaseStats.Apply(
                new StatsEffect(changeType, new Dictionary<StatsProperty, decimal>
                {
                    {property, value}
                })
            );
            bool decreased;
            if (changeType == ChangeType.Set)
            {
                decreased = changedBase.GetStat(property) - BaseStats.GetStat(property) < 0;
            }
            else
            {
                decreased = value < 0;
            }

            if (decreased)
            {
                // При понижении статов, нужно проверять с учетом предметов.
                // (базовое здоровье может быть меньше нуля, т.к. предметы тебя спасут)
                var changed = ApplyItems(changedBase, User.ActiveItemsManager.ActiveItems);
                var newValue = changed.GetStat(property);
                if (!allowLess && newValue < MinStats.GetStat(property))
                {
                    return false;
                }
            }
            else
            {
                // При повышении статов, нужно проверять без учета предметов.
                // (базовое здоровье не может быть больше максимума, но предметы могут повысить за пределы максимума)
                var newValue = changedBase.GetStat(property);
                var maxValue = MaxStats.GetStat(property);
                if (newValue > maxValue)
                {
                    // Если результат получился больше мсаксимума, то устанавливается максимум
                    changedBase = BaseStats.Apply(
                        new StatsEffect(ChangeType.Set, new Dictionary<StatsProperty, decimal>
                        {
                            {property, maxValue}
                        })
                    );
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

        public static event GameEventHandler OnDead;

        /// <summary>
        ///     Просто напросто убивает игрока
        /// </summary>
        public void Kill()
        {
            if (CurrentStats.GetStat(StatsProperty.Karma) == MaxStats.GetStat(StatsProperty.Karma))
            {
                ChangeStats(ChangeType.Set, StatsProperty.Karma, MinStats.GetStat(StatsProperty.Karma));
                ChangeStats(
                    ChangeType.Set,
                    StatsProperty.Health,
                    (MinStats.GetStat(StatsProperty.Health) + MaxStats.GetStat(StatsProperty.Health)) / 2
                );
                ChangeStats(ChangeType.Set, StatsProperty.Stamina, MinStats.GetStat(StatsProperty.Stamina));
                ChangeStats(ChangeType.Set, StatsProperty.Mana, MinStats.GetStat(StatsProperty.Mana));

                User.RoomManager.ChangeRoot("root/town");

                User.MessageManager.SendMessage(new SentMessage
                {
                    Text = "Такой хороший человек не может так просто умереть"
                });

                return;
            }

            OnDead?.Invoke(User);
            ChangeStats(ChangeType.Set, StatsProperty.Health, MinStats.GetStat(StatsProperty.Health));
            Dead = true;
            User.RoomManager.Go("_root", false);
        }

        public static decimal CalculateDefence(decimal damage, decimal defence)
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

            return damage * 19m / (defence + 19m) + 0.05m;
        }

        /// <summary>
        ///     Наносит урон с учетом защиты игрока. Убивает при необходимости
        /// </summary>
        /// <param name="value">Какой урон нанесен</param>
        /// <param name="defence">Учитывать ли защиту игрока</param>
        public void MakeDamage(decimal value, bool defence = true, bool kill = true)
        {
            if (defence)
            {
                value = CalculateDefence(value, CurrentStats.GetStat(StatsProperty.Defence));
            }

            ChangeStats(ChangeType.Add, StatsProperty.Health, -value, true);
            if (kill && CurrentStats.GetStat(StatsProperty.Health) <= MinStats.GetStat(StatsProperty.Health))
            {
                Kill();
            }
        }

        public decimal KarmaEffect(decimal value)
        {
            // 100 Karma = 15%
            const decimal step = 0.15m / 100;
            var percent = step * CurrentStats.GetStat(StatsProperty.Karma);
            return value * percent;
        }
    }
}