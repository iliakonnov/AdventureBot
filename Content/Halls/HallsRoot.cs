using AdventureBot.Room;

namespace Content.Halls
{
    [Root(Id)]
    public class HallsRoot : IRoot
    {
        public const string Id = "root/halls";
        public string Identifier => Id;
        public string RootRoomId => Halls.Id;
    }
}