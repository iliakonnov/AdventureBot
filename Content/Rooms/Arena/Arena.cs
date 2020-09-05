using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;

namespace Content.Rooms.Arena
{
    [Available(Id, Difficulity.Any, TownRoot.Id)]
    public class Arena : BetterRoomBase<Arena>
    {
        public const string Id = "room/arena";
        public override string Name => "Арена";
        public override string Identifier => Id;

        public override void OnEnter(User user)
        {
            SwitchAction<MainAction>(user);
            SendMessage(user,
                "Ты зашёл в помещение для подготовки к бою. Тебя встречает угрюмый орк, повидавший немало войн на своем веку: шрамы на лице и замена левого запястья на набалдашник от булавы отлично подчёркивают боевой опыт этой машины для убийства.");
            SendMessage(user,
                "– Людишка драться – людишка получать награда. Людишка не драться – Могул кидать людишка на улица",
                GetButtons(user));
            base.OnEnter(user);
        }

        [Action]
        public class MainAction : ActionBase<Arena>
        {
            public MainAction(Arena room) : base(room)
            {
            }

            [Button("Записаться")]
            public void Register(User user, ReceivedMessage message)
            {
                if (user.ItemManager.Get(Medallion.Id) != null)
                {
                    Room.SendMessage(user, "Да вы же и так уже записаны!");
                }
                else
                {
                    user.ItemManager.Add(new ItemInfo(Medallion.Id, 1));
                    Room.SendMessage(user, "Вам выдали медальон гладиатора. Когда появится соперник, вас вызовут сюда");
                }

                user.RoomManager.Leave();
            }

            [Button("Я не хочу драться")]
            public void Leave(User user, ReceivedMessage message)
            {
                Room.SendMessage(user, "Вас выкинули на улицу");
                user.RoomManager.Leave();
            }
        }
    }
}