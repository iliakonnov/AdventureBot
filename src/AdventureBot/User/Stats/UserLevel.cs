﻿using System;
using System.Linq;
using AdventureBot.Messenger;
using MessagePack;

namespace AdventureBot.User.Stats;

[MessagePackObject(true)]
public class UserLevel
{
    [IgnoreMember] internal User User;

    public UserLevel(User user)
    {
        User = user;
    }

    [Obsolete("This constructor is for serializator only")]
    [SerializationConstructor]
    public UserLevel(int level, decimal expirenceRequired, decimal expirenceCollected)
    {
        Level = level;
        ExpirenceRequired = expirenceRequired;
        ExpirenceCollected = expirenceCollected;
    }

    public int Level
    {
        get => User.DatabaseVariables.Level;
        private set
        {
            if (User != null)
            {
                User.DatabaseVariables.Level = value;
            }
        }
    }

    public decimal ExpirenceRequired { get; private set; }

    public decimal ExpirenceCollected
    {
        get => User.DatabaseVariables.Experience;
        private set
        {
            if (User != null)
            {
                User.DatabaseVariables.Experience = value;
            }
        }
    }

    public static event GameEventHandler<UserLevel> OnChanged;

    public void AddXp(decimal xp)
    {
        ExpirenceCollected += xp;
        if (ExpirenceCollected < ExpirenceRequired)
        {
            OnChanged?.Invoke(User, this);
            return;
        }

        ExpirenceCollected = 0;
        ExpirenceRequired = 4M * (decimal) Math.Pow(Level, 3) / 5M;
        Level += 1;
        if (Level % 3 == 0)
        {
            User.ActiveItemsManager.ActiveLimit += 2;
        }

        var available = User.ActiveItemsManager.ActiveLimit -
                        User.ActiveItemsManager.ActiveProportions.Values.Sum();
        User.MessageManager.SendMessage(new SentMessage
        {
            Text = $"<b>Вы достигли {Level} уровня! Доступно {available} предметов для распределения.</b>"
        });

        OnChanged?.Invoke(User, this);
    }
}