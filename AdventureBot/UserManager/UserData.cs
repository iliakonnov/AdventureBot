using System;
using System.Diagnostics;
using System.IO;
using AdventureBot.ObjectManager;
using MessagePack;
using MessagePack.ImmutableCollection;
using MessagePack.Resolvers;
using NLog;

namespace AdventureBot.UserManager
{
    public class UserData
    {
        public const int LastVersion = 4;

        private static readonly Logger Logger = LogManager.GetCurrentClassLogger();

        static UserData()
        {
            CompositeResolver.RegisterAndSetAsDefault(
                ImmutableCollectionResolver.Instance,
                StandardResolverAllowPrivate.Instance
            );
        }

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
                    var test = MessagePackSerializer.Deserialize<dynamic>(MessagePackSerializer.Serialize(new User.User(new UserId(0,0))));
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