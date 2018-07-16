using System;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot.Messenger
{
    [MessagePackObject(keyAsPropertyName: true)]
    public class RecivedMessage : ISerializable
    {
        public string Text;
        public ChatId ChatId;
        public UserId UserId;
        public int? ReplyId;
        [IgnoreMember] [CanBeNull] public Handler Action;
        public DateTimeOffset RecivedTime;

        public delegate void Handler(RecivedMessage message, User.User user);
    }

    [MessagePackObject(keyAsPropertyName: true)]
    public class SentMessage : ISerializable
    {
        public string Text;
        public ChatId ChatId = new ChatId(int.MinValue, long.MinValue);
        public bool Formatted = true;
        [CanBeNull] public string[][] Buttons = null;

        public DateTimeOffset SentTime;
        public string Intent { get; set; }
    }
}