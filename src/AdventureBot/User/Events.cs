namespace AdventureBot.User;

public delegate void GameEventHandler(User user);

public delegate void GameEventHandler<in T>(User user, T param);