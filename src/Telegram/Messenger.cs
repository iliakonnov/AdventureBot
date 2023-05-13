using System;
using System.Threading.Tasks;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.ObjectManager;
using AdventureBot.User;
using NLog;

namespace Telegram;

[Messenger]
public class Messenger : IMessenger
{
    // User:
    // Telegram.Messenger/available_messengers: {
    //    {chat_id}: {
    //        {bot_id}: true,
    //        ...
    //    },
    //    ...
    // }
    //
    // Global:
    // Telegram.Messenger/available_messengers: {
    //    {chat_id}: {
    //        {bot_id}: true,
    //        ...
    //    },
    //    ...
    // }

    private static readonly Logger Logger = LogManager.GetCurrentClassLogger();
    internal readonly TelegramBot messenger;

    public Messenger()
    {
        var token = Configuration.Config.GetSection("telegram_token").Value;
        messenger = new TelegramBot(token);
    }

    public async Task Send(SentMessage message, ReceivedMessage receivedMessage, User user)
    {
        const int maxSize = 4095;
        if (message.Text.Length > maxSize)
        {
            // Message too long, so split it to small part and all other.
            await Send(new SentMessage
            {
                Buttons = message.Buttons,
                ChatId = message.ChatId,
                Formatted = message.Formatted,
                Text = message.Text.Substring(0, maxSize),
                PreferToUpdate = false
            }, receivedMessage, user);

            await Send(new SentMessage
            {
                Buttons = message.Buttons,
                ChatId = message.ChatId,
                Formatted = message.Formatted,
                Text = message.Text.Substring(maxSize),
                PreferToUpdate = false
            }, receivedMessage, user);

            return;
        }

        await messenger.Send(message, receivedMessage);
    }

    public event MessageHandler MessageReceived;

    public void BeginPolling()
    {
        messenger.OnMessageReceived += message =>
        {
            try
            {
                MessageReceived?.Invoke(message);
            }
            catch (Exception e)
            {
                Logger.Error(e, "Error");
            }
        };
        messenger.BeginPolling();
    }
}