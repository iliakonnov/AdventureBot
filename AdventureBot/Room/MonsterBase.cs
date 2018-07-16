using System;
using System.Linq;
using AdventureBot.Messenger;
using AdventureBot.User.Stats;

namespace AdventureBot.Room
{
    public interface IMonster : IRoom
    {
        void MakeDamage(User.User user, decimal damage);
    }

    public abstract class MonsterBase : RoomBase, IMonster
    {
        public abstract decimal Health { get; }

        public abstract decimal GetDamage(User.User user);
        public abstract void Enter(User.User user, string[][] buttons);
        public abstract bool OnRunaway(User.User user);

        public void MakeDamage(User.User user, decimal damage)
        {
            var variables = GetRoomVariables(user);
            var hp = (decimal) (Serializable.Decimal) GetRoomVariables(user).Get("hp");
            variables.Set("old_hp", new Serializable.Decimal(hp));
            variables.Set("hp", new Serializable.Decimal(hp - damage));
        }

        public override void OnEnter(User.User user)
        {
            var variables = GetRoomVariables(user);
            variables.Set("old_hp", new Serializable.Decimal(Health));
            variables.Set("hp", new Serializable.Decimal(Health));
            
            var buttons = GetItems(user).Select(item => new[] {item}).ToArray();
            Enter(user, buttons);
        }

        public override bool OnLeave(User.User user)
        {
            var won = (decimal) (Serializable.Decimal) GetRoomVariables(user).Get("hp") <= 0;
            if (!won)
            {
                if (OnRunaway(user))
                {
                    SendMessage(user, "Вы убежали от монстра.");
                    return true;
                }

                SendMessage(user, "Вы попытались убежать, но монстр вам не отпускает.");
                return false;
            }

            SendMessage(user, "Вы победили монстра!");
            return true;
        }

        public override void OnMessage(User.User user, RecivedMessage message)
        {
            var buttons = GetItems(user).Select(item => new[] {item}).ToArray();
            if (!UseItem(user, message))
            {
                SendMessage(
                    user,
                    "Вы поискали в карманах необходимый предмет, но ничего не нашли",
                    buttons,
                    "unknown_item"
                );
            }
            else
            {
                var variables = GetRoomVariables(user);
                var hp = (decimal) (Serializable.Decimal) variables.Get("hp");
                
                var diff = hp - (decimal) (Serializable.Decimal) variables.Get("old_hp");
                SendMessage(
                    user,
                    $"HP: {hp} _{diff:(+#);(-#);}_"
                );
                
                if (hp <= 0)
                {
                    user.RoomManager.Leave();
                    return;
                }
                
                var dmg = GetDamage(user);
                SendMessage(
                    user,
                    $"Монстр бьет вас и вам становится нехоршо. Аж на {dmg} единиц здоровья хуже.",
                    buttons
                );
                user.Info.ChangeStats(StatsProperty.Health, -dmg);
            }
        }
    }
}