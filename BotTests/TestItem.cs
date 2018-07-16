using AdventureBot;
using AdventureBot.Item;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace BotTests
{
    internal class TestItem : ItemBase
    {
        public override void OnLeave(User user, ItemInfo info)
        {
            throw new System.NotImplementedException();
        }

        public override string Name => "Test item";
        public override string Description => "This item only for unit tests";
        public override decimal? Price => 0m;
        public override Flag<BuyGroup> Group => new Flag<BuyGroup>(BuyGroup.Guild);

        public override string Identifier { get; } = "test_item";
        public override StatsEffect Effect { get; }

        public TestItem(string identifier)
        {
            Identifier = identifier;
        }
        
        public TestItem(string identifier, StatsEffect effect)
        {
            Identifier = identifier;
            Effect = effect;
        }

        public override void OnUse(User user, ItemInfo info)
        {
        }

        public override bool CanUse(User user, ItemInfo info)
        {
            return true;
        }

        public override void OnMessage(User user, ItemInfo info)
        {
        }

        public override void OnEnter(User user, ItemInfo info)
        {
        }
    }
}