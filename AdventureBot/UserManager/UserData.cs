using System;
using System.Diagnostics;
using System.IO;
using MessagePack;
using NLog;
using AdventureBot.ObjectManager;
using MessagePack.ImmutableCollection;
using MessagePack.Resolvers;

namespace AdventureBot.UserManager
{
    public class UserData
    {
        static UserData()
        {
            CompositeResolver.RegisterAndSetAsDefault(
                ImmutableCollectionResolver.Instance,
                StandardResolverAllowPrivate.Instance
            );
        }
        
        private static readonly Logger Logger = LogManager.GetCurrentClassLogger();
        public const int LastVersion = 1;

        public UserData(UserId id, byte[] data, int version)
        {
            Data = data;
            Id = id;
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

        public static UserData Serialize(User.User user)
        {
            return new UserData(user.Info.UserId, MessagePackSerializer.Serialize(user), LastVersion);
        }
        
        public User.User Deserialize()
        {
            if (Data != null)
            {
                try
                {
                    if (Version == LastVersion)
                    {
                        return MessagePackSerializer.Deserialize<User.User>(Data);
                    }
                    var user = MessagePackSerializer.Deserialize<dynamic>(Data);
                    var migrated = Migrate(user);
                    return MessagePackSerializer.Deserialize<User.User>(MessagePackSerializer.Serialize(migrated));
                }
                catch (Exception e)
                {
                    var filename = $"{Id.Messenger}_{Id.Id}.userdump";
                    File.WriteAllBytes(filename, Data);
                    Logger.Error(e, "Cannot deserialize user {userId}. Dump saved to {filename}", Id, filename);
                }
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