using System.IO;
using System.Timers;
using MessagePack;

namespace AdventureBot
{
    public class GlobalVariables
    {
        private const string Filename = "globalVariables.msgpack";

        // ReSharper disable once PrivateFieldCanBeConvertedToLocalVariable (It must not be removed by GC)
        private static readonly Timer FlushTimer;

        static GlobalVariables()
        {
            FlushTimer = new Timer
            {
                AutoReset = true,
                Interval = 15 * 1000 // Every 15 seconds
            };
            FlushTimer.Elapsed += (sender, args) => Flush();
            FlushTimer.Start();

            if (File.Exists(Filename))
            {
                Variables = MessagePackSerializer.Deserialize<VariableContainer>(
                    File.ReadAllBytes(Filename));
            }
            else
            {
                Variables = new VariableContainer();
            }
        }

        public static VariableContainer Variables { get; }

        private static void Flush()
        {
            File.WriteAllBytes(Filename, MessagePackSerializer.Serialize(Variables));
        }
    }
}