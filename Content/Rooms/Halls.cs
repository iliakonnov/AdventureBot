using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;
using Content.Halls;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Upper, TownRoot.Id)]
    public class Halls : BetterRoomBase<Halls>
    {
        public const string Id = "room/halls";

        public override string Name => "Чертоги";
        public override string Identifier => Id;

        public override void OnEnter(User user)
        {
            SwitchAction<MainAction>(user);
            SendMessage(user,
                "Переступив через портал, ты почувствовал дыхание горячего пустынного ветра. Вокруг высохшие деревья, словно сожженные вечным пеклом, красная потрескавшаяся земля, густой туман из пепла...");
            SendMessage(user,
                "Инстинкты взывают к тебе, молят бежать, бежать как можно дальше. Землю словно выбило из-под ног, ты упал у ног скелета, держащего табличку \"Добро пожаловать в Чертоги!\"",
                GetButtons(user));
        }

        [Action]
        public class MainAction : ActionBase<Halls>
        {
            public MainAction(Halls room) : base(room)
            {
            }

            [Button("Идти дальше")]
            public void Go(User user, RecivedMessage message)
            {
                user.RoomManager.ChangeRoot(HallsRoot.Id);
            }

            [Button("Вернуться назад")]
            public void Back(User user, RecivedMessage message)
            {
                user.RoomManager.Leave();
            }
        }
    }
}