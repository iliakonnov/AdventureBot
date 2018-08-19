using System.Collections.Generic;
using System.Linq;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.User;
using ItemManager = AdventureBot.Item.ItemManager;

namespace Content.Town
{
    public static class ShopExtensions
    {
        public static bool BuyItem(this User user, ItemInfo item)
        {
            if (item.Item.Price == null)
            {
                return false;
            }

            var price = (decimal) item.Item.Price * item.Count;

            if (!user.Info.TryDecreaseGold(price))
            {
                return false;
            }

            user.ItemManager.Add(item);
            return true;
        }

        public static bool SellItem(this User user, ItemInfo item)
        {
            if (item.Item.Price == null)
            {
                return false;
            }

            var price = (decimal) item.Item.Price * item.Count * user.Info.SellMultiplier;

            if (!user.ItemManager.Remove(item))
            {
                return false;
            }

            user.Info.Gold += price;
            return true;
        }

        public static List<IItem> AvailableToBuy(this ItemManager manager, StructFlag<BuyGroup> filter)
        {
            return manager.Keys()
                .Select(manager.Get)
                .Where(item => item?.Price != null && item.Group.Intersects(filter))
                .ToList();
        }

        public static List<ItemInfo> AvailableToSell(this IEnumerable<ItemInfo> items, StructFlag<BuyGroup> filter)
        {
            return items
                .Where(item => item.Item.Price != null && item.Item.Group.Intersects(filter))
                .ToList();
        }
        
        public static List<ItemInfo> AvailableToSell(this IEnumerable<ItemInfo> items)
        {
            return items
                .Where(item => item.Item.Price != null)
                .ToList();
        }
    }
}