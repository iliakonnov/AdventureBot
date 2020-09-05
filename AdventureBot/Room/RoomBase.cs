using System;
using System.Collections.Generic;
using System.Linq;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;

namespace AdventureBot.Room
{
    public delegate void MessageReceived(User.User user, ReceivedMessage message);

    public abstract class RoomBase : IRoom
    {
        public VariableContainer GetRoomVariables(User.User user)
        {
            return user.VariableManager.GetRoomVariables(Identifier);
        }

        #region IRoom implementation

        public abstract string Name { get; }
        public abstract string Identifier { get; }
        public abstract void OnMessage(User.User user, ReceivedMessage message);

        public virtual bool OnLeave(User.User user)
        {
            UpdateCounter("rooms_leave", 1);
            return true;
        }

        private int UpdateCounter(string containerName, int diff)
        {
            int value;
            var container = GlobalVariables.Variables.Get<VariableContainer>(containerName);
            if (container == null)
            {
                container = new VariableContainer();
                GlobalVariables.Variables.Set(containerName, container);
                value = 0;
            }
            else
            {
                value = container.Get<Serializable.Int>(Identifier);
            }

            if (diff != 0)
            {
                container.Set(Identifier, new Serializable.Int(value + diff));
            }

            return value + diff;
        }

        public virtual void OnEnter(User.User user)
        {
            var enterCount = UpdateCounter("rooms_enter", 1) - 1;
            var leaveCount = UpdateCounter("rooms_leave", 0);

            if (enterCount != 0)
            {
                var percents = (decimal) leaveCount / enterCount;
                SendMessage(user, $"Из этого места выбрались живыми в {percents:#0.##%} случаев");
            }
            else
            {
                SendMessage(user, "Вы — первый, кто сюда зашел!");
            }
        }

        public virtual void OnReturn(User.User user)
        {
            UpdateCounter("rooms_leave", -1);
            user.RoomManager.Leave();
        }

        #endregion

        #region Routes & actions

        public MessageReceived[] Routes { get; set; }

        public MessageReceived GetCurrentRoute(User.User user)
        {
            var route = GetRouteIdx(user);

            return route == null ? null : Routes[(int) route];
        }

        private int? GetRouteIdx(User.User user)
        {
            var action = GetRoomVariables(user).Get("action");

            return (Serializable.Int) action;
        }

        public bool HandleAction(User.User user, ReceivedMessage message)
        {
            var route = GetCurrentRoute(user);

            if (route == null)
            {
                return false;
            }

            route(user, message);
            return true;
        }

        public void SwitchAction(User.User user, MessageReceived handler)
        {
            if (handler == null)
            {
                GetRoomVariables(user).Remove("action");
                return;
            }

            var idx = Array.IndexOf(Routes, handler);
            if (idx == -1)
            {
                throw new ArgumentException("Unregistered handler! Every handler must be defined in _routes");
            }

            GetRoomVariables(user).Set("action", new Serializable.Int(idx));
        }

        public void SwitchAndHandle(User.User user, MessageReceived handler, ReceivedMessage message)
        {
            SwitchAction(user, handler);
            handler?.Invoke(user, message);
        }

        #endregion

        #region Buttons

        public NullableDictionary<MessageReceived, Dictionary<string, MessageReceived>> Buttons { get; set; } =
            new NullableDictionary<MessageReceived, Dictionary<string, MessageReceived>>();

        private Dictionary<string, MessageReceived> GetCurrentButtons(User.User user)
        {
            Dictionary<string, MessageReceived> buttons;
            var route = GetRouteIdx(user);
            if (route == null)
            {
                buttons = Buttons[null];
            }
            else
            {
                Buttons.TryGetValue(Routes[(int) route], out buttons);
            }

            return buttons;
        }

        public void HandleButtonAlways(User.User user, ReceivedMessage message)
        {
            var buttons = GetCurrentButtons(user);

            if (buttons == null)
            {
                throw new Exception("Cannot handle buttons. Cannot find buttons for current action.");
            }

            if (buttons.TryGetValue(message.Text, out var handler))
            {
                handler(user, message);
            }
            else
            {
                SendMessage(user, "Ты говоришь что-то непонятное", GetButtons(user), "unknown_button");
            }
        }

        public string[][] GetButtons(User.User user)
        {
            var buttons = GetCurrentButtons(user);

            if (buttons == null)
            {
                return null;
            }

            var result = new string[buttons.Count][];

            var i = 0;
            foreach (var text in buttons.Keys)
            {
                result[i] = new[] {text};
                i++;
            }

            return result;
        }

        public bool HandleButton(User.User user, ReceivedMessage message)
        {
            var buttons = GetCurrentButtons(user);

            if (buttons == null)
            {
                return false;
            }

            if (!buttons.TryGetValue(message.Text, out var handler))
            {
                return false;
            }

            handler(user, message);
            return true;
        }

        #endregion

        #region Use items

        public static IEnumerable<string> GetItems(User.User user)
        {
            return user.ItemManager.Items
                .Where(i => i.CanUse(user))
                .Select(i => $"{i.Item.Name} (x{i.Count})");
        }

        public static bool UseItem(User.User user, ReceivedMessage message)
        {
            var item = user.ItemManager.Items.SingleOrDefault(i =>
                i.CanUse(user) && message.Text.StartsWith(i.Item.Name)
            );
            if (item == null)
            {
                return false;
            }

            item.OnUse(user);
            return true;
        }

        #endregion

        #region Small helpers

        public void SendMessage(User.User user, string message)
        {
            SendMessage(user, message, null, null);
        }

        public void SendMessage(User.User user, string message, string[][] buttons)
        {
            SendMessage(user, message, buttons, null);
        }

        public void SendMessage(User.User user, string message, string intent)
        {
            SendMessage(user, message, null, intent);
        }

        public void SendMessage(User.User user, string message, string[][] buttons, string intent)
        {
            if (intent == null)
            {
                intent = $"room/{Identifier}";
                var route = GetRouteIdx(user);
                if (route != null)
                {
                    intent += $"/{route}";
                }
            }

            user.MessageManager.SendMessage(new SentMessage
            {
                Text = message,
                Buttons = buttons,
                Intent = intent
            });
        }

        public static ItemManager GetAllItems()
        {
            return ObjectManager<IItem>.Instance.Get<ItemManager>();
        }

        public static RoomManager GetAllRooms()
        {
            return ObjectManager<IRoom>.Instance.Get<RoomManager>();
        }

        #endregion
    }
}