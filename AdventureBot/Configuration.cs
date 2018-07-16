using System.IO;
using Microsoft.Extensions.Configuration;

namespace AdventureBot
{
    public class Configuration
    {
        public static IConfigurationRoot Config { get; }
        
        static Configuration()
        {
            var builder = new ConfigurationBuilder()
                .SetBasePath(Directory.GetCurrentDirectory())
                .AddJsonFile("config.json");
            Config = builder.Build();
        }
    }
}