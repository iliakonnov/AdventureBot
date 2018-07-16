using System;
using AdventureBot.ObjectManager;
using AdventureBot.User.Stats;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot.Item
{
    [MessagePackObject(keyAsPropertyName: true)]
    public class ItemInfo : ISerializable
    {
        public int Count { get; internal set; }
        public string Identifier { get; }
        [IgnoreMember] public IItem Item { get; }

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
            Item = ObjectManager<IItem>.Instance.Get<ItemManager>().Get(identifier);
        }
        
        public ItemInfo(IItem item, int count)
        {
            Count = count;
            Item = item;
            Identifier = item.Identifier;
        }

        public bool CanUse(User.User user)
        {
            return Item.CanUse(user, this);
        }
        
        public void OnUse(User.User user)
        {
            Item.OnUse(user, this);
        }

        public ItemInfo Clone()
        {
            return new ItemInfo(Item, Count);
        }
    }
}