### Microsoft Tech Days Korea 2015  

- 일시 : 2015년 10월 27일 화요일 09:00 ~ 21:10  
- 장소 : 세종대학교 광개토관 컨벤션센터  

#### 등록  

아침부터 비가 많이 왔습니다. 아침 8시 30분 경에 도착했는데, 아직 등록을 진행하고 있지 않았습니다.  

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.01.jpg?raw=true)  
 
채널나인가이라는 작은 스티로폼 인형을 이벤트로 주던데, 현장 여기저기 있는 힌트 팻말을 보고 정답을 적어서 제출하면 되더군요. 아래 사진과 같은 표지판들을 찾아다니면서 정답을 적어서 받았습니다.  

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/2015-10-27-Techdays.03.jpg?raw=true)  

9시 25분부터 행사장을 열어줘서 입장을 할 수 있었습니다. 멀리서 보았을 때 3개의 화면이 보였는데, 가운데 자리에서 약간 왼쪽에 위치하여 Reserved 라고 표시괸 예약석 3줄 바로 뒤에 자리를 잡았습니다. 오늘 들을 세션들을 한번 체크하고, 아이패드와 키보드를 세팅하였습니다.

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.02.jpg?raw=true)  

#### 인사말
- 최기영 부사장, Microsoft

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.05.jpg?raw=true)  

Microsoft 한국지사 최기영 부사장님의 인사말이 있었습니다. 대략적인 내용은 다음과 같습니다.
- `tech days`는 개발자들이 Software를 통해서 더 많은 힘을 갖고 더 많은 것을 이룰수 있도록 해주기 위해서 준비한 행사임을 강조하였습니다.  
- Microsoft가 3번째 CEO 인도인 출신의 `Satya Nadella`를 회장으로 맞이하면서 많은 것이 바뀌고 있습니다.  
  - 과거에는 Open Source에 대해서는 배타적이었다면, 이제는 적극적으로 수용을 하고 있습니다.
  - 무엇보다도 `개발자 출신 CEO`인 만큼 개발자 입장에서 많은 것을 노력하고 있습니다.  
- Microsoft의 3가지 Mission이 있습니다.
  1. `Intelligent Cloud` : 지능화된 클라우드인 Azure Cloud를 제공하고 있습니다. 여러가지 Open Source 및 Hadoop, Linux, Java 등을 많은 고객들이 설치하여 사용중입니다.
  2. `Cross-Plaform` : Office 제품을 Android, Mac 에서도 사용이 가능하며, Mac / Linux에서 사용가능한 개발용 Editor인 Visual Studio Code 도 제공하고 있습니다.
  3. `Personal Computing` : 일반적인 의미의 PC가 아니라 개인별 맞춤 컴퓨팅 환경을 의미합니다. Universal Windows Platform, HoloLens 등 사용자 경험을 바탕으로 가상 현실 등 풍부한 시나리오를 공급하고자 노력하고 있습니다.
- 이런 Mission 들을 이루기 위해 가장 중요한 역할을 하는 것이 개발자 들이라는 것을 다시한번 강조하면서 인사말을 마쳤습니다.

#### Keynote
- Ayman Shoukry, Visual C++ Team Manager  

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.06.jpg?raw=true)  

Visual C++ Team Manager인 Ayman Shoukry의 Keynote Session이 있었습니다. 물론 영어로 진행이 되었으며 동시통역기가 자리마다 있었습니다. 대략적인 내용은 다음과 같습니다.

- `Empower` : 개발자가 의사결정을 할 수 있도록 개발Tool을 제공하고자 노력하고 있습니다.
  - 지구상의 어떤 곳에서도 모든 Platform에서 작업이 가능하도록 지원하고자 합니다.
  - 이제 하나의 Platform에서만 작업하는 시대는 지났습니다.
  - Mobile First, Cloud First인 시대가 이미 왔습니다.

