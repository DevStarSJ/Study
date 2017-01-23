# Action Method 내에서 Request Body 내용 가져오기

```C#
string body = "";
Request.InputStream.Seek(0, SeekOrigin.Begin);
using (StreamReader reader = new StreamReader(Request.InputStream))
{
    body = reader.ReadToEnd();
}
```