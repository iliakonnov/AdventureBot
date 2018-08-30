using System.Collections.Generic;
using System.Linq;
using System.Text;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;

namespace Content.Town.Auction
{
    public abstract class AddOfferActionBase : ActionBase<AuctionRoom>
    {
        protected AddOfferActionBase(AuctionRoom room) : base(room)
        {
        }

        public void Enter(User user)
        {
            var offers = Offers.Load();
            var message = new StringBuilder();
            var buttons = new List<string[]>();

            foreach (var itemInfo in user.ItemManager.Items)
            {
                var itemId = itemInfo.Identifier;
                if (!offers.TryGetValue(itemId, out var itemOffers))
                {
                    itemOffers = new ItemOffer(new List<Offer>(), new List<Offer>());
                }

                var myBuy = itemOffers.BuyOffers.SingleOrDefault(offer => offer.UserId.Equals(user.Info.UserId));
                var mySell = itemOffers.BuyOffers.SingleOrDefault(offer => offer.UserId.Equals(user.Info.UserId));
                var btnRow = new List<string>
                {
                    myBuy != null ? $"Не покупать {itemInfo.Item.Name}" : $"Купить {itemInfo.Item.Name}",
                    mySell != null ? $"Не продавать {itemInfo.Item.Name}" : $"Продать {itemInfo.Item.Name}"
                };
                message.AppendLine($"{itemInfo.Item.Name} x {itemInfo.Count}");
                buttons.Add(btnRow.ToArray());
            }

            Room.SendMessage(user, message.ToString(), buttons.Concat(new[] {new[] {"Назад"}}).ToArray());
        }

        [Fallback]
        public void ItemSelected(User user, RecivedMessage message)
        {
            var splitted = message.Text.Split(' ');

            var action = splitted[0].ToLower();
            string itemName;

            if (action == "Не")
            {
                action += " " + splitted[1];
                itemName = string.Join(" ", splitted.Skip(2));
            }
            else
            {
                itemName = string.Join(" ", splitted.Skip(1));
            }

            var itemMgr = RoomBase.GetAllItems();
            var item = itemMgr.Keys().Select(id => itemMgr.Get(id)).SingleOrDefault(i => i?.Name == itemName);
            if (item == null)
            {
                goto SomethingWrong;
            }

            var offers = Offers.Load();

            offers.TryGetValue(item.Identifier, out var itemOffers);

            var sellOffer = itemOffers?.SellOffers.SingleOrDefault(o => o.UserId.Equals(user.Info.UserId));
            var buyOffer = itemOffers?.SellOffers.SingleOrDefault(o => o.UserId.Equals(user.Info.UserId));
            switch (action)
            {
                case "Не покупать":
                {
                    if (buyOffer == null)
                    {
                        goto SomethingWrong;
                    }

                    itemOffers.BuyOffers.Remove(buyOffer);
                    break;
                }
                case "Не продавать":
                {
                    if (sellOffer == null)
                    {
                        goto SomethingWrong;
                    }

                    itemOffers.SellOffers.Remove(sellOffer);
                    break;
                }
                case "Купить":
                {
                    if (buyOffer != null)
                    {
                        goto SomethingWrong;
                    }

                    var state = new AddOfferState
                    {
                        Selling = false,
                        SelectedItemId = item.Identifier,
                        MaxQuantityAvailable = user.ItemManager.Get(item.Identifier)?.Count ?? 0
                    };
                    Room.GetRoomVariables(user).Set("state", StateContainer.Serialize(state));

                    Room.SwitchAction<AuctionRoom.PriceGroupSelectionAction>(user);
                    Room.GetAction<AuctionRoom.PriceGroupSelectionAction>().Enter(user);
                    break;
                }
                case "Продать":
                {
                    if (sellOffer != null)
                    {
                        goto SomethingWrong;
                    }

                    var state = new AddOfferState
                    {
                        Selling = true,
                        SelectedItemId = item.Identifier,
                        MaxQuantityAvailable = user.ItemManager.Get(item.Identifier)?.Count ?? 0
                    };
                    Room.GetRoomVariables(user).Set("state", StateContainer.Serialize(state));

                    Room.SwitchAction<AuctionRoom.PriceGroupSelectionAction>(user);
                    Room.GetAction<AuctionRoom.PriceGroupSelectionAction>().Enter(user);
                    break;
                }
                default:
                {
                    goto SomethingWrong;
                }
            }

            return;
            SomethingWrong:
            Enter(user);
        }

        [Button("Назад")]
        public void Back(User user, RecivedMessage message)
        {
            Room.SwitchAction<AuctionRoom.MyOffersAction>(user);
            Room.GetAction<AuctionRoom.MyOffersAction>().Enter(user);
        }
    }
}