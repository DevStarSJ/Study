### Microsoft Tech Days Korea 2015  

- 일시 : 2015년 10월 27일 화요일 09:00 ~ 21:10  
- 장소 : 세종대학교 광계토관 컨벤션센터  

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


2 김성엽 안드로이드개발
C++로 안드로이드 개발 및 크로스 플랫폼

50위 안드앱중 80프로가 C++
개발자에게 더많은 플랫폼은 더 많은 기회가 제공
고객의요구 데답용얍 사면서 모버일로도 가능하면 좋겠다
Ndk쓰면 5개정도 함수만 추가로쓰면 안드로이드개발가능

안드로이드 에뮬레이터
Hyper-v필요. Win 8 pro 이상
Bios에서 하드웨어 가상화가 지원되어야함
실제 물리메모리 사용. 충분한 램 6기가이상
최신노트북 프로급, 램 8기가

커뮤니티나 프로에서는 관리자 권한으로 실행해야함, 엔터프라이즈애서는 자동으로

블로그에 native app개발 내용들 있음
Native app개발 방법 소개
안드로이드 프로젝트의 구조맟 직접 개발해야할 함수들에 대해서 설명
Main.cpp에 7개 함수중 생성,해제 빼고 5개만 수정하여 사용하면됨

안드로이드 자바기반 앱 개발 시연
Shared library 하나로 안드로이드 윈도우 다 가능

	3.	김태영
데모만 진행

프로나마찬: 애니메
빌드가 녹색 등 컬러로 , 등 빌드리포트 : VSColorOutput
Change color theme
Color theme editor

알트드래그 후 한번에 수정
공백보여줌 : trailing whitespace visualizer
컨트럴수ㅏ프트v 이력저장
컨트럴 컴마 하고 검색
솔탐에서 열린파일위치열어주기

Json,xml을 클래스로 붙여놓기
레이아웃 저장

코드분석
Fxcop
Codecracker 시험판
라이브 시각적 투라, 라이브 속성 탐색기
Developer assistant : intellisense 및 검색
디버깅 포인트 import,export

	4.	김희준님

프로파일링
perfTips
진단툴을 이용하여 메모리해제안하는거 찾아내는 시연
메모리 스냅샷,
메니지드,네이티브

브레이크 포인트
트레이스 포인트
data break point : 메모리 주소에 브피 걸기
워치창 옮긴뒤 &붙여서 주소얻고 디버그 메뉴에서 찾아가서 주소와 바이트수 입력

트레이스포인트 : action bp가 걸리면 값 및 콜스택 출력

exception

intellitrace
실행을 녹화
ui 깨지는버그, 화면 레이아웃 깨지는 버그 등 프로그램이 죽지는 않지만 뭔가 미묘한 버그
오히려 crash되는군 덤프떠서 보면 됨
녹화를 떠서 뒤로 되돌려보면서 확인
닷넷만가능
엔터프라이즈이상만

run to cursor
step into specific
@err
,hr


void* 된거 볼려면 주석애ㅔ서 캐스팅하면 볼수있음

패러럴 스택, 패러럴 워치
멀티스레드 디버깅

경품추첨

저녁 스낵코너

저녁세션1 옥찬호
녹슨 C++코드에 모던 C++로 기름칠하기

#ifdef로 떡칠된코드, if중첩으로 도배된 코드
전처리기
리소스관리 등...

_UNICODE 를 함수 2개로 들어오는 타입에따라 구분
함수템플릿

매크로
변수대신사용 > enum > enum class
함수대신사용 > inline

리소스관리
메모리해제코드 > RAII 클래스로 만들어서 생성자, 해제자 로 처리
하지만 포인터로 만들면 생성자는 실행되지만 자동으로 소멸자는 호출 안된다
> 스마트포인터 
람다식
auto
ranged-for

오후세션2 유영천
UWP C++
minecraft ms가샀다 자바로된걸 c++로 만들었다
UWP 모바일 친화, 웹친화 ui쉽다
권한문제 sandbox 하드웨어 모든가능 못씀
iot에서 제외된 것들이많다. 파일선택 등...
배포쉽고, 디바이스 많지만 기능은 데탑앱보다 많이 딸린다
gdi 못쓰고 xaml
창모드지원
드래드앤드랍 지원
megayuchi
c++/cx를 조금은 사용 스마트포인트를 내장한 c++ c#과도 비슷. 메모리 할당 해제 안해도 됨
람다와 ppl 많이 사용
api호출이 c#형태
예제없으면 C#으로 한뒤 . 대신 화살표 왠만하면 돌아감
xaml ui
wpf랑 거의 같음

모든 작업은 비동기 ui 블록 절대 없게

uwp위해서 추가로 학습할것
xaml
c++/cx
async api + ppl






