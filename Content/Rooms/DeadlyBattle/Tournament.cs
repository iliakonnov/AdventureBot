using System.Collections.Generic;
using System.Linq;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Rooms.DeadlyBattle
{
    [Available(Id, Difficulity.Medium, TownRoot.Id)]
    public class Tournament : BetterRoomBase<Tournament>
    {
        public const string Id = "room/deadly_battle";
        public override string Name => "Турнир \"Смертельная битва\"";
        public override string Identifier => Id;

        public override void OnEnter(User user)
        {
            SwitchAction(user, typeof(Main));

            var monsters = new List<ISerializable>
            {
                new Serializable.String(KungLao.Id),
                new Serializable.String(SubZero.Id),
                new Serializable.String(Scorpio.Id),
                new Serializable.String(LiuKang.Id),
                new Serializable.String(JohnnyCage.Id),
                new Serializable.String(Jax.Id)
            };

            monsters.Shuffle(user.Random);
            monsters.Add(new Serializable.String(ShaoKahn.Id));

            GetRoomVariables(user).Set("monsters", new SerializableList(monsters));
            SendMessage(user, "Не хочешь поучаствовать?", GetButtons(user));
        }

        public override void OnReturn(User user)
        {
            if (GetRoomVariables(user).Get<Serializable.Bool>("mirror") == true)
            {
                GetRoomVariables(user).Remove("mirror");
                SendMessage(user, "Хватит смотрется в зеркало!", GetButtons(user));
                return;
            }

            var monstersList = GetRoomVariables(user).Get<SerializableList>("monsters");
            if (monstersList == null || monstersList.Count == 1)
            {
                SendMessage(user, "Поздравляю, ты всех победил на этой арене. Приходи ещё, когда они оклемаются.",
                    GetButtons(user));
                user.RoomManager.Leave();
                return;
            }

            monstersList.RemoveAt(0);
            string nextMonster = (Serializable.String) monstersList.First();
            var name = GetAllRooms().Get(nextMonster)?.Name;
            SwitchAction(user, typeof(Rest));
            SendMessage(user,
                $"— Ты победил, теперь можешь передохнуть, завтра тебе предстоит сражаться с {name}", GetButtons(user));
        }

        public void BeginBattle(User user)
        {
            var monstersList = GetRoomVariables(user).Get<SerializableList>("monsters");
            if (monstersList == null)
            {
                user.RoomManager.Leave();
                return;
            }

            user.Info.ChangeStats(StatsProperty.Health, user.Info.MaxStats.GetStat(StatsProperty.Health));
            user.Info.ChangeStats(StatsProperty.Stamina, user.Info.MaxStats.GetStat(StatsProperty.Stamina));
            user.Info.ChangeStats(StatsProperty.Mana, user.Info.MaxStats.GetStat(StatsProperty.Mana));

            string monster = (Serializable.String) monstersList.First();
            SendMessage(user, "Приготовься к битве!");
            user.RoomManager.Go(monster);
        }

        [Action]
        public class Main : ActionBase<Tournament>
        {
            public Main(Tournament room) : base(room)
            {
            }

            [Button("Да")]
            public void Yes(User user, ReceivedMessage message)
            {
                Room.BeginBattle(user);
            }

            [Button("Нет")]
            public void No(User user, ReceivedMessage message)
            {
                Room.SwitchAction(user, typeof(ConfirmExit));
                Room.SendMessage(user, "— Ты уверен? Противники будут сильны, но и награда велика!",
                    Room.GetButtons(user));
            }
        }

        [Action(0)]
        public class ConfirmExit : ActionBase<Tournament>
        {
            public ConfirmExit(Tournament room) : base(room)
            {
            }

            [Button("Давай-ка попробуем")]
            public void Yes(User user, ReceivedMessage message)
            {
                Room.BeginBattle(user);
            }

            [Button("Точно нет")]
            public void No(User user, ReceivedMessage message)
            {
                user.RoomManager.Leave();
            }
        }

        [Action(1)]
        public class Rest : ActionBase<Tournament>
        {
            public Rest(Tournament room) : base(room)
            {
            }

            [Button("Идти сражаться")]
            public void Continue(User user, ReceivedMessage message)
            {
                Room.BeginBattle(user);
            }

            [Button("Уйти отсюда")]
            public void Leave(User user, ReceivedMessage message)
            {
                Room.SendMessage(user,
                    "— Слабак! Проваливай! — после этих слов Шань Тсунг приказал страже выгнать тебя с арены.");
                user.RoomManager.Leave();
            }

            [Button("Посмотреться в зеркало")]
            public void Mirror(User user, ReceivedMessage message)
            {
                Room.GetRoomVariables(user).Set("mirror", new Serializable.Bool(true));
                user.RoomManager.Go(Town.Mirror.Id);
            }
        }
    }
}