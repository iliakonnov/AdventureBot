using System.Diagnostics;
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

            var attacks = variables.Get<SerializableList>("user_attacks");
            Debug.Assert(attacks != null, nameof(attacks) + " != null");
            attacks.Add(new Serializable.Decimal(damage));
            variables.Set("user_attacks", attacks);
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
            variables.Set("user_attacks", new SerializableList());
            variables.Set("total_damage", new Serializable.Decimal(0));

            var buttons = GetActions(user);
            Enter(user, buttons);
        }

        public override bool OnLeave(User.User user)
        {
            var variables = GetRoomVariables(user);
            var won = (decimal) variables.Get<Serializable.Decimal>("hp") <= 0;
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

            var userDamage = variables.Get<SerializableList>("user_attacks")
                .Select(s => (decimal) (Serializable.Decimal) s)
                .ToList();
            if (userDamage.Count != 0)
            {
                var averageDamage = userDamage.Sum() / userDamage.Count;
                if (averageDamage >= 1)
                {
                    var xp = variables.Get<Serializable.Decimal>("total_damage") / averageDamage;
                    user.Info.Level.AddXp(xp);
                }
            }
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
            variables.Set("total_damage",
                new Serializable.Decimal(variables.Get<Serializable.Decimal>("total_damage") + dmg));
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