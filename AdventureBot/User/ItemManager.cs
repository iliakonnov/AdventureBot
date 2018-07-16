using System;
using System.Collections.Generic;
using System.Linq;
using AdventureBot.Item;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot.User
{
    [MessagePackObject]
    public class ItemManager
    {
        [IgnoreMember] internal User _user;
        [IgnoreMember] public IReadOnlyList<ItemInfo> Items => _items;
        [Key("Items")] private readonly List<ItemInfo> _items = new List<ItemInfo>()
        {
            new ItemInfo(new Hand()),
            new ItemInfo(new Wand())
        }; 

        [Obsolete("This constructor for serializer only")]
        [UsedImplicitly]
        [SerializationConstructor]
        public ItemManager(List<ItemInfo> items)
        {
            _items = items;
        }

        public ItemManager(User user)
        {
            _user = user;

            if (_user.Info.UserId.Messenger == -1)  // Testing messenger, empty initial _items
            {
                _items.Clear();
            }
        }

        /// <summary>
        /// Добавляет предмет в инвентарь пользователя.
        /// Автоматически перерасчитывает текущиие активные предметы
        /// </summary>
        public void Add(ItemInfo item)
        {
            var found = _items.FirstOrDefault(x => x.Identifier == item.Identifier);
            if (found != null)
            {
                found.Count += item.Count;
            }
            else
            {
                _items.Add(item);
            }

            _user.ActiveItemsManager.RecalculateActive();
        }

        /// <summary>
        /// Удаляет предмет из инвентаря пользователя.
        /// Автоматически перерасчитывает текущиие активные предметы
        /// </summary>
        /// <returns>Удалось ли удалить данный предмет</returns>
        public bool Remove(ItemInfo item)
        {
            var found = _items.FirstOrDefault(x => x.Identifier == item.Identifier);
            if (found == null)
            {
                // Item not found
                return false;
            }

            if (found.Count < item.Count)
            {
                // Cannot remove so many
                return false;
            }

            found.Count -= item.Count;
            if (found.Count == 0)
            {
                _items.Remove(found);
            }

            _user.ActiveItemsManager.RecalculateActive();

            return true;
        }
        
        /// <summary>
        /// Возвращает предмет из инвентаря пользователя
        /// </summary>
        [CanBeNull]
        public ItemInfo Get(string identifier)
        {
            return _items.FirstOrDefault(x => x.Identifier == identifier);
        }

        internal void OnMessage()
        {
            _items.ForEach(i => i.Item.OnMessage(_user, i));
        }
        
        internal void OnEnter()
        {
            _items.ForEach(i => i.Item.OnEnter(_user, i));
        }
        
        internal void OnLeave()
        {
            _items.ForEach(i => i.Item.OnLeave(_user, i));
        }
    }
}