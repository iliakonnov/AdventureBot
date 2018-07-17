using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Threading;
using MessagePack;
using MessagePack.ImmutableCollection;
using MessagePack.Resolvers;
using Microsoft.Extensions.Logging;
using Mono.Data.Sqlite;
using Timer = System.Timers.Timer;

namespace AdventureBot
{
    public class UserManager : Singleton<UserManager>
    {
        private readonly ConcurrentDictionary<UserId, CachedUser> _cache =
            new ConcurrentDictionary<UserId, CachedUser>();

        private readonly string _connectionString;
        private readonly object _databaseLock = new object();

        // ReSharper disable once PrivateFieldCanBeConvertedToLocalVariable (It must not be removed by GC)
        private readonly Timer _flushTimer;

        private readonly DecreaseCounter _loadedUsers = new DecreaseCounter();
        private readonly ILogger _logger = Logger.CreateLogger<UserManager>();
        private DateTime _lastFlushed = DateTime.Now;
        private bool _toFlush;

        public UserManager()
        {
            _loadedUsers.OnZero += FlushUsers;

            CompositeResolver.RegisterAndSetAsDefault(
                ImmutableCollectionResolver.Instance,
                StandardResolverAllowPrivate.Instance
            );

            // SQLitePCL.Batteries.Init();
            _connectionString = $"Data Source = {Configuration.Config["database"]};";

            using (var connection = new SqliteConnection(_connectionString))
            using (var command = connection.CreateCommand())
            {
                connection.Open();
                using (var transaction = connection.BeginTransaction())
                {
                    command.Transaction = transaction;
                    command.CommandText =
                        @"CREATE TABLE IF NOT EXISTS `users` (
                            `messenger`	INTEGER,
                            `id`	INTEGER,
                            `data`	BLOB,
                            PRIMARY KEY(`id`)
                        );";
                    command.ExecuteNonQuery();

                    transaction.Commit();
                }
            }

            _flushTimer = new Timer
            {
                AutoReset = true,
                Interval = 1000 // Every second
            };
            _flushTimer.Elapsed += (sender, args) => FlushUsers();
            _flushTimer.Start();
        }

        private void FlushUsers()
        {
            if (_loadedUsers.Count != 0)
            {
                return;
            }

            if (_toFlush || DateTime.Now - _lastFlushed > new TimeSpan(0, 0, 15)) // Every 15 seconds
            {
                Flush(_cache.Values.Where(c => c.Changed));
                _lastFlushed = DateTime.Now;
                _toFlush = false;
            }
        }

        private User.User WaitUser(CachedUser user, bool safe = true)
        {
            if (safe)
            {
                if (user.Lock.Wait(3500))
                {
                    _loadedUsers.Increase();
                    return user.User;
                }

                throw new TimeoutException("Timeout waiting for user");
            }

            if (user.User == null)
            {
                return null;
            }

            var result = MessagePackSerializer.Deserialize<User.User>(MessagePackSerializer.SerializeUnsafe(user.User));
            result.Unsafe = true;
            return result;
        }

        private CachedUser AllocateUser(UserId userId, bool safe = true)
        {
            if (!safe)
            {
                return new CachedUser();
            }

            const int cacheSize = 500;
            const int maxTries = 3;
            for (var cnt = 0; cnt < maxTries; cnt++)
            {
                if (_cache.Count < cacheSize)
                {
                    // There is a place for new user
                    _cache[userId] = new CachedUser();
                    return _cache[userId];
                }

                // Cache is full, so remove one user and try again
                var oldest = _cache.Aggregate((l, r) => l.Value.LastLoaded > r.Value.LastLoaded ? l : r);
                Flush(oldest.Value);
            }

            // Something wrong and cache is always full, so return uncached user
            _logger.LogWarning("Cache is always full. Maybe bot overloaded?");
            return new CachedUser();
        }

