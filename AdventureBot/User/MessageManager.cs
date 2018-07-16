using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User.Stats;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot.User
{
    /// <summary>
    ///     Характеристики, которые возможно отображать под сообщением.
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

        /// <summary>
        ///     Характеристики по-умолчанию.
        ///     При переходе в новую комнату <see cref="MessageManager.ShownStats" /> сбрасывается на это значение
        /// </summary>
        Default = Health | Mana | Stamina
    }

    [MessagePackObject]
    public class MessageManager
    {
        [Key(nameof(LastMessages))] internal readonly Queue<SentMessage> LastMessages = new Queue<SentMessage>();
        [Key("intent")] private string _intent;
        [IgnoreMember] internal User _user;

        /// <summary>
        ///     Характеристики под сообщением.
        /// </summary>
        [Key(nameof(ShownStats))] public ShownStats ShownStats = ShownStats.Default;

        public MessageManager(User user)
        {
            _user = user;
            if (_user.MessageManager != null) ChatId = _user.MessageManager.ChatId;
        }

        [Obsolete("This constructor for serializer only")]
        [UsedImplicitly]
        [SerializationConstructor]
        public MessageManager(List<SentMessage> queue, string[][] buttons, Queue<SentMessage> lastMessages,
            ChatId chatId, RecivedMessage recievedMessage, ShownStats shownStats, string intent)
        {
            _queue = queue;
            _buttons = buttons;
            RecievedMessage = recievedMessage;
            LastMessages = lastMessages;
            ChatId = chatId;
            ShownStats = shownStats;
            _intent = intent;
        }

        [Key("queue")] private List<SentMessage> _queue { get; } = new List<SentMessage>();
        [Key("buttons")] private string[][] _buttons { get; set; }
        [Key(nameof(RecievedMessage))] internal RecivedMessage RecievedMessage { get; set; }


        /// <summary>
        ///     Id чата, в который будут отправляться сообщения
        /// </summary>
        [Key(nameof(ChatId))]
        public ChatId ChatId { get; internal set; }

        /// <summary>
        ///     Добавляет сообщение в очередь.
        /// </summary>
        public void SendMessage(SentMessage message)
        {
            _queue.Add(message);
            if (message.Buttons != null) _buttons = message.Buttons;

            if (message.Intent != null) _intent = message.Intent;
        }

        /// <summary>
        ///     Сразу же отправляет сообщение, не добавляя его в очередь.
        /// </summary>
        /// <param name="message"></param>
        internal void SendImmediately(SentMessage message)
        {
            ObjectManager<IMessenger>.Instance.Get<MessengerManager>().Reply(new SentMessage
            {
                Text = message.Text,
                Buttons = message.Buttons,
                Intent = message.Intent,
                ChatId = ChatId
            }, null, _user);
        }

        internal void OnRecieved(RecivedMessage message)
        {
            _user.ItemManager.OnMessage();

            var room = _user.RoomManager.GetRoom();
            if (room == null)
            {
                if (_user.RoomManager.Rooms.Count == 0)
                {
                    SendMessage(new SentMessage
                    {
                        Text = "Вы находитесь в *нигде*. Попробуйте /start, только это вам поможет"
                    });
                }
                else
                {
                    SendMessage(new SentMessage
                    {
                        Text = "Такое чувство, что вы в несуществующей комнате! Попробуем вытащить вас отсюда."
                    });
                    _user.RoomManager.Leave();
                }
            }
            else
            {
                room.OnMessage(_user, message);
            }
        }

        private string AddInfo(IEnumerable<string> messages)
        {
            // Path
            var roomMgr = ObjectManager<IRoom>.Instance.Get<Room.RoomManager>();
            var path = string.Join(">", _user.RoomManager.Rooms
                .Reverse()
                .Select(room => roomMgr.Get(room.Identifier)?.Name)
                .Concat(new[] {roomMgr.Get(_user.RoomManager.CurrentRoom?.Identifier)?.Name})
                .Where(n => n != null)
            );

            var stats = new StringBuilder();

            foreach (ShownStats shownStat in Enum.GetValues(typeof(ShownStats)))
                if ((shownStat & ShownStats) != 0)
                    switch (shownStat)
                    {
                        case ShownStats.Health:
                        {
                            var heart = "♥️";
                            var percent = _user.Info.CurrentStats.Effect[StatsProperty.Health] /
                                          _user.Info.MaxStats.Effect[StatsProperty.Health];
                            if (percent < 1m / 3)
                                heart = "🖤️"; // black
                            else if (percent < 2m / 3)
                                heart = "💛"; // yellow
                            else if (percent < 2m / 3) heart = "❤️"; // red

                            stats.Append($"{heart}{_user.Info.CurrentStats.Effect[StatsProperty.Health]:F2}");
                            break;
                        }
                        case ShownStats.Intelligence:
                        {
                            const StatsProperty prop = StatsProperty.Intelligence;
                            stats.Append($" {Stats.Stats.Emojis[prop]}{_user.Info.CurrentStats.Effect[prop]:F2}");
                            break;
                        }
                        case ShownStats.Strength:
                        {
                            const StatsProperty prop = StatsProperty.Strength;
                            stats.Append($" {Stats.Stats.Emojis[prop]}{_user.Info.CurrentStats.Effect[prop]:F2}");
                            break;
                        }
                        case ShownStats.Mana:
                        {
                            const StatsProperty prop = StatsProperty.Mana;
                            stats.Append($" {Stats.Stats.Emojis[prop]}{_user.Info.CurrentStats.Effect[prop]:F2}");
                            break;
                        }
                        case ShownStats.Stamina:
                        {
                            const StatsProperty prop = StatsProperty.Stamina;
                            stats.Append($" {Stats.Stats.Emojis[prop]}{_user.Info.CurrentStats.Effect[prop]:F2}");
                            break;
                        }
                        case ShownStats.Defence:
                        {
                            const StatsProperty prop = StatsProperty.Defence;
                            stats.Append($" {Stats.Stats.Emojis[prop]}{_user.Info.CurrentStats.Effect[prop]:F2}");
                            break;
                        }
                        case ShownStats.Gold:
                        {
                            stats.Append($" 💰{_user.Info.Gold:F2}");
                            break;
                        }
                        case ShownStats.Default:
                            break;
                        default:
                        {
                            throw new ArgumentOutOfRangeException();
                        }
                    }

            return string.Join("\n\n", Enumerable.Empty<string>()
                .Concat(new[] {$"_{path}_"})
                .Concat(messages)
                .Concat(new[] {stats.ToString()})
            );
        }

        internal void Finish()
        {
            if (_queue.Count == 0) return;

            var totalText = AddInfo(_queue.Select(m => m.Text));

            if (string.IsNullOrWhiteSpace(totalText)) return;

            var message = new SentMessage
            {
                Text = totalText,
                Buttons = _buttons,
                ChatId = ChatId,
                Intent = _intent
            };

            var room = _user.RoomManager.Rooms.FirstOrDefault();
            if (room != null) room.LastMessage = LastMessages.LastOrDefault();

            ObjectManager<IMessenger>.Instance.Get<MessengerManager>().Reply(message, RecievedMessage, _user);
            while (LastMessages.Count > 10) LastMessages.Dequeue();

            LastMessages.Enqueue(message);

            _queue.Clear();
            _buttons = null;
            _intent = null;
        }

        /// <summary>
        ///     Экранирует сообщение так, чтобы в нём не было симолов форматирования markdown'а
        /// </summary>
        public static string Escape(string message)
        {
            return message
                .Replace(@"`", @"\`")
                .Replace(@"_", @"\_")
                .Replace(@"*", @"\*");
        }
    }
}