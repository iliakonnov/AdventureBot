using AdventureBot.Messenger;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;

namespace Content.Town.Auction;

public abstract class MyOffersActionBase : ActionBase<AuctionRoom>
{
    protected MyOffersActionBase(AuctionRoom room) : base(room)
    {
    }

    public void Enter(User user)
    {
        Room.SendMessage(user, "Что вы желаете сделать?", Room.GetButtons(user));
    }

    [Button("Предложить")]
    public void Offer(User user, ReceivedMessage message)
    {
        Room.SwitchAction<AuctionRoom.AddOfferAction>(user);
        Room.GetAction<AuctionRoom.AddOfferAction>().Enter(user);
    }

    [Button("Отменить предложение")]
    public void CancelOffer(User user, ReceivedMessage message)
    {
        Room.SwitchAction<AuctionRoom.RemoveOfferAction>(user);
        Room.GetAction<AuctionRoom.RemoveOfferAction>().Enter(user);
    }

    [Button("Назад")]
    public void Back(User user, ReceivedMessage message)
    {
        Room.SwitchAction<AuctionRoom.MainAction>(user);
        Room.GetAction<AuctionRoom.MainAction>().Enter(user);
    }
}