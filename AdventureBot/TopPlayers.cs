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
        Gold,
        Level
    }

    public class TopPlayers : Singleton<TopPlayers>
    {
        private const decimal LevelMultiplier = 1000000000000000000000M;

        private Dictionary<TopParam, SortedByValueDictionary<UserId, decimal>> _top;

        public IReadOnlyDictionary<TopParam, IReadOnlyList<KeyValuePair<UserId, decimal>>> Top => _top.ToDictionary(
            keyValue => keyValue.Key,
            keyValue => keyValue.Value.Sorted
        );

        internal void Initialize()
        {
            _top = new Dictionary<TopParam, SortedByValueDictionary<UserId, decimal>>
            {
                {TopParam.Gold, new SortedByValueDictionary<UserId, decimal>()},
                {TopParam.Monsters, new SortedByValueDictionary<UserId, decimal>()},
                {TopParam.Rooms, new SortedByValueDictionary<UserId, decimal>()},
                {TopParam.Level, new SortedByValueDictionary<UserId, decimal>()}
            };
            foreach (var userId in DatabaseConnection.GetUsersList())
            {
                var user = UserProxy.GetUnsafe(userId);
                _top[TopParam.Gold].Add(userId, user.Info.Gold);
                _top[TopParam.Monsters].Add(userId, user.Info.Statistics.MonsterCount);
                _top[TopParam.Rooms].Add(userId, user.Info.Statistics.RoomsCount);
                _top[TopParam.Level].Add(userId, PackLevel(user.Info.Level.Level, user.Info.Level.ExpirenceCollected));
            }

            UserLevel.OnChanged += (user, level) =>
            {
                _top[TopParam.Level].Add(user.Info.UserId,
                    PackLevel(user.Info.Level.Level, user.Info.Level.ExpirenceCollected));
            };

            Statistics.OnChanged += user =>
            {
                _top[TopParam.Gold].Add(user.Info.UserId, user.Info.Gold);
                _top[TopParam.Monsters].Add(user.Info.UserId, user.Info.Statistics.MonsterCount);
                _top[TopParam.Rooms].Add(user.Info.UserId, user.Info.Statistics.RoomsCount);
            };
        }

        public static (int, decimal) UnpackLevel(decimal number)
        {
            var lvl = (int) (number / LevelMultiplier);
            var exp = number % LevelMultiplier;
            return (lvl, exp);
        }

        private static decimal PackLevel(int level, decimal exp)
        {
            // Based on experience formula at 2ac128090d2f8d61002cb668e20817d62119e03a: 4 * lvl ** 3 / 5
            // Works for levels up to 10 772 173
            // 10 772 173 lvl      =  999999874632709393373.6 exp, so multiply level by
            // 10^int(log10(exp)+1)= 1000000000000000000000
            // And 10 772 173 * 1000000000000000000000 + 999999874632709393373.6 is max possible decimal (lvl + 1 will overflow)

            if (level > 10_772_173)
            {
                return decimal.MaxValue;
            }

            return level * LevelMultiplier + exp;
        }
    }
}