using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Newtonsoft_Json
{
    class Program
    {
        class User
        {
            public string id { get; set; }
            public string name { get; set; }
            public int age { get; set; }
        }

        static void Main(string[] args)
        {
            var json = new JObject();
            json.Add("id", "Luna");
            json.Add("name", "Silver");
            json.Add("age", 19);

            var jarray = new JArray();
            jarray.Add(json);
            jarray.Add(json);

            //Console.WriteLine(json.ToString());

            //var json2 = new JObject(new { id = "Luna", name = "Silver", age = 19 });
            var json2 = JObject.Parse("{ id : \"Luna\" , name : \"Silver\" , age : 19 }");
            json2.Add("friends", jarray);

            var jarray2 = new JArray();
            jarray2.Add(json2);
            jarray2.Add(json2);
            json2.Add("lists", jarray2);

            //Console.WriteLine(json2.ToString());

            var lists = json2["lists"];

            //Console.WriteLine(lists.ToString());
            int num = 1;
            foreach (var listElement in lists)
            {
                listElement["id"] += $"{num++}";
                //Console.WriteLine(listElement.ToString());
            }

            User u = new User { id = "Luna", name = "Star", age = 19 };
            var json3 = JObject.FromObject(u);
            //Console.WriteLine(json3.ToString());

            var json4 = JObject.FromObject(new { id = "Luna", name = "Star", age = 19 });
            Console.WriteLine(json4.ToString());
        }
    }
}
