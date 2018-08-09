using System;
using System.Collections.Generic;
using System.Linq;

namespace AdventureBot.UserManager
{
    public class Cache : Singleton<Cache>
    {
        private class CachedUser
        {
            public User.User User { get; set; }
            public DateTimeOffset LastRequested { get; set; }
            public bool Flushed;
        }

        static Cache()
        {
            Flusher.Init();
        }

        private const int CacheSize = 100;

        private readonly Dictionary<UserId, CachedUser> _cache = new Dictionary<UserId, CachedUser>();

        public User.User Get(UserId id)
        {
            lock (_cache)
            {
                if (_cache.TryGetValue(id, out var user))
                {
                    user.LastRequested = DateTimeOffset.Now;
                    return user.User;
                }

                var cached = new CachedUser
                {
                    LastRequested = DateTimeOffset.Now,
                    User = DatabaseConnection.LoadUser(id),
                    Flushed = true
                };
                _cache[id] = cached;

                return cached.User;
            }
        }

        public void Put(User.User user)
        {
            lock (_cache)
            {
                if (_cache.TryGetValue(user.Info.UserId, out var cached))
                {
                    cached.User = user;
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

                _cache.Add(user.Info.UserId, new CachedUser {User = user, Flushed = false});
            }
        }

        private void RemoveOldeset()
        {
            // _cache must be locked
            CachedUser oldest = null;
            foreach (var value in _cache.Values)
            {
                if (oldest == null || value.LastRequested < oldest.LastRequested)
                {
                    oldest = value;
                }
            }

            if (oldest == null)
            {
                // _cache is empty
                return;
            }

            DatabaseConnection.SaveUsers(new[] {oldest.User});
            _cache.Remove(oldest.User.Info.UserId);
        }

        public void FlushAll()
        {
            lock (_cache)
            {
                var users = _cache
                    .Where(u => !u.Value.Flushed)
                    .ToList();
                DatabaseConnection.SaveUsers(users.Select(u => u.Value.User));
                users.ForEach(u => u.Value.Flushed = true);
            }
        }
    }
}