- Microsoft의 Open Source 활동은 10년전부터 진행되었습니다.
  - `.NET foundation`은  1년반 밖에 되지 않았지만 많은 활동들이 이루어 지고 있습니다.
  - `cppCon`의 core guideline을 `Bjarne Stroustrup`(C++ 창시자)과 함께 기여하고 있습니다.
  - `Apache Cordova` , `Adroid Emulator`도 진행하고 있으며, Google에서 만든 Emulator보다 더 성능이 좋습니다.
  - `.NET Core`를 Open Source화 하여 이제는 Windows 뿐만 아니라 Linux, Mac에서도 .NET Core가 올라가므로 `ASP.NET`이 모든 Platform에서 실행 됩니다.  

- C++의 Cross Platform
  - 현재는 플랫폼마다 주된 언어가 달라서, 각 플랫폼별로 Code의 재사용도 되지 않았고, 하나의 플랫폼이 지배적이 된다면, 나머지 플랫폼들이 간과될 수 밖에 없었습니다.  
  - Android, IOS, Windows 에서 모두 다 개발 가능한 언어는 `C/C++` 밖에 없습니다.  
  - US Android Market의 Top 100 App. 들 중 C++ Code가 들어간 것이 75%이상입니다.  
    - Facebook, Candy Crush 등 왠만한 App.들은 모두 C++를 사용하고 있습니다.  
  - PowerPoint가 처음에는 Windows-Only였지만, 95%이상이 Shared 가능한 C++ Code로 되어 있어서 Android, Mac에서 이제는 실행이 가능합니다.  

- `OpenGL Demo` 시연
  - Android, IOS, Shared 3개의 Project로 되어 있는 것을 보여주면서, Android 와 IOS가 같이 Shared Project를 사용하면서 실행이 가능하다는 것을 시연하였습니다.

- Visual C++의 `Linux Project` 지원
  - 다음달에 공식적으로 발표할 내용으로, `Visual Studio 2015 Update 1`에서 Linux Project도 Visual Studio에서 작업이 가능하도록 지원할 예정이라 했습니다.
  - Project 생성시 `readme.txt`를 보면 어떻게 빌드하고 배포하는지에 대한 설명이 있으며,
  - Linux에서 실행되는 것을 Windows에서 Debugging하는 것도 가능하다고 말했습니다.
    - `Pycon Korea 2015`에서 김명신 부장님이 Azure상에서 실행중인 Python Web Page를 Visual Studio에서 원격으로 Debugging하는 것을 보여주었는데, 비슷한 내용인 듯 합니다.  

#### General Session
- 마이크로소프트 에반젤리스트팀

1. 세상을 품은 플랫폼과 그 가능성에 대해서 - 김명신 부장님
  - 앞에서 얘기한 3가지 Mission (생산성, 지능적 Cloud, 맞춤형 컴퓨팅 환경)에 대해서 다시 한번 강조하였습니다.
  - 예전에는 새로운 기능이 추가될때마다 사용법이 어려웠지만, 이제는 펜, 몸동작 등 친숙한 방법으로 새로운 기능을 제공해주기 위해서 노력하고 있습니다.
  - Computer뿐만 아니라 모든 Device에서 서비스를 제공하도록 노력하고 있습니다.
  - Microsoft Azure Cloud에 대해서 전체적인 소개를 해 주었습니다.

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.07.jpg?raw=true)  

2. 맞춤형 Computing에 대한 Microsoft의 노력 - 밀덕 김영욱 부장님
  - Cross
    - Device들을 관통하는 Cross, Platform을 관통하는 Cross. 이렇게 2가지로 생각 할 수 있습니다.
    - Windows10 은 Device를 관통하는 Cross 입니다.
    - Visual Studio 2015는 Platform을 관통하는 Cross를 위해 노력하고 있습니다.
    - UWP (Universal Windows Platform)을 사용하면 Source Level의 호환이 아닌 Windows에서 만든 Binary를 그대로 Android에서 실행가능하도록 `Binary-level의 호환성`을 제공하고 있습니다.
    - `Bridge Technology` : Code의 Cross
      - Objective-C Code를 이용해서 Windows와 Android에서 돌아가는 Application 작성
      - Open Source로 진행중인데, 아직은 갈길이 많이 남았습니다.
      - Android까지는 Windows에서 Compile이 가능한데, IOS는 Mac에서 XCode를 가지고 Compile해야 합니다.
  - IoT 시연
    - Arduino, Raspberry_Pi 2를 이용한 무인 경비 시스템을 소개하였습니다.
    - 120s/min의 BB탄 Machine Gun을 장착하였으며, 근처 물체가 접근하면 발사합니다.
    - 모든 Data를 미국에 있는 Azure Cloud에 설치한 Event Hub로 실시간 전송합니다. (이게 뭐라고...)
    - 김영욱 부장님이 안전을 위해 고글과 널판지로 만든 튼튼한 방패를 들고 직접 무인 경비 시스템의 BB탄을 맞는 시범을 보였습니다.

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.08.jpg?raw=true)  

