namespace AdventureBot.Analysis
{
    internal static class Utils
    {
        public static string CurrentIntent(User.User user)
        {
            var room = user.RoomManager.CurrentRoom;
            if (room == null)
            {
                return "none";
            }

            var intent = user.RoomManager.CurrentRoom?.Identifier;
            var action = user.VariableManager.GetRoomVariables(room.Identifier).Get("action");
            switch (action)
            {
                case null:
                    return intent;
                case Serializable.Int integer:
                    intent += $"-{(int) integer}";
                    break;
                case Serializable.String str:
                    intent += $"-{(string) str}";
                    break;
            }

            return intent;
        }
    }
}