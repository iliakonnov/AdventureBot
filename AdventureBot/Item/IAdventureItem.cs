namespace AdventureBot.Item;

public interface IAdventureItem : IItem
{
    void OnAdventureEnter(User.User user, ItemInfo info);
    void OnAdventureLeave(User.User user, ItemInfo info);
}