#Client WebSocket Example without ASP.NET

ASP.NET을 사용하지 않고 일반적인 C# (Console, Winform) 에서 WebSocket Server에 접속하는 코드 예제 입니다.

## 1. WebSocketSharp 사용

nuget manager에서 `websocket-sharp.clone` 로 검색하면 나옵니다.

```C#
using WebSocketSharp;

WebSocket ws = new WebSocket(url: "ws://localhost:5000");
ws.Connect();

Console.WriteLine(ws.ReadyState); // Open


bool result = ws.Send(new byte[] { 0x03, 0x01, 0x10, 0xFF });

Console.WriteLine(result.ToString()); // true

```


## 2. System.Net.WebSockets 사용

별도의 nuget 설치 필요없이 사용이 가능합니다.

```C#
using System.Net.WebSockets;

ClientWebSocket ws = new ClientWebSocket();
Uri uri = new Uri("ws://localhost:5000");

await ws.ConnectAsync(uri, CancellationToken.None);

Console.WriteLine(ws.State); // open


var segment = new ArraySegment<byte>(new byte[] { 0x03, 0x01, 0x10, 0xFF });
await ws.SendAsync(segment, WebSocketMessageType.Binary, true, CancellationToken.None);

```
