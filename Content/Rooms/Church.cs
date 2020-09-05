using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Any, TownRoot.Id)]
    public class Church : BetterRoomBase<Church>
    {
        public const string Id = "room/church";

        public override string Name => "Храм";
        public override string Identifier => Id;

        public override void OnEnter(User user)
        {
            base.OnEnter(user);
            SwitchAction<MainHandler>(user);

            if (user.Info.CurrentStats.GetStat(StatsProperty.Karma) < 0)
            {
                SendMessage(user, "Даже тут не любят таких отщепенцев, как ты.");
                user.RoomManager.Leave();
                return;
            }

            SendMessage(user,
                "Пастафарианский храм! Ты чуть не задохнулся от жары, производимой электроплитками, на которых варилась паста и жарились тефтельки. С потолка свисает огромное количество различных приспособлений для варки макарон: дуршлаги, кастрюли, лопатки, щипцы. А по полу вперемешку разбросаны тарелки с остывающей пастой и мешки со спагетти, макаронами и ригаттой.",
                GetButtons(user));
        }

        [Action]
        public class MainHandler : ActionBase<Church>
        {
            public MainHandler(Church room) : base(room)
            {
            }

            [Button("Пожертвовать")]
            public void OnDonat(User user, ReceivedMessage message)
            {
                Room.SwitchAction<Donat>(user);
                Room.SendMessage(user, "Ты решил пожертвовать Макаронному Монстру немного своих сбережений.",
                    Room.GetButtons(user));
            }

            [Button("Уйти")]
            public void Leave(User user, ReceivedMessage message)
            {
                user.RoomManager.Leave();
            }
        }

        [Action(0)]
        public class Donat : ActionBase<Church>
        {
            public Donat(Church room) : base(room)
            {
            }

            [Button("150")]
            public void DonatMinium(User user, ReceivedMessage message)
            {
                if (user.Info.TryDecreaseGold(150))
                {
                    user.Info.ChangeStats(StatsProperty.Karma, 1);
                    Room.SendMessage(user,
                        "Ты отсыпал пару золотых монет на блюдечко. Почти моментально они испарились с легким синим дымком, и ты почувствовал что совершил ещё одно доброе дело.",
                        Room.GetButtons(user));
                }
                else
                {
                    Room.SendMessage(user,
                        "Ты отсыпал пару золотых монет на блюдечко. Они начали было испаряться, но вдруг затормозили и отскочили обратно. Думаю, у тебя недостаточно золота.",
                        Room.GetButtons(user));
                }
            }

            [Button("750")]
            public void Donat750(User user, ReceivedMessage message)
            {
                if (user.Info.TryDecreaseGold(750))
                {
                    user.Info.ChangeStats(StatsProperty.Karma, 5);
                    user.Info.ChangeStats(StatsProperty.Health, user.Info.MaxStats.GetStat(StatsProperty.Health), true);
                    Room.SendMessage(user,
                        "Ты отсыпал горсть золотых монет на блюдечко. Почти моментально они испарились с легким синим дымком, и ты почувствовал что совершил ещё одно доброе дело.");
                    Room.SendMessage(user,
                        "За такое щедрое пожертвование служители храма накормили тебя вкусной пастой.",
                        Room.GetButtons(user));
                }
                else
                {
                    Room.SendMessage(user,
                        "Ты отсыпал горсть золотых монет на блюдечко. Они начали было испаряться, но вдруг затормозили и отскочили обратно. Думаю, у тебя недостаточно золота.",
                        Room.GetButtons(user));
                }
            }

            [Button("1500")]
            public void DonatMaximum(User user, ReceivedMessage message)
            {
                if (user.Info.TryDecreaseGold(1500))
                {
                    user.Info.ChangeStats(StatsProperty.Karma, 10);
                    user.Info.ChangeStats(StatsProperty.Health, user.Info.MaxStats.GetStat(StatsProperty.Health), true);
                    user.Info.ChangeStats(StatsProperty.Defence, 5);
                    Room.SendMessage(user,
                        "Ты отсыпал горсть золотых монет на блюдечко. Почти моментально они испарились с легким синим дымком, и ты почувствовал что совершил ещё одно доброе дело.");
                    Room.SendMessage(user,
                        "За такое щедрое пожертвование служители храма накормили тебя вкусной пастой и обучили секретам защиты.",
                        Room.GetButtons(user));
                }
                else
                {
                    Room.SendMessage(user,
                        "Ты отсыпал горсть золотых монет на блюдечко. Они начали было испаряться, но вдруг затормозили и отскочили обратно. Думаю, у тебя недостаточно золота.",
                        Room.GetButtons(user));
                }
            }

            [Button("Уйти")]
            public void Leave(User user, ReceivedMessage message)
            {
                user.RoomManager.Leave();
            }
        }
    }
}