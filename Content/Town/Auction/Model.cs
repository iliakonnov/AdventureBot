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
    }

    public class ItemOffer
    {
        public List<Offer> SellOffers;
        public List<Offer> BuyOffers;

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
                .ToList();
        }
    }

    public class Offer
    {
        public UserId UserId;
        public decimal Price;

        public Offer(UserId userId, decimal price)
        {
            UserId = userId;
            Price = price;
        }

        public VariableContainer Serialize()
        {
            var result = new VariableContainer();
            result.Set("UserId", UserId);
            result.Set("Price", new Serializable.Decimal(Price));
            return result;
        }

        public static Offer Deserialize(VariableContainer container)
        {
            return new Offer(
                (UserId) container.Get("UserId"),
                container.Get<Serializable.Decimal>("Price")
            );
        }
    }
}