#Orange License

##Abstract

- Orange 6.1 제품의 Orange License 및 Activation Code 와 견롼된 모든 작업을 수행합니다.

##개발환경

- MFC (Visual Studio 2015)
- Chilkat Library (C++)

##빌드시 유의사항

1. try_2015 내에 License 폴더를 생성하여서 해당 폴더에 Checkout 받으셔야 합니다.
  - try_2015 내에 파일을 참조합니다.
  - 빌드시 header 파일과 lib, dll 파일들을 try_2015 폴더로 복사합니다.
2. 만약 Visual Studio 버전이나 Update 등의 큰 변화가 있는 경우 Chilkat도 해당 버전으로 변경해주어야 합니다.
  - Chilkat은 source code가 아닌 lib, dll 형태로 제공되기 때문에 변경해 주어야 정상동작합니다.
  - 컴파일 오류는 나지 않는데, 암호화 결과가 비정상적으로 나옵니다.

##Project 설명

###1. Citrus Project
- License Key, Activation Code생성 및 관리 관련 작업들을 수행합니다.
- multi-platform용으로 사용될 것을 감안하여 MFC class를 전혀 사용하지 않았습니다.

####1.1 BitSet class
- bit(0,1) 들을 저장하는 컨테이너 class 입니다.
- bit을 저장하고 읽어오는데 편리한 기능들을 제공합니다.

####1.2 Citrus class
- License Key, Activation Code 관련 작업을 수행합니다.
- `SetVersion()` : Orange 6.0 / 6.1 버전을 설정합니다.
- `GetTrialDays()` : 현재 License Key의 남은 기간을 일 단위로 return 합니다.
- `RegEnc()` : Registry에 Key 기록시 암호화 하는 기능을 제공합니다.
- `SetField()` : License Key중 특정 Field를 원하는 값으로 설정합니다.
- `GetField()` : License Key중 특정 Field의 값을 return 합니다.
- `GetFieldText()` : License Key중 PRODUCT, EDITION, LICENSE_TYPE에 대하여 문자열로 해당 값을 return 합니다.
- `GetExpiredText()` : License Key 만료일을 `2016-04-06` 형식으로 return 합니다.
- `GetProductText()` : License Key의 정보를 `Orange for Oracle 6.1` 형식으로 return 합니다.
- `GetErrorCode()`, `GetErrorString()` : License Key 생성 또는 검증시 발생한 오류 코드, 설명을 return 합니다.
- `ParseLicenseKey()` : 입력된 License Key를 검증합니다.
- `ParseEncryptedKey()` : 암호화된 형식으로 입력된 License Key를 검증합니다.
- `GetLicenseKey()` : License Key를 return 합니다.
- `GetLicenseText()` : License Key의 설명정보를 `Orange for Oracle 6.1 DBA Edition Trial License Expires on 2016-04-06` 형식으로 return 합니다.
- `GetExcryptedKey()` : License Key를 암호화된 형식으로 return 합니다.
- `GetIntSum()` , `GetIntSumChar()` : License Key 생성시 CheckSum 값 계산 관련 함수
- `GetUsingDays()` : License Key의 전체 기간을 일 단위로 return 합니다.
- `GetRemainDays()` : License Key의 남은 기간을 일 단위로 return 합니다.
- `GetExpiredTime()` : License Key 만료일은 time_t 형식으로 return 합니다.
- `VerifyActivationCode()` : 입력된 Activation Code를 검증합니다.
- `CalcExpiredTime()` : 시작일과 사용기간을 입력받아서 만료일을 return 합니다.
- `CalcUsingDays()` : 시작일과 만료일을 입력받아서 사용기간을 return 합니다.
- `Encrpt()` , `Decrypt()`: 입력된 문자열을 암호화/복호화 합니다.
- `MakeHash()` : Activation Code에서 사용하는 Hash값을 생성합니다.
- `ValidateHash()` : Hash 값과 Activation Code내의 항목들이 적합한지 검사합니다.
- `WS2()` : `std::string` 와 `std::wstring`를 변환해 줍니다.

