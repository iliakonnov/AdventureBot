#if false // Этот файл не должен компилироваться, он только в качестве шаблона

using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;

namespace Content.Rooms
{
    // Тут задается уровень сложности. Список доступных значений см. в RoomManager.Difficulity
    [Available(Id, Difficulity.None)]
    public class MonsterTemplate : MonsterBase
    {
        public const string Id = "monster/Какой-то уникальный идентификатор";
        public override string Name => "Имя этой локации";
        public override string Identifier => Id;
        protected override decimal Health => 12345; // Сколько здоровья у монстра

        protected override decimal GetDamage(User user)
        {
            return 12345; // Какой урон он наносит
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "Сообщение при входе к монстру", buttons);
            SendMessage(user, "Их может быть несколько =)", buttons);
        }

        protected override bool OnRunaway(User user)
        {
            SendMessage(user, "Сообщение при побеге от монстра. Если сообщения нет, то просто удалить эту строчку");
            return true; // Заменить true на false, чтобы нельзя было сбежать
        }

        protected override void OnWon(User user)
        {
            SendMessage(user, "Сообщение при победе");
            // Чтобы дать несколько разных вещей, надо просто продублировать строчку нижу несколько раз =)
            user.ItemManager.Add(new ItemInfo("Идентификатор вещи, которую надо дать", 1234)); // 1234 -- кол-во

            user.Info.Gold += 12345; // Сколько золота дать игроку. Если золота не надо, то удалить строчку
            user.Info.ChangeStats(StatsProperty.Karma, 12345); // То же самое, что и с золотом, но только карма
        }
    }
}

#endif