using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms.MegaMonster.Room
{
    [Available(Id, Difficulity.Medium)]
    public partial class MegaMonsterRoom : RoomBase, IMonster
    {
        public const string Id = "room/mega_monster";

        public MegaMonsterRoom()
        {
            Routes = new MessageRecived[]
            {
                Battle, Talk,
                GiveArtifact, ArtifactNotFound,
                GiveGold, NotEnoughGold,
                GiveKnowledge, NotEnoughKnowledge,
                SelectTarget
            };
            Buttons = new NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>>
            {
                {
                    null, new Dictionary<string, MessageRecived>
                    {
                        {"Сражаться", (user, message) => BeginBattle(user)},
                        {"Договориться", (user, message) => BeginTalk(user)}
                    }
                },
                {
                    SelectTarget, new Dictionary<string, MessageRecived>
                    {
                        {"В голову", (user, message) => BattleTarget(user, Place.Head)},
                        {"В тело", (user, message) => BattleTarget(user, Place.Head)},
                        {"В ноги", (user, message) => BattleTarget(user, Place.Head)}
                    }
                },
                {
                    Talk, new Dictionary<string, MessageRecived>
                    {
                        {"Артефакт", (user, message) => Artifact(user)},
                        {"Золото", (user, message) => Gold(user)},
                        {"Знания", (user, message) => Knowledge(user)},
                        {"Тут не о чем говорить. Битва!", (user, message) => BeginBattle(user)}
                    }
                },
                {
                    GiveArtifact, new Dictionary<string, MessageRecived>
                    {
                        {"Отдать", (user, message) => ConfirmGiveArtifact(user)},
                        {"Он мне самому нужен", (user, message) => BeginTalk(user)}
                    }
                },
                {
                    ArtifactNotFound, new Dictionary<string, MessageRecived>
                    {
                        {"У меня такого нет", (user, message) => BeginTalk(user)}
                    }
                },
                {
                    GiveGold, new Dictionary<string, MessageRecived>
                    {
                        {"Отдать", (user, message) => ConfirmGiveGold(user)},
                        {"Я не готов к такому", (user, message) => BeginTalk(user)}
                    }
                },
                {
                    NotEnoughGold, new Dictionary<string, MessageRecived>
                    {
                        {"У меня столько нет", (user, message) => BeginTalk(user)}
                    }
                },
                {
                    GiveKnowledge, new Dictionary<string, MessageRecived>
                    {
                        {"Обучить", (user, message) => ConfirmGiveKnowledge(user)},
                        {"Монстр недостоин знаний!", (user, message) => BeginTalk(user)}
                    }
                },
                {
                    NotEnoughKnowledge, new Dictionary<string, MessageRecived>
                    {
                        {"Я недостаточно умен", (user, message) => BeginTalk(user)}
                    }
                }
            };
        }

        public override string Name => "Монстр";
        public override string Identifier => Id;

        public override void OnEnter(User user)
        {
            base.OnEnter(user);
            GetRoomVariables(user).Remove("monster_stats");
            SwitchAction(user, null);
            using (var stats = new StatsContext(user.Random, GetRoomVariables(user)))
            {
                SendMessage(user, $"Ты встречаешь {stats.Stats.Name}!", GetButtons(user));
            }
        }

        public override void OnMessage(User user, RecivedMessage message)
        {
            if (!HandleAction(user, message))
            {
                HandleButtonAlways(user, message);
            }
        }

        private void BeginTalk(User user)
        {
            SwitchAction(user, Talk);
            SendMessage(user, "Что вы предложите монстру?", GetButtons(user));
        }

        private void Talk(User user, RecivedMessage message)
        {
            HandleButtonAlways(user, message);
        }
    }
}