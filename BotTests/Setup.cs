using Xunit.Abstractions;
using Xunit.Sdk;

[assembly: Xunit.TestFramework("BotTests.Setup", "BotTests")]
namespace BotTests;

public class Setup : XunitTestFramework
{
    public Setup(IMessageSink messageSink) : base(messageSink)
    {
        AdventureBot.Program.Initialize();
    }
}