using System.Linq;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;
using Content.Halls.Items;

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
            SendMessage(user, "<b>Добро пожаловать в Чертоги! Рады вас видеть!</b>", GetButtons(user));
            Explore(user);
        }

        public override void OnReturn(User user)
        {
            var currentRoom = GetRoomVariables(user).Get<Serializable.Int>("location") ?? 0;
            GetRoomVariables(user).Set("location", new Serializable.Int(currentRoom + 1));
            SendMessage(user, "<b>Рады вас видеть живыми!</b>");
            Explore(user);
        }

        private void Explore(User user)
        {
            var difficulity = Difficulity.Any;
            if (user.ItemManager.Get(NativeCross.Id) != null)
            {
                difficulity = Difficulity.Lower;
            }

            var rooms = GetAllRooms().Items()
                .Where(room => room.Attribute is AvailableAttribute attr
                               && (attr.Difficulity & difficulity) != 0
                               && attr.RootId == HallsRoot.Id)
                .OrderBy(room => room.Identificator)
                .Select(room => room.Identificator)
                .ToList();
            var selected = rooms[user.Random.Next(rooms.Count)];
            var selectedRoom = GetAllRooms().Get(selected);
            SendMessage(user, $"<b>Дальше вам прямиком к {selectedRoom?.Name}! Будем ждать!</b>");
            user.RoomManager.Go(selected);
        }

        [Action]
        public class MainAction : ActionBase<Halls>
        {
            public MainAction(Halls room) : base(room)
            {
            }

            [Button("Исследовать Чертоги")]
            public void Explore(User user, RecivedMessage message)
            {
                Room.Explore(user);
            }
        }
    }
}