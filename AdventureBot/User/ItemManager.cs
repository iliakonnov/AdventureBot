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
        [Key("Items")] private readonly List<ItemInfo> _items = new List<ItemInfo>
        {
            new ItemInfo(new Hand()),
            new ItemInfo(new Wand())
        };

        [IgnoreMember] internal User User;

        [Obsolete("This constructor for serializer only")]
        [UsedImplicitly]
        [SerializationConstructor]
        public ItemManager(List<ItemInfo> items)
        {
            _items = items.Where(info => info.Count != 0).ToList();
        }

        public ItemManager(User user)
        {
            User = user;

            if (User.Info.UserId.Messenger == -1) // Testing messenger, empty initial _items
            {
                _items.Clear();
            }
        }

        [IgnoreMember] public IReadOnlyList<ItemInfo> Items => _items.Where(info => info.Count != 0).ToList();

        /// <summary>
        ///     Добавляет предмет в инвентарь пользователя.
        ///     Автоматически перерасчитывает текущиие активные предметы
        /// </summary>
        public void Add(ItemInfo item)
        {
            var found = _items.FirstOrDefault(x => x.Identifier == item.Identifier);
            if (found != null)
            {
                found.Item.OnAdd(User, found, item.Count);
                found.Count += item.Count;
            }
            else
            {
                item.Item.OnAdd(User, item, item.Count);
                _items.Add(item);
            }

            User.ActiveItemsManager.RecalculateActive();
        }

        /// <summary>
        ///     Удаляет предмет из инвентаря пользователя.
        ///     Автоматически перерасчитывает текущиие активные предметы
        /// </summary>
        /// <returns>Удалось ли удалить данный предмет</returns>
        public bool Remove(ItemInfo item)
        {
            var found = _items.FirstOrDefault(x => x.Identifier == item.Identifier);
            if (found == null)
            {
                return false;
            }

            if (found.Count < item.Count)
            {
                return false;
            }

            found.Item.OnRemove(User, found, item.Count);
            found.Count -= item.Count;

            User.ActiveItemsManager.RecalculateActive();

            return true;
        }

        /// <summary>
        ///     Возвращает предмет из инвентаря пользователя
        /// </summary>
        [CanBeNull]
        public ItemInfo Get(string identifier)
        {
            return _items.FirstOrDefault(x => x.Identifier == identifier);
        }
    }
}