using JetBrains.Annotations;

namespace AdventureBot.Messenger
{
    public delegate void MessageHandler(RecivedMessage message);

    [PublicAPI]
    public interface IMessenger
    {
        void Send(SentMessage message, [CanBeNull] RecivedMessage recievedMessage, User.User user);
        event MessageHandler MessageRecieved;
        void BeginPolling();
    }
}