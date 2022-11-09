using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Linq;
using AdventureBot.ObjectManager;
using AdventureBot.Quest;
using MessagePack;

namespace AdventureBot.User;

[MessagePackObject]
public class QuestManager
{
    [Key("quests")] private readonly Dictionary<string, Dictionary<Guid, QuestInfo>> _quests = new();

    [IgnoreMember] internal User User;

    [SerializationConstructor]
    public QuestManager(Dictionary<string, Dictionary<Guid, QuestInfo>> quests)
    {
        _quests = quests;
    }

    public QuestManager(User user)
    {
        User = user;
    }

    [IgnoreMember]
    public ImmutableDictionary<string, ImmutableDictionary<Guid, QuestInfo>> Quests =>
        _quests.ToDictionary(kv => kv.Key, kv => kv.Value.ToImmutableDictionary()).ToImmutableDictionary();

    public Guid BeginQuest(string id)
    {
        var quest = ObjectManager<IQuest>.Instance.Get<Quest.QuestManager>().Get(id);
        if (quest == null)
        {
            throw new ArgumentException($"Quest with id '{id}' not found");
        }

        var info = new QuestInfo(quest);
        if (!_quests.TryGetValue(id, out var quests))
        {
            quests = new Dictionary<Guid, QuestInfo>();
            _quests[id] = quests;
        }

        quests[info.QuestId] = info;
        info.Quest.Begin(User, info.QuestId);
        return info.QuestId;
    }

    public bool FinishQuest(string id, Guid questId)
    {
        var quest = ObjectManager<IQuest>.Instance.Get<Quest.QuestManager>().Get(id);
        if (quest == null)
        {
            throw new ArgumentException($"Quest with id '{id}' not found");
        }

        if (!_quests.TryGetValue(id, out var quests) || !quests.TryGetValue(questId, out var info))
        {
            return false;
        }

        info.Quest.Finish(User, info.QuestId);
        quests.Remove(questId);

        return true;
    }
}