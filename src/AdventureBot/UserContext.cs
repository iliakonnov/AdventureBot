using System;
using System.Timers;
using AdventureBot.UserManager;
using NLog;
using Prometheus;

namespace AdventureBot;

public class UserContext : IDisposable
{
    private static readonly Logger Logger = LogManager.GetCurrentClassLogger();
    private static readonly Histogram UserOpenedDuration = Metrics.CreateHistogram("user_opened_duration", "Duration user was opened (ms)");

    private DateTime _opened;
    private Timer _timer;
    private UserProxy _unlinked;
    private UserProxy _proxy;

    public UserContext(UserId userId)
    {
        LoadUser(userId);
    }

    public UserContext(UserId userId, ChatId chatId)
    {
        LoadUser(userId);
        User.MessageManager.ChatId = chatId;
    }

    public User.User User => _proxy.User;

    public void Dispose()
    {
        UserOpenedDuration.Observe((DateTime.Now - _opened).TotalMilliseconds);
        Logger.Debug("User closed in {time}", DateTime.Now - _opened);
        _timer.Stop();
        _proxy?.Dispose();
        _unlinked?.Dispose();

        _timer.Dispose();
    }

    private void LoadUser(UserId userId)
    {
        Logger.Debug("Opening user {userId}", userId);
        _proxy = new UserProxy(userId);
        if (User.LinkedTo != null)
        {
            _unlinked = _proxy;
            // Load user not through UserContext, because it can be linked to other user and so on.
            _proxy = new UserProxy(_proxy.User.LinkedTo.Item1);
            if (User.Token != _unlinked.User.LinkedTo.Item2)
            {
                // Token was revoked, so unlink this user
                Unlink();
            }
        }

        InitializeTimer();
    }

    internal bool Unlink()
    {
        if (_unlinked == null)
        {
            return false;
        }

        _unlinked.User.LinkedTo = null;
        _proxy.Dispose();
        _proxy = _unlinked;
        return true;
    }

    private void InitializeTimer()
    {
        _timer = new Timer
        {
            Interval = 3000,
            AutoReset = true
        };
        _timer.Elapsed += TimerOnElapsed;
        _timer.Start();
        _opened = DateTime.Now;
    }

    private static void TimerOnElapsed(object sender, ElapsedEventArgs e)
    {
        throw new TimeoutException("User have been opened too long");
    }

    public static implicit operator User.User(UserContext userContext)
    {
        return userContext.User;
    }
}