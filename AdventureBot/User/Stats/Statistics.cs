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

        public int MonsterCount { get; private set; }
        public int RoomsCount { get; private set; }
        public static event GameEventHandler OnChanged;

        public void RoomTraveled()
        {
            RoomsCount += 1;
            OnChanged?.Invoke(User);
        }

        public void MonsterKilled()
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