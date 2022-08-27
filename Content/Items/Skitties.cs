using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items;

[Item(Id)]
public class Skitties : ItemBase, IAdventureItem
{
    public const string Id = "skitties/candy";
    public override StructFlag<BuyGroup> Group => new();
    public override string Name => "Конфета \"Skitties\"";
    public override string Description => string.Empty;
    public override decimal? Price => 50;
    public override string Identifier => Id;
    public override StatsEffect Effect => null;

    public override bool CanUse(User user, ItemInfo info)
    {
        return true;
    }

    public override void OnUse(User user, ItemInfo info)
    {
        if (user.ItemManager.Remove(new ItemInfo(Identifier, 1)))
        {
            user.Info.ChangeStats(StatsProperty.Health, 25);
        }
    }

    public void OnAdventureEnter(User user, ItemInfo info)
    {
        var cnt = user.VariableManager.UserVariables.Get<Serializable.Int>("skitties_diabetes") ?? 10;
        if (cnt == 1)
        {
            return;
        }

        user.MessageManager.SendMessage(new SentMessage
        {
            Text = "Диабет мучает тебя..."
        });
        cnt--;
        user.VariableManager.UserVariables.Set("skitties_diabetes", new Serializable.Int(cnt));
        user.Info.ChangeStats(StatsProperty.Health, -5);
    }

    public void OnAdventureLeave(User user, ItemInfo info)
    {
    }
}