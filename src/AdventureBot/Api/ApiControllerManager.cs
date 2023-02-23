using System;
using System.Threading;
using System.Threading.Tasks;
using AdventureBot.ObjectManager;
using EmbedIO;
using EmbedIO.WebApi;
using NLog;

namespace AdventureBot.Api;

public class ApiControllerManager : IManager<WebApiController>
{
    private WebServer _server;
    private static readonly Logger Logger = LogManager.GetCurrentClassLogger();

    public ApiControllerManager()
    {
        _server = new WebServer(o => o
                .WithUrlPrefix(Configuration.Config["api_host"])
                .WithMode(HttpListenerMode.EmbedIO));
        _server.StateChanged += (s, e) => Logger.Info("WebServer New State - {0}", e.NewState);
    }

    public void Register(GameObjectAttribute attribute, Func<WebApiController> factory)
    {
        if (attribute is WebApiAttribute attr)
        {
            _server = _server.WithWebApi(attr.BaseRoute, m => m.RegisterController(attribute.Type, factory.Invoke));
        }
    }

    public Task RunAsync(CancellationToken cancellationToken = default)
    {
        return _server.RunAsync(cancellationToken);
    }
}