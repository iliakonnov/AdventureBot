using System;
using System.Collections.Generic;
using AdventureBot;
using AdventureBot.ObjectManager;
using AdventureBot.Quest;
using AdventureBot.Room;
using AdventureBot.User;
using RoomManager = AdventureBot.Room.RoomManager;

namespace Content.Quests
{
    public abstract class KillMonsterBase : QuestBase
    {
        protected KillMonsterBase()
        {
            MonsterBase.OnKilled += (user, monster) =>
            {
                foreach (var id in GetQuestInstances(user).Keys)
                {
                    var neededMonster = GetMonsterId(user, id);
                    if (monster.Identifier == neededMonster)
                    {
                        GetQuestVariables(user, id).Set("killed", new Serializable.Bool(true));
                        //user.QuestManager.FinishQuest(Identifer, id);
                    }
                }
            };
        }

        public override string GetName(User user, Guid questId)
        {
            var monsterId = GetMonsterId(user, questId);
            var monster = ObjectManager<IRoom>.Instance.Get<RoomManager>().Get(monsterId);
            var reward = GetReward(user, questId);
            return reward != 0
                ? $"Убить {monster?.Name} за {GetReward(user, questId)} золота"
                : $"Убить {monster?.Name}";
        }

        public override decimal GetProgress(User user, Guid questId)
        {
            return IsFinished(user, questId) ? 100 : 0;
        }

        public override void Finish(User user, Guid questId)
        {
            user.Info.Gold += GetReward(user, questId);
        }

        public override void Begin(User user, Guid questId)
        {
            var mgr = ObjectManager<IRoom>.Instance.Get<RoomManager>();
            var monsters = new List<IMonster>();
            foreach (var key in mgr.Keys())
            {
                var room = mgr.Get(key);
                if (room is IMonster monster)
                {
                    monsters.Add(monster);
                }
            }

            var vars = GetQuestVariables(user, questId);
            vars.Set("killed", new Serializable.Bool(false));
            
            var rand = monsters[user.Random.Next(0, monsters.Count)];
            vars.Set("monster_id", new Serializable.String(rand.Identifier));

            var reward = (decimal) user.Random.Next(50, 250);
            vars.Set("reward", new Serializable.Decimal(reward));
        }

        public string GetMonsterId(User user, Guid guid)
        {
            return GetQuestVariables(user, guid).Get<Serializable.String>("monster_id");
        }
        
        public virtual decimal GetReward(User user, Guid guid)
        {
            return GetQuestVariables(user, guid).Get<Serializable.Decimal>("reward");
        }
        
        public bool IsFinished(User user, Guid guid)
        {
            return GetQuestVariables(user, guid).Get<Serializable.Bool>("killed");
        }
    }

    [Quest(Id)]
    public class KillMonster : KillMonsterBase
    {
        public override string Identifer => Id;
        public const string Id = "quest/kill_monster";
    }
    
    [Quest(Id)]
    public class KillMonsterFree : KillMonsterBase
    {
        public override string Identifer => Id;
        public const string Id = "quest/kill_monster/free";

        public override decimal GetReward(User user, Guid guid)
        {
            return 0;
        }

        public override void Finish(User user, Guid questId)
        {
            user.Info.Level.AddXp(50);
        }
    }
}