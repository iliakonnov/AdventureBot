using System;
using System.Timers;
using NLog;

namespace AdventureBot
{
    public class UserContext : IDisposable
    {
        private static readonly Logger Logger = LogManager.GetCurrentClassLogger();
        private DateTime _opened;
        private Timer _timer;

        public UserContext(UserId userId)
        {
            User = UserManager.Instance.Get(userId);
            InitializeTimer();
        }

        public UserContext(UserId userId, ChatId chatId)
        {
            Logger.Debug($"Opening user {userId}@{chatId}");
            User = UserManager.Instance.Get(userId);
            User.MessageManager.ChatId = chatId;
            InitializeTimer();
        }

        public User.User User { get; }

        public void Dispose()
        {
            Logger.Debug($"User closed in {DateTime.Now - _opened}");
            _timer.Stop();
            UserManager.Instance.Save(User);
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
            return userContext.User;
        }
    }
}