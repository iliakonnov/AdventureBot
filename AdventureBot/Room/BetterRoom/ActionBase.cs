using System;
using System.Collections.Generic;
using System.Reflection;
using AdventureBot.Messenger;

namespace AdventureBot.Room.BetterRoom
{
    public abstract class ActionBase<T> where T : BetterRoomBase<T>
    {
        private readonly MessageRecived _fallback;
        public readonly Dictionary<string, MessageRecived> Buttons;
        protected readonly T Room;

        protected ActionBase(T room)
        {
            Room = room;
            var self = GetType();

            Buttons = new Dictionary<string, MessageRecived>();
            _fallback = null;

            foreach (var method in self.GetMethods())
            {
                var attr = method.GetCustomAttribute<MessageHandlerAttribute>();
                if (attr == null)
                {
                    continue;
                }

                var handler = (MessageRecived) Delegate.CreateDelegate(typeof(MessageRecived), this, method, false);

                switch (attr)
                {
                    case ButtonAttribute button:
                    {
                        if (Buttons.ContainsKey(button.Text))
                        {
                            throw new Exception($"Multiple handlers for button {button.Text}");
                        }

                        Buttons[button.Text] = handler;
                        break;
                    }
                    case FallbackAttribute _:
                    {
                        if (_fallback != null)
                        {
                            throw new Exception("Multiple fallbacks found");
                        }

                        _fallback = handler;
                        break;
                    }
                }
            }

            if (_fallback == null)
            {
                _fallback = Room.HandleButtonAlways;
            }
        }

        public void OnMessage(User.User user, RecivedMessage message)
        {
            if (!Room.HandleButton(user, message))
            {
                _fallback(user, message);
            }
        }
    }
}