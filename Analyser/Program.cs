using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.Build.Locator;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis.MSBuild;
using Microsoft.CodeAnalysis.Text;

namespace Analyser
{
    class Program
    {
        static void Main()
        {
            if (!MSBuildLocator.IsRegistered) MSBuildLocator.RegisterDefaults(); // ensures correct version is loaded up
            var _ = typeof(Microsoft.CodeAnalysis.CSharp.Formatting.CSharpFormattingOptions); // this ensures library is referenced so the compiler would not try to optimise it away (if dynamically loading assemblies or doing other voodoo that can throw the compiler off) - probably less important than the above but we prefer to follow cargo cult here and leave it be for
            AnalyseSolution().GetAwaiter().GetResult();
        }

        static async Task AnalyseSolution()
        {
            using (var w = MSBuildWorkspace.Create())
            {
                var solution = await w.OpenSolutionAsync(@"AdventureBot.sln");
                
                foreach (var project in solution.Projects)
                {
                    var compilation = await project.GetCompilationAsync();
                    var classVisitor = new ClassVirtualizationVisitor();
                    foreach (var syntaxTree in compilation.SyntaxTrees)
                    {
                        classVisitor.Visit(syntaxTree.GetRoot());                
                    }
                    var classes = classVisitor.Classes;
                    Console.WriteLine("{0}", project.Name);
                    foreach (var @class in classes)
                    {
                        var sem = compilation.GetSemanticModel(@class.SyntaxTree);
                        var sym = sem.GetDeclaredSymbol(@class);
                        var interfaces = sym?.AllInterfaces
                            .Select(i => i.ToDisplayString())
                            .ToArray() ?? new string[0];

                        var is_room = interfaces.Contains("AdventureBot.Room.IRoom");
                        var is_monster = interfaces.Contains("AdventureBot.Room.IMonster");
                        var is_quest = interfaces.Contains("AdventureBot.Room.IQuestMonster");
                        var is_item = interfaces.Contains("AdventureBot.Item.IItem");

                        var bases = @class.BaseList?.Types
                            .Select(t => t.Type.ToString())
                            .ToArray() ?? new string[0];
                        var attributes = @class.AttributeLists
                            .SelectMany(a => a.Attributes)
                            .Select(a => a.Name.ToString())
                            .ToArray();
                        Console.WriteLine("\t[{2}] {0}: {1} : {3}",
                            @class.Identifier,
                            string.Join(", ", bases),
                            string.Join(", ", attributes),
                            string.Join(", ", interfaces));
                    }
                }
            }
        }

        class ClassVirtualizationVisitor : CSharpSyntaxRewriter
        {
            public ClassVirtualizationVisitor()
            {
                Classes = new List<ClassDeclarationSyntax>();
            }

            public List<ClassDeclarationSyntax> Classes { get; set; }

            public override SyntaxNode VisitClassDeclaration(ClassDeclarationSyntax node)
            {
                node = (ClassDeclarationSyntax)base.VisitClassDeclaration(node);
                Classes.Add(node); // save your visited classes
                return node;
            }
        }
    }
}