using MessagePack;

namespace AdventureBot;

public abstract class Singleton<T> where T : Singleton<T>, new()
{
    [IgnoreMember] public static T Instance { get; } = new();
}