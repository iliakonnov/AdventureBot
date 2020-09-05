using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot.Messenger
{
    [MessagePackObject(true)]
    public class ReceivedMessage
    {
        public delegate void Handler(ReceivedMessage message, User.User user);

        [IgnoreMember] [CanBeNull] public Handler Action;
        public ChatId ChatId;
        public string MessageId;
        public long? ReplyUserId;
        public string Text;
        public UserId UserId;
    }

    [MessagePackObject(true)]
    public class SentMessage
    {
        [CanBeNull] public string[][] Buttons = null;
        public ChatId ChatId = new ChatId(int.MinValue, long.MinValue);
        public bool Formatted = true;

        public string Text;
        public string Intent { get; set; }
    }
}