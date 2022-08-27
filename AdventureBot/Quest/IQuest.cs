﻿using System;
using JetBrains.Annotations;

namespace AdventureBot.Quest;

[PublicAPI]
public interface IQuest
{
    string Identifer { get; }
    string GetName(User.User user, Guid questId);
    decimal GetProgress(User.User user, Guid questId);
    void Finish(User.User user, Guid questId);
    void Begin(User.User user, Guid questId);
}