3. 최상의 개발도구 Visual Studio - 김태영 부장님
  - `TAEYO.NET`의 그 분이십니다. 실제로는 첨 봤는데 상당히 젋고 스마트해 보이시네요.
  - IntelliTest 시연 : 생성된 Code 상의 모든 경로를 다 Test하는 Code를 자동으로 생성 및 수행해줍니다.
  - ASP.NET 5.0을 Linux에 배포하는 시연을 보여주었습니다.

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.09.jpg?raw=true)  

4. 맺음말 - 김명신 부장님
  - 오후 세션에 대한 간단한 소개를 해 주었습니다.
  - Windows Phone에서 PPT를 직접 편집하는 시연을 보여주었습니다.
    - 노트북에 태블릿에 스마트폰을 넣고 무슨 가방이 아니라 군장같은것을 가지고 다니는 모습을 묘사해주었는데, 마치 주말의 내 모습 그대로 였습니다.
    - Windows Phone에 Project의 영상입력단자를 연결하니 바로 화면이 PC의 Windows 10과 같이 바뀌었습니다.
      - 이건 그냥 Phone이 아니라 PC 더군요.
      - 거기서 UWP 버전의 PowerPoint를 열어서 직접 편집하는것을 간단히 보여주었습니다.
      - 물론 모든 종류의 Desktop Application이 돌아가진 않겠지만, UWP로 작성된 App.들은 모두 돌아가겠죠.

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.10.jpg?raw=true)  

####점심시간

처음 행사 안내에 점심식사에 대한 따로 언급이 없어서 근처 식당이나, 대학내의 교내식당에서 사먹어야하는 줄 알고, 찾아봤는데 다행히 도시락으로 제공해 주었습니다. 한식이었으며, 맛있고 영양분을 골고루 섭취할수 있는 아주 훌륭한 도시락이었습니다.  

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.14.jpg?raw=true)  

밥을 먹고 로비로 나오니 전시된 바이크에 누님한분이 서있더군요.  그냥 지나가면서 대충 찍다보니 사진이 쫌... 최소한 밝기라도 맞췄어야 했을텐데요.  

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.12.jpg?raw=true)  

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.13.jpg?raw=true)  

오후 세션은 6개의 Track으로 나뉘어서 진행됩니다.

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.11.jpg?raw=true)  

며칠전에 참석한 `Data Grand Conference 2015`에서 시간마다 Track을 옮겨다니니 매번 자리 찾는것이 큰 일이더군요. Microsoft는 행사 후 동영상으로 다른곳보다 비교적 빨리 공개를 해주므로 그냥 1개의 Track에서 계속 앉아 있기로 결정했습니다. C++ 관련 Track이 진행이 진행되는 Track 2에 쭉 있기로 결정했습니다.

#### Track 2-1. What is new in Visual C++ 2015 and Future Directions
- Ulzii Luvsanbat , Ayman Shoukry

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.15.jpg?raw=true)  

Keynote를 하신 Visual C++의 Team Manager Ayman Shoukry는 계속 이 사람이 잘하고 있나 감시를 하는 듯한 모습이었고, Ulzii Luvsanbat 가 계속해서 진행을 하였습니다. Visual C++ 2015에서의 기능에 대하여 전반적으로 설명을 해 주었습니다.

