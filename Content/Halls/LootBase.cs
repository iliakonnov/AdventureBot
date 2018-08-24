using System.Collections.Generic;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Halls
{
    public abstract class LootBase : ItemBase
    {
        public override decimal? Price => null;
        public override StructFlag<BuyGroup> Group => new StructFlag<BuyGroup>();
        public override StatsEffect Effect => null;

        public override bool CanUse(User user, ItemInfo info)
        {
            return false;
        }
    }

    public class Recipe
    {
        public Recipe(decimal gold, string output, Dictionary<string, int> input)
        {
            Gold = gold;
            Input = input;
            Output = output;
        }

        public decimal Gold { get; }
        public Dictionary<string, int> Input { get; }
        public string Output { get; }
    }
}