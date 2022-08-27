using System;
using System.Linq;
using AdventureBot.Messenger;
using AdventureBot.User;
using NLog;

namespace AdventureBot.Analysis;

public static class Events
{
    private static readonly Logger Logger = LogManager.GetCurrentClassLogger();

    static Events()
    {
        RoomManager.OnEnter += Go;
        User.User.OnReset += Reset;
        UserInfo.OnDead += Dead;
        MessengerManager.OnReply += Sent;
        MessengerManager.OnReceived += Received;
    }

    internal static void Start()
    {
        // Needs just to initialize constructor
    }

    private static void Log(string message, string eventName, User.User user, params object[] parameters)
    {
        parameters =
            new object[] {eventName, user.Info.UserId.ToString(), Utils.CurrentIntent(user)}
                .Concat(parameters)
                .ToArray();
        Logger.Debug("Event {eventName} for user {user} at {intent}: " + message, parameters);
    }

    private static void Go(User.User user, string identificator)
    {
        Log("{roomId}", "go", user, identificator);
    }

    private static void Reset(User.User user)
    {
        Log("", "reset", user);
    }

    private static void Dead(User.User user)
    {
        Log("", "dead", user);
    }

    private static void Received(User.User user, ReceivedMessage message)
    {
        Log("id<{id}> '{message}'", "messageReceived", user, message.MessageId, message.Text);
    }

    private static void Sent(User.User user, Tuple<SentMessage, ReceivedMessage> message)
    {
        Log("in reply to '{reply}': {message}", "messageSent", user,
            message.Item2?.MessageId,
            message.Item1.Text);
    }
}