        /// <summary>
        ///     Loads user with given user_id. Returns null if user not found
        /// </summary>
        public User.User Get(UserId userId, bool safe = true)
        {
            if (_cache.TryGetValue(userId, out var cachedUser))
            {
                // This user in cache, so just return from cache
                cachedUser.LastLoaded = DateTime.Now;
                return WaitUser(cachedUser, safe);
            }

            // This user is not cached, so load it from disk
            var cached = AllocateUser(userId);

            WaitUser(cached, safe);

            lock (_databaseLock)
            {
                using (var connection = new SqliteConnection(_connectionString))
                using (var command = connection.CreateCommand())
                {
                    connection.Open();
                    using (var transaction = connection.BeginTransaction())
                    {
                        command.Transaction = transaction;
                        command.CommandText = "SELECT data FROM users WHERE id=@user_id AND messenger=@messenger";
                        command.Parameters.AddWithValue("@messenger", userId.Messenger);
                        command.Parameters.AddWithValue("@user_id", userId.Id);

                        using (var reader = command.ExecuteReader())
                        {
                            while (reader.Read())
                            {
                                if (reader["data"] == null || Convert.IsDBNull(reader["data"]))
                                {
                                    continue;
                                }

                                // Loads user from database and saves it to cache
                                var userdata = (byte[]) reader["data"];
                                var user = MessagePackSerializer.Deserialize<User.User>(userdata);
                                cached.User = user;
                                cached.User.Unsafe = !safe;

                                return cached.User;
                            }
                        }
                    }
                }
            }

            // User not found in database.
            cached.User = new User.User(userId) {Unsafe = !safe};

            return cached.User;
        }

        /// <summary>
        ///     Saves given user to cache instead of directly to disk.
        /// </summary>
        public void Save(User.User user)
        {
            if (user.Unsafe)
            {
                throw new ArgumentException("This user is not safe!");
            }

            _loadedUsers.Decrease();

            if (_cache.TryGetValue(user.Info.UserId, out var cachedUser))
            {
                // User cached, so just edit cache
                cachedUser.User = user;
                cachedUser.Changed = true;
                if (cachedUser.Lock.CurrentCount != 0)
                {
                    _logger.LogWarning($"CachedUser was not locked. {user.Info.UserId}");
                }
                else
                {
                    cachedUser.Lock.Release();
                }
            }
            else
            {
                // User not cached, so write directly to disk
                Flush(new CachedUser {User = user});
            }
        }

        /// <summary>
        ///     Flushes and removes user from cache
        /// </summary>
        private void Flush(CachedUser user)
        {
            if (user.Lock.CurrentCount == 0)
            {
                return;
            }

            Flush(new[] {user});
            _cache.TryRemove(user.User.Info.UserId, out _);
        }

        private void Flush(IEnumerable<CachedUser> users)
        {
            var beginTime = DateTime.Now;
            var cnt = 0;

            lock (_databaseLock)
            {
                using (var connection = new SqliteConnection(_connectionString))
                using (var command = connection.CreateCommand())
                {
                    connection.Open();
                    using (var transaction = connection.BeginTransaction())
                    {
                        command.Transaction = transaction;
                        command.CommandText =
                            "INSERT OR REPLACE INTO users (messenger, id, data) VALUES (@messenger, @user_id, @data)";

                        var messengerParam = command.Parameters.Add("@messenger", DbType.Int32);
                        var idParam = command.Parameters.Add("@user_id", DbType.Int32);
                        var dataParam = command.Parameters.Add("@data", DbType.Binary);

                        foreach (var user in users)
                        {
                            if (!user.Changed)
                            {
                                continue;
                            }

                            cnt++;

                            messengerParam.Value = user.User.Info.UserId.Messenger;
                            idParam.Value = user.User.Info.UserId.Id;
                            dataParam.Value = MessagePackSerializer.Serialize(user.User);
                            user.Changed = false;
                            command.ExecuteNonQuery();
                        }

                        transaction.Commit();
                    }
                }
            }

            if (cnt != 0)
            {
                _logger.LogInformation($"Flushed {cnt} users in {DateTime.Now - beginTime}");
            }
        }

        /// <summary>
        ///     Saves all cached users to disk.
        /// </summary>
        public void Flush()
        {
            // Just disallow to load new users
            _loadedUsers.Acquire();
            _toFlush = true;
            FlushUsers();
        }

        private class CachedUser
        {
            public CachedUser()
            {
                LastLoaded = DateTime.Now;
            }

            public SemaphoreSlim Lock { get; } = new SemaphoreSlim(1, 1);

            public DateTime LastLoaded { get; set; }
            public User.User User { get; set; }
            public bool Changed { get; set; }
        }

        private class DecreaseCounter
        {
            public delegate void ZeroHandler();

            private readonly ManualResetEventSlim _allowIncrease = new ManualResetEventSlim(true);
            public int Count { get; private set; }

            public event ZeroHandler OnZero;

            public void Increase()
            {
                _allowIncrease.Wait();
                Count++;
            }

            public void Decrease()
            {
                Count--;
                if (Count == 0)
                {
                    OnZero?.Invoke();
                    _allowIncrease.Set();
                }
            }

            public void Acquire()
            {
                _allowIncrease.Reset();
            }
        }
    }
}