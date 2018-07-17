using System;
using System.Collections.Generic;
using AdventureBot.Analysis;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.Room;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot.User
{
    [MessagePackObject(true)]
    public class RoomManager
    {
        [IgnoreMember] internal User _user;

        [Obsolete("This constructor for serializer only")]
        [UsedImplicitly]
        [SerializationConstructor]
        public RoomManager(StackedRoom currentRoom, Stack<StackedRoom> rooms)
        {
            CurrentRoom = currentRoom;
            Rooms = rooms;
        }

        public RoomManager(User user)
        {
            _user = user;
        }

        [CanBeNull] internal StackedRoom CurrentRoom { get; set; }
        internal Stack<StackedRoom> Rooms { get; } = new Stack<StackedRoom>();

        internal void Go(string roomIdentifier, bool leave = true)
        {
            if (!ObjectManager<IRoom>.Instance.Get<Room.RoomManager>().Contains(roomIdentifier))
            {
                throw new ArgumentException($"Unknown room: {roomIdentifier}");
            }

            if (leave)
            {
                var allowLeave = GetRoom()?.OnLeave(_user);
                if (allowLeave == false)
                {
                    return;
                }
            }

            if (CurrentRoom != null)
            {
                Rooms.Push(CurrentRoom);
            }

            CurrentRoom = new StackedRoom(roomIdentifier);
            _user.MessageManager.ShownStats = ShownStats.Default;
            Events.Go(_user, roomIdentifier);
            GetRoom()?.OnEnter(_user);
            _user.ItemManager.OnEnter();
        }

        /// <summary>
        ///     Переходит в указанную комнату
        /// </summary>
        /// <param name="roomIdentifier"></param>
        public void Go(string roomIdentifier)
        {
            Go(roomIdentifier, true);
        }

        internal void Leave(bool doReturn = true)
        {
            var allowLeave = GetRoom()?.OnLeave(_user);
            if (allowLeave == false)
            {
                return;
            }

            CurrentRoom = Rooms.Pop();
            _user.MessageManager.ShownStats = CurrentRoom?.ShownStats ?? ShownStats.Default;

            _user.ItemManager.OnLeave();

            if (doReturn)
            {
                GetRoom()?.OnReturn(_user);
            }
        }

        /// <summary>
        ///     Покидает текущую комнату
        /// </summary>
        public void Leave()
        {
            var allowLeave = GetRoom()?.OnLeave(_user);
            if (allowLeave == false)
            {
                return;
            }

            CurrentRoom = Rooms.Pop();
            _user.MessageManager.ShownStats = CurrentRoom.ShownStats;
            GetRoom()?.OnReturn(_user);
        }

        /// <summary>
        ///     Загружает и возвращает комнату, в которой пользователь находится на данный момент.
        ///     Может вернуть null, если не удалось загрузить комнату или пользователь нигде не находится.
        /// </summary>
        [CanBeNull]
        public IRoom GetRoom()
        {
            if (CurrentRoom == null)
            {
                return null;
            }

            return ObjectManager<IRoom>.Instance.Get<Room.RoomManager>().Get(CurrentRoom.Identifier);
        }

        /// <summary>
        ///     Комната, которую пользователь прошел на пути к текущей комнате
        /// </summary>
        [MessagePackObject(true)]
        public class StackedRoom
        {
            public readonly string Identifier;
            public readonly ShownStats ShownStats;
            public SentMessage LastMessage;

            [SerializationConstructor]
            public StackedRoom(string identifier, ShownStats shownStats, SentMessage lastMessage)
            {
                Identifier = identifier;
                ShownStats = shownStats;
                LastMessage = lastMessage;
            }

            public StackedRoom(string identifier)
            {
                Identifier = identifier;
                ShownStats = ShownStats.Default;
                LastMessage = null;
            }
        }
    }
}