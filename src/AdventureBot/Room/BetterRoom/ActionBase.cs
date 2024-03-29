﻿using System;
using System.Collections.Generic;
using System.Reflection;
using AdventureBot.Messenger;

namespace AdventureBot.Room.BetterRoom;

public abstract class ActionBase
{
    private readonly MessageReceived _fallback;
    public readonly Dictionary<string, MessageReceived> Buttons;
    protected internal readonly BetterRoomBase Room;

    protected ActionBase(BetterRoomBase room)
    {
        Room = room;
        var self = GetType();

        Buttons = new Dictionary<string, MessageReceived>();
        _fallback = null;

        foreach (var method in self.GetMethods())
        {
            var attr = method.GetCustomAttribute<MessageHandlerAttribute>();
            if (attr == null)
            {
                continue;
            }

            var handler = (MessageReceived)Delegate.CreateDelegate(typeof(MessageReceived), this, method, false);

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

    public void OnMessage(User.User user, ReceivedMessage message)
    {
        if (!Room.HandleButton(user, message))
        {
            _fallback(user, message);
        }
    }
}

public abstract class ActionBase<T> : ActionBase where T : BetterRoomBase
{
    protected ActionBase(T room) : base(room)
    {
    }

    protected new T Room => (T)((ActionBase)this).Room;
}