using AdventureBot.User;
using AdventureBot.User.Stats;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot.Item
{
    public enum BuyGroup
    {
        Market,
        Guild,
        Gym
    }

    /// <remarks>
    /// IItem must have parameterless constructor
    /// </remarks>
    [Union(0, typeof(ItemInfo))]
    public interface IItem
    {
        decimal? Price { get; set; }
        [NotNull] Flag<BuyGroup> Group { get; set; }

        string Name { get; set; }
        string Description { get; set; }

        [NotNull] string Identifier { get; set; }
        [CanBeNull] StatsEffect Effect { get; set; }

        void OnUse(User.User user, ItemInfo info);

        bool CanUse(User.User user, ItemInfo info);
        
        void OnMessage(User.User user, ItemInfo info);
        
        void OnEnter(User.User user, ItemInfo info);
        
        void OnLeave(User.User user, ItemInfo info);
    }

    public abstract class ItemBase<T> : IItem where T : ItemBase<T>, new()
    {
        public abstract string Identifier { get; set; }
        public abstract StatsEffect Effect { get; set; }
        public abstract void OnUse(User.User user, ItemInfo info);
        public abstract bool CanUse(User.User user, ItemInfo info);
        public abstract void OnMessage(User.User user, ItemInfo info);
        public abstract void OnEnter(User.User user, ItemInfo info);
        public abstract void OnLeave(User.User user, ItemInfo info);
        public abstract string Name { get; set; }
        public abstract string Description { get; set; }
        public abstract decimal? Price { get; set; }
        public abstract Flag<BuyGroup> Group { get; set; }

        public VariableContainer GetRoomVariables(User.User user)
        {
            return user.VariableManager.GetRoomVariables(Identifier);
        }
    }
}