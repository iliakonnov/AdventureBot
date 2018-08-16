using System;
using System.Collections.Immutable;

namespace AdventureBot.Quest
{
    public abstract class QuestBase : IQuest
    {
        protected VariableContainer GetQuestVariables(User.User user, Guid questId)
        {
            return user.VariableManager.GetQuestVariables(Identifer, questId);
        }
        
        protected ImmutableDictionary<Guid, QuestInfo> GetQuestInstances(User.User user)
        {
            return user.QuestManager.Quests[Identifer];
        }

        public abstract string Identifer { get; }
        public abstract string GetName(User.User user, Guid questId);
        public abstract decimal GetProgress(User.User user, Guid questId);
        public abstract void Finish(User.User user, Guid questId);
        public abstract void Begin(User.User user, Guid questId);
    }
}