####1.3 Cypher class
- 암/복호화 기능을 제공합니다.
- Chilkat Library를 내부적으로 사용했으며 해당 기능을 wrapping한 class 입니다.
- `EncriptDES()`, `DecriptDES()` : 입력받은 값을 Trible-DES로 암호화/복호화 합니다.
- `SHA256()` : 입력받은 값을 SHA256으로 Hash처리 합니다.

###2 OLicense Project
- License Key 및 Activation Code 관련 Registry 작업을 수행합니다.
- Citrus의 기능을 MFC용 CString로 wrapping 하였습니다.

####2.1 OLicenseKey class
- License Key 관련 작업 및 Registry 작업을 수행합니다.
- `Citrus class`와 함수명이 같은 것은 단순히 CString로 처리하기위한 wrapping 함수들입니다.
- `SetAppPath()` , `SetRegPath1()`, `SetRegPath2()` : Registry 경로를 설정하는 함수입니다.
- `SetExpiredMessageShown()` , `IsExpiredMessageShown()` : 기간제 License 에서 만료 경고 메세지를 표시여부를 Registry에 기록/확인하는 함수입니다.
- `MakeHostID()` : 하드웨어 정보를 읽어서 HostID를 생성합니다.
- `GetKeySerial()` : 제품, 에디션, 입력된 S/N을 이용하여 `00.01.27` 형식의 Registry 기록용 Key를 생성하는 함수입니다.
- `GetKeyList()` : Registry를 읽어서 입력되어 있는 License Key 목록을 return 합니다.
- `GetKey()` : `00.01.27` 형식의 Serial을 입력받아 해당 License Key를 return 합니다.
- `DeleteActivationCode()` : 입력받은 Serial의 Activation Code를 Registry에서 삭제합니다.
- `DeleteKey()` : 입력받은 Serial의 License Key를 Registry에서 삭제합니다.
- `RegisterLicenseKey()` : License Key를 Registry에 등록합니다.
- `RegistPeriod()` , `ReadPeriod()` , `CheckPeriod()`, `ResetCheckPeriod()` : 사용자 PC에서 Registry에 Subscription License 의 만료일 이전의 경고 메세지 띄우는 기간 및 Grace Period 관련된 값들을 Registy에 기록/읽기/확인/초기화 하는 역할을 수행합니다.
- `IsValidActivationCode()` : Activation Code와 License Key를 입력받아서 적합한지 확인합니다.

###3 ORestful Project
- Chilkat을 활용하여 WebService로 Post 하는 단 하나의 함수만을 제공합니다. : `CWVWebService::Post()`

###4 License Project
- `License.exe` 파일을 생성합니다.
- 각각의 Dialog 별로 많은 기능을 제공하지 않으므로 각 Dialog 별 기능에 대해서 간략하게 설명드리겠습니다.
- `Dlg_Container` : 다른 Dialog들을 실행시키는 Dialog 입니다. 기본 디자인 작업은 여기에서 하시면 모든 Dialog에 적용됩니다.
- `Dlg_MgrKey` : Toolkit의 Report Control을 활용하여 PC에 입력된 License Key 목록을 보여주며 관리해주는 기능을 제공합니다.
- `Dlg_ActComp` : Activation 과정이 끝났다는 것을 사용자에게 알리는 문구를 출력합니다.
- `Dlg_ActPend` : Offline Activation 과정 중 Pending 상태임을 알리는 문구를 출력합니다.
- `Dlg_ActWait` : 현재 Pending 중인 License Key가 있는데, 새로운 Key을 입력하고자 할때 경고 문구를 출력합니다.
- `Dlg_GenRetJson` : Deactivation Code를 생성하고 Registry에서 License Key 및 Activation Code를 삭제합니다.
- `Dlg_HostID` : Offline Activation 과정 중 Activation Code를 생성합니다.
- `Dlg_InAct` : Activation Code를 입력받아서 검증 후 Registry에 기록합니다.
- `Dlg_InKey` : License Key를 입력받아서 검증 후 Registry에 기록합니다.
- `Dlg_InMail` : 개인정보 수집,이용을 동의받으며 e-mail을 입력받습니다.
- `Dlg_RetComp` : Deactivation 과정이 끝났다는 것을 사용자에게 알리는 문구를 출력합니다.


