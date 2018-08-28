using AdventureBot.Messenger;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;

namespace Content.Town.Auction
{
    public abstract class MyOffersActionBase : ActionBase<AuctionRoom>
    {
        protected MyOffersActionBase(AuctionRoom room) : base(room)
        {
        }

        public static void Enter(User user)
        {
            // TODO: Send message to user
        }

        [Button("Предложить")]
        public void Offer(User user, RecivedMessage message)
        {
            
        }
        
        [Button("Отменить предложение")]
        public void CancelOffer(User user, RecivedMessage message)
        {
            
        }
        
        [Button("Назад")]
        public void Back(User user, RecivedMessage message)
        {
            Room.SwitchAction<AuctionRoom.MainAction>(user);
        }
    }
}