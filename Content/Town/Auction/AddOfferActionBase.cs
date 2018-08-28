using AdventureBot.Messenger;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;

namespace Content.Town.Auction
{
    public abstract class AddOfferActionBase : ActionBase<AuctionRoom>
    {
        protected AddOfferActionBase(AuctionRoom room) : base(room)
        {
        }
        
        public static void Enter(User user)
        {
            // TODO: Send message to user
        }

        [Fallback]
        public void ItemSelected(User user, RecivedMessage message)
        {
            Room.SwitchAction<AuctionRoom.ItemOffersAction>(user);
        }

        [Button("Назад")]
        public void Back(User user, RecivedMessage message)
        {
            Room.SwitchAction<AuctionRoom.MyOffersAction>(user);
            MyOffersActionBase.Enter(user);
        }
    }
}