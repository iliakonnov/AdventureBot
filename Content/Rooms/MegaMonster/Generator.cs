using System;
using System.Collections.Generic;
using System.Linq;
using AdventureBot.Item;
using AdventureBot.ObjectManager;

namespace Content.Rooms.MegaMonster
{
    public static class Generator
    {
        public static ResultStats GenerateStats(Random random)
        {
            var stats = new BaseStats
            {
                Artifact = random.NextDouble() < 0.5,
                Gold = (Level) random.Next(0, 3),
                KnowledgeGroup = (Knowledge) random.Next(0, 2),
                KnowledgeLevel = (Level) random.Next(0, 3)
            };
            var race = stats.LoadRace();
            Mutate(race, random);
            var result = Shuffle(race, random);
            return result;
        }

        private static void Mutate(RaceStats stats, MonsterProperty property, Random random)
        {
            switch (property)
            {
                case MonsterProperty.Artifact:
                {
                    stats.Mutate(random.NextDouble() < 0.5, property);
                    break;
                }
                case MonsterProperty.DefenceLevel:
                case MonsterProperty.KnowledgeLevel:
                case MonsterProperty.Gold:
                {
                    stats.Mutate((Level) random.Next(0, 3), property);
                    break;
                }
                case MonsterProperty.KnowledgeGroup:
                {
                    stats.Mutate((Knowledge) random.Next(0, 2), property);
                    break;
                }
                case MonsterProperty.Damage:
                {
                    stats.Mutate(stats.Damage * ((decimal) random.NextDouble() - 0.5M + 1), property);
                    break;
                }
                case MonsterProperty.Health:
                {
                    stats.Mutate(stats.Health * ((decimal) random.NextDouble() - 0.5M + 1), property);
                    break;
                }
                default:
                {
                    throw new ArgumentOutOfRangeException(nameof(property), property, null);
                }
            }
        }

        private static void Mutate(RaceStats stats, Random random)
        {
            var mutated = new HashSet<MonsterProperty>();
            for (var i = 0; i < random.Next(1, 4); i++)
            {
                MonsterProperty prop;
                do
                {
                    prop = (MonsterProperty) random.Next(0, 7);
                } while (mutated.Contains(prop));

                mutated.Add(prop);
                Mutate(stats, prop, random);
            }
        }

        private static decimal Shuffle(decimal value, Random random)
        {
            return value * ((decimal) random.NextDouble() * 0.4M - 0.2M + 1);
        }

        private static decimal LevelToNum(Level level, decimal few, decimal medium, decimal many)
        {
            switch (level)
            {
                case Level.Few:
                    return few;
                case Level.Medium:
                    return medium;
                case Level.Many:
                    return many;
                default:
                    throw new ArgumentOutOfRangeException(nameof(level), level, null);
            }
        }

        private static ResultStats Shuffle(RaceStats stats, Random random)
        {
            string artifact = null;
            if (stats.Artifact)
            {
                var manager = ObjectManager<IItem>.Instance.Get<ItemManager>();
                var items = manager.Items()
                    .Where(i => manager.Get(i.Identificator)?.Effect != null)
                    .ToList();
                artifact = items[random.Next(0, items.Count)].Identificator;
            }

            return new ResultStats
            {
                Name = $"{string.Join(" ", stats.Modifiers)} {stats.Name}",
                Damage = Shuffle(stats.Damage, random),
                Health = Shuffle(stats.Health, random),
                Defence = Shuffle(LevelToNum(stats.Defence, 10, 25, 40), random),
                DefencedPlaces = stats.DefencedPlaces,
                Gold = Shuffle(LevelToNum(stats.Gold, 30, 150, 300), random),
                ArtifactId = artifact,
                KnowledgeGroup = stats.KnowledgeGroup,
                KnowledgeMinimal = Shuffle(LevelToNum(stats.KnowledgeLevel, 10, 30, 60), random),
                KnowledgeRequired = Shuffle(LevelToNum(stats.KnowledgeLevel, 20, 50, 70), random)
            };
        }
    }
}