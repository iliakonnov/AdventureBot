using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;
using Content.Items;

namespace Content.Rooms
{
    [Room(Id)]
    public class Thanos : MonsterBase
    {
        public const string Id = "soulstone/Thanos";

        public override string Name => "Танос";
        public override string Identifier => Id;
        protected override decimal Health => 400000;

        protected override decimal GetDamage(User user)
        {
            var vars = GetRoomVariables(user);
            var oldHp = (decimal) vars.Get<Serializable.Decimal>("old_hp");
            var hp = (decimal) vars.Get<Serializable.Decimal>("hp");

            if (oldHp >= 300_000 && hp < 300_000)
            {
                SendMessage(user, "Танос использует Камень Силы и наносит сокрушительный удар!");
                return user.Random.Next(70, 90);
            }

            if (oldHp >= 250_000 && hp < 250_000)
            {
                SendMessage(user, "Танос использует Камень Пространства и уклоняется от твоей атаки!");
                return 0;
            }

            if (oldHp >= 200_000 && hp < 200_000)
            {
                var items = user.ItemManager.Items;
                var item = items[user.Random.Next(items.Count)];
                user.ItemManager.Remove(new ItemInfo(item.Identifier, 1));
                SendMessage(user, $"Танос использует Камень Реальности и обращает {item.Item.Name} в пепел!");
                return 0;
            }

            if (oldHp >= 100_000 && hp < 100_000)
            {
                var regen = (decimal) user.Random.Next(500, 1500);
                vars.Set("hp", new Serializable.Decimal(hp + regen));
                SendMessage(user,
                    $"Танос использует Камень Времени и возвращает себе {regen.Format()} единиц здоровья!");
                return 0;
            }

            if (oldHp >= 50_000 && hp < 50_000)
            {
                SendMessage(user, "Танос берет паузу на мгновение и использует Силу пяти камней!");
                return user.Random.Next(120, 240);
            }

            return 80;
        }

        protected override void Enter(User user, string[][] buttons)
        {
            user.ItemManager.Remove(new ItemInfo(Soulstone.Id, 6));
            SendMessage(user,
                "Ты положил последний камень в свой рюкзак. Через секунду мощный удар титана отбросил тебя на несколько метров. Рюкзак остался в руках у Таноса.");
            SendMessage(user,
                "– Не думал, что это будет так легко. Знаешь, когда восстанавливаешь баланс во Вселенной, как-то не до смеха, но это веский повод для улыбки.",
                buttons);
        }

        protected override bool OnRunaway(User user)
        {
            return false;
        }

        protected override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo(InfinityGlove.Id, 1));
        }
    }
}
