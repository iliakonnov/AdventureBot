using System;
using System.Collections.Generic;
using AdventureBot.UserManager;

namespace Migrations
{
    [Migrator(3)]
    public class Version3 : IMigrator
    {
        private static readonly Random NamesRandom = new Random();
        
        public dynamic Migrate(dynamic user)
        {
            user["Info"]["Level"] = new Dictionary<object, object>
            {
                {"Level", 0},
                {"ExpirenceRequired", 0M},
                {"ExpirenceCollected", 0M}
            };
            return user;
        }
    }
}