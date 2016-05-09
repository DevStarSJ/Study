`SignalR`을 `ASP.NET 5 Template`에서 사용하기 위해서는 `Startup.cs`의 `public void Configure(IApplicationBuilder app, ...)`에서 아래와 같은 구문이 필요합니다.

```C#
public class Startup
{
	public void Configure(IApplicationBuilder app)
	{
		app.UseServices(services =>
		{
			services.AddSignalR();
		});
		app.UseFileServer();
		app.UseSignalR();
	}
}
```

`app.UserServices()`를 사용하기 위해서는 `Microsoft.AspNet.RequestContainer` assembly를 포함시켜야 `IApplicationBuilder`의 extention method인 `UseServices`의 사용이 가능한데, 현재 version에서는 `ASP.NET 4.5.1`을 지원하지 않아서 사용이 불가능 합니다.
