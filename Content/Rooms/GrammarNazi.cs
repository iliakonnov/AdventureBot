using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;
using Content.Items;
using Content.Quests;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Lower, TownRoot.Id)]
    public class GrammarNazi : MonsterBase, IQuestMonster
    {
        public const string Id = "monster/grammar";
        protected override decimal Health => 65;
        public override string Name => "Граммар-наци";
        public override string Identifier => Id;

        protected override decimal GetDamage(User user)
        {
            return 15;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "Приносить боль таким людям – одно удовольствие. Намек понял?", buttons);
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }

        protected override void OnWon(User user)
        {
            user.Info.ChangeStats(StatsProperty.Karma, 1);
            user.ItemManager.Add(new ItemInfo(DictionaryOzhegov.Id, 1));
        }

        protected override void NotHandled(User user, RecivedMessage message)
        {
            switch (message.Text.ToLowerInvariant())
            {
                case "ложить":
                case "покласть":
                case "ихний":
                case "егошний":
                    SendMessage(user,
                        "Граммар-наци начинает биться в припадках, кричать, пускать пену изо рта, а в конце пытается перерезать себе вены одной из страниц словаря по Далю. Ты конечно его остановил, но ты всё равно монстр. Когда я говорил приносить боль, я имел в виду совсем не это");
                    user.Info.ChangeStats(StatsProperty.Karma, -2);
                    user.ItemManager.Add(new ItemInfo(DictionaryDahl.Id, 1));
                    user.RoomManager.Leave();
                    return;
                default:
                    base.NotHandled(user, message);
                    return;
            }
        }
    }
}