using AdventureBot.Room;

namespace Content.Town
{
    [Root(Id)]
    public class TownRoot : IRoot
    {
        public const string Id = "root/town";
        public string Identifier => Id;
        public string RootRoomId => Town.Id;
    }
}