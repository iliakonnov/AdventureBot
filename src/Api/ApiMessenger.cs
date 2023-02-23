using System;
using System.Threading.Tasks;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.User;

namespace Api;

[Messenger]
public class ApiMessenger : IMessenger
{
    internal const int MessengerId = 3;

    public ApiMessenger()
    {
        if (OnMessageReceivedStatic == null)
        {
            OnMessageReceivedStatic += message => MessageReceived?.Invoke(message);
        }
    }

    public Task Send(SentMessage message, ReceivedMessage receivedMessage, User user)
    {
        // Do nothing because PublicUser.MessageManager.LastMessages already contains last messages
        return Task.CompletedTask;
    }

    public event MessageHandler MessageReceived;

    public void BeginPolling()
    {
        // Do nothing since updates are processed using ApiController
    }

    internal static event MessageHandler OnMessageReceivedStatic;

    internal static (ChatId, UserId)? ParseToken(string token)
    {
        var splitted = token.Split(':');
        if (splitted.Length != 2)
        {
            return null;
        }

        if (!long.TryParse(splitted[0], out var id))
        {
            return null;
        }

        if (!Guid.TryParse(splitted[1], out var guid))
        {
            return null;
        }

        var user = new UserId(MessengerId, id);

        using (var context = new UserContext(user))
        {
            if (context.User.Token != guid)
            {
                return null;
            }
        }

        return (new ChatId(MessengerId, id), user);
    }

    internal static void InvokeOnMessageReceived(ReceivedMessage message)
    {
        OnMessageReceivedStatic?.Invoke(message);
    }
}