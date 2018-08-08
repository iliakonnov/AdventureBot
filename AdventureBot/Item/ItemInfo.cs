using System;
using AdventureBot.ObjectManager;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot.Item
{
    [MessagePackObject(true)]
    public class ItemInfo : ISerializable
    {
        public ItemInfo(IItem item)
        {
            Count = 1;
            Item = item;
            Identifier = item.Identifier;
        }

        [SerializationConstructor]
        public ItemInfo(string identifier, int count)
        {
            Identifier = identifier;
            Count = count;
            var item = ObjectManager<IItem>.Instance.Get<ItemManager>().Get(identifier);

            Item = item ?? throw new ArgumentException($"Item with identifier '{identifier}' not found!");
        }

        public ItemInfo(IItem item, int count)
        {
            Count = count;
            Item = item;
            Identifier = item.Identifier;
        }

        public int Count { get; internal set; }
        public string Identifier { get; }
        [IgnoreMember] [NotNull] public IItem Item { get; }

        public bool CanUse(User.User user)
        {
            return Item.CanUse(user, this);
        }

        public void OnUse(User.User user)
        {
            Item.OnUse(user, this);
        }
    }
}