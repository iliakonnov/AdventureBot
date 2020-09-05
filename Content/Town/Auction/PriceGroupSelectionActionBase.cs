using System.Linq;
using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.Room.BetterRoom;
using AdventureBot.User;

namespace Content.Town.Auction
{
    public abstract class PriceGroupSelectionActionBase : ActionBase<AuctionRoom>
    {
        protected PriceGroupSelectionActionBase(AuctionRoom room) : base(room)
        {
        }

        public void Enter(User user)
        {
            var prices = Math.GetPrices()
                .OrderBy(x => x.Item1)
                .Select(x => new[] {$"{x.Item1} — {x.Item2}"})
                .Concat(new[] {new[] {"Назад"}})
                .ToArray();
            Room.SendMessage(user, "Выберите стоимость предмета", prices);
        }

        [Fallback]
        public void Fallback(User user, ReceivedMessage message)
        {
            var priceGroups = Math.GetPrices().ToList();
            var splitted = message.Text.Split('—');
            if (splitted.Length == 2 && int.TryParse(splitted[0], out var beginning))
            {
                for (var i = 0; i < priceGroups.Count; i++)
                {
                    if (priceGroups[i].Item1 != beginning)
                    {
                        continue;
                    }

                    var state = StateContainer.Deserialize<AddOfferState>(
                        Room.GetRoomVariables(user).Get<VariableContainer>("state")
                    );
                    state.SelectedPriceGroup = i;
                    Room.GetRoomVariables(user).Set("state", StateContainer.Serialize(state));
                    Room.SwitchAction<AuctionRoom.PriceSelectionAction>(user);
                    Room.GetAction<AuctionRoom.PriceSelectionAction>().Enter(user);
                    return;
                }
            }

            Enter(user);
        }

        [Button("Назад")]
        public void Back(User user, ReceivedMessage message)
        {
            Room.SwitchAction<AuctionRoom.AddOfferAction>(user);
            Room.GetAction<AuctionRoom.AddOfferAction>().Enter(user);
        }
    }
}