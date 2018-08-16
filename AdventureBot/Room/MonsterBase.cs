using System.Linq;
using AdventureBot.Messenger;
using AdventureBot.User;

namespace AdventureBot.Room
{
    public interface IMonster : IRoom
    {
        void MakeDamage(User.User user, decimal damage);
        decimal GetCurrentHealth(User.User user);
    }

    public abstract class MonsterBase : RoomBase, IMonster
    {
        protected abstract decimal Health { get; }
        public static event GameEventHandler<IMonster> OnKilled;

        public virtual void MakeDamage(User.User user, decimal damage)
        {
            var variables = GetRoomVariables(user);
            var hp = (decimal) (Serializable.Decimal) variables.Get("hp");
            variables.Set("hp", new Serializable.Decimal(hp - damage));
        }

        public decimal GetCurrentHealth(User.User user)
        {
            var hp = (decimal) (Serializable.Decimal) GetRoomVariables(user).Get("hp");
            return hp;
        }

        public override void OnEnter(User.User user)
        {
            base.OnEnter(user);

            var variables = GetRoomVariables(user);
            var hp = Health - user.Info.KarmaEffect(Health);
            variables.Set("old_hp", new Serializable.Decimal(hp));
            variables.Set("hp", new Serializable.Decimal(hp));
            variables.Set("run", new Serializable.Bool(false));

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
                    GetRoomVariables(user).Set("run", new Serializable.Bool(true));
                    return base.OnLeave(user);
                }

                SendMessage(user, "Вы попытались убежать, но монстр вас не отпускает.");
                return false;
            }

            OnWon(user);
            SendMessage(user, "Вы победили монстра!");
            return base.OnLeave(user);
        }

        protected virtual void NotHandled(User.User user, RecivedMessage message)
        {
            SendMessage(
                user,
                "Вы поискали в карманах необходимый предмет, но ничего не нашли",
                GetActions(user),
                "unknown_item"
            );
        }

        public override void OnMessage(User.User user, RecivedMessage message)
        {
            if (!UseItem(user, message))
            {
                NotHandled(user, message);
            }
            else if (!(bool) GetRoomVariables(user).Get<Serializable.Bool>("run"))
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
                $"HP: {hp} _{diff.Format()}_"
            );

            variables.Set("old_hp", new Serializable.Decimal(hp));

            if (hp <= 0)
            {
                OnKilled?.Invoke(user, this);
                user.RoomManager.Leave();
                return;
            }

            var dmg = GetDamage(user);
            dmg -= user.Info.KarmaEffect(dmg);
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