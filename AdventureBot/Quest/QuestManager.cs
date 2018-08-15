using AdventureBot.ObjectManager;

namespace AdventureBot.Quest
{
    public class QuestAttribute : IdentifiableAttribute
    {
        public QuestAttribute(string identifier) : base(identifier)
        {
        }
    }

    public class QuestManager : StorageManager<IQuest, QuestAttribute>
    {
    }
}