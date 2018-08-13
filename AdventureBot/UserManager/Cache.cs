using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using MessagePack;
using MessagePack.ImmutableCollection;
using MessagePack.Resolvers;
using NLog;

namespace AdventureBot.UserManager
{
    public class Cache : Singleton<Cache>
    {
        private const int CacheSize = 100;
        private static readonly Logger Logger = LogManager.GetCurrentClassLogger();

        private readonly Dictionary<UserId, CachedUser> _cache = new Dictionary<UserId, CachedUser>();

        public Cache()
        {
            Flusher.Init();
            CompositeResolver.RegisterAndSetAsDefault(
                ImmutableCollectionResolver.Instance,
                StandardResolverAllowPrivate.Instance
            );
        }

        private User.User DeserializeUser(byte[] userdata, UserId id)
        {
            if (userdata != null)
            {
                try
                {
                    return MessagePackSerializer.Deserialize<User.User>(userdata);
                }
                catch (Exception e)
                {
                    var filename = $"{id.Messenger}_{id.Id}.userdump";
                    File.WriteAllBytes(filename, userdata);
                    Logger.Error(e, $"Cannot deserialize user {id}. Dump saved to {filename}");
                }
            }

            return new User.User(id);
        }

        public User.User Get(UserId id)
        {
            lock (_cache)
            {
                if (_cache.TryGetValue(id, out var user))
                {
                    user.LastRequested = DateTimeOffset.Now;
                    return DeserializeUser(user.UserData, id);
                }

                var cached = new CachedUser
                {
                    LastRequested = DateTimeOffset.Now,
                    UserData = DatabaseConnection.LoadUserData(id),
                    Flushed = true
                };
                _cache[id] = cached;

                return DeserializeUser(cached.UserData, id);
            }
        }

        public void Put(User.User user)
        {
            lock (_cache)
            {
                if (_cache.TryGetValue(user.Info.UserId, out var cached))
                {
                    cached.UserData = MessagePackSerializer.Serialize(user);
                    cached.Flushed = false;
                    return;
                }

                var cnt = 0;
                while (_cache.Count >= CacheSize)
                {
                    RemoveOldeset();
                    if (cnt++ > 5)
                    {
                        return;
                    }
                }

                _cache.Add(user.Info.UserId, new CachedUser
                {
                    UserData = MessagePackSerializer.Serialize(user),
                    Flushed = false
                });
            }
        }

        private void RemoveOldeset()
        {
            // _cache must be locked
            var lastRequested = DateTimeOffset.MaxValue;
            Tuple<UserId, byte[]> oldest = null;
            foreach (var kv in _cache)
            {
                if (oldest == null || kv.Value.LastRequested < lastRequested)
                {
                    lastRequested = kv.Value.LastRequested;
                    oldest = new Tuple<UserId, byte[]>(kv.Key, kv.Value.UserData);
                }
            }

            if (oldest == null)
            {
                // _cache is empty
                return;
            }

            DatabaseConnection.SaveUsers(new[] {oldest});
            _cache.Remove(oldest.Item1);
        }

        public void FlushAll()
        {
            lock (_cache)
            {
                var users = _cache
                    .Where(kv => !kv.Value.Flushed)
                    .ToList();
                DatabaseConnection.SaveUsers(users
                    .Select(kv => new Tuple<UserId, byte[]>(kv.Key, kv.Value.UserData))
                );
                users.ForEach(u => u.Value.Flushed = true);
            }
        }

        private class CachedUser
        {
            public bool Flushed;
            public byte[] UserData { get; set; }
            public DateTimeOffset LastRequested { get; set; }
        }
    }
}