- Refactoring 기능 : C#에 비해서 아직까진 많이 부족하지만, 따라가려고 노력 중입니다.
- Single File Intellisense : C++ 파일 하나면 열더라도 내부적으로 Project를 생성하여 기본 Library Header 파일과의 연동 및 Intellisense 기능을 사용 할 수 있습니다.
- Quick Action 기능 (`Ctrl + ,`)에 대한 몇가지 시연을 보여주었습니다.
  - `\n\t` 등이 포함된 문자열을 보기좋게 자동으로 표현해 주는 기능
  - Derived Class에서 pure virtual function 구현
  - Rename Function
  - Function의 declaration에서 peek windows로 definition 생성
  - Generic Lambda를 Extrac Function으로 생성
- `Send Smile`, `Send Frown`을 이용해서 건의를 전달해주면 Update시 반영을 합니다. Update 우선순위에 큰 영향을 미치는 항목이니 필요한 기능에 대해서는 자주 Send를 해주시는게 좋습니다.
- Diagnostic Monitor 및 Function 별로 수행시간 계산 : 내부적으로 복잡한 heuristic algorithm을 이용하여 실제 Machine에서의 수행시간과 거의 동일한 결과로 계산을 합니다.
- Update 1이 다음달 Release 됩니다.
  - Visual Studio 2013때와 같이 3개월 단위로 Update를 배포할 계획입니다.
  - 아직 C++11도 100% 다 수용하지 못하고 있습니다만, 표준을 따르도록 노력하고 있습니다.
  - `await`(C#에서 async task의 결과를 기다리는 keyword)가 Update 1에 반영될 예정입니다. (개인적으로는 정말 기쁜 소식입니다.)
  - CLang with microsoft code generator도 개발중에 있습니다. 이제 많은 IOS App.을 Windows에서도 돌릴 수 있습니다.
  - IDE 없이 Compiler만 별도로 제공할 계획입니다.
  - Remote Linux Debegging 기능 및 Linux Project 생성도 추가될 계획입니다.
- Code Optimization을 이용하여 algorithm을 대신 최적화 해줍니다.
  - for문 안에 반복적인 if가 있는 경우 if 조건을 먼저 수행하고 for-loop를 수행하는 식으로 자동으로 최적화 해줍니다.
- Multi-Build 기능을 제공할 계획입니다.
  - 지정한 시간(예를 들어서 퇴근후 시간)에 놀고있는 PC를 이용하여 Build에 사용하여 Build 시간을 줄일 수 있는 기능을 제공합니다.
- Visual Studio Code 가 C++도 지원되도록 할 계획입니다.

- QnA 시간에 나온 질문 중 `왜 Windows에서 C++을 사용해야 하느냐?`에 대해서 이렇게 답하였습니다.
  - 새로 만들것 같으면 `C#`이 훨씬 더 좋은 방법입니다.
  - Performce가 중요한 application이거나, UI가 아주 Heavy한 경우에는 C++이 더 좋습니다.
  - 기존의 C++ Code가 많은 Project인 경우에는 C++을 계속해서 사용하는 경우가 좋습니다.
    - 예를 들어서 Adobe의 application들은 과거 C++로 만들어 졌기 때문에 계속해서 C++로 개발중입니다.

#### Track 2-2. 알아두면 핵 이득! VC++로 안드로이드 개발하기
- 김성엽

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.16.jpg?raw=true)  

Visual Studio 2015를 이용하여 C++을 이용하여 Android app을 개발하는 내용 및 Android Project 생성 및 Emulator 실행을 보여주었습니다.

- 개발자에게 더 많은 Platform은 더 많은 기회가 생김을 의미합니다.
- 요즘 고객의 요구사항 중 Desktop용 App. 개발을 의뢰하면서 Mobile에서도 가능했으면 좋겠다는 것이 늘어가고 있습니다.
- Android NDK를 사용하면 5개 정도 함수만 구현해주면 C++로 Android app.의 개발이 가능합니다.
- Microsoft의 Android Emulator는 요구사항에 만족하지 않아도 설치는 되지만 실행은 되지 않습니다.
  - `Hyper-V`(Win8이상)가 필요합니다.
  - BIOS에서 `Hardware Virtualization`이 지원되는지도 확인을 해야 합니다.
  - 실제 물리 Memory를 사용해서 구동하므로 충분한 RAM (최소 6GB이상)이 필요합니다.
  - Visual Studio Community나 Professional에서는 관리자 권한으로 실행해야 하며, Enterprise 에서는 자동으로 관리자권한으로 실행됩니다.
