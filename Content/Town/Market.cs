using System.Collections.Generic;
using System.Linq;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Town
{
    [Room(identifier)]
    public class Market : RoomBase
    {
        private const string identifier = "town/market";
        public override string Identifier { get; } = identifier;
        public override string Name { get; } = "Рынок";

        public Market()
        {
            void Leave(User user, RecivedMessage message) => user.RoomManager.Leave();

            Routes = new MessageRecived[]
            {
                Buy, Buy2, Sell, Sell2
            };

            Buttons = new NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>>()
            {
                {
                    null, new Dictionary<string, MessageRecived>
                    {
                        {"Купить", Buy},
                        {"Продать", Sell},
                        {"Уйти", Leave}
                    }
                }
            };
        }

        public override void OnEnter(User user)
        {
            user.MessageManager.ShownStats = ShownStats.Gold;
            SendMessage(user, "Вы пришли на рынок. Тут есть много всего.", GetButtons(user));
        }

        public override bool OnLeave(User user)
        {
            SendMessage(user, "Никто не обратил внимания на то, что вы ушли отсюда");

            return true;
        }

        public override void OnMessage(User user, RecivedMessage message)
        {
            if (!HandleAction(user, message))
            {
                HandleButtonAlways(user, message);
            }
        }

        private List<IItem> AvailableToBuy(User user)
        {
            var items = GetAllItems();
            var group = new Flag<BuyGroup>(BuyGroup.Market);
            return items.Keys()
                .Select(id => items.Get(id))
                .Where(item => item != null && item.Group.Intersects(group))
                .ToList();
        }

        private void Buy(User user, RecivedMessage message)
        {
            var loaded = AvailableToBuy(user);
            var buttons = loaded
                .Select(item => new[] {item.Name})
                .Concat(new[] {new[] {"Ничего"}})
                .ToArray();
            SendMessage(user, "Что же вы хотите купить?", buttons);

            foreach (var item in loaded)
            {
                SendMessage(user, $"*{item.Name}* [{item.Price}]\n{item.Description}");
            }

            SwitchAction(user, Buy2);
        }

        private void Buy2(User user, RecivedMessage message)
        {
            if (message.Text == "Ничего")
            {
                SwitchAction(user, null);
                SendMessage(user, "Ну ладно тогда", GetButtons(user));
            }
            else
            {
                var dict = AvailableToBuy(user).ToDictionary(i => i.Name, i => i);
                if (dict.TryGetValue(message.Text, out var item))
                {
                    if (user.BuyItem(new ItemInfo(item, 1)))
                    {
                        SwitchAction(user, null);
                        SendMessage(user, "Отлично!", GetButtons(user));
                    }
                    else
                    {
                        SendMessage(user, "С вашими деньгами **этот** предмет купить не выйдет.");
                    }
                }
                else
                {
                    SendMessage(user, "У меня такого нет, но обязательно придите ещё раз.");
                }
            }
        }

        private List<ItemInfo> AvailableToSell(User user)
        {
            var items = user.ItemManager.Items;
            return items
                .Where(item => item.Item.Price != null)
                .ToList();
        }

        private void Sell(User user, RecivedMessage message)
        {
            var items = AvailableToSell(user);
            var buttons = items
                .Select(item => new[] {item.Item.Name})
                .Concat(new[] {new[] {"Ничего"}})
                .ToArray();
            SendMessage(user, "Что же вы хотите продать?", buttons);

            foreach (var item in items)
            {
                SendMessage(user,
                    $"*{item.Item.Name}* (x{item.Count}) [{item.Item.Price * user.Info.SellMultiplier}]\n{item.Item.Description}");
            }

            SwitchAction(user, Sell2);
        }

        private void Sell2(User user, RecivedMessage message)
        {
            if (message.Text == "Ничего")
            {
                SwitchAction(user, null);
                SendMessage(user, "Ну ладно тогда", GetButtons(user));
            }
            else
            {
                var items = AvailableToSell(user);
                var dict = items.ToDictionary(i => i.Item.Name, i => new ItemInfo(i.Identifier, 1));

                if (dict.TryGetValue(message.Text, out var item))
                {
                    if (user.SellItem(item))
                    {
                        SwitchAction(user, null);
                        SendMessage(user, "Отлично!", GetButtons(user));
                    }
                    else
                    {
                        SendMessage(user, "Вы даже продать не можете!");
                    }
                }
                else
                {
                    SendMessage(user, "Чтобы что-то продать, нужно сначала что-то купить");
                }
            }
        }
    }
}