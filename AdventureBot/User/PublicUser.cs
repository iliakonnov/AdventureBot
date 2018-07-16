using System;
using System.Runtime.CompilerServices;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot.User
{
    /// <summary>
    /// Общедоступная информация о пользователе. Не содержит какой-либо информации, которая может дать преимущество.
    /// </summary>
    [MessagePackObject(keyAsPropertyName: true)]
    public class PublicUser
    {
        [Obsolete("This constructor for serializer only")]
        [UsedImplicitly]
        [SerializationConstructor]
        public PublicUser()
        {
        }
        
        public PublicUser(User user)
        {
            Info = user.Info;
            ActiveItemsManager = user.ActiveItemsManager;
            ItemManager = user.ItemManager;
            RoomManager = user.RoomManager;
            MessageManager = user.MessageManager;
        }

        public UserInfo Info { get; internal set; }

        public ActiveItemsManager ActiveItemsManager { get; internal set; }

        public ItemManager ItemManager { get; internal set; }

        // Does not contain VariableManager

        public RoomManager RoomManager { get; internal set; }

        public MessageManager MessageManager { get; internal set; }
    }
}