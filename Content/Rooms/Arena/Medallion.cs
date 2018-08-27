using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Linq;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;
using AdventureBot.UserManager;

namespace Content.Rooms.Arena
{
    [Item(Id)]
    public class Medallion : ItemBase
    {
        public const string Id = "arena/medallion";

        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Медальон гладиатора";
        public override string Description => "Продайте его кому-нибудь, если не желаете сражаться";
        public override decimal? Price => 0;
        public override string Identifier => Id;
        public override StatsEffect Effect => null;

        public override bool CanUse(User user, ItemInfo info)
        {
            return false;
        }

        public Medallion()
        {
            MessengerManager.OnRecived += OnMessage;
            User.OnReset += OnReset;
        }

        private void OnMessage(User user, RecivedMessage message)
        {
            if (user.ItemManager.Get(Id) == null)
            {
                return;
            }

            var filter = new List<(DbColumnAttribute, string, object)>
            {
                (DatabaseVariables.GetColumn(v => v.Level), ">=", user.Info.Level.Level - 1),
                (DatabaseVariables.GetColumn(v => v.Level), "<=", user.Info.Level.Level + 1),
                (DatabaseVariables.GetColumn(v => v.LastMessageRecived), ">",
                    DateTime.Now - TimeSpan.FromMinutes(1.5))
            };
            var users = DatabaseConnection.QueryUsers(null, filter, null);
            ImmutableHashSet<UserId> gladiators;
            lock (GlobalVariables.Variables)
            {
                gladiators = GetGladiators()
                    .Cast<UserId>()
                    .ToImmutableHashSet();
            }

            if (!gladiators.Contains(user.Info.UserId))
            {
                user.MessageManager.SendMessage(new SentMessage
                {
                    Text = "<b>Отныне вы не гладиатор!</b>"
                });
                user.ItemManager.Remove(new ItemInfo(Id, 1));
                return;
            }

            gladiators = gladiators.Remove(user.Info.UserId);

            var filtered = users
                .Where(u => gladiators.Contains(u.Id))
                .Where(u =>
                {
                    using (var ctx = new UserContext(u.Id))
                    {
                        return ctx.User.RoomManager.GetRoom()?.Identifier != Battle.Id;
                    }
                })
                .ToList();

            if (filtered.Count == 0)
            {
                return;
            }

            var enemy = filtered[user.Random.Next(filtered.Count)];
            using (var ctx = new UserContext(enemy.Id))
            {
                Battle.BeginBattle(ctx.User, user, true);

                // Force send message after enetring battle to show OnEnter() to user
                ctx.User.MessageManager.Finish();
                
                // Force send message before enetring battle to clean queue.
                // OnEnter message will be handled by MessengerManager
                user.MessageManager.Finish();

                Battle.BeginBattle(user, ctx, false);
            }
        }

        private bool EnsureSingle(User user, ItemInfo info)
        {
            if (info.Count <= 1)
            {
                return false;
            }

            user.ItemManager.Remove(new ItemInfo(info.Identifier, info.Count - 1));
            return true;
        }

        private SerializableList GetGladiators()
        {
            // GlobalVariables must be locked
            var gladiators = GlobalVariables.Variables.Get<SerializableList>("arena/gladiators");
            if (gladiators == null)
            {
                gladiators = new SerializableList();
                GlobalVariables.Variables.Set("arena/gladiators", gladiators);
            }

            return gladiators;
        }

        public override void OnAdd(User user, ItemInfo info, int count)
        {
            if (EnsureSingle(user, info))
            {
                return;
            }

            lock (GlobalVariables.Variables)
            {
                var gladiators = GetGladiators();
                gladiators.Add(user.Info.UserId);
            }
        }

        public override void OnRemove(User user, ItemInfo info, int count)
        {
            if (EnsureSingle(user, info))
            {
                return;
            }

            OnReset(user);
        }

        private void OnReset(User user)
        {
            lock (GlobalVariables.Variables)
            {
                var gladiators = GetGladiators();
                gladiators.Remove(user.Info.UserId);
            }
        }
    }
}