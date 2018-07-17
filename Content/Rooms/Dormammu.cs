using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms
{
    [Available("monster/dormammu", Difficulity.Hard)]
    public class Dormammu : MonsterBase
    {
        public override string Name => "Дормамму";
        public override string Identifier => "monster/dormammu";
        public override decimal Health => 1_000_000;

        public override decimal GetDamage(User user)
        {
            return 70;
        }

        public override void Enter(User user, string[][] buttons)
        {
            GetRoomVariables(user).Set("diplomacy", new Serializable.Int(0));
            SendMessage(user, "Похоже,  он собирается затянуть землю в свое измерение. Самое время его остановить!",
                buttons);
        }

        public override void OnMessage(User user, RecivedMessage message)
        {
            if (message.Text == "Договориться")
            {
                var buttons = GetActions(user);

                SendMessage(user, "— Дормамму, я пришел договориться", buttons);

                var variables = GetRoomVariables(user);
                var current = variables.Get<Serializable.Int>("diplomacy");
                var newValue = (int) current + 1;
                variables.Set("diplomacy", new Serializable.Int(newValue));

                if (current == 10)
                {
                    SendMessage(user, "— Аааа, иди нахрен, Кэмбербетч", buttons);
                    user.RoomManager.Leave();
                }

                FinishTurn(user);
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
            user.Info.Gold += 1000;
        }
    }
}