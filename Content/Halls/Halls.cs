using System.Linq;
using AdventureBot;
using AdventureBot.Room;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;

namespace Content.Halls
{
    [Room(Id)]
    public class Halls : BetterRoomBase<Halls>
    {
        public const string Id = "halls";
        public override string Name => "Чертоги";
        public override string Identifier => Id;

        public override void OnEnter(User user)
        {
            SendMessage(user, "Добро пожаловать в Чертоги! Рады вас видеть!", GetButtons(user));
            Explore(user);
        }

        public override void OnReturn(User user)
        {
            var currentRoom = GetRoomVariables(user).Get<Serializable.Int>("location") ?? 0;
            GetRoomVariables(user).Set("location", new Serializable.Int(currentRoom + 1));
            SendMessage(user, "Рады вас видеть живыми!");
            Explore(user);
        }

        private void Explore(User user)
        {
            var rooms = GetAllRooms().Items()
                .Where(room => room.Attribute is AvailableAttribute attr
                               && attr.RootId == HallsRoot.Id)
                .OrderBy(room => room.Identificator)
                .Select(room => room.Identificator)
                .ToList();
            user.RoomManager.Go(rooms[user.Random.Next(rooms.Count)]);
        }
    }
}