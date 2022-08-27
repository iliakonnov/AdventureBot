using AdventureBot.UserManager;

namespace Migrations;

[Migrator(7)]
public class Version7 : IMigrator
{
    public dynamic Migrate(dynamic user)
    {
        user["Info"]["_name"] = user["Info"]["Name"];
        return user;
    }
}