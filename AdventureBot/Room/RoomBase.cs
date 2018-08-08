using System;
using System.Collections.Generic;
using System.Linq;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;

namespace AdventureBot.Room
{
    public abstract class RoomBase : IRoom
    {
        protected VariableContainer GetRoomVariables(User.User user)
        {
            return user.VariableManager.GetRoomVariables(Identifier);
        }

        protected delegate void MessageRecived(User.User user, RecivedMessage message);

        #region IRoom implementation

        public abstract string Name { get; }
        public abstract string Identifier { get; }
        public abstract void OnMessage(User.User user, RecivedMessage message);

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
                SendMessage(user, $"Из этого места смогли выбраться живым в {percents:#0.##%} случаев");
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

        protected MessageRecived[] Routes { get; set; }

        private int? GetRouteIdx(User.User user)
        {
            var action = GetRoomVariables(user).Get("action");

            return (Serializable.Int) action;
        }

        protected bool HandleAction(User.User user, RecivedMessage message)
        {
            var route = GetRouteIdx(user);

            if (route == null)
            {
                return false;
            }

            Routes[(int) route](user, message);
            return true;
        }

        protected void SwitchAction(User.User user, MessageRecived handler)
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

        protected void SwitchAndHandle(User.User user, MessageRecived handler, RecivedMessage message)
        {
            SwitchAction(user, handler);
            handler?.Invoke(user, message);
        }

        #endregion

        #region Buttons

        protected NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>> Buttons { get; set; } =
            new NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>>();

        private Dictionary<string, MessageRecived> GetCurrentButtons(User.User user)
        {
            Dictionary<string, MessageRecived> buttons;
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

        protected void HandleButtonAlways(User.User user, RecivedMessage message)
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

        protected string[][] GetButtons(User.User user)
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

        protected bool HandleButton(User.User user, RecivedMessage message)
        {
            var buttons = GetCurrentButtons(user);

            if (buttons == null)
            {
                return false;
            }

            if (buttons.TryGetValue(message.Text, out var handler))
            {
                handler(user, message);
                return true;
            }

            return false;
        }

        #endregion

        #region Use items

        protected static string[] GetItems(User.User user)
        {
            return user.ItemManager.Items
                .Where(i => i.CanUse(user))
                .Select(i => $"{i.Item.Name} (x{i.Count})")
                .ToArray();
        }

        protected static bool UseItem(User.User user, RecivedMessage message)
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

        protected void SendMessage(User.User user, string message, string[][] buttons = null, string intent = null)
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

        protected static ItemManager GetAllItems()
        {
            return ObjectManager<IItem>.Instance.Get<ItemManager>();
        }

        protected static RoomManager GetAllRooms()
        {
            return ObjectManager<IRoom>.Instance.Get<RoomManager>();
        }

        #endregion
    }
}