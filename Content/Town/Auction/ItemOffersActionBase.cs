﻿using System.Collections.Generic;
using System.Linq;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;

namespace Content.Town.Auction
{
    public abstract class ItemOffersActionBase : ActionBase<AuctionRoom>
    {
        protected ItemOffersActionBase(AuctionRoom room) : base(room)
        {
        }

        private (List<Offer>, string) GetOffers(Offers offers, BuySellState state)
        {
            var item = RoomBase.GetAllItems().Get(state.SelectedItemId);
            if (item == null)
            {
                return (null, null);
            }

            if (!offers.TryGetValue(item.Identifier, out var itemOffer))
            {
                return (null, item.Name);
            }

            return (state.Selling ? itemOffer.BuyOffers : itemOffer.SellOffers, item.Name);
        }

        public void Enter(User user)
        {
            var state = StateContainer.Deserialize<BuySellState>(
                Room.GetRoomVariables(user).Get<VariableContainer>("state")
            );
            var (itemOffers, itemName) = GetOffers(Offers.Load(), state);
            if (itemOffers == null || itemName == null)
            {
                Back(user, null);
                return;
            }

            var prices = new SortedDictionary<decimal, List<int>>();
            foreach (var offer in itemOffers.OrderBy(o => o.Created))
            {
                if (prices.TryGetValue(offer.Price, out var price))
                {
                    price.Add(offer.Count);
                }
                else
                {
                    prices[offer.Price] = new List<int> {offer.Count};
                }
            }

            var messageOffers = string.Join("\n", prices.Select(
                kv => $"{kv.Key} золота: {string.Join("+", kv.Value.OrderBy(i => i))} шт."
            ));
            var message = $"<b>{itemName}</b>\n{messageOffers}";

            var buttons = prices
                .Select(kv => new[] {kv.Key.Format()})
                .Concat(new[] {new[] {"Назад"}})
                .ToArray();
            Room.SendMessage(user, message, buttons);
        }

        [Fallback]
        public void OfferSelected(User user, RecivedMessage message)
        {
            var state = StateContainer.Deserialize<BuySellState>(
                Room.GetRoomVariables(user).Get<VariableContainer>("state")
            );
            var offers = Offers.Load();
            var (itemOffers, _) = GetOffers(offers, state);
            if (state.Count == null || state.SelectedItemCount == null)
            {
                // Selecting price
                if (!decimal.TryParse(message.Text, out var price))
                {
                    Enter(user);
                    return;
                }

                var matchingOffers = itemOffers.Where(o => o.Price == price).ToList();
                state.SelectedItemCount = matchingOffers.Select(o => o.Count).Sum();
                Room.GetRoomVariables(user).Set("state", StateContainer.Serialize(state));
            }
            else
            {
                // Selecting count
                if (!int.TryParse(message.Text, out var count) || count < 0 || count > state.SelectedItemCount)
                {
                    Room.SendMessage(user, $"Введите количество предметов (от 0 до {state.SelectedItemCount})");
                    return;
                }

                if (count == 0)
                {
                    // Looks like cancel
                    Back(user, message);
                    return;
                }

                var matchingOffers = itemOffers
                    .Where(o => o.Price == state.SelectedItemPrice)
                    .OrderBy(o => o.Created)
                    .ToList();

                var buyedCount = Logic.Buy(matchingOffers, user, count);
                Room.SendMessage(user, $"Вы купили {buyedCount} штук!");

                offers.Save();
                Back(user, message);
            }
        }

        [Button("Назад")]
        public void Back(User user, RecivedMessage message)
        {
            Room.GetAction<AuctionRoom.AllOffersAction>().Enter(user);
            Room.SwitchAction<AuctionRoom.AllOffersAction>(user);
        }
    }
}