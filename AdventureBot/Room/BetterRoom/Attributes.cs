using System;

namespace AdventureBot.Room.BetterRoom
{
    [AttributeUsage(AttributeTargets.Class)]
    public class ActionAttribute : Attribute
    {
        public int? Index { get; }

        public ActionAttribute(int index)
        {
            Index = index;
        }
        
        public ActionAttribute()
        {
            Index = null;
        }
    }

    [AttributeUsage(AttributeTargets.Method)]
    public class MessageHandlerAttribute : Attribute
    {
    }

    public class ButtonAttribute : MessageHandlerAttribute
    {
        public string Text { get; }
        
        public ButtonAttribute(string text)
        {
            Text = text;
        }
    }
    
    public class FallbackAttribute : MessageHandlerAttribute
    {   
    }
}