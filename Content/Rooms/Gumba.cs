using System.Linq;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;
using Content.Quests;

namespace Content.Rooms;

[Available(Id, Difficulity.Easy, TownRoot.Id)]
public class Gumba : MonsterBase, IQuestMonster
{
    public const string Id = "monster/gumba";
    protected override decimal Health => 15;
    public override string Name => "Гумба";
    public override string Identifier => Id;

    public override void OnMessage(User user, ReceivedMessage message)
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

    protected override decimal GetDamage(User user)
    {
        return 3;
    }

    protected override void Enter(User user, string[][] buttons)
    {
        SendMessage(user, "Какой миленький злобный грибочек!", GetActions(user));
    }

    protected override string[][] GetActions(User user)
    {
        return base.GetActions(user)
            .Concat(new[] {new[] {"Прыгнуть на голову"}})
            .ToArray();
    }

    protected override bool OnRunaway(User user)
    {
        return true;
    }

    protected override void OnWon(User user)
    {
        user.Info.Gold += 3;
    }
}