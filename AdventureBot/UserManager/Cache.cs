using System;
using System.Collections.Generic;
using System.Linq;

namespace AdventureBot.UserManager
{
    public class Cache : Singleton<Cache>
    {
        private const int CacheSize = 100;

        private readonly Dictionary<UserId, CachedUser> _cache = new Dictionary<UserId, CachedUser>();

        public Cache()
        {
            Flusher.Init();
        }

        public User.User Get(UserId id)
        {
            lock (_cache)
            {
                if (_cache.TryGetValue(id, out var user))
                {
                    user.LastRequested = DateTimeOffset.Now;
                    return user.UserData.Deserialize();
                }

                var cached = new CachedUser
                {
                    LastRequested = DateTimeOffset.Now,
                    UserData = DatabaseConnection.LoadUserData(id),
                    Flushed = true
                };
                _cache[id] = cached;

                return cached.UserData.Deserialize();
            }
        }

        public void Put(User.User user)
        {
            lock (_cache)
            {
                if (_cache.TryGetValue(user.Info.UserId, out var cached))
                {
                    cached.UserData = UserData.Serialize(user);
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
                    UserData = UserData.Serialize(user),
                    Flushed = false
                });
            }
        }

        private void RemoveOldeset()
        {
            // _cache must be locked
            var lastRequested = DateTimeOffset.MaxValue;
            UserData oldest = null;
            foreach (var kv in _cache)
            {
                if (oldest == null || kv.Value.LastRequested < lastRequested)
                {
                    lastRequested = kv.Value.LastRequested;
                    oldest = kv.Value.UserData;
                }
            }

            if (oldest == null)
            {
                // _cache is empty
                return;
            }

            DatabaseConnection.SaveUsers(new[] {oldest});
            _cache.Remove(oldest.Id);
        }

        public void FlushAll()
        {
            lock (_cache)
            {
                var users = _cache
                    .Where(kv => !kv.Value.Flushed)
                    .ToList();
                DatabaseConnection.SaveUsers(users
                    .Select(kv => kv.Value.UserData)
                );
                users.ForEach(u => u.Value.Flushed = true);
            }
        }

        private class CachedUser
        {
            public bool Flushed;
            public UserData UserData { get; set; }
            public DateTimeOffset LastRequested { get; set; }
        }
    }
}