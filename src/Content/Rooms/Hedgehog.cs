using AdventureBot.Room;
using AdventureBot.User;
using Content.Quests;

namespace Content.Rooms;

[Available(Id, Difficulity.Easy, TownRoot.Id)]
public class Hedgehog : MonsterBase, IQuestMonster
{
    public const string Id = "monster/hedgehog";
    protected override decimal Health => 30;
    public override string Name => "Злой ёж";
    public override string Identifier => Id;

    protected override decimal GetDamage(User user)
    {
        return 5;
    }

    protected override void Enter(User user, string[][] buttons)
    {
        SendMessage(user, "Вы встречаете самого настоящего ежа. Удивительно!", buttons);
    }

    protected override bool OnRunaway(User user)
    {
        return true;
    }

    protected override void OnWon(User user)
    {
    }
}