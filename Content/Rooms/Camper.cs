using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;
using Content.Items;
using Content.Quests;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Medium, TownRoot.Id)]
    public class Camper : MonsterBase, IQuestMonster
    {
        public const string Id = "monster/camper";
        protected override decimal Health => 70;
        public override string Name => "Кэмпер";
        public override string Identifier => Id;

        protected override decimal GetDamage(User user)
        {
            return 70;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "Сидел за ящиками, падла. Задай ему жару!", buttons);
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }

        protected override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo(Awp.Id, 1));
        }
    }
}