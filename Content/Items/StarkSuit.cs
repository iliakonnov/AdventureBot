using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items;

[Item(Id)]
public class StarkSuit : ItemBase
{
    public const string Id = "item/stark_suit";
    public override StructFlag<BuyGroup> Group => new(BuyGroup.Market);
    public override string Name => "Одноразовый костюм Старка";

    public override string Description =>
        "Его создал Старк когда-то для критических случаев, но ему так и не пришлось им пользоваться.";

    public override decimal? Price => 500;
    public override string Identifier => Id;
    public override StatsEffect Effect => null;

    public override bool CanUse(User user, ItemInfo info)
    {
        var room = user.RoomManager.GetRoom();
        return room != null && room.Identifier.StartsWith("town");
    }

    public override void OnUse(User user, ItemInfo info)
    {
        if (user.ItemManager.Remove(new ItemInfo(Identifier, 1)))
        {
            user.ItemManager.Add(new ItemInfo(ActivatedStarkSuit.Id, 1));
        }
    }
}

[Item(Id)]
public class ActivatedStarkSuit : ItemBase, IAdventureItem
{
    public const string Id = "stark_suit/activated";
    public override StructFlag<BuyGroup> Group => new(BuyGroup.NotSellable);
    public override string Name => "Активированный костюм Старка";
    public override string Description => "Надпись на этикетке: не рассчитан на продолжительное использование";
    public override decimal? Price => null;
    public override string Identifier => Id;

    public override StatsEffect Effect => new(ChangeType.Add, new Dictionary<StatsProperty, decimal>
    {
        {StatsProperty.Defence, 1000}
    });

    public override bool CanUse(User user, ItemInfo info)
    {
        return false;
    }

    public void OnAdventureEnter(User user, ItemInfo info)
    {
    }

    public override void OnAdd(User user, ItemInfo info, int count)
    {
        if (info.Count > 1)
        {
            user.MessageManager.SendMessage(new SentMessage
            {
                Text = "Ты попытался надеть два костюма сразу, но у тебя не получилось"
            });

            if (user.ItemManager.Remove(new ItemInfo(Identifier, 1)))
            {
                user.ItemManager.Add(new ItemInfo(StarkSuit.Id, 1));
            }
        }
        else
        {
            GetItemVariables(user).Set("counter", new Serializable.Int(2));
            user.MessageManager.SendMessage(new SentMessage
            {
                Text = "С тихим щелчком костюм закрепился на тебе"
            });
        }
    }

    public void OnAdventureLeave(User user, ItemInfo info)
    {
        var counter = GetItemVariables(user).Get<Serializable.Int>("counter") ?? 2;
        counter--;
        if (counter <= 0)
        {
            user.ItemManager.Remove(new ItemInfo(Identifier, 1));
            user.MessageManager.SendMessage(new SentMessage
            {
                Text = "Костюм взорвался прямо на тебе. Больно!"
            });
            user.Info.MakeDamage(15);
        }
        else
        {
            GetItemVariables(user).Set("counter", new Serializable.Int(counter - 1));
        }
    }
}