using AdventureBot.ObjectManager;

namespace AdventureBot.Api;

public class WebApiAttribute : GameObjectAttribute
{
    public readonly string BaseRoute;

    public WebApiAttribute(string baseRoute)
    {
        BaseRoute = baseRoute;
    }
}