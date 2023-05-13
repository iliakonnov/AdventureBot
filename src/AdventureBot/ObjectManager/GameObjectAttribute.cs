using System;

namespace AdventureBot.ObjectManager;

public class GameObjectAttribute : Attribute
{
    internal Type Type = null;
}

public class IdentifiableAttribute : GameObjectAttribute
{
    public IdentifiableAttribute(string identifier)
    {
        Identifier = identifier;
    }

    public string Identifier { get; }
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