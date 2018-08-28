using System.Collections.Generic;
using System.Linq;
using AdventureBot.Messenger;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;

namespace Content.Town.Auction
{
    public abstract class PriceSelectionActionBase : ActionBase<AuctionRoom>
    {
        protected PriceSelectionActionBase(AuctionRoom room) : base(room)
        {
        }

        [Fallback]
        public void Fallback(User user, RecivedMessage message)
        {
        }
    }
}