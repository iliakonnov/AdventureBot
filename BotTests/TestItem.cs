using AdventureBot;
using AdventureBot.Item;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace BotTests
{
    internal class TestItem : ItemBase<TestItem>
    {
        public override void OnLeave(User user, ItemInfo info)
        {
            throw new System.NotImplementedException();
        }

        public override string Name { get; set; } = "Test item";
        public override string Description { get; set; } = "This item only for unit tests";
        public override decimal? Price { get; set; } = 0m;
        public override Flag<BuyGroup> Group { get; set; } = new Flag<BuyGroup>(BuyGroup.Guild);

        public override string Identifier { get; set; }
        public override StatsEffect Effect { get; set; }

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