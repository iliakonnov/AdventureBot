using System;
using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Quest;
using AdventureBot.UserManager;

namespace Migrations
{
    [Migrator(2)]
    public class Version2 : IMigrator
    {
        private static readonly Random NamesRandom = new Random();
        
        public dynamic Migrate(dynamic user)
        {
            user["Info"]["Name"] = AdventureBot.NameGenerator.Generator.Generate(NamesRandom);
            user["Info"]["Statistics"] = new Dictionary<object, object>();
            user["Info"]["_gold"] = user["Info"]["Gold"];
            return user;
        }
    }
}