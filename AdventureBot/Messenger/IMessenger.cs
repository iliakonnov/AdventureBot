using System.Threading.Tasks;
using JetBrains.Annotations;

namespace AdventureBot.Messenger;

public delegate void MessageHandler(ReceivedMessage message);

[PublicAPI]
public interface IMessenger
{
    Task Send(SentMessage message, [CanBeNull] ReceivedMessage receivedMessage, User.User user);
    event MessageHandler MessageReceived;
    void BeginPolling();
}