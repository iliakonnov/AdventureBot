using System;
using System.Collections.Generic;
using System.Threading;

namespace AdventureBot.UserManager;

public class UserProxy
{
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
        return new UserProxy(id);
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

    private User.User Acquire()
    {
        var timeRemaining = _unlockAt - DateTime.Now;
        if (timeRemaining <= TimeSpan.Zero)
        {
            return GetUser();
        }

        _available.WaitOne(timeRemaining);
        return GetUser();
    }

    private User.User GetUnsafe()
    {
        return DatabaseConnection.LoadUserData(_id).Deserialize();
    }

    private User.User GetUser()
    {
        lock (_lock)
        {
            var user = DatabaseConnection.LoadUserData(_id).Deserialize();
            _loaded = user;
            _unlockAt = DateTime.Now + Timeout;
            _available.Reset();
            return user;
        }
    }

    private void Release(User.User user)
    {
        if (ReferenceEquals(user, _loaded))
        {
            lock (_lock)
            {
                DatabaseConnection.SaveUsers(new[] { UserData.Serialize(user)  });
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