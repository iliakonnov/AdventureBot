﻿using System;
using System.Collections.Generic;
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
        private string _currentRootId;
        [IgnoreMember] internal User User;

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
            User = user;
        }

        [CanBeNull] internal StackedRoom CurrentRoom { get; set; }
        internal Stack<StackedRoom> Rooms { get; } = new Stack<StackedRoom>();

        [IgnoreMember]
        public string CurrentRootRoom =>
            ObjectManager<IRoot>.Instance.Get<RootManager>().Get(_currentRootId)?.RootRoomId;

        public static event GameEventHandler<string> OnEnter;
        public static event GameEventHandler OnLeave;

        /// <summary>
        ///     Переходит в указанную комнату
        /// </summary>
        /// <param name="roomIdentifier"></param>
        public void Go(string roomIdentifier, bool leave = true)
        {
            if (!ObjectManager<IRoom>.Instance.Get<Room.RoomManager>().Contains(roomIdentifier))
            {
                throw new ArgumentException($"Unknown room: {roomIdentifier}");
            }

            if (leave)
            {
                var allowLeave = GetRoom()?.OnLeave(User);
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
            User.MessageManager.ShownStats = ShownStats.Default;

            GetRoom()?.OnEnter(User);
            OnEnter?.Invoke(User, roomIdentifier);
        }

        /// <summary>
        ///     Покидает текущую комнату
        /// </summary>
        public void Leave(bool doReturn = true, bool checkLeave = true)
        {
            if (checkLeave)
            {
                var allowLeave = GetRoom()?.OnLeave(User);
                if (allowLeave == false)
                {
                    return;
                }
            }

            if (Rooms.Count != 0)
            {
                CurrentRoom = Rooms.Pop();
                User.MessageManager.ShownStats = CurrentRoom?.ShownStats ?? ShownStats.Default;
            }
            else
            {
                CurrentRoom = null;
            }

            OnLeave?.Invoke(User);

            if (doReturn)
            {
                GetRoom()?.OnReturn(User);
            }
        }

        public void ChangeRoot(string rootIdentifier)
        {
            var root = ObjectManager<IRoot>.Instance.Get<RootManager>().Get(rootIdentifier);
            if (root == null)
            {
                throw new ArgumentException($"Cannot find root '{rootIdentifier}'");
            }

            _currentRootId = rootIdentifier;

            while ((User.RoomManager.CurrentRoom?.Identifier ?? "_root") != "_root")
            {
                // Leaving all rooms until root, without calling OnLeave and OnReturn
                User.RoomManager.Leave(false, false);
            }

            // Now we need to enter root to send message and update buttons
            User.RoomManager.Go(root.RootRoomId, false);
        }

        /// <summary>
        ///     Загружает и возвращает комнату, в которой пользователь находится на данный момент.
        ///     Может вернуть null, если не удалось загрузить комнату или пользователь нигде не находится.
        /// </summary>
        [CanBeNull]
        public IRoom GetRoom()
        {
            return CurrentRoom == null
                ? null
                : ObjectManager<IRoom>.Instance.Get<Room.RoomManager>().Get(CurrentRoom.Identifier);
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