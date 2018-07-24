using System;
using System.Timers;
using NLog;

namespace AdventureBot
{
    public class UserContext : IDisposable
    {
        private static readonly Logger Logger = LogManager.GetCurrentClassLogger();
        private readonly User.User _user;
        private DateTime _opened;
        private Timer _timer;

        public UserContext(UserId userId)
        {
            _user = UserManager.Instance.Get(userId);
            InitializeTimer();
        }

        public UserContext(UserId userId, ChatId chatId)
        {
            Logger.Debug($"Opening user {userId}@{chatId}");
            _user = UserManager.Instance.Get(userId);
            _user.MessageManager.ChatId = chatId;
            InitializeTimer();
        }

        public void Dispose()
        {
            Logger.Debug($"User closed in {DateTime.Now - _opened}");
            _timer.Stop();
            UserManager.Instance.Save(_user);
            _timer.Dispose();
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

        private void TimerOnElapsed(object sender, ElapsedEventArgs e)
        {
            throw new TimeoutException("User have been opened too long");
        }

        public static implicit operator User.User(UserContext userContext)
        {
            return userContext._user;
        }
    }
}