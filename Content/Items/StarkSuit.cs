using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item("item/stark_suit")]
    public class StarkSuit : ItemBase
    {
        public override Flag<BuyGroup> Group => new Flag<BuyGroup>(BuyGroup.Market);
        public override string Name => "Одноразовый костюм Старка";
        public override string Description => "Его создал Старк когда-то для критических случаев, но ему так и не пришлось им пользоваться.";
        public override decimal? Price => 500;
        public override string Identifier => "item/stark_suit";
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
                user.ItemManager.Add(new ItemInfo("stark_suit/activated", 1));
            }
        }
    }

    [Item("stark_suit/activated")]
    public class ActivatedStarkSuit : ItemBase, IAdventureItem
    {
        public override Flag<BuyGroup> Group => new Flag<BuyGroup>();
        public override string Name => "Активированное костюм Старка";
        public override string Description => "Надпись на этикетке: не рассчитан на продолжительное использование";
        public override decimal? Price => null;
        public override string Identifier => "stark_suit/activated";

        public override StatsEffect Effect => new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
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

            if (user.ItemManager.Remove(new ItemInfo(Identifier, 1)))
            {
                user.MessageManager.SendMessage(new SentMessage
                {
                    Text = "Ты попытался надеть два костюма сразу, но у тебя не получилось"
                });
                user.ItemManager.Add(new ItemInfo("item/stark_suit", 1));
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
}