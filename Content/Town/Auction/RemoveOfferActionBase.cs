using AdventureBot.Messenger;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;

namespace Content.Town.Auction
{
    public abstract class RemoveOfferActionBase : ActionBase<AuctionRoom>
    {
        protected RemoveOfferActionBase(AuctionRoom room) : base(room)
        {
        }
        
        public static void Enter(User user)
        {
            // TODO: Send message to user
        }

        [Fallback]
        public void OfferSelected(User user, RecivedMessage message)
        {
        }

        [Button("Назад")]
        public void Back(User user, RecivedMessage message)
        {
            Room.SwitchAction<AuctionRoom.MyOffersAction>(user);
            MyOffersActionBase.Enter(user);
        }
    }
}