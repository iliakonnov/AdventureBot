using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User.Stats;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot.User;

/// <summary>
/// Характеристики, которые возможно отображать под сообщением.
/// </summary>
[Flags]
public enum ShownStats
{
    Health = 1 << 0,
    Mana = 1 << 1,
    Stamina = 1 << 2,
    Gold = 1 << 3,
    Intelligence = 1 << 4,
    Strength = 1 << 5,
    Defence = 1 << 6,
    Karma = 1 << 7,

    /// <summary>
    /// Характеристики по-умолчанию.
    /// При переходе в новую комнату <see cref="MessageManager.ShownStats" /> сбрасывается на это значение
    /// </summary>
    Default = Health | Mana | Stamina
}

[MessagePackObject]
public class MessageManager
{
    [Key("LastMessages")] private readonly Queue<SentMessage> _lastMessages = new();
    [Key("intent")] private string _intent;

    /// <summary>
    /// Характеристики под сообщением.
    /// </summary>
    [Key(nameof(ShownStats))] public ShownStats ShownStats = ShownStats.Default;

    [IgnoreMember] internal User User;

    public MessageManager(User user)
    {
        User = user;
        if (User.MessageManager == null)
        {
            return;
        }

        ChatId = User.MessageManager.ChatId;
        ReceivedMessage = User.MessageManager.ReceivedMessage;
    }

    [Obsolete("This constructor for serializer only")]
    [UsedImplicitly]
    [SerializationConstructor]
    public MessageManager(List<SentMessage> queue, string[][] buttons, bool preferToUpdate,
        Queue<SentMessage> lastMessages,
        ChatId chatId, ReceivedMessage recievedMessage, ShownStats shownStats, string intent)
    {
        Queue = queue;
        Buttons = buttons ?? new string[0][];
        PreferToUpdate = preferToUpdate;
        ReceivedMessage = recievedMessage;
        _lastMessages = lastMessages;
        ChatId = chatId;
        ShownStats = shownStats;
        _intent = intent;
    }

    [IgnoreMember] public IReadOnlyCollection<SentMessage> LastMessages => _lastMessages;
    [IgnoreMember] [CanBeNull] public SentMessage LastMessage => _lastMessages.LastOrDefault();

    [Key("queue")] private List<SentMessage> Queue { get; } = new();
    [Key("buttons")] [NotNull] private string[][] Buttons { get; set; } = new string[0][];
    [Key("PreferToUpdate")] private bool PreferToUpdate { get; set; } = true;
    [Key("RecievedMessage")] internal ReceivedMessage ReceivedMessage { get; set; }

    [IgnoreMember] public DateTime LastMessageReceived => User.DatabaseVariables.LastMessageReceived;


    /// <summary>
    /// Id чата, в который будут отправляться сообщения
    /// </summary>
    [Key(nameof(ChatId))]
    public ChatId ChatId { get; internal set; }

    /// <summary>
    /// Добавляет сообщение в очередь.
    /// </summary>
    public void SendMessage(SentMessage message)
    {
        Queue.Add(message);
        if (message.Buttons != null)
        {
            Buttons = message.Buttons;
        }

        if (message.PreferToUpdate != null)
        {
            PreferToUpdate = PreferToUpdate && message.PreferToUpdate.Value;
        }

        if (message.Intent != null)
        {
            PreferToUpdate = PreferToUpdate && message.Intent == _intent;
            _intent = message.Intent;
        }
    }

    /// <summary>
    /// Сразу же отправляет сообщение, не добавляя его в очередь.
    /// </summary>
    /// <param name="message"></param>
    internal void SendImmediately(SentMessage message)
    {
        ObjectManager<IMessenger>.Instance.Get<MessengerManager>().Reply(new SentMessage
        {
            Text = message.Text,
            Buttons = message.Buttons,
            Intent = message.Intent,
            PreferToUpdate = message.PreferToUpdate,
            ChatId = ChatId
        }, null, User);
    }

    internal void OnReceived(ReceivedMessage message)
    {
        var room = User.RoomManager.GetRoom();
        User.DatabaseVariables.LastMessageReceived = DateTime.Now;
        switch (room)
        {
            case null when User.RoomManager.Rooms.Count == 0:
                SendMessage(new SentMessage
                {
                    Text = "Вы находитесь в <b>нигде</b>. Попробуйте /start, только это вам поможет"
                });
                break;
            case null:
                SendMessage(new SentMessage
                {
                    Text = "Такое чувство, что вы в несуществующей комнате! Попробуем вытащить вас отсюда."
                });
                User.RoomManager.Leave();
                break;
            default:
                Debug.Assert(room != null, nameof(room) + " != null");
                room.OnMessage(User, message);
                break;
        }
    }

