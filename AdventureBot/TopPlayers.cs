using System;
using System.Collections.Generic;
using System.Data.Common;
using System.Linq;
using AdventureBot.User;
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

    public static class TopPlayers
    {
        public static IEnumerable<(UserId, DatabaseVariables)> GetTop(TopParam param, int count)
        {
            var order = new List<(DbColumnAttribute, bool)>();
            switch (param)
            {
                case TopParam.Rooms:
                    order.Add((DatabaseVariables.GetColumn(x => x.Rooms), false));
                    break;
                case TopParam.Monsters:
                    order.Add((DatabaseVariables.GetColumn(x => x.Monsters), false));
                    break;
                case TopParam.Gold:
                    order.Add((DatabaseVariables.GetColumn(x => x.Gold), false));
                    break;
                case TopParam.Level:
                    order.Add((DatabaseVariables.GetColumn(x => x.Level), false));
                    order.Add((DatabaseVariables.GetColumn(x => x.Experience), false));
                    break;
                default:
                    throw new ArgumentOutOfRangeException(nameof(param), param, null);
            }

            var users = DatabaseConnection.QueryUsers(order, null, count);
            foreach (var userData in users)
            {
                yield return (userData.Id, userData.Variables);
            }
        }
    }
}