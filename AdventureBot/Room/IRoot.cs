using AdventureBot.ObjectManager;

namespace AdventureBot.Room
{
    public class RootAttribute : IdentifiableAttribute
    {
        public RootAttribute(string identifier) : base(identifier)
        {
        }
    }
    
    public class RootManager : StorageManager<IRoot, RootAttribute>
    {
    }
    
    public interface IRoot
    {
        string Identifier { get; }
        string RootRoomId { get; }
    }
}