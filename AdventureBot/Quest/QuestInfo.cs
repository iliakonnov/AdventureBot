using System;
using AdventureBot.ObjectManager;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot.Quest;

[MessagePackObject(true)]
public class QuestInfo
{
    public QuestInfo(IQuest quest)
    {
        Quest = quest;
        Identifier = quest.Identifer;
        QuestId = Guid.NewGuid();
    }

    [SerializationConstructor]
    public QuestInfo(string identifier, Guid questId)
    {
        Identifier = identifier;
        QuestId = questId;

        var quest = ObjectManager<IQuest>.Instance.Get<QuestManager>().Get(identifier);
        Quest = quest ?? throw new ArgumentException($"Quest with identifier '{identifier}' not found!");
    }

    public string Identifier { get; }
    public Guid QuestId { get; }
    [IgnoreMember] [NotNull] public IQuest Quest { get; }
}