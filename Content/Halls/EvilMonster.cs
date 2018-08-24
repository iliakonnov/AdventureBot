using System.Linq;
using AdventureBot;
using AdventureBot.Item;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Halls
{
    public interface IEvilWeapon : IItem
    {
        decimal DamageMultiplier { get; }
    }

    public abstract class EvilMonsterBase : MonsterBase
    {
        public override void MakeDamage(User user, decimal damage)
        {
            const int limit = 3;

            damage = user.ItemManager.Items
                .Select(i => i.Item as IEvilWeapon)
                .Where(i => i != null)
                .OrderByDescending(i => i.DamageMultiplier)
                .Take(limit)
                .Aggregate(damage, (current, item) => current * item.DamageMultiplier);

            base.MakeDamage(user, damage);
        }

        public override void OnEnter(User user)
        {
            GetRoomVariables(user).Remove("allow_run");
            base.OnEnter(user);
        }

        protected override bool OnRunaway(User user)
        {
            return GetRoomVariables(user).Get<Serializable.Bool>("allow_run") ?? false;
        }

        public void ForceRun(User user)
        {
            GetRoomVariables(user).Set("allow_run", new Serializable.Bool(true));
            user.RoomManager.Leave();
        }
    }
}