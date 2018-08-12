import System
import System.IO
import System.Linq
import System.Collections.Generic

booc = (`..\boo\bin\booc.exe`,)

print("""Booc.exe: ${booc[0]}""")


parameters = (
    "-r:Boo.Lang.Compiler.dll",
    "-r:Boo.Lang.dll",
    "-r:Boo.Lang.Extensions.dll",
    "-r:Boo.Lang.Interpreter.dll",
    "-r:Boo.Lang.Useful.dll",
    "-r:Boo.Lang.PatternMatching.dll",
    "-r:Boo.Lang.Parser.dll",
    "-r:AdventureBot.exe",

    "-t:library",
    "-utf8",
    "-v",
    "-ducky"
)

print("\nParameters:")
print(string.Join("\n", parameters))

files = List[of string]()

for file in Directory.GetFiles("src", "*.boo", SearchOption.AllDirectories):
    files.Add(file)

print("\nFiles:")
print(string.Join("\n", files))


File.WriteAllText("debug.bat", string.Join("^\n    ",
    booc.Concat(parameters)
        .Concat((
            "-debug+",
            `-o:Debug\BooRooms.dll`,
            `-lib:..\AdventureBot\bin\Debug\net461\`,
        ))
        .Concat(files)
))
File.WriteAllText("release.bat", string.Join("^\n    ",
    booc.Concat(parameters)
        .Concat((
            "-debug-",
            `-o:..\publish\BooRooms.dll`,
            `-lib:..\publish\`,
        ))
        .Concat(files)
))

print("Done!")
