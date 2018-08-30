using System;
using System.Collections.Generic;
using System.Linq;
using AdventureBot;

namespace Content.Town.Auction
{
    public class Offers : Dictionary<string, ItemOffer>
    {
        public VariableContainer Serialize()
        {
            var result = new VariableContainer();
            foreach (var offer in this)
            {
                result.Set(offer.Key, offer.Value.Serialize());
            }

            return result;
        }

        public static Offers Deserialize(VariableContainer items)
        {
            var result = new Offers();
            foreach (var key in items.Keys())
            {
                var offer = items.Get<VariableContainer>(key);
                result[key] = ItemOffer.Deserialize(offer);
            }

            return result;
        }

        public void Save()
        {
            lock (GlobalVariables.Variables)
            {
                GlobalVariables.Variables.Set("auction.offers", Serialize());
            }
        }

        public static Offers Load()
        {
            lock (GlobalVariables.Variables)
            {
                return Deserialize(GlobalVariables.Variables.Get<VariableContainer>("auction.offers"));
            }
        }
    }

    public class ItemOffer
    {
        public List<Offer> BuyOffers;
        public List<Offer> SellOffers;

        public ItemOffer(List<Offer> sellOffers, List<Offer> buyOffers)
        {
            SellOffers = sellOffers;
            BuyOffers = buyOffers;
        }

        public VariableContainer Serialize()
        {
            var result = new VariableContainer();
            result.Set("sell", SerializeMany(SellOffers));
            result.Set("buy", SerializeMany(BuyOffers));
            return result;
        }

        private SerializableList SerializeMany(IEnumerable<Offer> offers)
        {
            return new SerializableList(
                offers
                    .Where(offer => offer.Count != 0)
                    .Select(offer => offer.Serialize())
                    .Cast<ISerializable>()
                    .ToList()
            );
        }

        public static ItemOffer Deserialize(VariableContainer container)
        {
            return new ItemOffer(
                DeserializeMany(container.Get<SerializableList>("sell")),
                DeserializeMany(container.Get<SerializableList>("buy"))
            );
        }

        private static List<Offer> DeserializeMany(SerializableList list)
        {
            return list
                .Cast<VariableContainer>()
                .Select(Offer.Deserialize)
                .Where(offer => offer.Count != 0)
                .ToList();
        }
    }

    public class Offer
    {
        public int Count;
        public DateTimeOffset Created;
        public string ItemId;
        public decimal Price;
        public UserId UserId;

        public Offer(UserId userId, decimal price, int count, DateTimeOffset created, string itemId)
        {
            UserId = userId;
            Price = price;
            Count = count;
            Created = created;
            ItemId = itemId;
        }

        public VariableContainer Serialize()
        {
            var result = new VariableContainer();
            result.Set("UserId", UserId);
            result.Set("Price", new Serializable.Decimal(Price));
            result.Set("Count", new Serializable.Int(Count));
            result.Set("Created", new Serializable.Decimal(Created.ToUnixTimeSeconds()));
            result.Set("ItemId", new Serializable.String(ItemId));
            return result;
        }

        public static Offer Deserialize(VariableContainer container)
        {
            return new Offer(
                (UserId) container.Get("UserId"),
                container.Get<Serializable.Decimal>("Price"),
                container.Get<Serializable.Int>("Count"),
                DateTimeOffset.FromUnixTimeSeconds(container.Get<Serializable.Long>("Created")),
                container.Get<Serializable.String>("ItemId")
            );
        }
    }
}