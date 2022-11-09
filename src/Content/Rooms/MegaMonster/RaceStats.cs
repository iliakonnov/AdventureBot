using System;
using System.Collections.Generic;

namespace Content.Rooms.MegaMonster;

public class RaceStats : BaseStats
{
    private static readonly IReadOnlyDictionary<MonsterProperty, IReadOnlyDictionary<MutateResult, string>>
        _modifiers = new Dictionary<MonsterProperty, IReadOnlyDictionary<MutateResult, string>>
        {
            {
                MonsterProperty.Artifact, new Dictionary<MutateResult, string>
                {
                    {MutateResult.Decrease, "Минималистичного"},
                    {MutateResult.DecreaseMany, "Очень минималистичного"},
                    {MutateResult.Increase, "Максималистичного"},
                    {MutateResult.IncreaseMany, "Очень максималистичного"}
                }
            },
            {
                MonsterProperty.Damage, new Dictionary<MutateResult, string>
                {
                    {MutateResult.Decrease, "Слабого"},
                    {MutateResult.DecreaseMany, "Очень слабого"},
                    {MutateResult.Increase, "Сильного"},
                    {MutateResult.IncreaseMany, "Очень слабого"}
                }
            },
            {
                MonsterProperty.DefenceLevel, new Dictionary<MutateResult, string>
                {
                    {MutateResult.Decrease, "Мягкого"},
                    {MutateResult.DecreaseMany, "Очень мягкого"},
                    {MutateResult.Increase, "Крепкого"},
                    {MutateResult.IncreaseMany, "Очень крепкого"}
                }
            },
            {
                MonsterProperty.Gold, new Dictionary<MutateResult, string>
                {
                    {MutateResult.Decrease, "Щедрого"},
                    {MutateResult.DecreaseMany, "Очень щедрого"},
                    {MutateResult.Increase, "Жадного"},
                    {MutateResult.IncreaseMany, "Очень жадного"}
                }
            },
            {
                MonsterProperty.Health, new Dictionary<MutateResult, string>
                {
                    {MutateResult.Decrease, "Больного"},
                    {MutateResult.DecreaseMany, "Очень больного"},
                    {MutateResult.Increase, "Здорового"},
                    {MutateResult.IncreaseMany, "Очень здорового"}
                }
            },
            {
                MonsterProperty.KnowledgeLevel, new Dictionary<MutateResult, string>
                {
                    {MutateResult.Decrease, "Глупого"},
                    {MutateResult.DecreaseMany, "Очень глупого"},
                    {MutateResult.Increase, "Умного"},
                    {MutateResult.IncreaseMany, "Очень умного"}
                }
            }
        };

    public readonly List<string> Modifiers = new();
    public decimal Damage;
    public Level Defence;
    public Place DefencedPlaces;
    public decimal Health;

    public string Name;

    private void Modify(MutateResult mutate, MonsterProperty property)
    {
        Modifiers.Add(_modifiers[property][mutate]);
    }

    private Level Modifiy(Level before, Level after, MonsterProperty property)
    {
        switch (after)
        {
            case Level.Few when before == Level.Medium:
                Modify(MutateResult.Decrease, property);
                break;
            case Level.Few when before == Level.Many:
                Modify(MutateResult.DecreaseMany, property);
                break;
            case Level.Medium when before == Level.Many:
                Modify(MutateResult.Increase, property);
                break;
            case Level.Medium when before == Level.Few:
                Modify(MutateResult.DecreaseMany, property);
                break;
            case Level.Many when before == Level.Medium:
                Modify(MutateResult.Increase, property);
                break;
            case Level.Many when before == Level.Few:
                Modify(MutateResult.IncreaseMany, property);
                break;
        }

        return after;
    }

