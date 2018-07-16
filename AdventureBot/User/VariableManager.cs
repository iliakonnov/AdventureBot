using System;
using System.Collections.Generic;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot.User
{
    [MessagePackObject()]
    public class VariableManager
    {   
        [Key("RoomVariables")]
        private Dictionary<string, VariableContainer> _roomVariables = new Dictionary<string, VariableContainer>();

        [Key("ItemVariables")]
        private Dictionary<string, VariableContainer> _itemVariables = new Dictionary<string, VariableContainer>();
        
        [Key(nameof(PersistentVariables))] public VariableContainer PersistentVariables = new VariableContainer();

        [Key(nameof(UserVariables))] public VariableContainer UserVariables = new VariableContainer();

        public VariableManager()
        {
        }

        [Obsolete("This constructor for serializer only")]
        [UsedImplicitly]
        [SerializationConstructor]
        public VariableManager(
            Dictionary<string, VariableContainer> roomVariables,
            Dictionary<string, VariableContainer> itemVariables,
            VariableContainer persistentVariables,
            VariableContainer userVariables)
        {
            _roomVariables = roomVariables;
            _itemVariables = itemVariables;
            PersistentVariables = persistentVariables;
            UserVariables = userVariables;
        }

        internal void Reset()
        {
            _roomVariables = new Dictionary<string, VariableContainer>();
            _itemVariables = new Dictionary<string, VariableContainer>();
            UserVariables = new VariableContainer();
        }

        internal VariableContainer GetRoomVariables(string identifier)
        {
            if (!_roomVariables.ContainsKey(identifier))
            {
                _roomVariables[identifier] = new VariableContainer();
            }

            return _roomVariables[identifier];
        }

        internal VariableContainer GetItemVariables(string identifier)
        {
            if (!_itemVariables.ContainsKey(identifier))
            {
                _itemVariables[identifier] = new VariableContainer();
            }

            return _itemVariables[identifier];
        }
    }
}