﻿using System;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;
using Content.Quests;

namespace Content.Town
{
    [Room("town/tavern")]
    public class Tavern : BetterRoomBase
    {
        public Tavern() : base(typeof(Tavern))
        {
        }

        public override string Name => "Таверна";
        public override string Identifier => "town/tavern";

        public override void OnEnter(User user)
        {
            SwitchAction<MainAction>(user);
            SendMessage(user,
                "Дубовая нескладная дверь таверны отворилась перед тобой. Зайдя внутрь, ты понимаешь, что ничего не изменилось: горы мусора и битой посуды, невозмутимый хозяин, вопли пьянчуг и незнакомец в темном углу. Можешь пропустить стаканчик с каким-нибудь старым знакомым или же взяться за дело. Что выберешь?",
                GetButtons(user));
        }

        [Action]
        public class MainAction : ActionBase
        {
            public MainAction(BetterRoomBase room) : base(room)
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

            [Button("Уйти")]
            public void Leave(User user, RecivedMessage message)
            {
                user.RoomManager.Leave();
            }
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

        [Action(0)]
        public class Owner : ActionBase
        {
            public Owner(BetterRoomBase room) : base(room)
            {
            }

            [Button("Заказное дело")]
            public void Business(User user, RecivedMessage message)
            {
                Room.SwitchAction<MainAction>(user);

                var vars = Room.GetRoomVariables(user);
                var requestedTime = DateTimeOffset.FromUnixTimeSeconds(vars.Get<Serializable.Long>("time"));
                var requestsCount = (int) vars.Get<Serializable.Int>("count");

                if (requestsCount > 3)
                {
                    if (DateTimeOffset.Now - requestedTime > new TimeSpan(6, 0, 0))
                    {
                        vars.Set("time", new Serializable.Long(DateTimeOffset.Now.ToUnixTimeSeconds()));
                        requestsCount = 0;
                    }
                    else
                    {
                        Room.SendMessage(user,
                            "– Похоже, ты разделался со всеми. Ничего, за 6 часов ещё какой-нибудь уродец найдется.",
                            Room.GetButtons(user));
                        return;
                    }
                }

                var foundQuest = (Room as Tavern)?.TryFindQuest(user, KillMonster.Id, "_owner");
                if (foundQuest != null)
                {
                    if (foundQuest.Item2.IsFinished(user, foundQuest.Item1))
                    {
                        vars.Remove("questId_owner");
                        user.QuestManager.FinishQuest(KillMonster.Id, foundQuest.Item1);
                        Room.SendMessage(user,
                            "– Мда-а-а, круто ты его. Вот твоя награда. Если захочешь ещё - знай, что лучшие заказы только у меня.",
                            Room.GetButtons(user));
                        return;
                    }

                    Room.SendMessage(user,
                        "Приходи за наградой когда выполнишь задание",
                        Room.GetButtons(user));
                    return;
                }

                vars.Set("count", new Serializable.Int(requestsCount + 1));
                var questId = user.QuestManager.BeginQuest(KillMonster.Id);
                var quest = user.QuestManager.Quests[KillMonster.Id][questId].Quest as KillMonster;
                vars.Set("questId_owner", new Serializable.String(questId.ToString()));

                var monsterId = quest?.GetMonsterId(user, questId);
                var monster = GetAllRooms().Get(monsterId);

                Room.SendMessage(user,
                    $"– Сейчас за голову {monster?.Name} назначена особая награда ценой в {quest?.GetReward(user, questId).Format()} золота. Как только разберёшься, приходи ко мне.",
                    Room.GetButtons(user));
            }

            [Button("Слухи")]
            public void Gossip(User user, RecivedMessage message)
            {
                Room.SendMessage(user,
                    "– Знаешь, сплетни - это не мое, но зеваки шепчут, что самая достоверная информация о делах в городе есть в [@AdventureTavern](https://t.me/AdventureTavern)",
                    Room.GetButtons(user));
            }
        }

        [Action(1)]
        public class Sergeant : ActionBase
        {
            public Sergeant(BetterRoomBase room) : base(room)
            {
            }

            [Button("Да")]
            public void Yes(User user, RecivedMessage message)
            {
                Room.SwitchAction<MainAction>(user);
                
                var vars = Room.GetRoomVariables(user);

                var questId = user.QuestManager.BeginQuest(KillMonsterFree.Id);
                var quest = user.QuestManager.Quests[KillMonsterFree.Id][questId].Quest as KillMonsterFree;
                vars.Set("questId_sergeant", new Serializable.String(questId.ToString()));

                var monsterId = quest?.GetMonsterId(user, questId);
                var monster = GetAllRooms().Get(monsterId);

                Room.SendMessage(user, $"– Пойди и убей {monster?.Name}", Room.GetButtons(user));
            }

            [Button("Я пришел за наградой")]
            public void Reward(User user, RecivedMessage message)
            {
                Room.SwitchAction<MainAction>(user);
                
                var existingQuest = (Room as Tavern)?.TryFindQuest(user, KillMonsterFree.Id, "_sergeant");
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
    }
}