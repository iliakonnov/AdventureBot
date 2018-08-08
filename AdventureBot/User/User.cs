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
        [IgnoreMember] public readonly Random Random = new Random();

        [Obsolete("This constructor for serializer only")]
        [UsedImplicitly]
        [SerializationConstructor]
        public User(ItemManager itemManager, ActiveItemsManager activeItemsManager, UserInfo info,
            VariableManager variableManager, RoomManager roomManager, MessageManager messageManager, Guid token,
            Tuple<UserId, Guid> linkedTo)
        {
            ItemManager = itemManager;
            ItemManager.User = this;

            ActiveItemsManager = activeItemsManager;
            ActiveItemsManager.User = this;

            RoomManager = roomManager;
            RoomManager.User = this;

            Info = info;
            Info.User = this;

            MessageManager = messageManager;
            MessageManager.User = this;

            VariableManager = variableManager;

            Token = token;
            LinkedTo = linkedTo;
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

        public Guid Token { get; set; } = Guid.Empty;
        internal Tuple<UserId, Guid> LinkedTo { get; set; }

        private void Reset(UserId userId)
        {
            ActiveItemsManager = new ActiveItemsManager(this);
            Info = new UserInfo(userId, this);
            ItemManager = new ItemManager(this);
            RoomManager = new RoomManager(this);
            MessageManager = new MessageManager(this);

            if (VariableManager != null)
            {
                VariableManager.Reset();
            }
            else
            {
                VariableManager = new VariableManager();
            }

            if (Token == Guid.Empty)
            {
                Token = Guid.NewGuid();
            }

            Events.Reset(this);
        }

        internal void Reset()
        {
            Reset(Info.UserId);
        }
    }
}