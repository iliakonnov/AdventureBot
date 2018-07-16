using System;
using AdventureBot.Analysis;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot.User
{
    [MessagePackObject(true)]
    public class User : ISerializable
    {
        /// <summary>
        ///     Генератор случайных чисел
        /// </summary>
        [IgnoreMember] public Random Random = new Random();

        [Obsolete("This constructor for serializer only")]
        [UsedImplicitly]
        [SerializationConstructor]
        public User(ItemManager itemManager, ActiveItemsManager activeItemsManager, UserInfo info,
            VariableManager variableManager, RoomManager roomManager, MessageManager messageManager)
        {
            ItemManager = itemManager;
            ItemManager._user = this;

            ActiveItemsManager = activeItemsManager;
            ActiveItemsManager._user = this;

            RoomManager = roomManager;
            RoomManager._user = this;

            Info = info;
            Info._user = this;

            MessageManager = messageManager;
            MessageManager._user = this;

            VariableManager = variableManager;
        }

        public User(UserId userId)
        {
            Reset(userId);
        }

        /// <summary>
        ///     Информация о пользователе и его характеристики
        /// </summary>
        public UserInfo Info { get; private set; }

        /// <summary>
        ///     Управление текущими активными предметами пользователя
        /// </summary>
        public ActiveItemsManager ActiveItemsManager { get; private set; }

        /// <summary>
        ///     Управление предметами пользователя
        /// </summary>
        public ItemManager ItemManager { get; private set; }

        /// <summary>
        ///     Хранилище переменных пользователя
        /// </summary>
        public VariableManager VariableManager { get; private set; }

        /// <summary>
        ///     Переход между комнатами
        /// </summary>
        public RoomManager RoomManager { get; private set; }

        public MessageManager MessageManager { get; private set; }

        [IgnoreMember] internal bool Unsafe { get; set; }

        private void Reset(UserId userId)
        {
            ActiveItemsManager = new ActiveItemsManager(this);
            Info = new UserInfo(userId, this);
            ItemManager = new ItemManager(this);
            RoomManager = new RoomManager(this);
            MessageManager = new MessageManager(this);

            if (VariableManager != null)
                VariableManager.Reset();
            else
                VariableManager = new VariableManager();

            Events.Reset(this);
        }

        internal void Reset()
        {
            Reset(Info.UserId);
        }
    }
}