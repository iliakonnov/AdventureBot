using AdventureBot.Item;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Halls;

[Available(Id, Difficulity.Any, HallsRoot.Id)]
public class DemonOutcast : EvilMonsterBase
{
    public const string Id = "halls/demonOutcast";

    public override string Name => "Демон-изгой";
    public override string Identifier => Id;
    protected override decimal Health => 500;

    protected override decimal GetDamage(User user)
    {
        return 20;
    }

    protected override void Enter(User user, string[][] buttons)
    {
        SendMessage(user, "Его народ отверг его, заковал в кандалы. Но он, как и все демоны, жаждет крови.",
            buttons);
    }

    protected override void OnWon(User user)
    {
        user.ItemManager.Add(new ItemInfo(OutcastChain.Id, 1));
    }
}

[Item(Id)]
public class OutcastChain : LootBase, IEvilWeapon
{
    public const string Id = "halls/outcastChain";

    public override string Name => "Цепь изгоя";
    public override string Description => string.Empty;
    public override string Identifier => Id;

    public override bool CanUse(User user, ItemInfo info)
    {
        return false;
    }

    public decimal DamageMultiplier => 1.05M;
}