using AdventureBot;
using AdventureBot.Messenger;
using AdventureBot.Room;
using AdventureBot.User;

namespace Content.Rooms;

[Available(Id, Difficulity.Hard, TownRoot.Id)]
public class Dormammu : MonsterBase
{
    public const string Id = "monster/dormammu";
    public override string Name => "Дормамму";
    public override string Identifier => Id;
    protected override decimal Health => 1_000_000;

    protected override decimal GetDamage(User user)
    {
        return 70;
    }

    protected override void Enter(User user, string[][] buttons)
    {
        GetRoomVariables(user).Set("diplomacy", new Serializable.Int(0));
        SendMessage(user, "Похоже,  он собирается затянуть землю в свое измерение. Самое время его остановить!",
            buttons);
    }

    public override void OnMessage(User user, ReceivedMessage message)
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

    protected override bool OnRunaway(User user)
    {
        return true;
    }

    protected override void OnWon(User user)
    {
        user.Info.Gold += 1000;
    }
}