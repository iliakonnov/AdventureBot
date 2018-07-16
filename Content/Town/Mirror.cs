using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Town
{
    [Room("town/mirror")]
    public class Mirror : RoomBase
    {
        public Mirror()
        {
            Routes = new MessageRecived[] {EditStats};
            Buttons = new NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>>
            {
                {
                    null, new Dictionary<string, MessageRecived>
                    {
                        {
                            "Перераспределить предметы", (user, message) =>
                            {
                                SwitchAction(user, EditStats);
                                SendMessage(user, "Ты начал тщательно рыться в карманах");
                                EditStats(user, message);
                            }
                        },
                        {
                            "Инвентарь", (user, message) =>
                            {
                                SendMessage(user, "У тебя в карманах можно найти:", GetButtons(user));
                                foreach (var info in user.ItemManager.Items)
                                {
                                    var active = user.ActiveItemsManager.ActiveItems
                                        .FirstOrDefault(item => item.Identifier == info.Identifier);
                                    var description = new StringBuilder($"*{info.Item.Name}* (x{info.Count})");

                                    if (active != null)
                                    {
                                        description.Append($" ({active.Count} активно)");
                                    }

                                    if (!string.IsNullOrWhiteSpace(info.Item.Description))
                                    {
                                        description.AppendLine().Append(info.Item.Description);
                                    }

                                    if (info.Item.Effect != null && info.Item.Effect.Effect.Count != 0)
                                    {
                                        description.AppendLine();

                                        foreach (var effect in info.Item.Effect.Effect)
                                        {
                                            description.Append($"{Stats.Emojis[effect.Key]}: {effect.Value:F2} ");
                                            if (active != null)
                                            {
                                                description.Append($" (*{effect.Value * active.Count:+#.##;-#.##;0}*) ");
                                            }
                                        }
                                    }

                                    SendMessage(user, description.ToString());
                                }
                            }
                        },
                        {
                            "Уйти", (user, message) => user.RoomManager.Leave()
                        }
                    }
                }
            };
        }

        public override string Name => "Зеркало";
        public override string Identifier => "town/mirror";

        public override void OnEnter(User user)
        {
            SendMessage(user, "Вы смотрите в зеркало и узнаете о себе много нового.", GetButtons(user));

            ShowStats(user);
        }

        public override bool OnLeave(User user)
        {
            return true;
        }

        public override void OnMessage(User user, RecivedMessage message)
        {
            if (!HandleAction(user, message)) HandleButtonAlways(user, message);
        }

        private void ShowStats(User user)
        {
            var stats = new StringBuilder().AppendLine("Текущие характеристики:");
            foreach (var stat in user.Info.CurrentStats.Effect)
            {
                var emoji = Stats.Emojis[stat.Key];
                stats.Append(emoji);
                switch (stat.Key)
                {
                    case StatsProperty.Health:
                        stats.Append(" Здоровье");
                        break;
                    case StatsProperty.Intelligence:
                        stats.Append(" Интеллект");
                        break;
                    case StatsProperty.Strength:
                        stats.Append(" Сила");
                        break;
                    case StatsProperty.Mana:
                        stats.Append(" Мана");
                        break;
                    case StatsProperty.Stamina:
                        stats.Append(" Остаток сил");
                        break;
                    case StatsProperty.Defence:
                        stats.Append(" Защита");
                        break;
                    default:
                        throw new ArgumentOutOfRangeException();
                }

                stats.Append(": ").Append(stat.Value).AppendLine();
            }

            SendMessage(user, stats.ToString());
        }

        private string[][] EditButtons(User user)
        {
            // Show current proportions
            var numbers = new[] {-5, -3, -1, +1, +3, +5};
            var buttons = new List<string[]>
            {
                new[] {"Закончить"}
            };

            foreach (var proportion in user.ActiveItemsManager.GetAvailableProportions())
            {
                var emoji = string.Join(",", proportion.Values.Select(k => Stats.Emojis[k]));
                var row = new string[numbers.Length];
                for (var i = 0; i < numbers.Length; i++)
                {
                    var number = numbers[i];
                    row[i] = $"{emoji} {number:+#.##;-#.##;0}";
                }

                buttons.Add(row);
            }

            return buttons.ToArray();
        }

        private void EditStats(User user, RecivedMessage message)
        {
            var splitted = message.Text.Split(' ');
            if (splitted[0] == "Закончить")
            {
                SwitchAction(user, null);
                SendMessage(user, "Тебе надоело рыться в карманах", GetButtons(user));
                return;
            }

            // Handle change
            var reverse = Stats.Emojis.ToDictionary(kv => kv.Value, kv => kv.Key);
            var changed = false;

            var flag = new Flag<StatsProperty>();
            foreach (var propEmoji in splitted[0].Split(','))
                if (reverse.TryGetValue(propEmoji, out var prop))
                    flag |= new Flag<StatsProperty>(prop);

            var count = 0;
            if (!flag.Values.IsEmpty && int.TryParse(splitted[1], out count))
            {
                user.ActiveItemsManager.ChangeProportion(flag, count);
                changed = true;
            }

            // Show current stats
            ShowStats(user);

            // Show current proportions
            var current = new StringBuilder().AppendLine("Текущее распределение:");
            foreach (var proportion in user.ActiveItemsManager.ActiveProportions)
            {
                var emoji = string.Join(",", proportion.Key.Values.Select(k => Stats.Emojis[k]));
                current.Append(emoji).Append(": ").Append(proportion.Value);
                if (changed && flag.Equals(proportion.Key)) current.Append($" _({count:+#.##;-#.##;0})_");
                current.AppendLine();
            }

            SendMessage(user, current.ToString(), EditButtons(user));

            // Show how many available
            var used = user.ActiveItemsManager.ActiveProportions.Select(kv => kv.Value).Sum();
            var total = user.ActiveItemsManager.ActiveLimit;
            SendMessage(user, $"Распределено {used} из {total}. Доступно {total - used} активных предметов");
        }
    }
}