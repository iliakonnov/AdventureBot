using System;
using System.Timers;

namespace AdventureBot.UserManager
{
    public static class Flusher
    {
        private static readonly TimeSpan FlushDelay = new TimeSpan(0, 0, 10);

        // ReSharper disable once PrivateFieldCanBeConvertedToLocalVariable (It must not be disposed by GC)
        private static Timer FlushTimer;
        private static DateTime _lastFlushed = DateTime.Now;

        public static void Init()
        {
            FlushTimer = new Timer(FlushDelay.TotalSeconds)
            {
                AutoReset = true,
                Interval = FlushDelay.TotalSeconds
            };
            FlushTimer.Elapsed += (sender, args) => Flush();
            FlushTimer.Start();
        }

        private static void Flush()
        {
            if (DateTime.Now - _lastFlushed < FlushDelay)
            {
                return;
            }

            _lastFlushed = DateTime.Now;
            Cache.Instance.FlushAll();
        }
    }
}