- Native app 개발 방법 및 Project 구조에 대하여 소개를 해 주었으며, Android Java Project 생성 및 실행도 간단히 보여주었습니다.
- 모든 예제 및 설명은 블로그에 자세히 소개되어 있으니 참조하라고 하였습니다.

#### Track 2-3. Visual Studio를 사용하는 비주얼 개발자를 위한 Tips & Tricks (No Slide, All Demo!) 알아두면 핵 이득!
- 김태영

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.17.jpg?raw=true)

엄청나게 많은 사람들이 이번 세션을 들으러 들어왔습니다. 역시나 말을 아주 재밌게 잘 하십니다. Visual Studio를 사용할 때 알아두면 편리하거나, 좀 더 화려하게 화면을 꾸미는 Tip을 소개해주었습니다.

- Nuget Package를 이용해서 설치가 가능한 IDE 파워툴에 대한 소개입니다.
  - Pronama-chan IDE : Editor 창에 미소녀가 표시됩니다.
  - VSColorOutput : Build창이 Color로 출력됩니다.
  - Change Color Theme
  - Color Theme Editor
  - Trailing Whitespace Visualizer : space 등의 공간을 다른 색으로 표시합니다.

- Code 정적 분석 기능 (C#)
  - Code 의 정적 분석 기능 활성화/해제를 보여주었습니다.
  - Fxcop, Codecracker(시험판) 등의 추가적으로 적용도 가능합니다.

- Visual Studio의 기능 소개
  - Alt + Drag 후 한번에 수정
  - Ctrl + Shift + v : 저장 이력 저장
  - Ctrl + , 후 검색
  - Solution Explorer에서 열린 파일 위치 열어주기 버튼
  - JSON, XML을 Class로 붙여넣기
  - IDE Layout 저장 및 불러오기

#### Track 2-4. 디버깅, 어디까지 해봤니? 당신이 아마도 몰랐을 디버깅 꿀팁 공개
- 김희준

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.18.jpg?raw=true)

Visual Studio 2015의 Debugging 에 대한 여러가지 시연을 보여주었습니다. 하지만 아직까지는 Native(C++)에 대해서는 적용되지 않고, Managed(C#)에만 적용 가능한 것들이 많아서 아쉬웠습니다.

- Data Break Point
  - Native(C++)도 가능합니다.
  - 변수명을 Watch 창에 &를 붙여서 적어주면 Memory 주소를 알 수 있습니다.
  - Debug 메뉴에서 Memory 주소와 Byte수를 입력하면 해당 값이 바뀌었을 때 Break 됩니다.

- Trace Point
  - Break Point를 Action 쪽 설정값을 주면 Break 되진 않고, 거기서 설정한 출력값 (Value, Call Stack 등...)을 Output 창에 출력합니다.

- Intellitrace
  - 실행을 녹화하여 추후 원하는 시점으로 돌아가서 Debugging이 가능합니다.
  - UI가 깨진다던지, Button을 눌렀을 때 이상동작이 있는 것 같이 프로그램이 죽지는 않지만 뭔가 원인을 모르겠는 버그를 찾는데 편리합니다.
  - Managed(C#)만 되고, Enterprise 이상 버전에서만 지원합니다.

- `Run to Cursor` / `Step into Specific`
  - C++의 경우 parameter로 string이 있는 경우 `F11`을 눌러도 해당 함수 안으로 들어가기 위해서는 몇단계를 거쳐야하는데, 바로 들어갈 수 있도록 해줍니다.

- `void*`의 값을 보고 싶으면 주석에서 casting 한 형식을 적어준 다음 마우스를 올리면 볼 수 있습니다.

- 시간 관계상 설명은 못해줬지만 Multithread 환경의 경우 Parallel Stack, Parallel Watch 활용이 가능합니다.

####경품추첨 및 스낵코너

경품추첨이 있었습니다. 등록할때 작성한 명함 또는 명함이 없는 사람들은 이름을 적어서 냈는데, 모두 다 종이만 뽑혔습니다. 명함은 단 한번도 뽑히지 않았습니다.

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.19.jpg?raw=true)

그리고 로비에는 저녁 세션 참가자들을 위한 칵테일 과 스낵 코너가 마련되었는데, 칵테일은 한 30분은 줄서야 먹을 수 있을만큼 줄이 길었구요. 스낵도 사람이 너무 많아서 먹기가 많이 불편했습니다. 그래도 다행히 빵종류만 있을줄 알았는데, 김밥과 떡이 있었습니다.

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.20.jpg?raw=true)

