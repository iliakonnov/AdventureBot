using AdventureBot.ObjectManager;

namespace AdventureBot.UserManager
{
    public class MigratorAttribute : IdentifiableAttribute
    {
        public MigratorAttribute(int version) : base(version.ToString())
        {
        }
    }

    public interface IMigrator
    {
        dynamic Migrate(dynamic user);
    }

    public class MigratorManager : StorageManager<IMigrator, MigratorAttribute>
    {
    }
}