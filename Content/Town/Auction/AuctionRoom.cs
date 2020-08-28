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
        public override string Name => "Рынок";
        public override string Identifier => Id;

        public override void OnEnter(User user)
        {
            GetAction<MainAction>().Enter(user);
        }

        [Action]
        public class MainAction : ActionBase<AuctionRoom>
        {
            public MainAction(AuctionRoom room) : base(room)
            {
            }

            public void Enter(User user)
            {
                Room.SendMessage(user, "Здесь вы можете купить или продать что угодно по самым лучшим ценам!",
                    Room.GetButtons(user));
            }

            [Button("Посмотреть предложения")]
            public void ShowOffers(User user, RecivedMessage message)
            {
                Room.SwitchAction<AllOffersAction>(user);
                Room.GetAction<AllOffersAction>().Enter(user);
            }

            [Button("Мои предложения")]
            public void MyOffers(User user, RecivedMessage message)
            {
                Room.SwitchAction<MyOffersAction>(user);
                Room.GetAction<MyOffersAction>().Enter(user);
            }
            
            [Button("Уйти")]
            public void Exit(User user, RecivedMessage message)
            {
                user.RoomManager.Leave();
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

        [Action(5)]
        public class PriceGroupSelectionAction : PriceGroupSelectionActionBase
        {
            public PriceGroupSelectionAction(AuctionRoom room) : base(room)
            {
            }
        }

        [Action(6)]
        public class PriceSelectionAction : PriceSelectionActionBase
        {
            public PriceSelectionAction(AuctionRoom room) : base(room)
            {
            }
        }

        [Action(7)]
        public class QuantitySelectionAction : QuantitySelectionActionBase
        {
            public QuantitySelectionAction(AuctionRoom room) : base(room)
            {
            }
        }
    }
}