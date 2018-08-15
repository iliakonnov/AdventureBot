using System.Diagnostics;
using AdventureBot.Analysis;
using AdventureBot.Messenger;

namespace AdventureBot.User
{
    public delegate void GameEventHandler(User user);

    public delegate void GameEventHandler<in T>(User user, T param);

    public static class EventRouter
    {
        static EventRouter()
        {
            RoomManager.OnEnter += OnEnter;
            RoomManager.OnLeave += OnLeave;
        }

        internal static void Initialize()
        {
            // Needed to run static constructor.
        }

        private static void OnEnter(User user, string roomIdentifier)
        {
            Events.Go(user, roomIdentifier);
            
            // Handle items
            foreach (var item in user.ItemManager.Items)
            {
                item.Item.OnEnter(user, item);
            }
        }
        
        private static void OnLeave(User user)
        {
            // Handle items
            foreach (var item in user.ItemManager.Items)
            {
                item.Item.OnLeave(user, item);
            }
        }
    }
}