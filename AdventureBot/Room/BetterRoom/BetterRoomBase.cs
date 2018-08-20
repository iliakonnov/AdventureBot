using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using AdventureBot.Messenger;

namespace AdventureBot.Room.BetterRoom
{
    public abstract class BetterRoomBase<T> : RoomBase where T : BetterRoomBase<T>
    {
        private Dictionary<Type, MessageRecived> _actions = new Dictionary<Type, MessageRecived>();
        private MessageRecived _rootAction;

        protected BetterRoomBase()
        {
            Buttons = new NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>>();
            var routes = new List<Tuple<int, ActionBase<T>>>();
            var indexes = new HashSet<int>();
            var self = typeof(T);
            foreach (var type in self.GetNestedTypes())
            {
                var action = type.GetCustomAttribute<ActionAttribute>();
                if (action == null)
                {
                    continue;
                }

                if (!typeof(ActionBase<T>).IsAssignableFrom(type))
                {
                    throw new Exception("Action must inherit from ActionBase");
                }

                var ctor = type.GetConstructor(new[] {typeof(T)});
                if (ctor == null)
                {
                    throw new Exception("Action must have constructor with single BetterRoomBase argument");
                }

                var instance = (ActionBase<T>) ctor.Invoke(new object[] {this});

                MessageRecived handler = null;
                if (action.Index != null)
                {
                    var index = (int) action.Index;
                    if (indexes.Contains(index))
                    {
                        throw new Exception($"Muliply definition of action with index {action.Index}");
                    }

                    routes.Add(new Tuple<int, ActionBase<T>>(index, instance));
                    handler = instance.OnMessage;
                }
                else
                {
                    if (_rootAction != null)
                    {
                        throw new Exception("Muliply definition of default action");
                    }

                    _rootAction = instance.OnMessage;
                }

                _actions[type] = handler;
                Buttons[handler] = instance.Buttons;
            }

            Routes = routes.OrderBy(r => r.Item1).Select(r => (MessageRecived) r.Item2.OnMessage).ToArray();
        }

        public void SwitchAction(User.User user, Type action)
        {
            SwitchAction(user, _actions[action]);
        }

        public void SwitchAction<TAction>(User.User user) where TAction : ActionBase<T>
        {
            SwitchAction(user, _actions[typeof(TAction)]);
        }

        public override void OnMessage(User.User user, RecivedMessage message)
        {
            if (!HandleAction(user, message))
            {
                // Null action
                _rootAction(user, message);
            }
        }
    }
}