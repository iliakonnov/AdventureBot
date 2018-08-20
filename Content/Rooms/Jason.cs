using System;
using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;
using Content.Items;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Hard, TownRoot.Id)]
    public class Jason : MonsterBase
    {
        public const string Id = "monster/jason";
        public override string Name => "Джейсон Вурхиз";
        public override string Identifier => Id;

        protected override decimal Health
        {
            get
            {
                if (IsFriday())
                {
                    return 1500 * 2;
                }

                return 1500;
            }
        }

        private static bool IsFriday()
        {
            var today = DateTime.Now.Date;
            return today.DayOfWeek == DayOfWeek.Friday && today.Day == 13;
        }

        protected override decimal GetDamage(User user)
        {
            if (IsFriday())
            {
                return 45 * 2;
            }

            return 45;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(
                user,
                IsFriday()
                    ? "Сегодня его день, и он будет убивать!"
                    : "Сегодня не его день, и он очень зол!",
                buttons
            );
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }

        protected override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo(HockeyMask.Id, 1));
        }
    }
}