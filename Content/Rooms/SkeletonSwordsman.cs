#if false
 using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;
using AdventureBot.User.Stats;
 namespace Content.Rooms
{
    [Available("monster/SkeletonSwordsman", Difficulity.Easy)]
    public class MonsterTemplate : MonsterBase
    {
        public const string Id = "monster/SkeletonSwordsman";
        public override string Name => "Скелет-воин";
        public override string Identifier => Id;
        protected override decimal Health => 35;
         protected override decimal GetDamage(User user)
        {
            return 12; 
        }
         protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, "Мы же не в данже! Ох уж эти некроманты! Гадят своими мертвецами где попало!", buttons);
        }
         protected override bool OnRunaway(User user)
        {
            SendMessage(user, "Сообщение при побеге от монстра. Если сообщения нет, то просто удалить эту строчку");
            return true; 
        }
         protected override void OnWon(User user)
        {
            SendMessage(user, "Сообщение при победе");
             user.Info.Gold += 20;
            user.Info.ChangeStats(StatsProperty.Karma, 0); 
        }
    }
}
 #endif 
