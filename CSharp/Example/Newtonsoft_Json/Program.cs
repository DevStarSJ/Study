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

            //Console.WriteLine(json.ToString());

            var json2 = JObject.Parse("{ id : \"Luna\" , name : \"Silver\" , age : 19 }");
            json2.Add("blog", "devluna.blogspot.kr");
            //Console.WriteLine(json2.ToString());

            User u = new User { id = "SJ", name = "Philip", age = 25 };
            var json3 = JObject.FromObject(u);
            //Console.WriteLine(json3.ToString());

            var json4 = JObject.FromObject(new { id = "J01", name = "June", age = 23 });
            //Console.WriteLine(json4.ToString());

            var json5 = JObject.Parse("{ id : \"sjy\" , name : \"seok-joon\" , age : 27 }");
            json5.Add("friend1", json);
            json5.Add("friend2", json2);
            json5.Add("friend3", json3);
            json5.Add("friend4", json4);
            //Console.WriteLine(json5.ToString());

            var json4_name = json4["name"];
            //Console.WriteLine(json4_name);

            json4.Remove("name");
            //Console.WriteLine(json4.ToString());

            json5.RemoveAll();
            //Console.WriteLine(json5.ToString());



            var jarray = new JArray();
            jarray.Add(1);
            jarray.Add("Luna");
            jarray.Add(DateTime.Now);
            //Console.WriteLine(jarray.ToString());

            var jFriends = new JArray();
            jFriends.Add(json);
            jFriends.Add(json2);
            jFriends.Add(json3);
            jFriends.Add(json4);
            //Console.WriteLine(jFriends.ToString());

            var jarray2 = new JArray();
            jarray2.Add(jarray);
            jarray2.Add(jFriends);
            //Console.WriteLine(jarray2.ToString());

            var jf0 = jFriends[0];
            //Console.WriteLine(jf0.ToString());

            //foreach(JObject fElement in jFriends)
            //{
            //    var fName = fElement["name"] ?? "<NULL>";
            //    Console.WriteLine(fName);
            //}

            jFriends.Remove(jFriends[1]);
            jFriends.Remove(jFriends[2]);
            //Console.WriteLine(jFriends.ToString());

            json2.Add("Friends", jFriends);
            Console.WriteLine(json2.ToString());
        }
    }
}
