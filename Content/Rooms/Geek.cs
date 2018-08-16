using System.Linq;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;
using Content.Items;

namespace Content.Rooms
{
    [Available(Id, Difficulity.Medium)]
    public class Geek : MonsterBase
    {
        public const string Id = "monster/geek";
        public override string Name => "Гик";
        public override string Identifier => Id;
        protected override decimal Health => 150;

        protected override decimal GetDamage(User user)
        {
            return 25;
        }

        protected override string[][] GetActions(User user)
        {
            return base.GetActions(user)
                .Concat(new[] {new[] {"А когда HL-3 выйдет?"}})
                .ToArray();
        }

        protected override void Enter(User user, string[][] buttons)
        {
            SendMessage(user,
                "\"...Ты в С++ делал хоть клик? Ты хоть в один фандом вник? Знаешь эльфийский язык? Хотя бы english can you speak?\"");
            SendMessage(user,
                "Да, эта бурная смесь из тонны ненужной информации, предрассудков и бесконечного неуважения к псевдо-гикам умеет внушать страх",
                buttons);
        }

        public override void OnMessage(User user, RecivedMessage message)
        {
            if (message.Text == "А когда HL-3 выйдет?")
            {
                SendMessage(user,
                    "За толстыми линзами очков блеснули слезы. Гик пошатнулся, рухнул на пол, свернулся калачиком и тихонько заплакал. Вокруг него образовалась небольшая лужа. Думаю, нам пора оставить его наедине с собой на некоторое время");
                user.RoomManager.Leave();
            }
            else
            {
                base.OnMessage(user, message);
            }
        }

        protected override bool OnRunaway(User user)
        {
            return true;
        }

        protected override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo(DungeonsAndDragons.Id, 1));
        }
    }
}