using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Rooms
{
    [Available("monster/sans", Difficulity.Hard)]
    public class Sans : MonsterBase
    {
        public override string Name => "Санс";
        public override string Identifier => "monster/sans";
        protected override decimal Health => 35;

        protected override decimal GetDamage(User user)
        {
            return 70;
        }

        public override void MakeDamage(User user, decimal damage)
        {
            var variables = GetRoomVariables(user);
            var count = (int) variables.Get<Serializable.Int>("count");
            if (count < 15)
            {
                SendMessage(user,
                    user.Random.Next(0, 2) == 0
                        ? "– Упс, промахнулся!"
                        : "– Ух, чуть не попал!");
                variables.Set("count", new Serializable.Int(count + 1));
            }
            else
            {
                base.MakeDamage(user, Health);
            }
        }

        protected override void Enter(User user, string[][] buttons)
        {
            if (user.Info.CurrentStats.GetStat(StatsProperty.Karma) >= 15)
            {
                SendMessage(user, "И тебе повезло, что его друзья не жаловались на тебя. Иди с миром.", buttons);
                user.RoomManager.Leave();
            }
            else
            {
                SendMessage(user,
                    "– Какой прекрасный день! Травка зеленеет, птички щебечут. В такой день дети вроде тебя должны... ГОРЕТЬ В АДУ",
                    buttons);
            }
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }

        protected override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo("sans/ketchup", 1));
        }
    }
}