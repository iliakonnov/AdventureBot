using AdventureBot.UserManager;

namespace Migrations;

[Migrator(5)]
public class Version5 : IMigrator
{
    public dynamic Migrate(dynamic user)
    {
        user["Info"]["Gold"] = user["Info"]["_gold"];
        return user;
    }
}