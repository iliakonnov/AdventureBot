using System.Collections.Generic;
using System.Linq;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Town
{
    [Room(identifier)]
    public class Market : RoomBase
    {
        private const string identifier = "town/market";

        public Market()
        {
            void Leave(User user, RecivedMessage message)
            {
                user.RoomManager.Leave();
            }

            Routes = new MessageRecived[]
            {
                Buy, Buy2, Sell, Sell2
            };

            Buttons = new NullableDictionary<MessageRecived, Dictionary<string, MessageRecived>>
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

        public override string Identifier { get; } = identifier;
        public override string Name { get; } = "Рынок";

        public override void OnEnter(User user)
        {
            SwitchAction(user, null);
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
            if (!HandleAction(user, message)) HandleButtonAlways(user, message);
        }

        private void Buy(User user, RecivedMessage message)
        {
            var loaded = GetAllItems().AvailableToBuy(new Flag<BuyGroup>(BuyGroup.Market));
            var buttons = loaded
                .Select(item => new[] {item.Name})
                .Concat(new[] {new[] {"Ничего"}})
                .ToArray();
            SendMessage(user, "Что же вы хотите купить?", buttons);

            foreach (var item in loaded) SendMessage(user, $"*{item.Name}* [{item.Price}]\n{item.Description}");

            SwitchAction(user, Buy2);
        }

        private void Buy2(User user, RecivedMessage message)
        {
            if (message.Text == "Ничего")
            {
                SwitchAction(user, null);
                SendMessage(user, "Ну ладно тогда", GetButtons(user));
                return;
            }

            var dict = GetAllItems().AvailableToBuy(new Flag<BuyGroup>(BuyGroup.Market))
                .ToDictionary(i => i.Name, i => i);
            if (dict.TryGetValue(message.Text, out var item))
            {
                if (user.BuyItem(new ItemInfo(item, 1)))
                {
                    SwitchAction(user, null);
                    SendMessage(user, "Отлично!", GetButtons(user));
                }
                else
                {
                    SendMessage(user, "С вашими деньгами *этот* предмет купить не выйдет.");
                }
            }
            else
            {
                SendMessage(user, "У меня такого нет, но обязательно придите ещё раз.");
            }
        }

        private void Sell(User user, RecivedMessage message)
        {
            var items = user.ItemManager.Items.AvailableToSell(new Flag<BuyGroup>(BuyGroup.Market));
            var buttons = items
                .Select(item => new[] {item.Item.Name})
                .Concat(new[] {new[] {"Ничего"}})
                .ToArray();
            SendMessage(user, "Что же вы хотите продать?", buttons);

            foreach (var item in items)
                SendMessage(user,
                    $"*{item.Item.Name}* (x{item.Count}) [{item.Item.Price * user.Info.SellMultiplier}]\n{item.Item.Description}");

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
                var items = user.ItemManager.Items.AvailableToSell(new Flag<BuyGroup>(BuyGroup.Market));
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