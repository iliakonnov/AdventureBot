using System.Collections.Generic;
using System.Linq;
using AdventureBot.Messenger;

namespace AdventureBot.Room
{
    public abstract class BossBase : RoomBase, IMonster
    {
        protected abstract decimal InitialGold { get; }
        protected abstract decimal Health { get; }
        private string GlobalVariablesKey => $"boss/{Identifier}";

        public void MakeDamage(User.User user, decimal damage)
        {
            var vars = Load();
            vars.Health -= damage;
            vars.TotalDamage += damage;

            var attacker = vars.Attackers.Single(a => a.UserId.Equals(user.Info.UserId));
            attacker.DamageDealed += damage;

            Save(vars);
            if (vars.Health <= 0)
            {
                foreach (var usr in vars.Attackers)
                {
                    if (vars.TotalDamage == 0)
                    {
                        vars.TotalDamage = Health;
                    }

                    var percent = usr.DamageDealed / vars.TotalDamage;
                    var reward = vars.Gold * percent;
                    using (var ctx = new UserContext(usr.UserId))
                    {
                        ctx.User.Info.Gold += reward;
                        SendMessage(ctx.User,
                            $"<b>Вы получаете {reward.Format()} ({(percent * 100).Format()}%) монет за вклад в убийство босса {Name}!</b>");
                        if (ctx.User.RoomManager.CurrentRoom?.Identifier == Identifier)
                        {
                            ctx.User.RoomManager.Leave();
                        }
                    }
                }

                lock (GlobalVariables.Variables)
                {
                    GlobalVariables.Variables.Remove(GlobalVariablesKey);
                }
            }
        }

        public decimal GetCurrentHealth(User.User user)
        {
            return Load().Health;
        }

        public override void OnEnter(User.User user)
        {
            base.OnEnter(user);
            var vars = Load();
            vars.Attackers.Add(new Attacker
            {
                UserId = user.Info.UserId,
                DamageDealed = 0
            });
            Save(vars);
            SendMessage(user, $"Вы попали к боссу! У него {vars.Gold} золота и {vars.Health} здоровья",
                GetActions(user));
        }

        public override void OnMessage(User.User user, RecivedMessage message)
        {
            if (message.Text == "Сбежать")
            {
                user.RoomManager.Leave();
                return;
            }

            if (UseItem(user, message))
            {
                var vars = Load();

                if (vars.Attackers.FirstOrDefault(a => a.UserId.Equals(user.Info.UserId)) == null)
                {
                    SendMessage(user, "Похоже, что босс уже умер", new[] {new[] {"Уйти"}});
                    return;
                }

                var damage = GetDamage(user);
                user.Info.MakeDamage(damage);

                SendMessage(user,
                    $"Босс наносит вам {damage} урона! У него {vars.Gold} золота и {vars.Health} здоровья",
                    GetActions(user));

                return;
            }

            SendMessage(user, "Нету у вас такого", GetActions(user));
        }

        public override bool OnLeave(User.User user)
        {
            var vars = Load();
            var attacker = vars.Attackers.Single(a => a.UserId.Equals(user.Info.UserId));

            if (vars.Health <= 0)
            {
                // Winner
                return base.OnLeave(user);
            }

            SendMessage(user,
                "Половина вашего золота уходит в фонд борьбы с боссами! И не надейтесь на вознаграждение");

            var gold = user.Info.Gold / 2;
            user.Info.Gold -= gold;

            vars.Gold += gold;
            vars.Attackers.Remove(attacker);
            Save(vars);

            return base.OnLeave(user);
        }

        protected abstract decimal GetDamage(User.User user);

        private string[][] GetActions(User.User user)
        {
            return GetItems(user)
                .Concat(new[] {"Сбежать"})
                .Select(i => new[] {i})
                .ToArray();
        }

        private Variables Load()
        {
            lock (GlobalVariables.Variables)
            {
                var vars = GlobalVariables.Variables.Get<VariableContainer>(GlobalVariablesKey);
                if (vars == null)
                {
                    return new Variables
                    {
                        Gold = InitialGold,
                        Health = Health,
                        TotalDamage = 0,
                        Attackers = new List<Attacker>()
                    };
                }

                return new Variables
                {
                    Gold = vars.Get<Serializable.Decimal>("gold"),
                    Health = vars.Get<Serializable.Decimal>("health"),
                    TotalDamage = vars.Get<Serializable.Decimal>("totalDamage"),
                    Attackers = Attacker.Load(vars.Get<SerializableList>("attackers"))
                };
            }
        }

        private void Save(Variables variables)
        {
            var vars = new VariableContainer();
            vars.Set("gold", new Serializable.Decimal(variables.Gold));
            vars.Set("health", new Serializable.Decimal(variables.Health));
            vars.Set("totalDamage", new Serializable.Decimal(variables.TotalDamage));
            vars.Set("attackers", Attacker.Save(variables.Attackers));
            lock (GlobalVariables.Variables)
            {
                GlobalVariables.Variables.Set(GlobalVariablesKey, vars);
            }
        }

        private class Variables
        {
            public List<Attacker> Attackers;
            public decimal Gold;
            public decimal Health;
            public decimal TotalDamage;
        }

        public class Attacker
        {
            public decimal DamageDealed;
            public UserId UserId;

            public static List<Attacker> Load(SerializableList list)
            {
                if (list == null)
                {
                    return new List<Attacker>();
                }

                var result = new List<Attacker>();
                foreach (VariableContainer container in list)
                {
                    result.Add(new Attacker
                    {
                        DamageDealed = container.Get<Serializable.Decimal>("damageDealed"),
                        UserId = (UserId) container.Get("userId")
                    });
                }

                return result;
            }

            public static SerializableList Save(IEnumerable<Attacker> attackers)
            {
                var result = new SerializableList();
                foreach (var attacker in attackers)
                {
                    var container = new VariableContainer();
                    container.Set("damageDealed", new Serializable.Decimal(attacker.DamageDealed));
                    container.Set("userId", attacker.UserId);
                    result.Add(container);
                }

                return result;
            }
        }
    }
}