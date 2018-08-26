using System;
using System.Diagnostics;
using System.IO;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using MessagePack;
using MessagePack.ImmutableCollection;
using MessagePack.Resolvers;
using NLog;

namespace AdventureBot.UserManager
{
    public class UserData
    {
        private const int LastVersion = 6;

        private static readonly Logger Logger = LogManager.GetCurrentClassLogger();

        static UserData()
        {
            CompositeResolver.RegisterAndSetAsDefault(
                ImmutableCollectionResolver.Instance,
                StandardResolverAllowPrivate.Instance
            );
        }

        public UserData(UserId id, byte[] data, DatabaseVariables variables, int version)
        {
            Data = data;
            Id = id;
            Variables = variables;
            Version = version;
        }

        public UserData(UserId id)
        {
            Data = null;
            Id = id;
            Version = LastVersion;
        }

        public byte[] Data { get; }
        public UserId Id { get; }
        public int Version { get; }
        public DatabaseVariables Variables { get; }

        public static UserData Serialize(User.User user)
        {
            return new UserData(
                user.Info.UserId,
                MessagePackSerializer.Serialize(user),
                user.DatabaseVariables,
                LastVersion);
        }

        public User.User Deserialize()
        {
            if (Data == null)
            {
                return new User.User(Id);
            }

            try
            {
                User.User result;
                if (Version == LastVersion)
                {
                    result = MessagePackSerializer.Deserialize<User.User>(Data);
                    result.DatabaseVariables.Fill(Variables);
                    return result;
                }

                var user = MessagePackSerializer.Deserialize<dynamic>(Data);
                var migrated = Migrate(user);
                result = MessagePackSerializer.Deserialize<User.User>(MessagePackSerializer.Serialize(migrated));
                result.DatabaseVariables.Fill(Variables);
                return result;
            }
            catch (Exception e)
            {
                var filename = $"{Id.Messenger}_{Id.Id}.userdump";
                File.WriteAllBytes(filename, Data);
                Logger.Error(e, "Cannot deserialize user {userId}. Dump saved to {filename}", Id, filename);
            }

            return new User.User(Id);
        }

        private dynamic Migrate(dynamic user)
        {
            var version = Version;
            while (version != LastVersion)
            {
                var migrator = ObjectManager<IMigrator>.Instance.Get<MigratorManager>().Get(version.ToString());
                Debug.Assert(migrator != null, nameof(migrator) + " != null");
                user = migrator.Migrate(user);
                version++;
            }

            return user;
        }
    }
}