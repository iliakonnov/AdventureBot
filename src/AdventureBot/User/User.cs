using System;
using JetBrains.Annotations;
using MessagePack;

namespace AdventureBot.User;

[MessagePackObject(true)]
public class User
{
    /// <summary>
    /// Генератор случайных чисел
    /// </summary>
    [IgnoreMember] public readonly Random Random = new();

    [Obsolete("This constructor for serializer only")]
    [UsedImplicitly]
    [SerializationConstructor]
    public User(ItemManager itemManager, ActiveItemsManager activeItemsManager, UserInfo info,
        VariableManager variableManager, RoomManager roomManager, MessageManager messageManager,
        QuestManager questManager, Guid token, Tuple<UserId, Guid> linkedTo)
    {
        ItemManager = itemManager;
        ItemManager.User = this;

        ActiveItemsManager = activeItemsManager;
        ActiveItemsManager.User = this;

        RoomManager = roomManager;
        RoomManager.User = this;

        Info = info;
        Info.User = this;
        Info.Statistics.User = this;
        Info.Level.User = this;

        MessageManager = messageManager;
        MessageManager.User = this;

        QuestManager = questManager;
        QuestManager.User = this;

        VariableManager = variableManager;

        Token = token;
        LinkedTo = linkedTo;
    }

    public User(UserId userId)
    {
        Reset(userId);
    }

    /// <summary>
    /// Информация о пользователе и его характеристики
    /// </summary>
    public UserInfo Info { get; private set; }

    /// <summary>
    /// Управление текущими активными предметами пользователя
    /// </summary>
    public ActiveItemsManager ActiveItemsManager { get; private set; }

    /// <summary>
    /// Управление предметами пользователя
    /// </summary>
    public ItemManager ItemManager { get; private set; }

    /// <summary>
    /// Хранилище переменных пользователя
    /// </summary>
    public VariableManager VariableManager { get; private set; }

    /// <summary>
    /// Переход между комнатами
    /// </summary>
    public RoomManager RoomManager { get; private set; }

    public MessageManager MessageManager { get; private set; }

    public QuestManager QuestManager { get; private set; }

    [IgnoreMember] internal DatabaseVariables DatabaseVariables { get; private set; } = new();

    public Guid Token { get; set; } = Guid.Empty;
    internal Tuple<UserId, Guid> LinkedTo { get; set; }

    public static event GameEventHandler OnReset;

    private void Reset(UserId userId)
    {
        ActiveItemsManager = new ActiveItemsManager(this);
        Info = new UserInfo(userId, this);
        ItemManager = new ItemManager(this);
        RoomManager = new RoomManager(this);
        MessageManager = new MessageManager(this);
        QuestManager = new QuestManager(this);
        DatabaseVariables = new DatabaseVariables();

        if (VariableManager != null)
        {
            VariableManager.Reset();
        }
        else
        {
            VariableManager = new VariableManager();
        }

        if (Token == Guid.Empty)
        {
            Token = Guid.NewGuid();
        }

        OnReset?.Invoke(this);
    }

    internal void Reset()
    {
        Reset(Info.UserId);
    }
}