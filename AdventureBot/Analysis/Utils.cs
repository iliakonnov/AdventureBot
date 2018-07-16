using System.IO;
using System.Net.Http;
using System.Runtime.Serialization.Json;
using Microsoft.Extensions.Configuration;

namespace AdventureBot.Analysis
{
    internal static class Utils
    {
        public static string Token = Configuration.Config.GetValue<string>("chatbase_token");  // "f39a97d0-6e29-441c-b24d-607ca86eedb8"

        public static string GetPlatform(int messengerId)
        {
            string platform;
            switch (messengerId)
            {
                case -1:
                    platform = "testing";
                    break;
                case 1:
                    platform = "telegram";
                    break;
                default:
                    platform = "unknown";
                    break;
            }

            platform += $" (#{messengerId})";
            return platform;
        }

        public static string CurrentIntent(User.User user)
        {
            var room = user.RoomManager.CurrentRoom;
            if (room != null)
            {
                var intent = user.RoomManager.CurrentRoom?.Identifier;
                var action = user.VariableManager.GetRoomVariables(room.Identifier).Get("action");
                if (action != null)
                {
                    if (action is Serializable.Int integer)
                    {
                        intent += $"-{(int) integer}";
                    }
                    else if (action is Serializable.String str)
                    {
                        intent += $"-{(string) str}";
                    }
                }

                return intent;
            }

            return "none";
        }
    }
}