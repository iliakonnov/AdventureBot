using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;
using Content.Items;
using Content.Quests;

namespace Content.Rooms;

[Available(Id, Difficulity.Hard, TownRoot.Id)]
public class Legolas : MonsterBase, IQuestMonster
{
    public const string Id = "monster/legolas";
    protected override decimal Health => 1000;
    public override string Name => "Леголас";
    public override string Identifier => Id;

    protected override decimal GetDamage(User user)
    {
        return 70;
    }

    protected override void Enter(User user, string[][] buttons)
    {
        SendMessage(user,
            "Никогда не промахивается и может глушить эль галлонами не пьянея.  Стрела пролетела в миллиметре от твоей макушки.");
        SendMessage(user, "— Это был предупредительный выстрел!", buttons);
    }

    protected override bool OnRunaway(User user)
    {
        return true;
    }

    protected override void OnWon(User user)
    {
        user.ItemManager.Add(new ItemInfo(Bow.Id, 1));
    }
}