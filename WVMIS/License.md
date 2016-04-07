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

##1. WVMIS

###1.1 Program.cs

