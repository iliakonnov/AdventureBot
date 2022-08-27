using AdventureBot;

namespace Content.Rooms.MegaMonster;

public class ResultStats
{
    public string ArtifactId;
    public decimal Damage;
    public decimal Defence;
    public Place DefencedPlaces;
    public decimal Gold;
    public decimal Health;
    public Knowledge KnowledgeGroup;
    public decimal KnowledgeMinimal;
    public decimal KnowledgeRequired;

    public string Name;

    public void Serialize(VariableContainer container)
    {
        container.Set(nameof(ArtifactId), new Serializable.String(ArtifactId));
        container.Set(nameof(Gold), new Serializable.Decimal(Gold));
        container.Set(nameof(KnowledgeGroup), new Serializable.Int((int) KnowledgeGroup));
        container.Set(nameof(KnowledgeMinimal), new Serializable.Decimal(KnowledgeMinimal));
        container.Set(nameof(KnowledgeRequired), new Serializable.Decimal(KnowledgeRequired));

        container.Set(nameof(Name), new Serializable.String(Name));
        container.Set(nameof(Defence), new Serializable.Decimal(Defence));
        container.Set(nameof(DefencedPlaces), new Serializable.Int((int) DefencedPlaces));
        container.Set(nameof(Damage), new Serializable.Decimal(Damage));
        container.Set(nameof(Health), new Serializable.Decimal(Health));
    }

    public static ResultStats Deserialize(VariableContainer container)
    {
        return new ResultStats
        {
            ArtifactId = container.Get<Serializable.String>(nameof(ArtifactId)),
            Gold = container.Get<Serializable.Decimal>(nameof(Gold)),
            KnowledgeGroup = (Knowledge) (int) container.Get<Serializable.Int>(nameof(KnowledgeGroup)),
            KnowledgeMinimal = container.Get<Serializable.Decimal>(nameof(KnowledgeMinimal)),
            KnowledgeRequired = container.Get<Serializable.Decimal>(nameof(KnowledgeRequired)),

            Name = container.Get<Serializable.String>(nameof(Name)),
            Defence = container.Get<Serializable.Decimal>(nameof(Defence)),
            DefencedPlaces = (Place) (int) container.Get<Serializable.Int>(nameof(DefencedPlaces)),
            Damage = container.Get<Serializable.Decimal>(nameof(Damage)),
            Health = container.Get<Serializable.Decimal>(nameof(Health))
        };
    }

    public override string ToString()
    {
        return
            $"{nameof(ArtifactId)}: {ArtifactId}, {nameof(Gold)}: {Gold}, {nameof(KnowledgeGroup)}: {KnowledgeGroup}, {nameof(KnowledgeMinimal)}: {KnowledgeMinimal}, {nameof(KnowledgeRequired)}: {KnowledgeRequired}, {nameof(Name)}: {Name}, {nameof(Defence)}: {Defence}, {nameof(DefencedPlaces)}: {DefencedPlaces}, {nameof(Damage)}: {Damage}, {nameof(Health)}: {Health}";
    }
}