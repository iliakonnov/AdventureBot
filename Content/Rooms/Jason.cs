using System;
using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("monster/jason", Difficulity.Hard)]
    public class Jason : MonsterBase
    {
        public override string Name => "Джейсон Вурхиз";
        public override string Identifier => "moster/jason";

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
            user.ItemManager.Add(new ItemInfo("jason/mask", 1));
        }
    }
}