using System;
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
            using var vars = new Variables(this);
            vars.Health -= damage;
            vars.TotalDamage += damage;

            var attacker = vars.Attackers.SingleOrDefault(a => a.UserId.Equals(user.Info.UserId));
            if (attacker == null)
            {
                SendMessage(user, "Вы бы рады и ударить босса, но кажется уже поздно");
                return;
            }
            attacker.DamageDealed += damage;

            vars.Save();
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
                        if (percent > 0.3M)
                        {
                            MonsterBase.MonsterKilled(ctx, this);
                        }

                        ctx.User.Info.Gold += reward;
                        SendMessage(ctx.User,
                            $"<b>Вы получаете {reward.Format()} ({(percent * 100).Format()}%) монет за вклад в убийство босса {Name}!</b>");
                        if (ctx.User.RoomManager.CurrentRoom?.Identifier == Identifier)
                        {
                            ctx.User.RoomManager.Leave();
                        }
                    }
                }

                vars.Remove();
            }
        }

        public decimal GetCurrentHealth(User.User user)
        {
            using var vars = new Variables(this);
            return vars.Health;
        }

        public override void OnEnter(User.User user)
        {
            base.OnEnter(user);
            using var vars = new Variables(this);
            vars.Attackers.Add(new Attacker
            {
                UserId = user.Info.UserId,
                DamageDealed = 0
            });
            vars.Save();
            SendMessage(user,
                $"Вы попали к боссу! У него {vars.Gold.Format()} золота и {vars.Health.Format()} здоровья",
                GetActions(user));
        }

        public override void OnMessage(User.User user, ReceivedMessage message)
        {
            if (message.Text == "Сбежать" || message.Text == "Уйти")
            {
                user.RoomManager.Leave();
                return;
            }

            if (UseItem(user, message))
            {
                using var vars = new Variables(this);

                if (vars.Attackers.FirstOrDefault(a => a.UserId.Equals(user.Info.UserId)) == null)
                {
                    SendMessage(user, "Похоже, что босс уже умер", new[] {new[] {"Уйти"}});
                    return;
                }

                var damage = GetDamage(user);
                user.Info.MakeDamage(damage);

                SendMessage(user,
                    $"Босс наносит вам {damage.Format()} урона! У него {vars.Gold.Format()} золота и {vars.Health.Format()} здоровья",
                    GetActions(user));

                return;
            }

            SendMessage(user, "Нету у вас такого", GetActions(user));
        }

        public override bool OnLeave(User.User user)
        {
            using var vars = new Variables(this);

            var attacker = vars.Attackers.SingleOrDefault(a => a.UserId.Equals(user.Info.UserId));
            if (attacker == null)
            {
                SendMessage(user,
                    "Вам не место в этой битве, уходите быстрее.");
                return base.OnLeave(user);
            }

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
            vars.Save();

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

        private class Variables: IDisposable
        {
            private readonly string _key;
            private readonly bool _lockWasTaken;

            public readonly List<Attacker> Attackers;
            public decimal Gold;
            public decimal Health;
            public decimal TotalDamage;

            public Variables(BossBase boss)
            {
                System.Threading.Monitor.Enter(GlobalVariables.Variables, ref _lockWasTaken);
                _key = boss.GlobalVariablesKey;
                
                var vars = GlobalVariables.Variables.Get<VariableContainer>(_key);
                if (vars == null)
                {
                    Gold = boss.InitialGold;
                    Health = boss.Health;
                    TotalDamage = 0;
                    Attackers = new List<Attacker>();
                }
                else
                {
                    Gold = vars.Get<Serializable.Decimal>("gold");
                    Health = vars.Get<Serializable.Decimal>("health");
                    TotalDamage = vars.Get<Serializable.Decimal>("totalDamage");
                    Attackers = Attacker.Load(vars.Get<SerializableList>("attackers"));
                }
            }

            public void Save()
            {
                var vars = new VariableContainer();
                vars.Set("gold", new Serializable.Decimal(Gold));
                vars.Set("health", new Serializable.Decimal(Health));
                vars.Set("totalDamage", new Serializable.Decimal(TotalDamage));
                vars.Set("attackers", Attacker.Save(Attackers));
                GlobalVariables.Variables.Set(_key, vars);
            }

            public void Remove()
            {
                GlobalVariables.Variables.Remove(_key);
            }

            public void Dispose()
            {
                if (_lockWasTaken) System.Threading.Monitor.Exit(GlobalVariables.Variables);
            }
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