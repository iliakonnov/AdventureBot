using System.Reflection;
using System.Text.RegularExpressions;
using PythonStubs;

static class Program
{
    private static Queue<Type> scheduled = new();
    private static HashSet<Guid> written = new();
    private static Dictionary<string, StubFile> files = new();

    public static void Schedule(Type type)
    {
        if (written.Contains(type.GUID))
        {
            return;
        }

        scheduled.Enqueue(type);
    }

    public static void Main()
    {
        var outDir = Environment.GetCommandLineArgs()[1];
        var namespaces = new Dictionary<string, HashSet<string>>();
        var assemblies = new[]
        {
            Assembly.Load("AdventureBot"),
        };
        var types = assemblies.SelectMany(assembly => assembly.GetTypes());
        scheduled = new Queue<Type>(types);

        if (Directory.Exists(outDir))
        {
            Directory.Delete(outDir, true);
        }

        while (scheduled.TryDequeue(out var type))
        {
            if (!written.Add(type.GUID))
            {
                continue;
            }

            if (type.IsNotPublic || type.Namespace == null || type.IsCompilerGenerated())
            {
                continue;
            }

            if (type.IsGenericType)
            {
                type = type.GetGenericTypeDefinition();
            }

            var name = type.FullName!.Replace('+', '.').Split('[')[0];
            name = Regex.Replace(name, @"`\d+", "");
            var namespacePath = string.Join('.', name.Split('.').SkipLast(1)).Replace('.', Path.DirectorySeparatorChar);
            var directory = Path.Join(outDir, namespacePath);
            var path = Path.Join(directory, "__init__.pyi");

            if (!files.ContainsKey(path))
            {
                files[path] = new StubFile();
            }

            files[path].WriteType(type);

            if (!namespaces.ContainsKey(directory))
            {
                namespaces[directory] = new HashSet<string>();
            }
        }

        foreach (var (path, file) in files)
        {
            var directory = Path.GetDirectoryName(path);
            Directory.CreateDirectory(directory);
            using var writer = new StreamWriter(path);
            file.Save(writer);
        }

        Directory.CreateDirectory(Path.Combine(outDir, "stubhelper"));
        File.WriteAllText(Path.Combine(outDir, "stubhelper", "__init__.py"),
            @"import typing

T = typing.TypeVar('T')

class ref(typing.Generic[T]):
    def __init__(self, val: T):
        self.val = val

class ptr(typing.Generic[T]):
    def __init__(self, val: T):
        self.val = val
");

        File.Create(Path.Join(outDir, "__init__.pyi"));
    }
}