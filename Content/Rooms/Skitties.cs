﻿using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Any, TownRoot.Id)]
    public class Skitties : RoomBase
    {
        public const string Id = "room/skitties";

        public Skitties()
        {
            Buttons = new NullableDictionary<MessageReceived, Dictionary<string, MessageReceived>>
            {
                {
                    null, new Dictionary<string, MessageReceived>
                    {
                        {
                            "Попробовать", (user, message) =>
                            {
                                SendMessage(user,
                                    "Вполне себе обычные вкусненькие конфеты. Правда, ты не заметил, как съел полведра и теперь чувствуешь, как содержание глюкозы в твоей крови достигло критической отметки. Кажется, у тебя диабет. Но есть и плюсы: отойдя на метров двести, ты обнаружил у себя в кармане конфеты \"Skitties\". Да-да, те самые.");
                                user.VariableManager.UserVariables.Set("skitties_diabetes", new Serializable.Int(10));
                                user.ItemManager.Add(new ItemInfo(Items.Skitties.Id, 10));
                                user.RoomManager.Leave();
                            }
                        },
                        {
                            "Нет, спасибо", (user, message) =>
                            {
                                SendMessage(user,
                                    "— Ну ладно дружище, дело твое! — после этих слов он подобрал ведро, сел на жирафа и ускакал на Юго-Запад");
                                user.RoomManager.Leave();
                            }
                        }
                    }
                }
            };
        }

        public override string Name => "?";
        public override string Identifier => Id;

        public override void OnEnter(User user)
        {
            base.OnEnter(user);

            SendMessage(user,
                "Ты увидел афроамериканца, который доил жирафа конфетами, ел их и угарал как укуренный. Ты начал было мысленно перечислять все галюциногенные грибы, которые могли быть подмешаны в зелье, но темнокожий предложил тебе этих самых конфет. Что будем делать?",
                GetButtons(user));
        }


        public override void OnMessage(User user, ReceivedMessage message)
        {
            HandleButtonAlways(user, message);
        }
    }
}