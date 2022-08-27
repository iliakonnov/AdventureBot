using System;
using AdventureBot.UserManager;

namespace Migrations;

[Migrator(6)]
public class Version6 : IMigrator
{
    public dynamic Migrate(dynamic user)
    {
        user["MessageManager"]["LastMessageRecived"] = DateTime.MinValue;
        return user;
    }
}