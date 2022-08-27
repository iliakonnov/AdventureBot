﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.NameGenerator;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Town;

[Room(Id)]
public class Mirror : RoomBase
{
    public const string Id = "town/mirror";

    public Mirror()
    {
        Routes = new MessageReceived[] {EditStats, Inventory, ChangeName};
        Buttons = new NullableDictionary<MessageReceived, Dictionary<string, MessageReceived>>
        {
            {
                null, new Dictionary<string, MessageReceived>
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
                        "Имущество", (user, message) =>
                        {
                            GetRoomVariables(user).Set("current_page", new Serializable.Int(0));
                            SwitchAction(user, Inventory);
                            Inventory(user, message);
                        }
                    },
                    {
                        "Сменить имя", (user, message) =>
                        {
                            SwitchAction(user, ChangeName);
                            SendMessage(user, "Какое имя вы желаете?", GetButtons(user));
                        }
                    },
                    {
                        "Квесты", (user, message) =>
                        {
                            var found = false;
                            foreach (var quests in user.QuestManager.Quests.Values)
                            {
                                foreach (var quest in quests.Values)
                                {
                                    found = true;
                                    var msg = quest.Quest.GetName(user, quest.QuestId);
                                    msg += $"\nВыполнено {quest.Quest.GetProgress(user, quest.QuestId).Format()}%";
                                    SendMessage(user, msg, GetButtons(user));
                                }
                            }

                            if (!found)
                            {
                                SendMessage(user, "У вас нет квестов", GetButtons(user));
                            }
                        }
                    },
                    {
                        "Уйти", (user, message) => user.RoomManager.Leave()
                    }
                }
            },
            {
                ChangeName,
                new Dictionary<string, MessageReceived>
                {
                    {
                        "Сгенерировать случайное",
                        (user, message) => { user.Info.Name = Generator.Generate(user.Random); }
                    }
                }
            }
        };
    }

    public override string Name => "Зеркало";
    public override string Identifier => Id;

    public override void OnEnter(User user)
    {
        SendMessage(user, "Вы смотрите в зеркало и узнаете о себе много нового.", GetButtons(user));

        ShowStats(user);
    }

    public override bool OnLeave(User user)
    {
        return true;
    }

    public override void OnMessage(User user, ReceivedMessage message)
    {
        if (!HandleAction(user, message))
        {
            HandleButtonAlways(user, message);
        }
    }

    public void ChangeName(User user, ReceivedMessage message)
    {
        if (!HandleButton(user, message))
        {
            var name = message.Text
                .Replace("<strong>", "<b>").Replace("</strong>", "</b>")
                .Replace("<em>", "<i>").Replace("</em>", "</i>");
            var tags = new[] {"b", "i", "code", "pre"};
            string openedTag = null;
            var valid = true;
            for (var i = 0; i < name.Length;)
            {
                var tagFound = false;
                foreach (var tag in tags)
                {
                    var opening = $"<{tag}>";
                    if (i + opening.Length <= name.Length && name.Substring(i, opening.Length) == opening)
                    {
                        // Found opening tag
                        if (openedTag != null)
                        {
                            // Nested tags: <i><b>
                            valid = false;
                            goto NameValidated;
                        }

                        openedTag = tag;
                        tagFound = true;
                        i += opening.Length;
                        break; // breaks out from inner loop: foreach (var tag in tags)
                    }

                    var closing = $"</{tag}>";
                    if (i + closing.Length <= name.Length && name.Substring(i, closing.Length) == closing)
                    {
                        // Found closing tag
                        if (openedTag != tag)
                        {
                            // wrong closing tag: <i></b>
                            valid = false;
                            goto NameValidated;
                        }

                        openedTag = null;
                        tagFound = true;
                        i += closing.Length;
                        break; // breaks out from inner loop: foreach (var tag in tags)
                    }
                }

                if (!tagFound)
                {
                    // No tag was found
                    i++;
                }
            }

            NameValidated:
            valid = valid && openedTag == null; // Every tag was closed
            if (!valid)
            {
                name = MessageManager.Escape(name);
            }

            user.Info.Name = name;
        }

        SwitchAction(user, null);
        SendMessage(user, $"Отныне вас зовут {user.Info.Name}", GetButtons(user));
    }

    private void ShowStats(User user)
    {
        var stats = new StringBuilder().Append("Имя: ").AppendLine(user.Info.Name);
        stats.AppendLine(
            $"Уровень: {user.Info.Level.Level} ({user.Info.Level.ExpirenceCollected.Format()} / {user.Info.Level.ExpirenceRequired.Format()})");
        stats.AppendLine("Текущие характеристики:");
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
                case StatsProperty.Karma:
                    stats.Append(" Карма");
                    break;
                default:
                    throw new ArgumentOutOfRangeException();
            }

            stats.Append(": ").Append(stat.Value.Format()).AppendLine();
        }

        SendMessage(user, stats.ToString());
    }

    private static string[][] EditButtons(User user)
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

    private void EditStats(User user, ReceivedMessage message)
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

        var flag = new StructFlag<StatsProperty>();
        foreach (var propEmoji in splitted[0].Split(','))
        {
            if (reverse.TryGetValue(propEmoji, out var prop))
            {
                flag |= new StructFlag<StatsProperty>(prop);
            }
        }

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
            if (changed && flag.Equals(proportion.Key))
            {
                current.Append($" <i>({count:+#.##;-#.##;0})</i>");
            }

            current.AppendLine();
        }

        SendMessage(user, current.ToString(), EditButtons(user));

        // Show how many available
        var used = user.ActiveItemsManager.ActiveProportions.Select(kv => kv.Value).Sum();
        var total = user.ActiveItemsManager.ActiveLimit;
        SendMessage(user, $"Распределено {used} из {total}. Доступно {total - used} активных предметов");
    }

    private void Inventory(User user, ReceivedMessage message)
    {
        var variables = GetRoomVariables(user);
        var currentPage = (Serializable.Int) variables.Get("current_page") ?? 0;
        string use = null;
        switch (message.Text)
        {
            case "Выйти":
                SwitchAction(user, null);
                ShowStats(user);
                SendMessage(user, string.Empty, GetButtons(user));
                return;
            case "Вперед":
                currentPage++;
                break;
            case "Назад":
                currentPage--;
                break;
            default:
                if (message.Text.StartsWith("Использовать"))
                {
                    use = message.Text.Substring("Использовать ".Length);
                }

                break;
        }

        variables.Set("current_page", new Serializable.Int(currentPage));

        const int itemsPerPage = 8;
        var pageCount = user.ItemManager.Items.Count / itemsPerPage;
        currentPage = Math.Min(pageCount, currentPage);
        currentPage = Math.Max(0, currentPage);

        var items = user.ItemManager.Items
            .Skip(currentPage * itemsPerPage)
            .Take(itemsPerPage)
            .ToList();

        if (use != null)
        {
            foreach (var info in items)
            {
                if (info.Item.Name == use)
                {
                    info.OnUse(user);
                    break;
                }
            }

            SwitchAction(user, null);
            SendMessage(user, string.Empty, GetButtons(user));
            return;
        }

        var buttons = new List<string[]>();
        SendMessage(user, $"Страница {currentPage + 1} из {pageCount + 1}");

        foreach (var info in items)
        {
            var active = user.ActiveItemsManager.ActiveItems
                .FirstOrDefault(item => item.Identifier == info.Identifier);
            var description = new StringBuilder($"<b>{info.Item.Name}</b> (x{info.Count})");

            if (info.CanUse(user))
            {
                buttons.Add(new[] {$"Использовать {info.Item.Name}"});
            }

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
                    description.Append($"{Stats.Emojis[effect.Key]}: {effect.Value.Format()} ");
                    if (active != null)
                    {
                        description.Append(
                            $" (<b>{(effect.Value * active.Count).Format()}</b>) ");
                    }
                }
            }

            SendMessage(user, description.ToString());
        }

        var endingButtons = new List<string>();
        if (currentPage > 0)
        {
            endingButtons.Add("Назад");
        }

        endingButtons.Add("Выйти");
        if (currentPage < pageCount)
        {
            endingButtons.Add("Вперед");
        }

        buttons.Add(endingButtons.ToArray());

        SendMessage(user, string.Empty, buttons.ToArray());
    }
}