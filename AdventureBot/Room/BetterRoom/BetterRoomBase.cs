using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using AdventureBot.Messenger;

namespace AdventureBot.Room.BetterRoom;

public abstract class BetterRoomBase<T> : RoomBase where T : BetterRoomBase<T>
{
    private readonly Dictionary<Type, ActionBase<T>> _actions = new();
    private readonly ActionBase<T> _rootAction;
    private readonly Type _rootActionType;

    protected BetterRoomBase()
    {
        Buttons = new NullableDictionary<MessageReceived, Dictionary<string, MessageReceived>>();
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
                throw new Exception("Action must have constructor without parameters");
            }

            var instance = (ActionBase<T>) ctor.Invoke(new object[] {this});

            ActionBase<T> handler = null;
            if (action.Index != null)
            {
                var index = (int) action.Index;
                if (indexes.Contains(index))
                {
                    throw new Exception($"Muliply definition of action with index {action.Index}");
                }

                indexes.Add((int) action.Index);
                routes.Add(new Tuple<int, ActionBase<T>>(index, instance));
                handler = instance;
            }
            else
            {
                if (_rootAction != null)
                {
                    throw new Exception("Muliply definition of default action");
                }

                _rootAction = instance;
                _rootActionType = type;
            }

            _actions[type] = handler;
            if (handler != null)
            {
                Buttons[handler.OnMessage] = instance.Buttons;
            }
            else
            {
                Buttons[null] = instance.Buttons;
            }
        }

        if (_rootAction == null)
        {
            throw new Exception("Default action not found");
        }

        Routes = routes
            .OrderBy(r => r.Item1)
            .Select(r => (MessageReceived) r.Item2.OnMessage)
            .ToArray();
    }

    public void SwitchAction(User.User user, Type action)
    {
        if (action == _rootActionType)
        {
            base.SwitchAction(user, null);
        }
        else
        {
            base.SwitchAction(user, GetAction(action).OnMessage);
        }
    }

    public void SwitchAction<TAction>(User.User user) where TAction : ActionBase<T>
    {
        SwitchAction(user, typeof(TAction));
    }

    public TAction GetAction<TAction>() where TAction : ActionBase<T>
    {
        return (TAction) GetAction(typeof(TAction));
    }

    public ActionBase<T> GetAction(Type action)
    {
        return _actions[action] ?? _rootAction;
    }

    public override void OnMessage(User.User user, ReceivedMessage message)
    {
        if (!HandleAction(user, message))
        {
            // Null action
            _rootAction.OnMessage(user, message);
        }
    }
}