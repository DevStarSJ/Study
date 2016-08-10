using System;

public class Test1Attribute : Attribute
{
    public int t1 { get; set; }
    public Test1Attribute(int t)
    {
        t1 = t;
    }
}

public class Test2Attribute : Attribute
{
    public int t2 { get; set; }
    public Test2Attribute(int t)
    {
        t2 = t;
    }
}

public class Parent
{
    [Test1(1)]
    [Test2(2)]
    public int id { get; set; }
}

class Program
{
    static void Main(string[] args)
    {
        var propertyInfo = typeof(Parent).GetProperty(nameof(Parent.id));

        var attributes = Attribute.GetCustomAttributes(propertyInfo, true);
        foreach (var a in attributes)
        {
            Console.WriteLine(a.GetType().ToString());

            if (a.GetType() == typeof(Test1Attribute))
            {
                Console.WriteLine((a as Test1Attribute).t1);
            }
            else if (a.GetType() == typeof(Test2Attribute))
            {
                Console.WriteLine((a as Test2Attribute).t2);
            }
        }
    }
}
