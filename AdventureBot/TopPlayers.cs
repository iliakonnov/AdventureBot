using System.Collections.Generic;
using System.Linq;
using AdventureBot.User.Stats;
using AdventureBot.UserManager;

namespace AdventureBot
{
    public enum TopParam
    {
        Rooms,
        Monsters,
        Gold
    }

    public class TopPlayers : Singleton<TopPlayers>
    {
        public IReadOnlyDictionary<TopParam, IReadOnlyList<KeyValuePair<decimal, UserId>>> Top => _top.ToDictionary(
            keyValue => keyValue.Key,
            keyValue => keyValue.Value.Sorted
        );
        private Dictionary<TopParam, SortedByValueDictionary<UserId, decimal>> _top;

        internal void Initialize()
        {
            _top = new Dictionary<TopParam, SortedByValueDictionary<UserId, decimal>>
            {
                {TopParam.Gold, new SortedByValueDictionary<UserId, decimal>()},
                {TopParam.Monsters, new SortedByValueDictionary<UserId, decimal>()},
                {TopParam.Rooms, new SortedByValueDictionary<UserId, decimal>()}
            };
            foreach (var userId in DatabaseConnection.GetUsersList())
            {
                var user = UserProxy.GetUnsafe(userId);
                _top[TopParam.Gold].Add(userId, user.Info.Gold);
                _top[TopParam.Monsters].Add(userId, user.Info.Statistics.MonsterCount);
                _top[TopParam.Rooms].Add(userId, user.Info.Statistics.RoomsCount);
            }

            Statistics.OnChanged += user =>
            {
                _top[TopParam.Gold].Add(user.Info.UserId, user.Info.Gold);
                _top[TopParam.Monsters].Add(user.Info.UserId, user.Info.Statistics.MonsterCount);
                _top[TopParam.Rooms].Add(user.Info.UserId, user.Info.Statistics.RoomsCount);
            };
        }
    }
}
