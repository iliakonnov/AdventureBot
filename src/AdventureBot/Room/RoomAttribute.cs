using AdventureBot.ObjectManager;

namespace AdventureBot.Room;

public class RoomAttribute : IdentifiableAttribute
{
    public RoomAttribute(string identifier) : base(identifier)
    {
    }
}

public class AvailableAttribute : RoomAttribute
{
    public AvailableAttribute(string identifier, Difficulity difficulity, string rootId) : base(identifier)
    {
        Difficulity = difficulity;
        RootId = rootId;
    }

    public Difficulity Difficulity { get; }
    public string RootId { get; }
}