using System.IO;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot
{
    [PublicAPI]
    public static class DebugHelpers
    {
        public static byte[] Serialize<T>(T obj)
        {
            return MessagePackSerializer.Serialize(obj);
        }

        public static string SerializeJson<T>(T obj)
        {
            var data = Serialize(obj);
            return MessagePackSerializer.ToJson(data);
        }

        public static void Dump<T>(T obj, string output)
        {
            File.WriteAllBytes(output, Serialize(obj));
        }

        public static void DumpJson<T>(T obj, string output)
        {
            File.WriteAllText(output, SerializeJson(obj));
        }

        public static T LoadJson<T>(string input)
        {
            return DeserializeJson<T>(File.ReadAllText(input));
        }

        public static T LoadBinary<T>(string input)
        {
            return Deserialize<T>(File.ReadAllBytes(input));
        }

        public static T Deserialize<T>(byte[] data)
        {
            return MessagePackSerializer.Deserialize<T>(data);
        }

        public static T DeserializeJson<T>(string json)
        {
            var data = MessagePackSerializer.FromJson(json);
            return MessagePackSerializer.Deserialize<T>(data);
        }
    }
}