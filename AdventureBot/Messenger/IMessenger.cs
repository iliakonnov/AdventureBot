using System;
using System.Threading.Tasks;
using JetBrains.Annotations;

namespace AdventureBot.Messenger
{
    public delegate void MessageHandler(RecivedMessage message);
    
    public interface IMessenger
    {
        void Send(SentMessage message, [CanBeNull] RecivedMessage recievedMessage, User.User user);
        event MessageHandler MessageRecieved;
        void BeginPolling();
    }
}