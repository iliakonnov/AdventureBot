using System;
using System.Timers;
using AdventureBot.UserManager;
using NLog;

namespace AdventureBot
{
    public class UserContext : IDisposable
    {
        private static readonly Logger Logger = LogManager.GetCurrentClassLogger();
        private DateTime _opened;
        private Timer _timer;
        private User.User _unlinked;

        public UserContext(UserId userId)
        {
            LoadUser(userId);
        }

        public UserContext(UserId userId, ChatId chatId)
        {
            LoadUser(userId);
            User.MessageManager.ChatId = chatId;
        }

        public User.User User { get; private set; }

        public void Dispose()
        {
            Logger.Debug("User closed in {time}", DateTime.Now - _opened);
            _timer.Stop();
            UserProxy.Save(User);
            if (_unlinked != null)
            {
                UserProxy.Save(_unlinked);
            }

            _timer.Dispose();
        }

        private void LoadUser(UserId userId)
        {
            Logger.Debug("Opening user {userId}", userId);
            User = UserProxy.Get(userId);
            if (User.LinkedTo != null)
            {
                _unlinked = User;
                // Load user not through UserContext, because it can be linked to other user and so on.
                User = UserProxy.Get(User.LinkedTo.Item1);
                if (User.Token != _unlinked.LinkedTo.Item2)
                {
                    // Token was revoked, so unlink this user
                    Unlink();
                }
            }

            InitializeTimer();
        }

        internal void Unlink()
        {
            _unlinked.LinkedTo = null;
            User = _unlinked;
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
}