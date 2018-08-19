namespace AdventureBot.Item
{
    public abstract class PetBase : ItemBase
    {
        public override void OnAdd(User.User user, ItemInfo info, int count)
        {
            var currentPet = user.VariableManager.UserVariables.Get<ItemInfo>("pet");
            if (currentPet != null)
            {
                user.ItemManager.Remove(currentPet);
            }

            user.VariableManager.UserVariables.Set("pet", info);
        }
    }
}