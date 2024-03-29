﻿using System.Collections.Generic;
using System.Linq;
using System.Text;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;

namespace Content.Town.Auction;

public abstract class RemoveOfferActionBase : ActionBase<AuctionRoom>
{
    protected RemoveOfferActionBase(AuctionRoom room) : base(room)
    {
    }

    public void Enter(User user)
    {
        var buyOffers = Offers.Load()
            .SelectMany(kv => kv.Value.BuyOffers)
            .Where(offer => offer.UserId.Equals(user.Info.UserId));
        var sellOffers = Offers.Load()
            .SelectMany(kv => kv.Value.SellOffers)
            .Where(offer => offer.UserId.Equals(user.Info.UserId));

        var message = new StringBuilder();
        var buttons = new List<string>();
        var itemMgr = RoomBase.GetAllItems();

        foreach (var offer in buyOffers)
        {
            var item = itemMgr.Get(offer.ItemId);
            if (item == null)
            {
                continue;
            }

            message.AppendLine($"{item.Name}: беру {offer.Count} шт за {offer.Price.Format()} каждая");
            buttons.Add($"Покупаю {item.Name}");
        }

        foreach (var offer in sellOffers)
        {
            var item = itemMgr.Get(offer.ItemId);
            if (item == null)
            {
                continue;
            }

            message.AppendLine($"{item.Name}: продаю {offer.Count} шт за {offer.Price.Format()} каждая");
            buttons.Add($"Продаю {item.Name}");
        }

        Room.SendMessage(user, message.ToString(), buttons
            .Concat(new[] {"Назад"})
            .Select(msg => new[] {msg})
            .ToArray()
        );
    }

    [Fallback]
    public void OfferSelected(User user, ReceivedMessage message)
    {
        var splitted = message.Text.Split(' ');
        if (splitted.Length < 2)
        {
            Enter(user);
            return;
        }

        var action = splitted[0];
        var itemName = string.Join(" ", splitted.Skip(1));
        var itemMgr = RoomBase.GetAllItems();
        var item = itemMgr.Keys()
            .Select(key => itemMgr.Get(key))
            .SingleOrDefault(i => i?.Name == itemName);
        if (item == null)
        {
            goto SomethingWrong;
        }

        var offers = Offers.Load();
        if (!offers.TryGetValue(item.Identifier, out var itemOffers))
        {
            // No such item, so no offers to remove
            goto SomethingWrong;
        }

        Offer neededOffer;

        Offer Filter(IEnumerable<Offer> offr)
        {
            return offr
                .SingleOrDefault(offer =>
                    offer.UserId.Equals(user.Info.UserId)
                    && offer.ItemId == item.Identifier
                );
        }

        var selling = false;
        switch (action)
        {
            case "Покупаю":
            {
                neededOffer = Filter(itemOffers.BuyOffers);
                break;
            }
            case "Продаю":
            {
                neededOffer = Filter(itemOffers.SellOffers);
                selling = true;
                break;
            }
            default:
                goto SomethingWrong;
        }

        if (neededOffer == null)
        {
            goto SomethingWrong;
        }

        if (selling)
        {
            user.ItemManager.Add(new ItemInfo(neededOffer.ItemId, neededOffer.Count));
        }
        else
        {
            user.Info.Gold += neededOffer.Count * neededOffer.Price;
        }

        neededOffer.Count = 0;
        offers.Save();

        SomethingWrong:
        Enter(user);
    }

    [Button("Назад")]
    public void Back(User user, ReceivedMessage message)
    {
        Room.SwitchAction<AuctionRoom.MyOffersAction>(user);
        Room.GetAction<AuctionRoom.MyOffersAction>().Enter(user);
    }
}