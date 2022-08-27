using System;
using System.Diagnostics;
using System.Linq;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;
using AdventureBot.User.Stats;
using RoomManager = AdventureBot.Room.RoomManager;

namespace Content.Rooms.Arena;

[Room(Id)]
public class Battle : BetterRoomBase<Battle>, IMonster
{
    public const string Id = "arena/battle";
    public override string Name => "Гладиатор";
    public override string Identifier => Id;

    public override void OnEnter(User user)
    {
        base.OnEnter(user);

        SendMessage(user, @"<b>Правила арены</b>:
1. Вы тут не умрете по-настоящему
2. Удары наносите по очереди
3. Но если противник за 1.5 минуты не нанес удара, то можно нанести внеочередной удар
4. Победителю достается половина золота проигравшего
5. Сбежать отсюда нельзя!
Удачи!");

        GetRoomVariables(user).Set("stats", new StatsEffect(ChangeType.Set, user.Info.BaseStats.Effect));
        foreach (var maxStat in user.Info.MaxStats.Effect)
        {
            user.Info.ChangeStats(maxStat.Key, maxStat.Value, true);
        }

        if (user.MessageManager.LastMessage.Buttons != null)
        {
            GetRoomVariables(user).Set("buttons", new SerializableList(
                user.MessageManager.LastMessage.Buttons
                    .Select(row =>
                        new SerializableList(
                            row
                                .Select(btn => new Serializable.String(btn))
                                .Cast<ISerializable>()
                                .ToList()
                        )
                    )
                    .Cast<ISerializable>()
                    .ToList()
            ));
        }

        SendMessage(user,
            GetRoomVariables(user).Get<Serializable.Bool>("turn") == true
                ? "<b>Вы атакуете первым</b>"
                : "<b>Первым атакует ваш противник</b>",
            GetActions(user));
    }

    public override bool OnLeave(User user)
    {
        if (!(GetRoomVariables(user).Get<Serializable.Bool>("can_leave") ?? false))
        {
            return false;
        }

        var stats = GetRoomVariables(user).Get<StatsEffect>("stats");
        if (stats != null)
        {
            foreach (var keyValuePair in stats.Effect)
            {
                user.Info.ChangeStats(keyValuePair.Key, keyValuePair.Value, true);
            }
        }

        var buttons = GetRoomVariables(user).Get<SerializableList>("buttons");
        string[][] realButtons;
        if (buttons != null)
        {
            realButtons = buttons
                .Cast<SerializableList>()
                .Select(row => row
                    .Cast<Serializable.String>()
                    .Select(s => (string) s)
                    .ToArray()
                )
                .ToArray();
        }
        else
        {
            realButtons = new string[][] { };
        }

        user.ItemManager.Remove(new ItemInfo(Medallion.Id, 1));
        SendMessage(user, "Вы покидаете арену. Обязательно запишитесь ещё раз!", realButtons);

        return base.OnLeave(user);
    }

    public void MakeDamage(User user, decimal damage)
    {
        using (var ctx = new UserContext((UserId) GetRoomVariables(user).Get("enemy")))
        {
            ctx.User.Info.MakeDamage(damage, kill: false);

            SendMessage(ctx.User, $"Вам наносят {damage} урона!", GetActions(ctx.User));

            var health = ctx.User.Info.CurrentStats.GetStat(StatsProperty.Health);
            SendMessage(user, $"У противника {health.Format()} <i>({(-damage).Format()})</i> здоровья!",
                GetActions(user));

            if (health <= 0)
            {
                // Finish battle
                Win(user, ctx.User);
                Lose(user, ctx.User);
            }
        }
    }

    public decimal GetCurrentHealth(User user)
    {
        using (var ctx = new UserContext((UserId) GetRoomVariables(user).Get("enemy")))
        {
            return ctx.User.Info.CurrentStats.GetStat(StatsProperty.Health);
        }
    }

    public static void BeginBattle(User user, User enemy, bool firstTurn)
    {
        var self = (Battle) ObjectManager<IRoom>.Instance
            .Get<RoomManager>()
            .Get(Id);
        Debug.Assert(self != null, nameof(self) + " != null");

        self.SendMessage(user, $"Ого, вы на арене! Ваш противник: {enemy.Info.Name}");

        self.GetRoomVariables(user).Set("enemy", enemy.Info.UserId);
        self.GetRoomVariables(user).Set("turn", new Serializable.Bool(firstTurn));
        self.GetRoomVariables(user)
            .Set("lastMessage", new Serializable.Long(DateTimeOffset.Now.ToUnixTimeSeconds()));
        user.RoomManager.Go(Id, false);
    }

    private void Win(User winner, User loser)
    {
        SendMessage(winner, "Поздравляю вас с победой!");
        GetRoomVariables(winner).Set("can_leave", new Serializable.Bool(true));
        winner.Info.Gold += loser.Info.Gold / 2;
        winner.RoomManager.Leave(false);
    }

    private void Lose(User winner, User loser)
    {
        SendMessage(loser, "В следующий раз получится лучше!");
        GetRoomVariables(loser).Set("can_leave", new Serializable.Bool(true));
        loser.Info.Gold -= loser.Info.Gold / 2;
        loser.RoomManager.Leave(false);
    }

    public string[][] GetActions(User user)
    {
        return GetItems(user).Select(i => new[] {i}).ToArray();
    }

    [Action]
    public class MainAction : ActionBase<Battle>
    {
        public MainAction(Battle room) : base(room)
        {
        }

        [Fallback]
        public new void OnMessage(User user, ReceivedMessage message)
        {
            var variables = Room.GetRoomVariables(user);

            var itemToUse = user.ItemManager.Items.SingleOrDefault(i =>
                i.CanUse(user) && message.Text.StartsWith(i.Item.Name)
            );
            if (itemToUse == null)
            {
                Room.SendMessage(user, "Нельзя такое использовать", Room.GetActions(user));
                return;
            }

            using (var ctx = new UserContext((UserId) variables.Get("enemy")))
            {
                var enemyVariables = Room.GetRoomVariables(ctx);

                if (variables.Get<Serializable.Bool>("turn") != true)
                {
                    var lastMessage =
                        DateTimeOffset.FromUnixTimeSeconds(enemyVariables.Get<Serializable.Long>("lastMessage"));
                    if (DateTimeOffset.Now - lastMessage > TimeSpan.FromMinutes(1.5))
                    {
                        enemyVariables.Set("lastMessage",
                            new Serializable.Long(DateTimeOffset.Now.ToUnixTimeSeconds()));
                        Room.SendMessage(user, "Пока противник спит, вы наносите ещё один удар!",
                            Room.GetActions(user));
                    }
                    else
                    {
                        Room.SendMessage(user, "Не ваш ход, увы", Room.GetActions(user));
                        return;
                    }
                }

                enemyVariables.Set("turn", new Serializable.Bool(true));
                variables.Set("turn", new Serializable.Bool(false));
                variables.Set("lastMessage", new Serializable.Long(DateTimeOffset.Now.ToUnixTimeSeconds()));
            }

            // Must be outside of ctx (up to 3 user deserialization!)
            itemToUse.OnUse(user);

            using (var ctx = new UserContext((UserId) variables.Get("enemy")))
            {
                Room.SendMessage(ctx, "Ваш ход! Чем же вы ответите?");
                // Force send message to damaged user
                ctx.User.MessageManager.Finish();
            }
        }
    }
}