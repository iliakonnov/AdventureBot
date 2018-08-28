using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;

namespace Content.Town.Auction
{
    [Room(Id)]
    public class AuctionRoom : BetterRoomBase<AuctionRoom>
    {
        public const string Id = "town/auction";
        public override string Name => "Аукцион";
        public override string Identifier => Id;
        
        [Action]
        public class MainAction : ActionBase<AuctionRoom>
        {
            public MainAction(AuctionRoom room) : base(room)
            {
            }

            [Button("Посмотреть предложения")]
            public void ShowOffers(User user, RecivedMessage message)
            {
                Room.SwitchAction<AllOffersAction>(user);
                AllOffersActionBase.Enter(user);
            }

            [Button("Мои предложения")]
            public void MyOffers(User user, RecivedMessage message)
            {
                Room.SwitchAction<MyOffersAction>(user);
                MyOffersActionBase.Enter(user);
            }
        }

        [Action(0)]
        public class MyOffersAction : MyOffersActionBase
        {
            public MyOffersAction(AuctionRoom room) : base(room)
            {
            }
        }
        
        [Action(1)]
        public class AllOffersAction : AllOffersActionBase
        {
            public AllOffersAction(AuctionRoom room) : base(room)
            {
            }
        }
        
        [Action(2)]
        public class ItemOffersAction : ItemOffersActionBase
        {
            public ItemOffersAction(AuctionRoom room) : base(room)
            {
            }
        }

        [Action(3)]
        public class RemoveOfferAction : RemoveOfferActionBase
        {
            public RemoveOfferAction(AuctionRoom room) : base(room)
            {
            }
        }
        
        [Action(4)]
        public class AddOfferAction : AddOfferActionBase
        {
            public AddOfferAction(AuctionRoom room) : base(room)
            {
            }
        }
        
        [Action(4)]
        public class PriceGroupSelectionAction : PriceGroupSelectionActionBase
        {
            public PriceGroupSelectionAction(AuctionRoom room) : base(room)
            {
            }
        }
        
        [Action(4)]
        public class PriceSelectionAction : PriceSelectionActionBase
        {
            public PriceSelectionAction(AuctionRoom room) : base(room)
            {
            }
        }
    }
}