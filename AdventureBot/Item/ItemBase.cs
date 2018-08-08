using AdventureBot.User.Stats;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot.Item
{
    public enum BuyGroup
    {
        Market,
        Guild,
        Gym,
        Merchant
    }

    [PublicAPI]
    [Union(0, typeof(ItemInfo))]
    public interface IItem
    {
        decimal? Price { get; }
        [NotNull] StructFlag<BuyGroup> Group { get; }

        string Name { get; }
        string Description { get; }

        [NotNull] string Identifier { get; }
        [CanBeNull] StatsEffect Effect { get; }

        void OnUse(User.User user, ItemInfo info);

        bool CanUse(User.User user, ItemInfo info);

        void OnMessage(User.User user, ItemInfo info);

        void OnEnter(User.User user, ItemInfo info);

        void OnLeave(User.User user, ItemInfo info);

        void OnAdd(User.User user, ItemInfo info, int count);

        void OnRemove(User.User user, ItemInfo info, int count);
    }

    public abstract class ItemBase : IItem
    {
        public abstract string Identifier { get; }
        public abstract StatsEffect Effect { get; }

        public abstract bool CanUse(User.User user, ItemInfo info);

        public virtual void OnUse(User.User user, ItemInfo info)
        {
        }

        public virtual void OnMessage(User.User user, ItemInfo info)
        {
        }

        public virtual void OnEnter(User.User user, ItemInfo info)
        {
        }

        public virtual void OnLeave(User.User user, ItemInfo info)
        {
        }

        public virtual void OnAdd(User.User user, ItemInfo info, int count)
        {
        }

        public virtual void OnRemove(User.User user, ItemInfo info, int count)
        {
        }


        public abstract string Name { get; }
        public abstract string Description { get; }
        public abstract decimal? Price { get; }
        public abstract StructFlag<BuyGroup> Group { get; }

        protected VariableContainer GetItemVariables(User.User user)
        {
            return user.VariableManager.GetItemVariables(Identifier);
        }
    }
}