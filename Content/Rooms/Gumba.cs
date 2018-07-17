using System;
using System.Linq;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("monster/gumba", Difficulity.Easy)]
    public class Gumba : MonsterBase
    {
        public override string Name => "Гумба";
        public override string Identifier => "monster/gumba";
        public override decimal Health => 15;

        public override decimal GetDamage(User user)
        {
            return 3;
        }

        public override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "Какой миленький злобный грибочек!", GetActions(user));
        }

        protected override string[][] GetActions(User user)
        {
            return base.GetActions(user)
                .Concat(new[] {new[] {"Прыгнуть на голову"}})
                .ToArray();
        }

        public override void OnMessage(User user, RecivedMessage message)
        {
            if (message.Text == "Прыгнуть на голову")
            {
                SendMessage(user,
                    "Ты возомнил себя рэстлером и с криком \"Watcha Watcha Watcha Watcha RKO!\" упал на гриб. Его сплющило так, что сок его внутренностей забрызгал все в радиусе двух метров. Мда, ты просто редкостный садист.",
                    GetActions(user));
                MakeDamage(user, Health);
                FinishTurn(user);
            }
            else
            {
                base.OnMessage(user, message);
            }
        }

        public override bool OnRunaway(User user)
        {
            return true;
        }

        public override void OnWon(User user)
        {
            user.Info.Gold += 3;
        }
    }
}