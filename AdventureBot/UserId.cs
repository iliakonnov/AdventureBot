using MessagePack;

namespace AdventureBot
{
    [MessagePackObject]
    public struct UserId
    {
        [Key(0)] public int Messenger;
        [Key(1)] public long Id;

        public UserId(int messenger, long id)
        {
            Messenger = messenger;
            Id = id;
        }

        public override string ToString()
        {
            return $"<User: {Messenger}/{Id}>";
        }
    }
    
    [MessagePackObject]
    public struct ChatId
    {
        [Key(0)] public int Messenger;
        [Key(1)] public long Id;

        public ChatId(int messenger, long id)
        {
            Messenger = messenger;
            Id = id;
        }
        
        public override string ToString()
        {
            return $"<Chat: {Messenger}/{Id}>";
        }
    }
}