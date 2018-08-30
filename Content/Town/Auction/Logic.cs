using System.Collections.Generic;
using System.Collections.ObjectModel;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.User;

namespace Content.Town.Auction
{
    public static class Logic
    {
        public static int Buy(List<Offer> offers, User buyer, int count)
        {
            var selectedOffers = new List<(Offer, int)>();
            var idx = 0;
            while (count > 0 && idx < offers.Count)
            {
                var offer = offers[idx++];
                var cnt = System.Math.Min(offer.Count, count);
                offer.Count -= cnt;
                selectedOffers.Add((offer, cnt));
                count -= cnt;
            }

            if (count != 0)
            {
                // Cannot buy everything
            }

            var result = 0;
            foreach (var (offer, cnt) in selectedOffers)
            {
                var price = offer.Price * cnt;
                if (!buyer.Info.TryDecreaseGold(price))
                {
                    return result;
                }

                using (var ctx = new UserContext(offer.UserId))
                {
                    ctx.User.Info.Gold += price;
                }

                buyer.ItemManager.Add(new ItemInfo(offer.ItemId, cnt));
                result += cnt;
            }

            return result;
        }
    }
}