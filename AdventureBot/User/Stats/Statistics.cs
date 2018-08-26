using System;
using AdventureBot.Room;
using MessagePack;

namespace AdventureBot.User.Stats
{
    [MessagePackObject(true)]
    public class Statistics
    {
        [IgnoreMember] internal User User;

        static Statistics()
        {
            MonsterBase.OnKilled += (user, monster) => user.Info.Statistics.MonsterKilled();
        }

        [Obsolete("This constructor is for serializer only")]
        [SerializationConstructor]
        public Statistics()
        {
        }

        public Statistics(User user)
        {
            User = user;
        }

        public int MonsterCount
        {
            get => User.DatabaseVariables.Monsters;
            private set
            {
                if (User != null) User.DatabaseVariables.Monsters = value;
            }
        }

        public int RoomsCount
        {
            get => User.DatabaseVariables.Rooms;
            private set
            {
                if (User != null) User.DatabaseVariables.Rooms = value;
            }
        }

        public static event GameEventHandler OnChanged;

        public void RoomTraveled()
        {
            RoomsCount += 1;
            OnChanged?.Invoke(User);
        }

        private void MonsterKilled()
        {
            MonsterCount += 1;
            OnChanged?.Invoke(User);
        }

        internal void GoldChanged()
        {
            OnChanged?.Invoke(User);
        }
    }
}