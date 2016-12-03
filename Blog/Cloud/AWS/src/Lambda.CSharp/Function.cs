using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

using Amazon.Lambda.Core;
using Amazon.Lambda.Serialization;

using System.IO;
using System.Text;

using Newtonsoft.Json.Linq;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializerAttribute(typeof(Amazon.Lambda.Serialization.Json.JsonSerializer))]

namespace AWSLambdaTest
{
    public class Function
    {

		/// <summary>
		/// A simple function that takes a string and does a ToUpper
		/// </summary>
		/// <param name="input"></param>
		/// <param name="context"></param>
		/// <returns></returns>
		//public string FunctionHandler(string input, ILambdaContext context)
		//{
		//	return input?.ToUpper();
		//}

		//public string FunctionHandler(Stream stream, ILambdaContext context)
		//{
		//	List<byte> bytes = new List<byte>();
		//	while (stream.CanRead)
		//	{
		//		int readByte = stream.ReadByte();
		//		if (readByte != -1)
		//			bytes.Add((byte)readByte);
		//		else
		//			break;
		//	}

		//	string text = Encoding.UTF8.GetString(bytes.ToArray());
		//	return text;
		//}

		public Stream FunctionHandler(Stream stream, ILambdaContext context)
		{
			List<byte> bytes = new List<byte>();
			while (stream.CanRead)
			{
				int readByte = stream.ReadByte();
				if (readByte != -1)
					bytes.Add((byte)readByte);
				else
					break;
			}

			string text = Encoding.UTF8.GetString(bytes.ToArray());

			var json = JObject.Parse(text);
			json["name"] = "LunaSter";

			text = json.ToString();

			MemoryStream stream1 = new MemoryStream(Encoding.UTF8.GetBytes(text));
			return stream1;
		}
	}
}
