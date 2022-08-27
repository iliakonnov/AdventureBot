using AdventureBot.Room;
using AdventureBot.User;
using Content.Quests;

namespace Content.Rooms;

[Available("monster/CreepMelee", Difficulity.Easy, TownRoot.Id)]
public class MonsterTemplate : MonsterBase, IQuestMonster
{
    public const string Id = "monster/CreepMelee";
    protected override decimal Health => 45;
    public override string Name => "Крип-мечник";
    public override string Identifier => Id;

    protected override decimal GetDamage(User user)
    {
        return 15;
    }

    protected override void Enter(User user, string[][] buttons)
    {
        SendMessage(user, "Неотъемлемая часть любой РПГ. Ты им смерть - они тебе деньги", buttons);
    }

    protected override bool OnRunaway(User user)
    {
        return true;
    }

    protected override void OnWon(User user)
    {
        user.Info.Gold += 45;
    }
}