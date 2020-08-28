using System;
using System.Collections.Generic;
using System.Text;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;
using AdventureBot.User.Stats;
using AdventureBot.UserManager;
using Content.Quests;

namespace Content.Town
{
    [Room(Id)]
    public class Tavern : BetterRoomBase<Tavern>
    {
        public const string Id = "town/tavern";

        public override string Name => "Таверна";
        public override string Identifier => Id;

        public override void OnEnter(User user)
        {
            SwitchAction<MainAction>(user);
            SendMessage(user,
                "Дубовая нескладная дверь таверны отворилась перед тобой. Зайдя внутрь, ты понимаешь, что ничего не изменилось: горы мусора и битой посуды, невозмутимый хозяин, вопли пьянчуг и незнакомец в темном углу. Можешь пропустить стаканчик с каким-нибудь старым знакомым или же взяться за дело. Что выберешь?",
                GetButtons(user));
        }

        private Tuple<Guid, KillMonsterBase> TryFindQuest(User user, string questId, string varSuffix)
        {
            var vars = GetRoomVariables(user);
            var existingQuestId = vars.Get<Serializable.String>("questId" + varSuffix);
            if (existingQuestId == null)
            {
                return null;
            }

            var quests = user.QuestManager.Quests[questId];
            var questGuid = Guid.Parse(existingQuestId);
            if (quests.TryGetValue(questGuid, out var questInfo))
            {
                return new Tuple<Guid, KillMonsterBase>(questGuid, questInfo.Quest as KillMonsterBase);
            }

            return null;
        }

        [Action]
        public class MainAction : ActionBase<Tavern>
        {
            public MainAction(Tavern room) : base(room)
            {
            }

            [Button("К хозяину")]
            public void ToOwner(User user, RecivedMessage message)
            {
                Room.SwitchAction<Owner>(user);
                Room.SendMessage(user, "– Ну здравствуй, вечный странник. Зачем пожаловали?", Room.GetButtons(user));
            }

            [Button("К сержанту Дэмэйджу")]
            public void ToSergeant(User user, RecivedMessage message)
            {
                Room.SwitchAction<Sergeant>(user);
                Room.SendMessage(user,
                    "– Эхехе, салага! Сильно же тебя разнесло! Протрястись не хочешь? А то есть пара незаконченных дел.",
                    Room.GetButtons(user));
            }

            [Button("К доске почета")]
            public void ToLeaderboard(User user, RecivedMessage message)
            {
                Room.SwitchAction<Leaderboard>(user);
                Room.SendMessage(user, "Здесь есть все лучшие люди этого города", Room.GetButtons(user));
            }

            [Button("Уйти")]
            public void Leave(User user, RecivedMessage message)
            {
                user.RoomManager.Leave();
            }
        }

        [Action(0)]
        public class Owner : ActionBase<Tavern>
        {
            public Owner(Tavern room) : base(room)
            {
            }

            [Button("Заказное дело")]
            public void Business(User user, RecivedMessage message)
            {
                Room.SwitchAction<MainAction>(user);

                var vars = Room.GetRoomVariables(user);

                var foundQuest = Room.TryFindQuest(user, KillMonster.Id, "_owner");
                if (foundQuest != null)
                {
                    // Quest exists

                    if (foundQuest.Item2.IsFinished(user, foundQuest.Item1))
                    {
                        // Quest exists and finished
                        vars.Remove("questId_owner");
                        user.QuestManager.FinishQuest(KillMonster.Id, foundQuest.Item1);
                        Room.SendMessage(user,
                            "– Мда-а-а, круто ты его. Вот твоя награда. Если захочешь ещё - знай, что лучшие заказы только у меня.",
                            Room.GetButtons(user));
                        return;
                    }

                    // Quest exists but not finished
                    Room.SendMessage(user,
                        "Приходи за наградой когда выполнишь задание",
                        Room.GetButtons(user));
                    return;
                }

                // Quest does not exists

                var requestedTime = DateTimeOffset.FromUnixTimeSeconds(vars.Get<Serializable.Long>("time"));
                var requestsCount = (int) vars.Get<Serializable.Int>("count");

                if (requestsCount > 3)
                {
                    // Quest does not exists and more than 3 tries

                    if (DateTimeOffset.Now - requestedTime > new TimeSpan(6, 0, 0))
                    {
                        // Quest does not exists and more than 3 tries and time exceeded
                        vars.Set("time", new Serializable.Long(DateTimeOffset.Now.ToUnixTimeSeconds()));
                        requestsCount = 0;
                    }
                    else
                    {
                        // Quest does not exists and more than 3 tries in last 6 hours
                        Room.SendMessage(user,
                            "– Похоже, ты разделался со всеми. Ничего, за 6 часов ещё какой-нибудь уродец найдется.",
                            Room.GetButtons(user));
                        return;
                    }
                }

                // Quest does not exists and *less* than 3 tries in last 6 hours
                vars.Set("count", new Serializable.Int(requestsCount + 1));
                var questId = user.QuestManager.BeginQuest(KillMonster.Id);
                var quest = (KillMonster) user.QuestManager.Quests[KillMonster.Id][questId].Quest;
                vars.Set("questId_owner", new Serializable.String(questId.ToString()));

                var monsterId = quest.GetMonsterId(user, questId);
                var monster = GetAllRooms().Get(monsterId);

                Room.SendMessage(user,
                    $"– Сейчас за голову {monster?.Name} назначена особая награда ценой в {quest.GetReward(user, questId).Format()} золота. Как только разберёшься, приходи ко мне.",
                    Room.GetButtons(user));
            }

