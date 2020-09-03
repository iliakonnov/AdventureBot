namespace Analyser
{
    internal class Room: ClassInfo
    {
        public bool IsMonster { get; private set; }
        public bool IsQuest { get; private set; }
        public bool IsBoss { get; private set; }
        
        protected override void Fill()
        {
            throw new System.NotImplementedException();
        }
    }
}