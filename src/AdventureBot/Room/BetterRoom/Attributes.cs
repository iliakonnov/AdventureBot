using System;

namespace AdventureBot.Room.BetterRoom;

[AttributeUsage(AttributeTargets.Class)]
public class ActionAttribute : Attribute
{
    public ActionAttribute(int index)
    {
        Index = index;
    }

    public ActionAttribute()
    {
        Index = null;
    }

    public int? Index { get; }
}

[AttributeUsage(AttributeTargets.Method)]
public class MessageHandlerAttribute : Attribute
{
}

public class ButtonAttribute : MessageHandlerAttribute
{
    public ButtonAttribute(string text)
    {
        Text = text;
    }

    public string Text { get; }
}

public class FallbackAttribute : MessageHandlerAttribute
{
}