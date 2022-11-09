using System.Collections.Generic;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot.Messenger;

[MessagePackObject(true)]
public class ReceivedMessage
{
    public delegate void Handler(ReceivedMessage message, User.User user);

    [IgnoreMember] [CanBeNull] public Handler Action;
    public ChatId ChatId;
    public string MessageId;
    public dynamic MessengerSpecificData = null;
    public string Text;
    public UserId UserId;
}

[MessagePackObject(true)]
public class SentMessage
{
    [CanBeNull] public string[][] Buttons = null;
    public ChatId ChatId = new(int.MinValue, long.MinValue);
    public Dictionary<int, dynamic> MessengerSpecificData = new();
    public bool Formatted = true;
    public bool? PreferToUpdate = null;

    public string Text;
    public string Intent { get; set; }
}