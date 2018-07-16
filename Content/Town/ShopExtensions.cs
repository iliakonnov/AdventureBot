using AdventureBot.Item;
using AdventureBot.User;

namespace Content.Town
{
    public static class ShopExtensions
    {
        public static bool BuyItem(this User user, ItemInfo item)
        {
            if (item.Item.Price == null) return false;

            var price = (decimal) item.Item.Price * item.Count;

            if (user.Info.TryDecreaseGold(price))
            {
                user.ItemManager.Add(item);
                return true;
            }

            return false;
        }

        public static bool SellItem(this User user, ItemInfo item)
        {
            if (item.Item.Price == null) return false;

            var price = (decimal) item.Item.Price * item.Count * user.Info.SellMultiplier;

            if (user.ItemManager.Remove(item))
            {
                user.Info.Gold += price;
                return true;
            }

            return false;
        }
    }
}