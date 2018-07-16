using Microsoft.Extensions.Logging;

namespace AdventureBot
{
    public static class Logger
    {
        public static ILoggerFactory LoggerFactory { get; } = new LoggerFactory()
            .AddConsole(Configuration.Config.GetSection("Logging"));

        public static ILogger CreateLogger<T>()
        {
            return LoggerFactory.CreateLogger<T>();
        }
    }
}