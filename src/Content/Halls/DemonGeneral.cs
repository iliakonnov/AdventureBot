using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Halls;

[Available(Id, Difficulity.Any, HallsRoot.Id)]
public class DemonGeneral : EvilMonsterBase
{
    public const string Id = "halls/DemonGeneral";

    public override string Name => "Генерал демонов";
    public override string Identifier => Id;
    protected override decimal Health => 1200;

    protected override decimal GetDamage(User user)
    {
        return 25;
    }

    protected override void Enter(User user, string[][] buttons)
    {
        SendMessage(user,
            "Один из самых сильных демонов в Чертогах. Топор, покрытый застывшей кровью недругов, непробиваемая броня из закаленного адского камня и крутые рога -- то, что заставляет дрожать каждое существо в Чертогах. Ты осознал, что тебе нужны его крутые рога. Забери их.",
            buttons);
    }

    protected override void OnWon(User user)
    {
        user.ItemManager.Add(new ItemInfo(DemonGeneralHorns.Id, 1));
    }
}

[Item(Id)]
public class DemonGeneralHorns : LootBase
{
    public const string Id = "DemonGeneral/Horns";

    public override string Name => "Рога генерала демонов";
    public override string Description => string.Empty;
    public override string Identifier => Id;
}