#WVMIS

##Abstract

WareValley Orange 제품의 License 및 제품, 고객, 계약 상황들을 관리하는 기능을 제공합니다.  
C#의 Winform을 사용했으며, UI Control은 DevExpress를 활용하였습니다.  
Oracle database server에 접속하여 데이터를 관리합니다.  
아래 기능은 MFC에서 생성한 DLL과 연동하여 그 기능을 지원합니다.
- License Key 생성
- License Key 정상 여부 확인
- Activation Request Code 정상 여부 확인
- Activation Code 생성
- Deactivation Code 생성

##개발환경

- C# (Visual Studio 2015)
- DevExpress v15.1
- Oracle
- MFC (Visual Studio 2015)
- Chilkat Library (C++)

##Project 설명

1. WVMIS
  - 실제 작업을 한 Project 입니다.
  - MDI 기반의 Winform으로 구성되었습니다.
2. LunaStar
  - Library 성격의 Project 입니다.
  - 이번 Solution과는 무관하게 기존에 작업된 Project 입니다.
  - 이번 Solution에서는 다음의 기능을 제공합니다.
    - Oracle database 연결 및 SQL 작업
    - Winform을 구성하는 User defined Control
    - File I/O
    - DevExpress의 extra skin 제공
    - MDI, 각종 Form의 각종 기능을 미리 작업해서 WVMIS에서 상속받아서 활용 (편의상 WVMIS로 위치를 옮김)
    - Menu, 환경설정 관련 사항을 File에서 읽고 쓰기 (편의상 WVMIS로 위치를 옮김)
    - MDI의 Menu를 NavigationBar + Tree Items 구조로 구성 (편의상 WVMIS로 위치를 옮김)
3. Setup
  - 배포시 Setup 파일을 생성해주는 Project 입니다.

###1. WVMIS

####1.1 Program.cs
  - Main() : Program의 시작점 입니다.
  - SetStaticEnvironment() : 고정적 환경변수를 가져옵니다.
  - SetDBList() : 접속 Database 관련 사항을 읽어옵니다.

####1.2 Forms
- Winform들을 모아놓음

#####1.2.1 MDI.cs
- MDI Form
- 선택된 Menu의 Form을 실행시키는 역할을 합니다.
- 이번 Project와는 무관하게 LunaStar에서 가져온 것으로 자세한 설명을 생략합니다.

#####1.2.2 Base/FormBase.cs
- 작업할 모든 Winform들의 부모 class
- 현재 상태 (입력, 수정, 삭제, 선택) 에 따른 각종 Control들의 Enable 상태 변경
- SQL문을 database 로 전달하여 그 결과로 DataTable을 return
- SQL문 만으로 그 결과를 Control에 반영
- 이번 Project와는 무관하게 LunaStar에서 가져온 것으로 자세한 설명을 생략합니다.

#####1.2.3 CR
- 기준정보 관련 Form들을 모아두었습니다.

#####1.2.3.1 CR_PROD
- 제품정보를 관리합니다.
-  RefreshGrid() : Grid에 목록을 출력합니다.
-  view_List_FocusedRowChanged() : Grid에서 특정 항목 선택시 동작하는 Event
-  ClearText(), SetSaveBtn(), SetKey() : Control들의 상태를 변경합니다. FormBase에 의해 호출됩니다.
-  btn_Add_Click() : 추가 버튼 Click Event
-  btn_Modify_Click() : 수정 버튼 Click Event
-  btn_Delete_Click() : 삭제 버튼 Click Event
-  btn_Save_Click() : 저장 버튼 Click Event
-  btn_Cancel_Click() : 취소 버튼 Click Event

#####1.2.3.2 CR_PERIOD
- 기간 정책을 관리합니다.
-  RefreshGrid() : Grid에 목록을 출력합니다.
-  InitCurrentValues() : 현재의 기간 정책 값을 화면의 SpinEditor에 적용합니다.
-  btn_Save_Click() : 저장 버튼 Click Event







