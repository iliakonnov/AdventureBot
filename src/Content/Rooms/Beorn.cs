using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;
using Content.Items;
using Content.Quests;

namespace Content.Rooms;

[Available(Id, Difficulity.Hard, TownRoot.Id)]
public class Beorn : MonsterBase, IQuestMonster
{
    public const string Id = "monster/beorn";
    protected override decimal Health => 1500;
    public override string Name => "Беорн";
    public override string Identifier => Id;

    protected override decimal GetDamage(User user)
    {
        return 50;
    }

    protected override void Enter(User user, string[][] buttons)
    {
        SendMessage(
            user,
            "Этот огромный человекоподобный медведь — когда-то одно из самых опасных существ в Средиземье. Говорят, его когти настолько остры, что можно поцарапаться, просто взглянув на них, но пруфа нет. Пора проверить!",
            buttons
        );
    }

    protected override bool OnRunaway(User user)
    {
        return true;
    }

    protected override void OnWon(User user)
    {
        user.ItemManager.Add(new ItemInfo(BeornSkin.Id, 1));
    }
}