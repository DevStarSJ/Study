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

###1. Citrus
- License Key, Activation Code생성 및 관리 관련 작업들을 수행합니다.
- multi-platform용으로 사용될 것을 감안하여 MFC class를 전혀 사용하지 않았습니다.

####1.1 BitSet class
- bit(0,1) 들을 저장하는 컨테이너 class 입니다.
- bit을 저장하고 읽어오는데 편리한 기능들을 제공합니다.

####1.2 Citrus class : 
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

