using System;
using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;

namespace Content.Town.Auction
{
    public abstract class QuantitySelectionActionBase : ActionBase<AuctionRoom>
    {
        protected QuantitySelectionActionBase(AuctionRoom room) : base(room)
        {
        }

        public void Enter(User user)
        {
            var state = StateContainer.Deserialize<AddOfferState>(
                Room.GetRoomVariables(user).Get<VariableContainer>("state")
            );
            // TODO: Calculate maxValue here, not in AddOfferAction
            var maxValue = state.MaxQuantityAvailable == int.MaxValue ? "∞" : state.MaxQuantityAvailable.ToString();
            Room.SendMessage(user, $"Теперь введите количество (не больше {maxValue})", Room.GetButtons(user));
        }

        [Fallback]
        public void Fallback(User user, RecivedMessage message)
        {
            if (int.TryParse(message.Text, out var quantity))
            {
                var state = StateContainer.Deserialize<AddOfferState>(
                    Room.GetRoomVariables(user).Get<VariableContainer>("state")
                );
                if (quantity <= state.MaxQuantityAvailable && quantity >= 0)
                {
                    state.QuantitySelected = quantity;
                    Room.GetRoomVariables(user).Set("state", StateContainer.Serialize(state));

                    if (state.QuantitySelected != 0)
                    {
                        var offers = Offers.Load();
                        if (!offers.TryGetValue(state.SelectedItemId, out var itemOffers))
                        {
                            itemOffers = new ItemOffer(new List<Offer>(), new List<Offer>());
                            offers[state.SelectedItemId] = itemOffers;
                        }

                        var offer = new Offer(
                            user.Info.UserId,
                            state.SelectedItemPrice,
                            state.QuantitySelected,
                            DateTimeOffset.Now,
                            state.SelectedItemId
                        );

                        if (state.Selling)
                        {
                            if (user.ItemManager.Remove(new ItemInfo(offer.ItemId, offer.Count)))
                            {
                                itemOffers.SellOffers.Add(offer);
                            }
                        }
                        else
                        {
                            if (user.Info.TryDecreaseGold(state.SelectedItemPrice * state.QuantitySelected))
                            {
                                itemOffers.BuyOffers.Add(offer);
                            }
                        }

                        offers.Save();
                    }

                    Room.SwitchAction<AuctionRoom.AddOfferAction>(user);
                    Room.GetAction<AuctionRoom.AddOfferAction>().Enter(user);
                    return;
                }
            }

            // Something wrong
            Enter(user);
        }

        [Button("Назад")]
        public void Back(User user, RecivedMessage message)
        {
            Room.SwitchAction<AuctionRoom.PriceSelectionAction>(user);
            Room.GetAction<AuctionRoom.PriceSelectionAction>().Enter(user);
        }
    }
}