using System;
using System.Net;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using MathNet.Numerics.LinearAlgebra;
using MathNet.Numerics.LinearAlgebra.Double;
using Microsoft.Azure;
using Microsoft.WindowsAzure.Storage;
using Microsoft.WindowsAzure.Storage.File;
using Newtonsoft.Json;

public static async Task<object> Run(HttpRequestMessage req, TraceWriter log)
{
	log.Info($"C# HTTP trigger function processed a request. RequestUri={req.RequestUri}");

	string xStr = req.GetQueryNameValuePairs().FirstOrDefault(q => q.Key == "x").Value;
	double[] x1 = JsonConvert.DeserializeObject<double[]>(xStr);
	var x2 = Convert2D(x1);

	PredictModel model = await GetPredictModel(ConnectionString, ShareName, ResultFile);

	var W = DenseMatrix.OfArray(model.W);
	var X = DenseMatrix.OfArray(x2);
	var H = ArrayAdd(X.Multiply(W).Row(0).AsArray(), model.b);

	var sigmoid = H.Select(Sigmoid);

	var response = new ResponseModel();
	response.rating = Softmax(sigmoid).ToArray();
	response.answer = Argmax(response.rating);


	var jsonResponse = JsonConvert.SerializeObject(response);

	return new HttpResponseMessage(HttpStatusCode.OK)
	{
		Content = new StringContent(jsonResponse, Encoding.UTF8, "application/json")
	};
}

const string ConnectionString = "DefaultEndpointsProtocol=https;AccountName=[NAME];AccountKey=[KEY];EndpointSuffix=[...]";
const string ShareName = "tensorflow-savedata";
const string ResultFile = "result.json";

public class PredictModel
{
	public double[,] W { get; set; }
	public double[] b { get; set; }
}

public class ResponseModel
{
	public int answer { get; set; }
	public double[] rating { get; set; }
}

static IEnumerable<double> Softmax(IEnumerable<double> M, double t = 1.0)
{
	var E = M.Select(x => Math.Exp(x / t));
	var total = E.Sum();
	return E.Select(x => x / total);
}

static double Sigmoid(double z)
{
	return 1 / (1 + Math.Pow(Math.E, -1.0 * z));
}

static int Argmax(IEnumerable<double> M)
{
	var max_num = -1.0;
	var max_index = -1;
	for (int i = 0; i < M.Count(); i++)
	{
		var y = M.ElementAt(i);
		if (y > max_num)
		{
			max_num = y;
			max_index = i;
		}
	}

	return max_index;
}

static double[,] Convert2D(double[] d1)
{
	var d2 = new double[1, d1.Length];
	for (int i = 0; i < d1.Length; i++)
	{
		d2[0, i] = d1[i];
	}
	return d2;
}

static double[] ArrayAdd(double[] A, double[] B)
{
	return A.Select((a, i) => a + B[i]).ToArray();
}

static async Task<PredictModel> GetPredictModel(string connectionString, string shareName, string fileName)
{
	CloudStorageAccount storageAccount = CreateStorageAccountFromConnectionString(connectionString);
	CloudFileClient fileClient = storageAccount.CreateCloudFileClient();
	CloudFileShare share = fileClient.GetShareReference(shareName);

	try
	{
		await share.CreateIfNotExistsAsync();
	}
	catch (Exception)
	{
		throw;
	}

	CloudFileDirectory root = share.GetRootDirectoryReference();
	CloudFile file = root.GetFileReference(fileName);

	byte[] buffer = new byte[65535];
	await file.DownloadToByteArrayAsync(buffer, 0);

	var strJson = System.Text.Encoding.Default.GetString(buffer);
	return JsonConvert.DeserializeObject<PredictModel>(strJson);
}

private static CloudStorageAccount CreateStorageAccountFromConnectionString(string storageConnectionString)
{
	try
	{
		return CloudStorageAccount.Parse(storageConnectionString);
	}
	catch (Exception e)
	{
		throw;
	}
}