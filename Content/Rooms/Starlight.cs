using System;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Rooms
{
    [Available("monster/starlight", Difficulity.Hard)]
    public class Starlight : MonsterBase
    {
        public override string Name => "Старлайт";
        public override string Identifier => "monster/starlight";
        protected override decimal Health => 1000;
        protected override decimal GetDamage(User user)
        {
            return 50;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            var variables = GetRoomVariables(user);
            var rnd = user.Random.Next(0, 3);
            string propText;
            StatsProperty prop;
            switch (rnd)
            {
                case 0:
                    propText = "силы";
                    prop = StatsProperty.Defence;
                    user.MessageManager.ShownStats |= ShownStats.Strength;
                    break;
                case 1:
                    propText = "интеллекта";
                    prop = StatsProperty.Intelligence;
                    user.MessageManager.ShownStats |= ShownStats.Intelligence;
                    break;
                case 2:
                    propText = "защиты";
                    prop = StatsProperty.Defence;
                    user.MessageManager.ShownStats |= ShownStats.Defence;
                    break;
                default:
                    throw new ArgumentOutOfRangeException(nameof(rnd));
            }

            var backup = user.Info.BaseStats.GetStat(prop);
            variables.Set("prop", new Serializable.Int((int) prop));
            variables.Set("value", new Serializable.Decimal(backup));
            user.Info.ChangeStats(prop, Stats.DefaultStats[prop], true);
            
            SendMessage(user, $"Старлайт Гриммер лишает вас {propText}!", buttons);
        }

        protected override bool OnRunaway(User user)
        {
            SendMessage(user, "Вы убегаете, но вот восполнить потери времени нет");
            return true;
        }

        protected override void OnWon(User user)
        {
            var variables = GetRoomVariables(user);
            var prop = (StatsProperty) (int) variables.Get<Serializable.Int>("prop");
            var backup = (decimal) variables.Get<Serializable.Decimal>("value");
            user.Info.ChangeStats(prop, backup, true);
            user.ItemManager.Add(new ItemInfo("starlight/wand", 1));
        }
    }
}