using System.Linq;
using AdventureBot.Item;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("monster/geek", Difficulity.Medium)]
    public class Geek : MonsterBase
    {
        public override string Name => "Гик";
        public override string Identifier => "monster/geek";
        public override decimal Health => 150;

        public override decimal GetDamage(User user)
        {
            return 25;
        }

        protected override string[][] GetActions(User user)
        {
            return base.GetActions(user)
                .Concat(new[] {new[] {"А когда HL-3 выйдет?"}})
                .ToArray();
        }

        public override void Enter(User user, string[][] buttons)
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

        public override bool OnRunaway(User user)
        {
            return true;
        }

        public override void OnWon(User user)
        {
            user.ItemManager.Add(new ItemInfo("geek/D&D", 1));
        }
    }
}