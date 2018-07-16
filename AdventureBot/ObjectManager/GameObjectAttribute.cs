using System;

namespace AdventureBot.ObjectManager
{
    public class GameObjectAttribute : Attribute
    {
    }

    public class IdentifiableAttribute : GameObjectAttribute
    {
        public string Identifier { get; }

        public IdentifiableAttribute(string identifier)
        {
            Identifier = identifier;
        }
    }
    
    public class ItemAttribute : IdentifiableAttribute
    {
        public ItemAttribute(string identifier) : base(identifier)
        {
        }
    }

    public class MessengerAttribute : GameObjectAttribute
    {
    }
}