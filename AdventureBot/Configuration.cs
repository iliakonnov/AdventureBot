using System.IO;
using Microsoft.Extensions.Configuration;

namespace AdventureBot
{
    public static class Configuration
    {
        static Configuration()
        {
            var builder = new ConfigurationBuilder()
                .SetBasePath(Directory.GetCurrentDirectory())
                .AddJsonFile("config.json");
            Config = builder.Build();
        }

        public static IConfigurationRoot Config { get; }
    }
}