using System;
using AdventureBot;

namespace Content.Town.Auction
{
    public interface IState<out T> where T: IState<T>
    {
        T Deserialize(VariableContainer container);
        VariableContainer Serialize();
        string StateId { get; }
    }

    public static class StateContainer
    {
        public static T Deserialize<T>(VariableContainer container) where T : IState<T>, new()
        {
            var deserializer = new T();

            var stateId = container.Get<Serializable.String>("stateId");
            if (stateId != deserializer.StateId)
            {
                throw new ArgumentException(
                    $"Cannot deserialize state {deserializer.StateId} instead of saved state {stateId}",
                    nameof(container));
            }

            var innerState = container.Get<VariableContainer>("state");
            return deserializer.Deserialize(innerState);
        }

        public static VariableContainer Serialize<T>(IState<T> state) where T : IState<T>
        {
            var container = new VariableContainer();
            container.Set("stateId", new Serializable.String(state.StateId));

            var innerState = state.Serialize();
            container.Set("state", innerState);

            return container;
        }
    }

    public class BuySellState : IState<BuySellState>
    {
        public string StateId => nameof(BuySellState);

        public bool Selling;
        public string SelectedItemId;
        public decimal SelectedItemPrice;
        public int? SelectedItemCount;

        public VariableContainer Serialize()
        {
            var result = new VariableContainer();
            result.Set("Selling", new Serializable.Bool(Selling));
            result.Set("SelectedItemId", new Serializable.String(SelectedItemId));
            result.Set("SelectedItemPrice", new Serializable.Decimal(SelectedItemPrice));
            if (SelectedItemCount != null)
            {
                result.Set("SelectedItemCount", new Serializable.Int((int) SelectedItemCount));
            }
            return result;
        }

        public BuySellState Deserialize(VariableContainer container)
        {
            return new BuySellState
            {
                Selling = container.Get<Serializable.Bool>("Selling"),
                SelectedItemId = container.Get<Serializable.String>("SelectedItemId"),
                SelectedItemPrice = container.Get<Serializable.Decimal>("SelectedItemPrice"),
                SelectedItemCount = (int?) container.Get<Serializable.Int>("SelectedItemCount")
            };
        }
    }
    
    public class AddOfferState : IState<AddOfferState>
    {
        public string SelectedItemId;
        public int SelectedPriceGroup;
        public int SelectedItemPrice;
        public int MaxQuantityAvailable;
        public int QuantitySelected;
        public bool Selling;
        
        public AddOfferState Deserialize(VariableContainer container)
        {
            return new AddOfferState
            {
                SelectedItemId = container.Get<Serializable.String>("SelectedItemId"),
                SelectedPriceGroup = container.Get<Serializable.Int>("SelectedPriceGroup"),
                SelectedItemPrice = container.Get<Serializable.Int>("SelectedItemPrice"),
                MaxQuantityAvailable = container.Get<Serializable.Int>("MaxQuantityAvailable"),
                QuantitySelected = container.Get<Serializable.Int>("QuantitySelected"),
                Selling = container.Get<Serializable.Bool>("Selling")
            };
        }

        public VariableContainer Serialize()
        {
            var result = new VariableContainer();
            result.Set("SelectedItemId", new Serializable.String(SelectedItemId));
            result.Set("SelectedPriceGroup", new Serializable.Int(SelectedPriceGroup));
            result.Set("SelectedItemPrice", new Serializable.Int(SelectedItemPrice));
            result.Set("MaxQuantityAvailable", new Serializable.Int(MaxQuantityAvailable));
            result.Set("QuantitySelected", new Serializable.Int(QuantitySelected));
            result.Set("Selling", new Serializable.Bool(Selling));
            return result;
        }

        public string StateId => "AddOfferState";
    }
}