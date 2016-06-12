using System.Collections.Generic;
using System.Threading.Tasks;

class StaticClass
{
    public static IEnumerable<string> Names { set; get; }

    static StaticClass()
    {
        //Names = Task.Run(async () => { return await GetNamesAsync(); }).Result;
        //InitAsync();
        //Names = GetNames();
    }

    public static void Init()
    {
        Names = Task.Run(async () => { return await GetNamesAsync(); }).Result;
    }

    public static async Task<IEnumerable<string>> GetNamesAsync()
    {
        List<string> nameList = new List<string>
        {
            "Luna", "Star", "Philip"
        };

        return nameList;
    }

    public static IEnumerable<string> GetNames()
    {
        return Task.Run(async () => { return await AsyncClass.GetNamesAsync(); }).Result; ;
    }

    //private static async void InitAsync()
    //{
    //    Names = await InitNamesAsync();
    //}
}

class AsyncClass
{
    public static async Task<IEnumerable<string>> GetNamesAsync()
    {
        List<string> nameList = new List<string>
        {
            "Luna", "Star", "Philip"
        };

        return nameList;
    }
}

class Program
{
    static void Main(string[] args)
    {
        StaticClass.Init();
        foreach (string name in StaticClass.Names)
        {
            System.Console.WriteLine(name);
        }
    }
}
