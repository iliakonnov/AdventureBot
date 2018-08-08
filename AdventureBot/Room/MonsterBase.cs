using System.Linq;
using AdventureBot.Messenger;

namespace AdventureBot.Room
{
    public interface IMonster : IRoom
    {
        void MakeDamage(User.User user, decimal damage);
    }

    public abstract class MonsterBase : RoomBase, IMonster
    {
        protected abstract decimal Health { get; }

        public void MakeDamage(User.User user, decimal damage)
        {
            var variables = GetRoomVariables(user);
            var hp = (decimal) (Serializable.Decimal) GetRoomVariables(user).Get("hp");
            variables.Set("hp", new Serializable.Decimal(hp - damage));
        }

        public override void OnEnter(User.User user)
        {
            base.OnEnter(user);

            var variables = GetRoomVariables(user);
            variables.Set("old_hp", new Serializable.Decimal(Health));
            variables.Set("hp", new Serializable.Decimal(Health));

            var buttons = GetActions(user);
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
                    return base.OnLeave(user);
                }

                SendMessage(user, "Вы попытались убежать, но монстр вам не отпускает.");
                return false;
            }

            OnWon(user);
            SendMessage(user, "Вы победили монстра!");
            return base.OnLeave(user);
        }

        public override void OnMessage(User.User user, RecivedMessage message)
        {
            if (!UseItem(user, message))
            {
                SendMessage(
                    user,
                    "Вы поискали в карманах необходимый предмет, но ничего не нашли",
                    GetActions(user),
                    "unknown_item"
                );
            }
            else
            {
                FinishTurn(user);
            }
        }

        protected void FinishTurn(User.User user)
        {
            var variables = GetRoomVariables(user);
            var hp = (decimal) (Serializable.Decimal) variables.Get("hp");

            var diff = hp - (decimal) (Serializable.Decimal) variables.Get("old_hp");
            SendMessage(
                user,
                $"HP: {hp} _{diff:(+#);(-#);(0)}_"
            );

            variables.Set("old_hp", new Serializable.Decimal(hp));

            if (hp <= 0)
            {
                user.RoomManager.Leave();
                return;
            }

            var dmg = GetDamage(user);
            SendMessage(
                user,
                $"Монстр бьет вас и вам становится нехоршо. Аж на {dmg} единиц здоровья хуже.",
                GetActions(user)
            );
            user.Info.MakeDamage(dmg);
        }

        protected virtual string[][] GetActions(User.User user)
        {
            return GetItems(user).Select(item => new[] {item}).ToArray();
        }

        protected abstract decimal GetDamage(User.User user);
        protected abstract void Enter(User.User user, string[][] buttons);
        protected abstract bool OnRunaway(User.User user);
        protected abstract void OnWon(User.User user);
    }
}