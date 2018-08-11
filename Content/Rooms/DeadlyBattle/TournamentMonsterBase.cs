using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms.DeadlyBattle
{
    public abstract class TournamentMonsterBase : MonsterBase
    {
        protected abstract string Loot { get; }
        
        protected override decimal Health => 150;
        protected override decimal GetDamage(User user)
        {
            return 15;
        }
        
        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user, $"Твой противник — {Name}!", buttons);
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }
        
        protected override void OnWon(User user)
        {
            if (Loot != null)
            {
                user.ItemManager.Add(new ItemInfo(Loot, 1));
            }
        }
    }
}