using System;
using System.Collections.Generic;
using System.Threading;

namespace AdventureBot.UserManager;

public class UserProxy
{
    private static readonly Dictionary<UserId, UserProxy> _proxies = new();

    private static readonly TimeSpan Timeout = new(0, 0, 5);
    private readonly ManualResetEvent _available = new(true);
    private readonly UserId _id;

    private readonly object _lock = new();
    private User.User _loaded;
    private DateTime _unlockAt;

    private UserProxy(UserId id)
    {
        _id = id;
    }

    private static UserProxy GetLoadedUser(UserId id)
    {
        lock (_proxies)
        {
            if (_proxies.TryGetValue(id, out var proxy))
            {
                return proxy;
            }

            proxy = new UserProxy(id);
            _proxies[id] = proxy;
            return proxy;
        }
    }

    public static User.User Get(UserId id)
    {
        return GetLoadedUser(id).Acquire();
    }

    public static User.User GetUnsafe(UserId id)
    {
        return GetLoadedUser(id).GetUnsafe();
    }

    public static void Save(User.User user)
    {
        GetLoadedUser(user.Info.UserId).Release(user);
    }

    public User.User Acquire()
    {
        var timeRemaining = _unlockAt - DateTime.Now;
        if (timeRemaining <= TimeSpan.Zero)
        {
            return GetUser();
        }

        _available.WaitOne(timeRemaining);
        return GetUser();
    }

    public User.User GetUnsafe()
    {
        lock (_lock)
        {
            return Cache.Instance.Get(_id);
        }
    }

    private User.User GetUser()
    {
        lock (_lock)
        {
            var user = Cache.Instance.Get(_id);
            _loaded = user;
            _unlockAt = DateTime.Now + Timeout;
            _available.Reset();
            return user;
        }
    }

    public void Release(User.User user)
    {
        if (ReferenceEquals(user, _loaded))
        {
            lock (_lock)
            {
                Cache.Instance.Put(user);
                _available.Set();
                _loaded = null;
            }
        }
        else
        {
            throw new Exception("This user cannot be saved");
        }
    }
}