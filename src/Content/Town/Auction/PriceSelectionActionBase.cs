using System.Linq;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;

namespace Content.Town.Auction;

public abstract class PriceSelectionActionBase : ActionBase<AuctionRoom>
{
    protected PriceSelectionActionBase(AuctionRoom room) : base(room)
    {
    }

    public void Enter(User user)
    {
        var state = StateContainer.Deserialize<AddOfferState>(
            Room.GetRoomVariables(user).Get<VariableContainer>("state")
        );
        var prices = Math.GetSubPrices(state.SelectedPriceGroup)
            .OrderBy(x => x)
            .Select(x => new[] {x.ToString()})
            .Concat(new[] {new[] {"Назад"}})
            .ToArray();
        Room.SendMessage(user, "Выберите стоимость из списка", prices);
    }

    [Fallback]
    public void Fallback(User user, ReceivedMessage message)
    {
        var state = StateContainer.Deserialize<AddOfferState>(
            Room.GetRoomVariables(user).Get<VariableContainer>("state")
        );
        var prices = Math.GetSubPrices(state.SelectedPriceGroup).ToList();

        if (int.TryParse(message.Text, out var price) && prices.Contains(price))
        {
            state.SelectedItemPrice = price;
            Room.GetRoomVariables(user).Set("state", StateContainer.Serialize(state));
            Room.SwitchAction<AuctionRoom.QuantitySelectionAction>(user);
            Room.GetAction<AuctionRoom.QuantitySelectionAction>().Enter(user);
            return;
        }

        Enter(user);
    }

    [Button("Назад")]
    public void Back(User user, ReceivedMessage message)
    {
        Room.SwitchAction<AuctionRoom.PriceGroupSelectionAction>(user);
        Room.GetAction<AuctionRoom.PriceGroupSelectionAction>().Enter(user);
    }
}