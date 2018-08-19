using System;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;
using AdventureBot.User.Stats;
using Content.Items;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Any)]
    public class Portal : BetterRoomBase
    {
        public const string Id = "room/portal";

        public Portal() : base(typeof(Portal))
        {
        }

        public override string Name => "Портал";
        public override string Identifier => Id;

        public override void OnEnter(User user)
        {
            SwitchAction<MainAction>(user);
            SendMessage(user,
                "Бродя по лесу, ты наткнулся на треугольный портал и зелёный голографический шар возле него. Выбрав точку на этом шаре, можно открыть портал в любое место во Вселенной. Куда откроешь портал?",
                GetButtons(user));
            base.OnEnter(user);
        }

        [Action]
        public class MainAction : ActionBase
        {
            public MainAction(BetterRoomBase room) : base(room)
            {
            }

            [Button("Вормир")]
            public void Vormir(User user, RecivedMessage message)
            {
                if (user.Info.CurrentStats.GetStat(StatsProperty.Karma) <= -50)
                {
                    Room.SwitchAction<BadUser>(user);
                }
                else
                {
                    Room.SwitchAction<GoodUser>(user);
                }

                Room.SendMessage(user,
                    "Ты попал на холодную скалистую планету, покрытую бахромой вечного тумана. Из этого тумана выплыло нечто, покрытое с ног до головы темным неземным материалом");
                Room.SendMessage(user,
                    $"– Здравствуй, {user.Info.Name}. Скорее всего, ты пришел за Камнем Души. Но знаешь ли ты цену этой силы?",
                    Room.GetButtons(user));
            }
        }

        [Action(0)]
        public class BadUser : ActionBase
        {
            public BadUser(BetterRoomBase room) : base(room)
            {
            }

            [Button("Да")]
            public void Yes(User user, RecivedMessage message)
            {
                Room.SendMessage(user, "– Я уверен, что знаешь. Я проведу тебя к нему.");
                Room.SendMessage(user,
                    "Через 15 минут ходьбы по ущельям и скалам вы дошли до обрыва. Вглядываясь в плато, что находится под обрывом, ты не заметил, как туман сгустился до состояния болота. Это болото поглощает тебя. Ты пытаешься вырваться, но тщетно. Каждая клетка твоего тела оповещает о близкой гибели и небытия. Ты закрываешь глаза и... оказываешься в том же месте, откуда пришел. У себя в ладони ты обнаруживаешь Камень Души!",
                    Room.GetButtons(user));
                user.ItemManager.Add(new ItemInfo(Soulstone.Id, 1));
                user.RoomManager.Leave();
            }
        }

        [Action(1)]
        public class GoodUser : ActionBase
        {
            public GoodUser(BetterRoomBase room) : base(room)
            {
            }

            [Button("Нет")]
            public void No(User user, RecivedMessage message)
            {
                Room.SendMessage(user, "– Я не могу тратить более времени на тебя.");
                Room.SendMessage(user, "Густой туман окутал тебя. Через секунду ты стоял на главной улице Города",
                    Room.GetButtons(user));
                user.RoomManager.Leave();
            }
        }
    }
}