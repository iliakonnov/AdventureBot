using System;
using Npgsql;

namespace AdventureBot.UserManager;

public class UserProxy : IDisposable
{
    private readonly UserId _id;
    private NpgsqlTransaction _transaction;
    private User.User _loaded;

    public UserProxy(UserId id)
    {
        _id = id;
    }

    public static User.User GetUnsafe(UserId userId)
    {
        return DatabaseConnection.LoadUserData(userId).Deserialize();
    }

    public User.User User
    {
        get
        {
            if (_loaded != null)
            {
                return _loaded;
            }

            _transaction ??= DatabaseConnection.GetConnection().BeginTransaction();
            var user = DatabaseConnection.LoadUserData(_id, _transaction).Deserialize();
            _loaded = user;
            return user;
        }
    }

    private void Save(User.User user)
    {
        DatabaseConnection.SaveUser(UserData.Serialize(user), _transaction);
    }

    public void Dispose()
    {
        if (_loaded != null)
        {
            Save(_loaded);
        }

        _transaction?.Dispose();
    }
}