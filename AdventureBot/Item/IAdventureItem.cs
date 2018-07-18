namespace AdventureBot.Item
{
    public interface IAdventureItem : IItem
    {
        void OnAdventureEnter();
        void OnAdventureLeave();
    }
}