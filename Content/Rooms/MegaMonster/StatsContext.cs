using System;
using AdventureBot;

namespace Content.Rooms.MegaMonster
{
    public class StatsContext : IDisposable
    {
        public readonly ResultStats Stats;
        private readonly VariableContainer _roomVariables;

        public StatsContext(Random random, VariableContainer roomVariables)
        {
            _roomVariables = roomVariables;
            
            var container = roomVariables.Get<VariableContainer>("monster_stats");
            Stats = container != null
                ? ResultStats.Deserialize(container)
                : Generator.GenerateStats(random);
        }

        public void Dispose()
        {
            var container = new VariableContainer();
            Stats.Serialize(container);
            _roomVariables.Set("monster_stats", container);
        }
    }
}