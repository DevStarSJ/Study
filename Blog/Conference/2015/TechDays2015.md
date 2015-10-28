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
  3. `Personal Computing` : Universal Windows Platform, HoloLens 등 사용자 경험을 바탕으로 가상 현실 등 풍부한 시나리오를 공급하고자 노력하고 있습니다.
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

#### General Session : 세상을 품은 플랫폼과 그 가능성에 대해서
마이크로소프트 에반젤리스트팀
김명신 부장님

생산성, 지능적 클라우드 조직, 맞춤형컴퓨팅 환경

새로운 기능이 추가될때마다 사용하기 어려웠다.
이제는 펜, 몸동작 등 친숙한 방법으로 이제는 새로운 기능을 제공해주기 위해서 노력하고있다.
컴퓨터뿐만 아니라 모든 디바이스에서 재공하고자 노력하고 있다.

맞춤형 컴퓨팅에 대한 마소의 노력
김영욱부장님 밀덕
Cross 
Multiple device families, 각각의 디바이스를 관통하는 크로스
플랫폼을 관통하는 크로스
윈도우즈10은 디바이스를 관통하는 크로스
소스레벨 호환성이 아닌 바이너리 레벨의 호환성
윈도우에서 돌아가는 바이너리를 안드로이드이서 바로 실행UWP
브릿지 테크놀러지
오브젝티브씨 코드로 안드로이드를 생산
등...
안드로이드까지는 컴파일이 가능한데 ios는 맥북에서 컴파일해야한다. Xcode가 필요하다
아두이노 라즈베리팡이 로 만든 비비탄 분당 120발 쏘는 경개병 시연
데이터를 이벤트 허브로 미국 서버로 전송

클라우드
김명신 부장님

마이크로소프트 애저Asure

김태영부장님
최상의 개발도구
Visual Studio

IntelliTest 시연
자동으로 테스트 코드 생성맟 수행
Asp.net 5.0을 리눅스에 배포 하는 시연

마지막 김명신부장님

윈폰에서 ppt 편집 시연

트랙2-1

사실 C#에서는 많이 화려하게 개발이 가능하지만 c++은 아직 부족하지만,
많이 따라가려고 노력했다.
Refactoring, single file intellisense

시연
컨투럴 콤마
긴 문자열 스마트탭 raw string indentation ?
Derived class 에서 quick action하면 pure virtual function 구현
Rename function
Function의 declaration에서 defination을 생성 peek window로
Generic lambda 를 extract function으로 생성
Send smile / send frown 오렌지에도 들어가면 좋을듯
Diagnostic monitor가 자동으로 뜸
Function 별로 수행시간 계산 > 복잡한 휴레스틱 알고리즘

Await update1
아직 11도 100프로 못하고 있다
generic lambda, noexcept, inline namespace, thread safe local, alignof alignas, unicode string literals modifiers, auto return decudcing, constexpr, 

Clang with microsoft code generator
많은 ios앱을 윈도우즈에서 돌릴수있다
캔디크러시도 가능

빌드타임을 줄였다고 하는데...
코드 최적화 컴플렉스한 알고리즘을 대신 최적화
For if > if for
다음달 첫 업데이트 3개월주기

멀티빌드 여러기계로 빌드 퇴근뒤 놀고있는 피시들
Ide말고 컴파일러만 원한다
Remote linux debugging
Vs code for c++

큐엔에이

씨뿔뿔 쓰는 이유 윈도우에서

기존 c++ 코드가 있는 경우 어도비 리더 는 시샵이전에 있던 코드
퍼포먼스 유아이가 해비한 경우
크로스플랫폼의 경우 기존앱을 확대하고자 할 경우

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






