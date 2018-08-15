using System;
using System.Collections.Generic;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot.User
{
    [MessagePackObject]
    public class VariableManager
    {
        [Key("ItemVariables")]
        private Dictionary<string, VariableContainer> _itemVariables = new Dictionary<string, VariableContainer>();

        [Key("QuestVariables")] private Dictionary<string, Dictionary<Guid, VariableContainer>> _questVariables =
            new Dictionary<string, Dictionary<Guid, VariableContainer>>();

        [Key("RoomVariables")]
        private Dictionary<string, VariableContainer> _roomVariables = new Dictionary<string, VariableContainer>();

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
            Dictionary<string, Dictionary<Guid, VariableContainer>> questVariables,
            VariableContainer persistentVariables,
            VariableContainer userVariables)
        {
            _roomVariables = roomVariables;
            _itemVariables = itemVariables;
            _questVariables = questVariables;
            PersistentVariables = persistentVariables;
            UserVariables = userVariables;
        }

        internal void Reset()
        {
            _roomVariables = new Dictionary<string, VariableContainer>();
            _itemVariables = new Dictionary<string, VariableContainer>();
            _questVariables = new Dictionary<string, Dictionary<Guid, VariableContainer>>();
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

        internal VariableContainer GetQuestVariables(string identifier, Guid questId)
        {
            if (!_questVariables.TryGetValue(identifier, out var variables))
            {
                variables = new Dictionary<Guid, VariableContainer>();
                _questVariables[identifier] = variables;
            }

            if (!variables.TryGetValue(questId, out var result))
            {
                result = new VariableContainer();
                variables[questId] = result;
            }

            return result;
        }
    }
}