####Community Session 4-1. 녹슨 C++코드에 모던 C++로 기름칠하기
- 옥찬호

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.21.jpg?raw=true)

제가 운영진으로 몸담고 있는 `Facebook C++ Korea`의 대표입니다. C++의 안좋은 Code에 대한 예시 및 그것을 Modern C++을 이용하여 고치는 경우에 대해서 소개를 하였으며, 관련 새로운 문법에 대해서 몇가지 소개해 주었습니다.

- `#ifdef` 와 같은 전처리기는 왠만하면 사용하지 않는 것을 추천하였으며, 함수안에서 일부만 전처리기로 처리하는 것은 좋지 않습니다.
  - `_UNICODE` 를 확인하는 경우는 `function template`를 활용하여 함수를 나누는 것이 좋습니다.
- - if 중첩으로 depth가 계속 증가하는 code의 경우는 검사조건을 반대로하여 바로 return 하는 식으로 고쳐서 depth 증가를 피할 수 있습니다.

- Macro의 사용은 무조건 피하는 것이 좋습니다.
  - 변수 대신 사용하는 경우는 `enum` < `enum class` 를 활용하는 것이 좋습니다.
  - 함수 대신 사용하는 경우는 `inline`등을 이용하여 함수로 구현하는 것이 좋습니다.

- 기타 Smart Point auto, ranged-for 를 소개하였습니다.

####Community Session 4-2. 프로그래밍 언어의 F1머신 C++을 타고 Windows 10 UWP 앱 개발의 세계로
- 유영천 (megayuchi)

![DGC2015](https://github.com/DevStarSJ/Study/blob/master/Blog/Conference/2015/image/small.2015-10-27-Techdays.22.jpg?raw=true)

UWP (Universla Windows Platform) app. 을 C++로 개발하는 것에 대한 소개였습니다. 개인적으로 가장 관심이 가는 세션이었습니다.

- Java로 된 minecraft를 Microsoft가 인수하여 UWP로 다시 구현하였습니다.
- UWP는 Mobile 및 Web UI를 구현하기가 쉽습니다.
- 아직까지는 sandbox의 권한문제 때문에 hareware의 모든 기능을 다 사용하지는 못합니다.
- IoT상의 Windows10의 UWP는 Desktop에서 실행되는 것에 비해 제외된 것들이 많습니다.
  - File 선택창을 못띄웁니다.
- 배포가 쉽고, 여러 Device에서 실행이 가능하지만, 기능이 Desktop application보다는 많이 부족합니다.
- GDI를 사용하지 않고 XAML을 이용하여 화면에 출력합니다.
  - C#의 WPF랑 거의 흡사한 형태입니다.
- Windows10부터는 창모드도 지원하며, file drag & drop도 지원되어서 웬만하면 Desktop용 application을 개발하는것 보다는 UWP로 개발하는게 여러모로 유리합니다.
- `C++/CX` 문법을 조금은 배우셔야 합니다.
  - 기본적으로 모든 객체에 대해서는 reference로 전달되며, smart point를 내장하고 있어서, memory 할당 해제를 할 필요가 없습니다.
- Lambda 식과 PPL을 많이 사용합니다.
  - 절대로 UWP는 UI를 Block할 수 없게 설계되어 있어서 무조건 비동기로 실행시키게 되어 있습니다.
- 만약 C++로 예제 code를 찾기 힘들면 C#으로 검색한 뒤어 . 대신에 -> 로만 고쳐서 왠만해서는 잘 돌아갑니다.
  - API 호출도 C# 형식에 가깝습니다.
- 기존 C++ 개발자가 UWP를 위해서는 몇가지 추가로 학습하셔야 합니다.
  - XAML
  - C++/CX 문법
  - PPL 및 async api
