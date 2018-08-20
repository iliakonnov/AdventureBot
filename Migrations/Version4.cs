using System;
using AdventureBot.UserManager;

namespace Migrations
{
    [Migrator(4)]
    public class Version4 : IMigrator
    {
        private static readonly Random NamesRandom = new Random();

        public dynamic Migrate(dynamic user)
        {
            user["RoomManager"]["CurrentRootId"] = "root/town";
            return user;
        }
    }
}