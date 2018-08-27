﻿using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;
using Content.Items;
using Content.Quests;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Hard, TownRoot.Id)]
    public class Sans : MonsterBase, IQuestMonster
    {
        public const string Id = "monster/sans";
        protected override decimal Health => 35;
        public override string Name => "Санс";
        public override string Identifier => Id;

        public override void MakeDamage(User user, decimal damage)
        {
            var variables = GetRoomVariables(user);
            var count = (int) variables.Get<Serializable.Int>("count");
            variables.Set("count", new Serializable.Int(count + 1));

            if (count < 1)
            {
                SendMessage(user, "– Ты действительно думал, что я просто буду стоять на месте?");
            }
            else if (count < 15)
            {
                SendMessage(user,
                    user.Random.Next(0, 2) == 0
                        ? "– Упс, промахнулся!"
                        : "– Ух, чуть не попал!");
                variables.Set("count", new Serializable.Int(count + 1));
            }
            else
            {
                base.MakeDamage(user, 9_999_999);
            }
        }

        protected override decimal GetDamage(User user)
        {
            return 70;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            var variables = GetRoomVariables(user);
            variables.Set("count", new Serializable.Int(0));

            if (user.Info.CurrentStats.GetStat(StatsProperty.Karma) >= 15)
            {
                SendMessage(user, "И тебе повезло, что его друзья не жаловались на тебя. Иди с миром.", buttons);
                user.RoomManager.Leave();
            }
            else
            {
                SendMessage(user,
                    "– Какой прекрасный день! Травка зеленеет, птички щебечут. В такой день дети вроде тебя должны... <b>ГОРЕТЬ В АДУ</b>",
                    buttons);
            }
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }

        protected override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo(Ketchup.Id, 1));
        }
    }
}