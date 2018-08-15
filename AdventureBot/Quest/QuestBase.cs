using System;

namespace AdventureBot.Quest
{
    public abstract class QuestBase : IQuest
    {
        protected VariableContainer GetQuestVariables(User.User user, Guid questId)
        {
            return user.VariableManager.GetQuestVariables(Identifer, questId);
        }

        public abstract string Identifer { get; }
        public abstract string GetName(User.User user, Guid questId);
        public abstract decimal GetProgress(User.User user, Guid questId);
        public abstract void Finish(User.User user, Guid questId);
        public abstract void Begin(User.User user, Guid questId);
    }
}