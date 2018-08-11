using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms.DeadlyBattle
{
    [Room(Id)]
    public class ShaoKahn : MonsterBase
    {
        public const string Id = "tournament/ShaoKahn";
        public override string Name => "Шао Кан";
        public override string Identifier => Id;
        protected override decimal Health => 200_000;

        protected override decimal GetDamage(User user)
        {
            var variables = GetRoomVariables(user);
            decimal health = variables.Get<Serializable.Decimal>("hp");

            var special = false;
            if (health <= 100_000 && (bool) variables.Get<Serializable.Bool>("special") != true)
            {
                variables.Set("special", new Serializable.Bool(true));
                special = true;
            }

            if (!special)
            {
                return 70;
            }

            SendMessage(user, "Шао Кан замахивается на тебя своим ужасным молотом. Ты пытаешься уклониться...");
            if (user.Random.NextDouble() > 0.4)
            {
                SendMessage(user, "... но тщетно!");
                return user.Random.Next(80, 120);
            }

            SendMessage(user, "... и тебе удалось!");
            return 0;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "— Ты победил всех! Достойный боец... Выходи на арену и получи награду!");
            SendMessage(user, "— Сразись со мной!", buttons);
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }

        protected override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo(Hammer.Id, 1));
        }
    }
}