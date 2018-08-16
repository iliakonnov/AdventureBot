using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Items
{
    [Item(Id)]
    public class GolemHeart : ItemBase
    {
        public const string Id = "item/golem_heart";
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>(BuyGroup.Market);
        public override string Name => "Сердце голема";
        public override string Description => "Делает кожу каменной";
        public override decimal? Price => 50;
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
                user.ItemManager.Add(new ItemInfo(ActivatedGolemHeart.Id, 1));
            }
        }
    }

    [Item(Id)]
    public class ActivatedGolemHeart : ItemBase, IAdventureItem
    {
        public const string Id = "golem_heart/activated";
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override string Name => "Активированное сердце голема";
        public override string Description => "Делает кожу каменной";
        public override decimal? Price => null;
        public override string Identifier => Id;

        public override StatsEffect Effect => new StatsEffect(ChangeType.Add, new Dictionary<StatsProperty, decimal>
        {
            {StatsProperty.Defence, 100}
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
            GetItemVariables(user).Set("counter", new Serializable.Int(2));
            if (user.ItemManager.Remove(new ItemInfo(Identifier, 1)))
            {
                user.MessageManager.SendMessage(new SentMessage
                {
                    Text = "Твоя каменная кожа рассыпалась, чтобы собраться заново"
                });
            }
            else
            {
                user.MessageManager.SendMessage(new SentMessage
                {
                    Text = "Ты чувствуешь, как кожа каменеет"
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
                    Text = "Твоя кожа снова стала обычной"
                });
            }
            else
            {
                GetItemVariables(user).Set("counter", new Serializable.Int(counter - 1));
            }
        }
    }
}