    private decimal Modify(decimal before, decimal after, MonsterProperty property)
    {
        // 0%-15% -- Same
        // 15% - 30% -- Different
        // 30% -- 50% -- Very different

        var diff = after / before - 1;
        var abs = Math.Abs(diff);

        if (abs > 0.3M)
        {
            // Very differnet
            Modify(diff > 0
                ? MutateResult.IncreaseMany
                : MutateResult.DecreaseMany, property);
        }
        else if (abs > 0.15M)
        {
            // Different
            Modify(diff > 0
                ? MutateResult.Increase
                : MutateResult.Decrease, property);
        }

        return after;
    }

    public void Mutate(Level newVal, MonsterProperty property)
    {
        switch (property)
        {
            case MonsterProperty.Gold:
                Gold = Modifiy(Gold, newVal, property);
                break;
            case MonsterProperty.KnowledgeLevel:
                KnowledgeLevel = Modifiy(KnowledgeLevel, newVal, property);
                break;
            case MonsterProperty.DefenceLevel:
                Defence = Modifiy(Defence, newVal, property);
                break;
            case MonsterProperty.Damage:
            case MonsterProperty.Health:
            case MonsterProperty.KnowledgeGroup:
            case MonsterProperty.Artifact:
                throw new ArgumentException($"Cannot set Level to {property}", nameof(property));

            default:
                throw new ArgumentOutOfRangeException(nameof(property), property, null);
        }
    }

    public void Mutate(decimal newVal, MonsterProperty property)
    {
        switch (property)
        {
            case MonsterProperty.Damage:
                Damage = Modify(Damage, newVal, property);
                break;
            case MonsterProperty.Health:
                Health = Modify(Health, newVal, property);
                break;
            case MonsterProperty.Artifact:
            case MonsterProperty.DefenceLevel:
            case MonsterProperty.KnowledgeLevel:
            case MonsterProperty.KnowledgeGroup:
            case MonsterProperty.Gold:
                throw new ArgumentException($"Cannot set decimal to {property}", nameof(property));
            default:
                throw new ArgumentOutOfRangeException(nameof(property), property, null);
        }
    }

    public void Mutate(bool newVal, MonsterProperty property)
    {
        switch (property)
        {
            case MonsterProperty.Artifact:
            {
                switch (newVal)
                {
                    case true when !Artifact:
                        Modify(MutateResult.Increase, MonsterProperty.Artifact);
                        break;
                    case false when Artifact:
                        Modify(MutateResult.Decrease, MonsterProperty.Artifact);
                        break;
                }

                Artifact = newVal;

                break;
            }
            case MonsterProperty.DefenceLevel:
            case MonsterProperty.KnowledgeLevel:
            case MonsterProperty.KnowledgeGroup:
            case MonsterProperty.Gold:
            case MonsterProperty.Damage:
            case MonsterProperty.Health:
                throw new ArgumentException($"Cannot set bool to {property}", nameof(property));
            default:
                throw new ArgumentOutOfRangeException(nameof(property), property, null);
        }
    }

    public void Mutate(Knowledge newVal, MonsterProperty property)
    {
        switch (property)
        {
            case MonsterProperty.KnowledgeGroup:
                switch (newVal)
                {
                    case Knowledge.Strength:
                        Modifiers.Add("Спортивного");
                        break;
                    case Knowledge.Intelligence:
                        Modifiers.Add("Магического");
                        break;
                    default:
                        throw new ArgumentOutOfRangeException(nameof(newVal), newVal, null);
                }

                break;
            case MonsterProperty.Artifact:
            case MonsterProperty.DefenceLevel:
            case MonsterProperty.KnowledgeLevel:
            case MonsterProperty.Gold:
            case MonsterProperty.Damage:
            case MonsterProperty.Health:
                throw new ArgumentException($"Cannot set bool to {property}", nameof(property));
            default:
                throw new ArgumentOutOfRangeException(nameof(property), property, null);
        }
    }

    public override string ToString()
    {
        return
            $"{nameof(Modifiers)}: {Modifiers}, {nameof(Name)}: {Name}, {nameof(Defence)}: {Defence}, {nameof(DefencedPlaces)}: {DefencedPlaces}, {nameof(Damage)}: {Damage}, {nameof(Health)}: {Health}";
    }
}