            [Button("Слухи")]
            public void Gossip(User user, RecivedMessage message)
            {
                Room.SendMessage(user,
                    "– Знаешь, сплетни - это не мое, но зеваки шепчут, что самая достоверная информация о делах в городе есть в <a href=\"https://t.me/AdventureTavern\">@AdventureTavern</a>",
                    Room.GetButtons(user));
            }
            
            [Button("Назад")]
            public void Back(User user, RecivedMessage message)
            {
                Room.SwitchAction<MainAction>(user);
                Room.SendMessage(user, "Хозяин странно на тебя посмотрел", Room.GetButtons(user));
            }
        }

        [Action(1)]
        public class Sergeant : ActionBase<Tavern>
        {
            public Sergeant(Tavern room) : base(room)
            {
            }

            [Button("Да")]
            public void Yes(User user, RecivedMessage message)
            {
                Room.SwitchAction<MainAction>(user);

                var vars = Room.GetRoomVariables(user);

                var existingQuest = Room.TryFindQuest(user, KillMonsterFree.Id, "_sergeant");
                if (existingQuest != null)
                {
                    Room.SendMessage(user,
                        "А не слишком ли много ты на себя берешь? Сначала с текущими делами разберись",
                        Room.GetButtons(user));
                    return;
                }

                var questId = user.QuestManager.BeginQuest(KillMonsterFree.Id);
                var quest = (KillMonsterFree) user.QuestManager.Quests[KillMonsterFree.Id][questId].Quest;
                vars.Set("questId_sergeant", new Serializable.String(questId.ToString()));

                var monsterId = quest.GetMonsterId(user, questId);
                var monster = GetAllRooms().Get(monsterId);

                Room.SendMessage(user, $"– Пойди и убей {monster?.Name}", Room.GetButtons(user));
            }

            [Button("Я пришел за наградой")]
            public void Reward(User user, RecivedMessage message)
            {
                Room.SwitchAction<MainAction>(user);

                var existingQuest = Room.TryFindQuest(user, KillMonsterFree.Id, "_sergeant");
                if (existingQuest != null)
                {
                    if (existingQuest.Item2.IsFinished(user, existingQuest.Item1))
                    {
                        user.QuestManager.FinishQuest(KillMonsterFree.Id, existingQuest.Item1);
                        Room.SendMessage(user,
                            "– Прости, парнишка, денег у меня нет, зато есть боевой и жизненный опыт! Учись, пока я живой!",
                            Room.GetButtons(user));
                        return;
                    }

                    Room.SendMessage(user,
                        "– О награде рано говорить, пока задание не выполнил",
                        Room.GetButtons(user));
                    return;
                }

                Room.SendMessage(user, "– Ты о чем вообще?", Room.GetButtons(user));
            }

            [Button("Нет")]
            public void No(User user, RecivedMessage message)
            {
                Room.SwitchAction<MainAction>(user);
                Room.SendMessage(user,
                    "– Муштровать не буду, не в армии. Но скажу, что ты очень многое упускаешь.",
                    Room.GetButtons(user));
            }
        }

        [Action(2)]
        public class Leaderboard : ActionBase<Tavern>
        {
            public Leaderboard(Tavern room) : base(room)
            {
            }

            private static void DisplayTop(StringBuilder sb, IEnumerable<(UserId, DatabaseVariables)> top,
                Func<User, (UserId, DatabaseVariables), string> formatter)
            {
                var cnt = 0;
                foreach (var topPlayer in top)
                {
                    if (cnt++ > 10)
                    {
                        break;
                    }

                    var usr = UserProxy.GetUnsafe(topPlayer.Item1);
                    sb.AppendLine($"<b>{cnt}</b>. {formatter(usr, topPlayer)}");
                }
            }

            [Button("Самые богатые")]
            public void ByGold(User user, RecivedMessage message)
            {
                var top = new StringBuilder();
                DisplayTop(top, TopPlayers.GetTop(TopParam.Gold, 10),
                    (usr, topPlayer) => $"У {usr.Info.Name} имеется {topPlayer.Item2.Gold.Format()} золота");

                Room.SendMessage(user, top.ToString(), Room.GetButtons(user));
            }

            [Button("Путешественники")]
            public void ByRooms(User user, RecivedMessage message)
            {
                var top = new StringBuilder();
                DisplayTop(top, TopPlayers.GetTop(TopParam.Rooms, 10),
                    (usr, topPlayer) => $"{usr.Info.Name} побывал в {topPlayer.Item2.Rooms} комнатах");

                Room.SendMessage(user, top.ToString(), Room.GetButtons(user));
            }

            [Button("Убийцы монстров")]
            public void ByMonsters(User user, RecivedMessage message)
            {
                var top = new StringBuilder();
                DisplayTop(top, TopPlayers.GetTop(TopParam.Monsters, 10),
                    (usr, topPlayer) => $"{usr.Info.Name} убил {topPlayer.Item2.Monsters} монстров");

                Room.SendMessage(user, top.ToString(), Room.GetButtons(user));
            }

            [Button("Самые опытные")]
            public void ByLevel(User user, RecivedMessage message)
            {
                var top = new StringBuilder();
                DisplayTop(top, TopPlayers.GetTop(TopParam.Level, 10),
                    (usr, topPlayer) =>
                        $"{usr.Info.Name} достиг {topPlayer.Item2.Level} уровня");

                Room.SendMessage(user, top.ToString(), Room.GetButtons(user));
            }

            [Button("Отойти отсюда")]
            public void Away(User user, RecivedMessage message)
            {
                Room.SwitchAction<MainAction>(user);
                Room.SendMessage(user, string.Empty, Room.GetButtons(user));
            }
        }
    }
}