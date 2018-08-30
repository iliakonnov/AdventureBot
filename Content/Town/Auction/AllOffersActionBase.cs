using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;

namespace Content.Town.Auction
{
    public abstract class AllOffersActionBase : ActionBase<AuctionRoom>
    {
        protected AllOffersActionBase(AuctionRoom room) : base(room)
        {
        }

        private static Tuple<decimal, decimal> FindMinMax(IEnumerable<Offer> offers)
        {
            Tuple<decimal, decimal> result = null;
            foreach (var offer in offers)
            {
                if (result != null)
                {
                    result = new Tuple<decimal, decimal>(
                        System.Math.Min(result.Item1, offer.Price),
                        System.Math.Max(result.Item2, offer.Price)
                    );
                }
                else
                {
                    result = new Tuple<decimal, decimal>(offer.Price, offer.Price);
                }
            }

            return result;
        }

        public void Enter(User user)
        {
            var offers = Offers.Load();
            var message = new StringBuilder();
            var itemManager = RoomBase.GetAllItems();
            var buttons = new List<string[]>(offers.Count);
            foreach (var kv in offers)
            {
                var item = itemManager.Get(kv.Key);
                var sellPrices = FindMinMax(kv.Value.SellOffers);
                var buyPrices = FindMinMax(kv.Value.BuyOffers);
                if (sellPrices == null && buyPrices == null
                    || item == null)
                {
                    continue;
                }

                message.Append($"{item.Name}");
                var buttonRow = new List<string>(2);
                if (sellPrices != null)
                {
                    message.Append(sellPrices.Item1 != sellPrices.Item2
                        ? $"; продают от {sellPrices.Item1.Format()} до {sellPrices.Item2.Format()}"
                        : $"; продают за {sellPrices.Item1.Format()}");
                    buttonRow.Add($"Купить {item.Name}");
                }

                if (buyPrices != null)
                {
                    message.Append(buyPrices.Item1 != buyPrices.Item2
                        ? $"; покупают от {buyPrices.Item1.Format()} до {buyPrices.Item2.Format()}"
                        : $"; покупают за {buyPrices.Item1.Format()}");
                    buttonRow.Add($"Продать {item.Name}");
                }

                buttons.Add(buttonRow.ToArray());

                message.AppendLine();
            }

            user.MessageManager.SendMessage(new SentMessage
            {
                Text = message.ToString(),
                Buttons = buttons
                    .Concat(new[] {new[] {"Назад"}})
                    .ToArray()
            });
        }

        [Fallback]
        public void OfferSelected(User user, RecivedMessage message)
        {
            var splitted = message.Text.Split(' ');
            if (splitted.Length < 2)
            {
                goto SomethingWrong;
            }

            var action = splitted[0];
            var itemName = string.Join(" ", splitted.Skip(1));
            var itemManger = RoomBase.GetAllItems();
            var item = itemManger.Keys()
                .Select(id => itemManger.Get(id))
                .SingleOrDefault(i => i != null && i.Name == itemName);
            if (item == null)
            {
                goto SomethingWrong;
            }

            var offers = Offers.Load();
            if (!offers.TryGetValue(item.Identifier, out var offer))
            {
                goto SomethingWrong;
            }

            var state = new BuySellState
            {
                SelectedItemId = item.Identifier
            };

            switch (action)
            {
                case "Продать":
                {
                    state.Selling = false;
                    break;
                }
                case "Купить":
                {
                    state.Selling = true;
                    return;
                }
                default:
                    goto SomethingWrong;
            }

            Room.GetRoomVariables(user).Set("state", StateContainer.Serialize(state));
            Room.SwitchAction<AuctionRoom.ItemOffersAction>(user);

            return;
            SomethingWrong:
            Enter(user);
        }

        [Button("Назад")]
        public void Back(User user, RecivedMessage message)
        {
            Room.SwitchAction<AuctionRoom.MainAction>(user);
        }
    }
}