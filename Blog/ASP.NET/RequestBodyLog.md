# Get Request Body in Action Method

```C#
string body = "";
Request.InputStream.Seek(0, SeekOrigin.Begin);
using (StreamReader reader = new StreamReader(Request.InputStream))
{
    body = reader.ReadToEnd();
}
```