using AdventureBot.Messenger;

namespace AdventureBot.Room
{
    public interface IRoom
    {
        string Name { get; }
        string Identifier { get; }
        void OnEnter(User.User user);
        void OnReturn(User.User user);
        bool OnLeave(User.User user);
        void OnMessage(User.User user, RecivedMessage message);
    }
}