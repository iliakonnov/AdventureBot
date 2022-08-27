using System;
using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Quest;
using AdventureBot.UserManager;

namespace Migrations;

[Migrator(1)]
public class Version1 : IMigrator
{
    public dynamic Migrate(dynamic user)
    {
        user["QuestManager"] = new Dictionary<object, object>
        {
            {"quests", new Dictionary<string, Dictionary<Guid, QuestInfo>>()}
        };
        user["VariableManager"]["QuestVariables"] = new Dictionary<string, Dictionary<Guid, VariableContainer>>();
        return user;
    }
}