using System;
using AdventureBot.ObjectManager;

namespace AdventureBot.Room;

[Flags]
public enum Difficulity
{
    None = 0,
    Easy = 1 << 0,
    Medium = 1 << 1,
    Hard = 1 << 2,

    Lower = Easy | Medium,
    Upper = Medium | Hard,
    Any = Easy | Medium | Hard
}

public class RoomManager : StorageManager<IRoom, RoomAttribute>
{
}