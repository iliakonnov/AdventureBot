using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Halls;

[Available(Id, Difficulity.Any, HallsRoot.Id)]
public class ObsidianGolem : EvilMonsterBase
{
    public const string Id = "halls/ObsidianGolem";

    public override string Name => "Обсидиановый голем";
    public override string Identifier => Id;
    protected override decimal Health => 900;

    protected override decimal GetDamage(User user)
    {
        return 20;
    }

    protected override void Enter(User user, string[][] buttons)
    {
        SendMessage(user,
            "По пути ты оказался на широком плато, усеянном небольшими вулканоподобными кратерами. Один из таких кратеров в двух метрах от тебя с треском и скрипом собрался в огромного обсидианового голема, пылающего магмой. Начинает казаться, что все в Чертогах пытается тебя убить.",
            buttons);
    }

    protected override void OnWon(User user)
    {
        user.ItemManager.Add(new ItemInfo(ObsidianPlate.Id, 5));
    }
}

[Item(Id)]
public class ObsidianPlate : LootBase
{
    public const string Id = "ObsidianGolem/plate";

    public override string Name => "Обсидиановая пластина";
    public override string Description => string.Empty;
    public override string Identifier => Id;
}