    private string AddInfo(IEnumerable<string> messages)
    {
        void AddStat(StringBuilder stringBuilder, StatsProperty property)
        {
            stringBuilder.Append(
                $" {Stats.Stats.Emojis[property]}{User.Info.CurrentStats.GetStat(property).Format()}");
        }

        // Path
        var roomMgr = ObjectManager<IRoom>.Instance.Get<Room.RoomManager>();
        var path = string.Join(">", User.RoomManager.Rooms
            .Reverse()
            .Select(room => roomMgr.Get(room.Identifier)?.Name)
            .Concat(new[] {roomMgr.Get(User.RoomManager.CurrentRoom?.Identifier)?.Name})
            .Where(n => n != null)
        );

        var stats = new StringBuilder();

        foreach (ShownStats shownStat in Enum.GetValues(typeof(ShownStats)))
        {
            if ((shownStat & ShownStats) == 0)
            {
                continue;
            }

            switch (shownStat)
            {
                case ShownStats.Health:
                {
                    var heart = "♥️";
                    var percent = User.Info.CurrentStats.GetStat(StatsProperty.Health) /
                                  User.Info.MaxStats.GetStat(StatsProperty.Health);
                    if (percent < 1m / 3)
                    {
                        heart = "🖤️"; // black
                    }
                    else if (percent < 2m / 3)
                    {
                        heart = "💛"; // yellow
                    }
                    else if (percent < 2m / 3)
                    {
                        heart = "❤️"; // red
                    }

                    stats.Append($"{heart}{User.Info.CurrentStats.GetStat(StatsProperty.Health).Format()}");
                    break;
                }
                case ShownStats.Intelligence:
                {
                    AddStat(stats, StatsProperty.Intelligence);
                    break;
                }
                case ShownStats.Strength:
                {
                    AddStat(stats, StatsProperty.Strength);
                    break;
                }
                case ShownStats.Mana:
                {
                    AddStat(stats, StatsProperty.Mana);
                    break;
                }
                case ShownStats.Stamina:
                {
                    AddStat(stats, StatsProperty.Stamina);
                    break;
                }
                case ShownStats.Defence:
                {
                    AddStat(stats, StatsProperty.Defence);
                    break;
                }
                case ShownStats.Karma:
                {
                    AddStat(stats, StatsProperty.Karma);
                    break;
                }
                case ShownStats.Gold:
                {
                    stats.Append($" 💰{User.Info.Gold.Format()}");
                    break;
                }
                case ShownStats.Default:
                    break;
                default:
                {
                    throw new ArgumentOutOfRangeException();
                }
            }
        }

        return string.Join("\n\n", Enumerable.Empty<string>()
            .Concat(new[] {$"<i>{path}</i>"})
            .Concat(messages)
            .Concat(new[] {stats.ToString()})
        );
    }

    public void Finish()
    {
        if (Queue.Count == 0)
        {
            return;
        }

        var totalText = AddInfo(Queue.Select(m => m.Text));

        if (string.IsNullOrWhiteSpace(totalText))
        {
            return;
        }

        var message = new SentMessage
        {
            Text = totalText,
            Buttons = Buttons,
            PreferToUpdate = PreferToUpdate,
            ChatId = ChatId,
            Intent = _intent
        };

        var room = User.RoomManager.Rooms.FirstOrDefault();
        if (room != null)
        {
            room.LastMessage = _lastMessages.LastOrDefault();
        }

        ObjectManager<IMessenger>.Instance.Get<MessengerManager>().Reply(message, ReceivedMessage, User);
        while (_lastMessages.Count > 10)
        {
            _lastMessages.Dequeue();
        }

        _lastMessages.Enqueue(message);

        Queue.Clear();
        PreferToUpdate = true;
    }

    /// <summary>
    /// Экранирует сообщение так, чтобы в нём не было симолов форматирования
    /// </summary>
    public static string Escape(string message)
    {
        return message
            .Replace("&", "&amp;")
            .Replace("<", "&lt;")
            .Replace(">", "&gt;");
    }
}