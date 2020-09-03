using System;
using System.IO;
using Microsoft.Build.Locator;

namespace Analyser
{
    static class Startup
    {
        public static FileInfo SolutionPath;
        
        [STAThread]
        static void Main(string[] args)
        {
            // ensures correct version is loaded up
            if (!MSBuildLocator.IsRegistered) MSBuildLocator.RegisterDefaults();

            // this ensures library is referenced so the compiler would not try to optimise it away
            // (if dynamically loading assemblies or doing other voodoo that can throw the compiler off)
            // - probably less important than the above but we prefer to follow cargo cult here and leave it be for
            var _1 = typeof(Microsoft.CodeAnalysis.CSharp.Formatting.CSharpFormattingOptions);
            var _2 = typeof(AdventureBot.Item.Hand);
            var _3 = typeof(Content.TownRoot);
            
            SolutionPath = new FileInfo(args[0]);
            
            new Eto.Forms.Application().Run(new MainForm());
        }
    }
}