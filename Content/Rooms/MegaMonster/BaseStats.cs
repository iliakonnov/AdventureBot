using System.Collections.Generic;
using System.Linq;

namespace Content.Rooms.MegaMonster
{
    public class BaseStats
    {
        private static readonly IReadOnlyCollection<RaceStats> Races = new[]
        {
            new RaceStats
            {
                Artifact = true,
                Gold = Level.Few,
                KnowledgeGroup = Knowledge.Strength,
                KnowledgeLevel = Level.Few,
                Name = "Гоблина",
                Defence = Level.Few,
                DefencedPlaces = Place.None,
                Damage = 10,
                Health = 50
            },
            new RaceStats
            {
                Artifact = true,
                Gold = Level.Few,
                KnowledgeGroup = Knowledge.Strength,
                KnowledgeLevel = Level.Medium,
                Name = "Скелета",
                Defence = Level.Medium,
                DefencedPlaces = Place.Legs,
                Damage = 15,
                Health = 60
            },
            new RaceStats
            {
                Artifact = true,
                Gold = Level.Few,
                KnowledgeGroup = Knowledge.Strength,
                KnowledgeLevel = Level.Many,
                Name = "Вампира",
                Defence = Level.Many,
                DefencedPlaces = Place.Body | Place.Legs,
                Damage = 25,
                Health = 80
            },
            new RaceStats
            {
                Artifact = true,
                Gold = Level.Few,
                KnowledgeGroup = Knowledge.Intelligence,
                KnowledgeLevel = Level.Few,
                Name = "Призрака",
                Defence = Level.Few,
                DefencedPlaces = Place.None,
                Damage = 10,
                Health = 50
            },
            new RaceStats
            {
                Artifact = true,
                Gold = Level.Few,
                KnowledgeGroup = Knowledge.Intelligence,
                KnowledgeLevel = Level.Medium,
                Name = "Фею",
                Defence = Level.Medium,
                DefencedPlaces = Place.Body,
                Damage = 20,
                Health = 45
            },
            new RaceStats
            {
                Artifact = true,
                Gold = Level.Few,
                KnowledgeGroup = Knowledge.Intelligence,
                KnowledgeLevel = Level.Many,
                Name = "Мага",
                Defence = Level.Many,
                DefencedPlaces = Place.Head | Place.Legs,
                Damage = 30,
                Health = 60
            },
            new RaceStats
            {
                Artifact = true,
                Gold = Level.Medium,
                KnowledgeGroup = Knowledge.Strength,
                KnowledgeLevel = Level.Few,
                Name = "Гремлина",
                Defence = Level.Few,
                DefencedPlaces = Place.Head,
                Damage = 15,
                Health = 35
            },
            new RaceStats
            {
                Artifact = true,
                Gold = Level.Medium,
                KnowledgeGroup = Knowledge.Strength,
                KnowledgeLevel = Level.Medium,
                Name = "Циклопа",
                Defence = Level.Medium,
                DefencedPlaces = Place.Body,
                Damage = 30,
                Health = 60
            },
            new RaceStats
            {
                Artifact = true,
                Gold = Level.Medium,
                KnowledgeGroup = Knowledge.Strength,
                KnowledgeLevel = Level.Many,
                Name = "Гнома",
                Defence = Level.Many,
                DefencedPlaces = Place.Head | Place.Body | Place.Legs,
                Damage = 30,
                Health = 80
            },
            new RaceStats
            {
                Artifact = true,
                Gold = Level.Medium,
                KnowledgeGroup = Knowledge.Intelligence,
                KnowledgeLevel = Level.Few,
                Name = "Пегаса",
                Defence = Level.Few,
                DefencedPlaces = Place.Body | Place.Legs,
                Damage = 20,
                Health = 45
            },
            new RaceStats
            {
                Artifact = true,
                Gold = Level.Medium,
                KnowledgeGroup = Knowledge.Intelligence,
                KnowledgeLevel = Level.Medium,
                Name = "Чёрта",
                Defence = Level.Medium,
                DefencedPlaces = Place.Head | Place.Legs,
                Damage = 30,
                Health = 70
            },
            new RaceStats
            {
                Artifact = true,
                Gold = Level.Medium,
                KnowledgeGroup = Knowledge.Intelligence,
                KnowledgeLevel = Level.Many,
                Name = "Элементаля",
                Defence = Level.Many,
                DefencedPlaces = Place.None,
                Damage = 40,
                Health = 100
            },
            new RaceStats
            {
                Artifact = true,
                Gold = Level.Many,
                KnowledgeGroup = Knowledge.Strength,
                KnowledgeLevel = Level.Few,
                Name = "Нагу",
                Defence = Level.Few,
                DefencedPlaces = Place.Legs,
                Damage = 25,
                Health = 65
            },
            new RaceStats
            {
                Artifact = true,
                Gold = Level.Many,
                KnowledgeGroup = Knowledge.Strength,
                KnowledgeLevel = Level.Medium,
                Name = "Горгулью",
                Defence = Level.Medium,
                DefencedPlaces = Place.Body,
                Damage = 35,
                Health = 70
            },
            new RaceStats
            {
                Artifact = true,
                Gold = Level.Many,
                KnowledgeGroup = Knowledge.Strength,
                KnowledgeLevel = Level.Many,
                Name = "Демона",
                Defence = Level.Many,
                DefencedPlaces = Place.Head | Place.Body | Place.Legs,
                Damage = 50,
                Health = 120
            },
            new RaceStats
            {
                Artifact = true,
                Gold = Level.Many,
                KnowledgeGroup = Knowledge.Intelligence,
                KnowledgeLevel = Level.Few,
                Name = "Эльфа",
                Defence = Level.Few,
                DefencedPlaces = Place.Body | Place.Legs,
                Damage = 45,
                Health = 55
            },
            new RaceStats
            {
                Artifact = true,
                Gold = Level.Many,
                KnowledgeGroup = Knowledge.Intelligence,
                KnowledgeLevel = Level.Medium,
                Name = "Джинна",
                Defence = Level.Medium,
                DefencedPlaces = Place.Legs,
                Damage = 50,
                Health = 80
            },
            new RaceStats
            {
                Artifact = true,
                Gold = Level.Many,
                KnowledgeGroup = Knowledge.Intelligence,
                KnowledgeLevel = Level.Many,
                Name = "Феникса",
                Defence = Level.Many,
                DefencedPlaces = Place.None,
                Damage = 60,
                Health = 150
            },
            new RaceStats
            {
                Artifact = false,
                Gold = Level.Few,
                KnowledgeGroup = Knowledge.Strength,
                KnowledgeLevel = Level.Few,
                Name = "Грифона",
                Defence = Level.Few,
                DefencedPlaces = Place.Body,
                Damage = 20,
                Health = 70
            },
            new RaceStats
            {
                Artifact = false,
                Gold = Level.Few,
                KnowledgeGroup = Knowledge.Strength,
                KnowledgeLevel = Level.Medium,
                Name = "Минотавра",
                Defence = Level.Medium,
                DefencedPlaces = Place.Head | Place.Legs,
                Damage = 35,
                Health = 80
            },
            new RaceStats
            {
                Artifact = false,
                Gold = Level.Few,
                KnowledgeGroup = Knowledge.Strength,
                KnowledgeLevel = Level.Many,
                Name = "Голема",
                Defence = Level.Many,
                DefencedPlaces = Place.None,
                Damage = 50,
                Health = 100
            },
            new RaceStats
            {
                Artifact = false,
                Gold = Level.Few,
                KnowledgeGroup = Knowledge.Intelligence,
                KnowledgeLevel = Level.Few,
                Name = "Мантикору",
                Defence = Level.Few,
                DefencedPlaces = Place.Legs,
                Damage = 25,
                Health = 65
            },
            new RaceStats
            {
                Artifact = false,
                Gold = Level.Few,
                KnowledgeGroup = Knowledge.Intelligence,
                KnowledgeLevel = Level.Medium,
                Name = "Единорога",
                Defence = Level.Medium,
                DefencedPlaces = Place.Head | Place.Legs,
                Damage = 40,
                Health = 75
            },
            new RaceStats
            {
                Artifact = false,
                Gold = Level.Few,
                KnowledgeGroup = Knowledge.Intelligence,
                KnowledgeLevel = Level.Many,
                Name = "Друида",
                Defence = Level.Many,
                DefencedPlaces = Place.Body | Place.Legs,
                Damage = 55,
                Health = 110
            },
            new RaceStats
            {
                Artifact = false,
                Gold = Level.Medium,
                KnowledgeGroup = Knowledge.Strength,
                KnowledgeLevel = Level.Few,
                Name = "Зомби",
                Defence = Level.Few,
                DefencedPlaces = Place.None,
                Damage = 15,
                Health = 60
            },
            new RaceStats
            {
                Artifact = false,
                Gold = Level.Medium,
                KnowledgeGroup = Knowledge.Strength,
                KnowledgeLevel = Level.Medium,
                Name = "Орка",
                Defence = Level.Medium,
                DefencedPlaces = Place.Body,
                Damage = 45,
                Health = 90
            },
            new RaceStats
            {
                Artifact = false,
                Gold = Level.Medium,
                KnowledgeGroup = Knowledge.Strength,
                KnowledgeLevel = Level.Many,
                Name = "Огра",
                Defence = Level.Many,
                DefencedPlaces = Place.Legs,
                Damage = 55,
                Health = 135
            },
            new RaceStats
            {
                Artifact = false,
                Gold = Level.Medium,
                KnowledgeGroup = Knowledge.Intelligence,
                KnowledgeLevel = Level.Few,
                Name = "Виверну",
                Defence = Level.Few,
                DefencedPlaces = Place.None,
                Damage = 30,
                Health = 55
            },
            new RaceStats
            {
                Artifact = false,
                Gold = Level.Medium,
                KnowledgeGroup = Knowledge.Intelligence,
                KnowledgeLevel = Level.Medium,
                Name = "Монаха",
                Defence = Level.Medium,
                DefencedPlaces = Place.Body | Place.Legs,
                Damage = 35,
                Health = 70
            },
            new RaceStats
            {
                Artifact = false,
                Gold = Level.Medium,
                KnowledgeGroup = Knowledge.Intelligence,
                KnowledgeLevel = Level.Many,
                Name = "Лича",
                Defence = Level.Many,
                DefencedPlaces = Place.Head | Place.Body | Place.Legs,
                Damage = 65,
                Health = 150
            },
            new RaceStats
            {
                Artifact = false,
                Gold = Level.Many,
                KnowledgeGroup = Knowledge.Strength,
                KnowledgeLevel = Level.Few,
                Name = "Василиска",
                Defence = Level.Few,
                DefencedPlaces = Place.None,
                Damage = 30,
                Health = 85
            },
            new RaceStats
            {
                Artifact = false,
                Gold = Level.Many,
                KnowledgeGroup = Knowledge.Strength,
                KnowledgeLevel = Level.Medium,
                Name = "Цербера",
                Defence = Level.Medium,
                DefencedPlaces = Place.Head,
                Damage = 50,
                Health = 95
            },
            new RaceStats
            {
                Artifact = false,
                Gold = Level.Many,
                KnowledgeGroup = Knowledge.Strength,
                KnowledgeLevel = Level.Many,
                Name = "Кентавра",
                Defence = Level.Many,
                DefencedPlaces = Place.Body | Place.Legs,
                Damage = 60,
                Health = 140
            },
            new RaceStats
            {
                Artifact = false,
                Gold = Level.Many,
                KnowledgeGroup = Knowledge.Intelligence,
                KnowledgeLevel = Level.Few,
                Name = "Горгону",
                Defence = Level.Few,
                DefencedPlaces = Place.Head,
                Damage = 25,
                Health = 60
            },
            new RaceStats
            {
                Artifact = false,
                Gold = Level.Many,
                KnowledgeGroup = Knowledge.Intelligence,
                KnowledgeLevel = Level.Medium,
                Name = "Дракона",
                Defence = Level.Medium,
                DefencedPlaces = Place.None,
                Damage = 45,
                Health = 100
            },
            new RaceStats
            {
                Artifact = false,
                Gold = Level.Many,
                KnowledgeGroup = Knowledge.Intelligence,
                KnowledgeLevel = Level.Many,
                Name = "Дьявола",
                Defence = Level.Many,
                DefencedPlaces = Place.Head | Place.Body | Place.Legs,
                Damage = 65,
                Health = 170
            }
        };

        public bool Artifact;
        public Level Gold;
        public Knowledge KnowledgeGroup;
        public Level KnowledgeLevel;

        public RaceStats LoadRace()
        {
            var result = Races.FirstOrDefault(r =>
                             r.Artifact == Artifact
                             && r.Gold == Gold
                             && r.KnowledgeGroup == KnowledgeGroup
                             && r.KnowledgeLevel == KnowledgeLevel
                         ) ?? Races.First();

            return (RaceStats) result.MemberwiseClone();
        }
    }
}