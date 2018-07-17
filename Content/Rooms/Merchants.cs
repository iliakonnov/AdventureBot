using System.Collections.Generic;
using System.Linq;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;
using Content.Town;

namespace Content.Rooms
{
    [Available("room/merchants", Difficulity.Any)]
    public class Merchants : RoomBase
    {
        private const int ItemCount = 3;

        public Merchants()
        {
            Routes = new MessageRecived[] {Shop, Shop2};
            Buttons = new NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>>
            {
                {
                    null, new Dictionary<string, MessageRecived>
                    {
                        {
                            "Закупиться", (user, message) =>
                            {
                                SwitchAction(user, Shop);
                                HandleAction(user, message);
                            }
                        },
                        {
                            "Ограбить", (user, message) =>
                            {
                                SendMessage(user,
                                    "Несмотря на их натренированные языки, сами купцы были довольно хилыми даже по твоим меркам. Поэтому на каждое из этих слащавых лиц пришлось всего по одному удару. Ты заработал немного монет и мое личное неуважение.");
                                user.Info.Gold += user.Random.Next(500, 850);
                                user.RoomManager.Leave();
                            }
                        },
                        {
                            "Уйти", (user, message) => user.RoomManager.Leave()
                        }
                    }
                }
            };
        }

        public override string Name => "Торговцы с Востока!";
        public override string Identifier => "room/merchants";

        public override void OnEnter(User user)
        {
            SwitchAction(user, null);
            user.MessageManager.ShownStats = ShownStats.Gold;
            SendMessage(
                user,
                "Перед тобой расположился небольшой караван, состоящий из трех верблюдов и нескольких купцов. Под листвой ветвистого дуба расположилась миниатюрная, но необыкновенно красивая палатка. От этого места так и веет восточным колоритом."
            );
            SendMessage(
                user,
                "— Дорогой, не желаешь отведать вкуснейших сухофруктов во всей Азии? Или нарядиться в тончайшие атласные шелка? А может, тебе не терпится пролить крови искусно отделанным ножом из слоновой кости? Мы привозим только лучшее! Еще ни одного разочарованного клиента!",
                GetButtons(user)
            );
        }

        public override bool OnLeave(User user)
        {
            return true;
        }

        public override void OnMessage(User user, RecivedMessage message)
        {
            if (!HandleAction(user, message))
            {
                HandleButtonAlways(user, message);
            }
        }

        private void Shop(User user, RecivedMessage message)
        {
            var items = GetAllItems();
            var flag = new Flag<BuyGroup>(BuyGroup.Merchant, BuyGroup.Market);
            var available = items.Keys()
                .Select(id => items.Get(id))
                .Where(item => item?.Price != null && item.Group.Intersects(flag))
                .ToArray();

            foreach (var item in available)
            {
                SendMessage(user, $"*{item.Name}* (x{ItemCount}) [{item.Price * ItemCount}]\n{item.Description}");
            }

            SendMessage(
                user,
                "— За звонкую монету можно приобрести все, что угодно!",
                available
                    .Select(item => new[] {item.Name})
                    .Concat(new[] {new[] {"Ничего"}})
                    .ToArray()
            );

            SwitchAction(user, Shop2);
        }

        private void Shop2(User user, RecivedMessage message)
        {
            var dict = GetAllItems()
                .AvailableToBuy(new Flag<BuyGroup>(BuyGroup.Merchant, BuyGroup.Market))
                .ToDictionary(i => i.Name, i => i);
            if (dict.TryGetValue(message.Text, out var item))
            {
                SwitchAction(user, null);
                if (user.BuyItem(new ItemInfo(item, ItemCount)))
                {
                    SendMessage(user, "— Приятно иметь дело с таким щедрым господином!", GetButtons(user));
                }
                else
                {
                    SendMessage(user, "— Даже мешок золота не возместит потраченного на тебя времени!");
                    user.RoomManager.Leave();
                }
            }
            else
            {
                SendMessage(user, "— Увы, но мы о таком никогда не слышали ранее.");
            }
        }
    }
}