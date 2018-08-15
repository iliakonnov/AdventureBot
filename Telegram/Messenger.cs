using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Linq;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.User;
using JetBrains.Annotations;
using NLog;

namespace Telegram
{
    public abstract class Messenger : IMessenger
    {
        // User:
        // Telegram.Messenger/available_messengres: {
        //    {chat_id}: {
        //        {bot_id}: true,
        //        ...
        //    },
        //    ...
        // }
        //
        // Global:
        // Telegram.Messenger/available_messengres: {
        //    {chat_id}: {
        //        {bot_id}: true,
        //        ...
        //    },
        //    ...
        // }

        private const string RootVariable = "Telegram.Messenger/available_messengers";
        private static readonly Logger Logger = LogManager.GetCurrentClassLogger();
        private readonly TelegramBot _defaultMessenger;
        private readonly List<TelegramBot> _messengers;
        internal readonly ImmutableHashSet<int> MessengerIds;

        internal Messenger(List<TelegramBot> messengers)
        {
            foreach (var messenger in messengers)
            {
                messenger.Messenger = this;
            }

            _messengers = messengers;
            MessengerIds = _messengers.Select(m => m.Id).ToImmutableHashSet();
            _defaultMessenger = messengers.First(m => m.ReciveMessages);
        }

        public async void Send(SentMessage message, RecivedMessage recievedMessage, User user)
        {
            const int maxSize = 4095;
            if (message.Text.Length > maxSize)
            {
                // Message too long, so split it to small part and all other.
                Send(new SentMessage
                {
                    Buttons = message.Buttons,
                    ChatId = message.ChatId,
                    Formatted = message.Formatted,
                    Text = message.Text.Substring(0, maxSize)
                }, recievedMessage, user);

                Send(new SentMessage
                {
                    Buttons = message.Buttons,
                    ChatId = message.ChatId,
                    Formatted = message.Formatted,
                    Text = message.Text.Substring(maxSize)
                }, recievedMessage, user);

                return;
            }

            var availableMessengers =
                DefaultMessengers(user.VariableManager.PersistentVariables, user.MessageManager.ChatId);
            var availableIds = availableMessengers.Keys()
                .Select(int.Parse)
                .ToImmutableHashSet();
            var messengers = _messengers.Where(m => availableIds.Contains(m.Id)).ToList();

            if (messengers.Count == 0)
            {
                foreach (var availableId in availableIds)
                {
                    RemoveBot(availableId, null, user);
                }

                NewBot(_defaultMessenger.Id, null, user);
                await _defaultMessenger.Send(message, recievedMessage);
            }
            else
            {
                var bestMessenger = messengers.Aggregate((l, r) => l.LastMessageSent < r.LastMessageSent ? l : r);
                await bestMessenger.Send(message, recievedMessage);
            }
        }

        public event MessageHandler MessageRecieved;

        public void BeginPolling()
        {
            foreach (var messenger in _messengers)
            {
                messenger.MessageRecieved += message =>
                {
                    try
                    {
                        MessageRecieved?.Invoke(message);
                    }
                    catch (Exception e)
                    {
                        Logger.Error(e, "Error");
                    }
                };
                messenger.BeginPolling();
            }
        }

        internal void NewUser(long chatId, User user)
        {
            var globalMessengers = DefaultMessengers(GlobalVariables.Variables, new ChatId(1, chatId));
            var userMessengers =
                DefaultMessengers(user.VariableManager.PersistentVariables, user.MessageManager.ChatId);
            foreach (var key in globalMessengers.Keys())
            {
                userMessengers.Set(key, new Serializable.Bool(true));
            }
        }

        internal void ListBots(User user)
        {
            var messengers =
                DefaultMessengers(user.VariableManager.PersistentVariables, user.MessageManager.ChatId);
            foreach (var key in messengers.Keys())
            {
                user.MessageManager.SendMessage(new SentMessage {Text = key});
            }
        }

        internal void NewBot(int id, long? chatId, User user, bool quiet = false)
        {
            if (!MessengerIds.Contains(id))
            {
                throw new ArgumentException($"Unknown bot id: {id}");
            }

            if (!quiet)
            {
                user.MessageManager.SendMessage(new SentMessage {Text = "Ура! Новый бот!"});
            }

            if (chatId != null)
            {
                var globalMessengers = DefaultMessengers(GlobalVariables.Variables, new ChatId(1, (long) chatId));
                globalMessengers.Set(id.ToString(), new Serializable.Bool(true));
            }

            var availableMessengers =
                DefaultMessengers(user.VariableManager.PersistentVariables, user.MessageManager.ChatId);
            availableMessengers.Set(id.ToString(), new Serializable.Bool(true));
        }

        internal void RemoveBot(int id, long? chatId, User user, bool quiet = false)
        {
            if (!quiet)
            {
                user.MessageManager.SendMessage(new SentMessage {Text = "Прощай, бот"});
            }

            if (chatId != null)
            {
                var globalMessengers = DefaultMessengers(GlobalVariables.Variables, new ChatId(1, (long) chatId));
                globalMessengers.Remove(id.ToString());
            }

            DefaultMessengers(user.VariableManager.PersistentVariables, user.MessageManager.ChatId)
                .Remove(id.ToString());
        }

        /// <summary>
        ///     Returns available messengers for specified chat by available chats.
        ///     Checks that {chat_id} is not null.
        /// </summary>
        [NotNull]
        private VariableContainer DefaultMessengersInner(VariableContainer availableChats, ChatId chatId)
        {
            var chat = chatId.Id.ToString();

            var availableMessengers = availableChats.Get<VariableContainer>(chat);
            if (availableMessengers != null)
            {
                return availableMessengers;
            }

            availableMessengers = new VariableContainer();

            var defaultId = _messengers[0].Id;
            availableMessengers.Set(defaultId.ToString(), new Serializable.Bool(true));
            availableChats.Set(chat, availableMessengers);

            return availableMessengers;
        }

        /// <summary>
        ///     Returns available messengers for specified chat by user.
        ///     Checks that {RootVariable} is not null.
        /// </summary>
        [NotNull]
        private VariableContainer DefaultMessengers(VariableContainer variables, ChatId chatId)
        {
            var availableChats = variables.Get<VariableContainer>(RootVariable);
            if (availableChats != null)
            {
                return DefaultMessengersInner(availableChats, chatId);
            }

            var container = new VariableContainer();
            variables.Set(RootVariable, container);
            return DefaultMessengersInner(container, chatId);
        }
    }
}