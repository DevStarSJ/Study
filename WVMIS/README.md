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
  - Main() : Program의 시작점 입니다.
  - SetStaticEnvironment() : 고정적 환경변수를 가져옵니다.
  - SetDBList() : 접속 Database 관련 사항을 읽어옵니다.

###1.2 Forms
- Winform들을 모아놓음

####1.2.1 MDI.cs
- MDI Form
- 선택된 Menu의 Form을 실행시키는 역할을 합니다.
- 이번 Project와는 무관하게 LunaStar에서 가져온 것으로 자세한 설명을 생략합니다.

#####1.2.2 Base/FormBase.cs
- 작업할 모든 Winform들의 부모 class
- 현재 상태 (입력, 수정, 삭제, 선택) 에 따른 각종 Control들의 Enable 상태 변경
- SQL문을 database 로 전달하여 그 결과로 DataTable을 return
- SQL문 만으로 그 결과를 Control에 반영
- 이번 Project와는 무관하게 LunaStar에서 가져온 것으로 자세한 설명을 생략합니다.

####1.2.3 CR
- 기준정보 관련 Form들을 모아두었습니다.

#####1.2.3.1 CR_PROD
- `1.1 제품관리` 를 눌렀을 때 실행됩니다.
- 제품정보를 관리합니다.
-  `RefreshGrid()` : Grid에 목록을 출력합니다.
-  `view_List_FocusedRowChanged()` : Grid에서 특정 항목 선택시 발생하는 Event
-  `ClearText()`, `SetSaveBtn()`, `SetKey()` : Control들의 상태를 변경합니다. FormBase에 의해 호출됩니다.
-  `btn_Add_Click()` : 추가 버튼 Click Event
-  `btn_Modify_Click()` : 수정 버튼 Click Event
-  `btn_Delete_Click()` : 삭제 버튼 Click Event
-  `btn_Save_Click()` : 저장 버튼 Click Event
-  `btn_Cancel_Click()` : 취소 버튼 Click Event

#####1.2.3.2 CR_PERIOD
- `1.2 기간 정책`을 눌렀을 때 실행됩니다.
- 기간 정책을 관리합니다.
-  `RefreshGrid()` : Grid에 목록을 출력합니다.
-  `InitCurrentValues()` : 현재의 기간 정책 값을 화면의 SpinEditor에 적용합니다.
-  `btn_Save_Click()` : 저장 버튼 Click Event

#####1.2.3.3 CR_CUST
- `2.1 고객관리`를 눌렀을 때 실행됩니다.
- 고객사 및 담당자를 관리합니다.
- `InitControl()` : 각종 Combobox 의 값들을 설정합니다.
- `RefreshGrid_CustList()` : 고객 List를 출력합니다.
- `VIEW_CUST_LIST_FocusedRowChanged()` : 고객 List에서 선택 했을 경우 발생하는 Event
- `ClearText()`, `SetSaveBtn()` : Control들의 상태를 변경합니다. FormBase에 의해 호출됩니다.
- `BTN_C_ADD_Click()` : 고객 -> 신규 버튼 Click Event
- `BTN_C_MOD_Click()` : 고객 -> 수정 버튼 Click Event
- `BTN_C_CANCEL_Click()` : 고객 -> 취소 버튼 Click Event
- `BTN_C_DEL_Click()` : 고객 -> 삭제 버튼 Click Event
- `BTN_C_SAVE_Click()` : 고객 -> 저장 버튼 Click Event
- `EBTN_ZIPCODE_ButtonClick()` : 고객 -> 주소입력시 활성화 되는 우편번호 버튼 Click Event
- `RefreshGrid_AccountList()` : 담당자 List를 출력합니다.
- `SetAccState()` : 담당자 관련 Control 들의 Enable 상태를 설정합니다.
- `ClearAccText()`, `SetAccSaveBtn()` : SetAccState()에 의해 호출됩니다.
- `VIEW_ACCOUNT_LIST_FocusedRowChanged()` : 담당자 List에서 선택 했을 경우 발생하는 Event
- `VIEW_ACCOUNT_LIST_DataSourceChanged()` : 선택된 고객이 변경될 경우 VIEW_ACCOUNT_LIST_FocusedRowChanged() 호출
- `EBTN_A_ZIPCODE_ButtonClick()` : 담당자 -> 주소입력시 활성화 되는 우편번호 버튼 Click Event
- `BTN_A_ADD_Click()` : 담당자 -> 추가 버튼 Click Event
- `BTN_A_MOD_Click()` : 담당자 -> 수정 버튼 Click Event
- `BTN_A_CANCEL_Click()` : 담당자 -> 취소 버튼 Click Event
- `BTN_A_DEL_Click()` : 담당자 -> 삭제 버튼 Click Event
- `BTN_A_SAVE_Click()` : 담당자 -> 저장 버튼 Click Event

#####1.2.3.4 CR_CONT
- `3.1 계약관리`를 눌렀을 때 실행됩니다.
- 계약 정보를 관리합니다.
- `InitControl()` : 각종 Control의 초기값을 설정합니다.
- `ClearText()`, `SetSaveBtn()` : Control들의 상태를 변경합니다. FormBase에 의해 호출됩니다.
- `RefreshList()` : 계약 List를 Grid에 출력합니다.
- `view_List_FocusedRowChanged()` : Grid에서 선택이 변경된 경우 발생하는 Event
- `btn_save_Click()` : 저장 버튼 Click Event
- `btn_ProdDetail_Click()` : 제품 상세 버튼 Click Event
- `btnEdit_PartnerName_ButtonPressed()` : 협력업체 -> 업체명 Click Event
- `btnEdit_CustoerName_ButtonPressed()` : 고객사 -> 업체명 Click Event
- `btnEdit_PartnerSales_ButtonPressed()` : 협력업체 -> Sales 담당자 Click Event
- `btnEdit_CustomerSales_ButtonPressed()` : 고객사 -> Sales 담당자 Click Event
- `btnEdit_PartnerBilling_ButtonPressed()` : 협력업체 -> Billing 담당자 Click Event
- `btnEdit_CustomerBilling_ButtonPressed()` : 고객사 -> Billing 담당자 Click Event
- `btnEdit_PartnerTech_ButtonPressed()` : 협력업체 -> Tech 담당자 Click Event
- `btnEdit_CustomerTech_ButtonPressed()` : 고객사 -> Tech 담당자 Click Event
- `btn_add_Click()` : 신규 계약 버튼 Click Event
- `btn_cancel_Click()` : 취소 버튼 Click Event
- `btn_modify_Click()` : 계약 변경 버튼 Click Event
- `btn_delete_Click()` : 계약 삭제 버튼 Click Event
- `btn_prodHist_Click()` : 제품 계약 내역 Click Event
- `XUCC_FindAll_CheckedChanged()` : 전체기간 Checkbox Event

#####1.2.3.5 CR_CHKKEY
- `3.2 제품 키 확인`를 누르면 실행됩니다.
- License Key를 입력하면 해당 정보를 표시해 줍니다.
- `GetLicenseText()` : MFC DLL의 함수입니다.
- `GetText()` : GetLicenseText()의 결과를 C# string로 변환해줍니다.
- `btn_key_Click()` : 확인 버튼 Click Event

#####1.2.3.6 CR_ACT
- `4.1 활성화 관리`를 누르면 실행됩니다.
- 활성화 내역을 조회합니다.
- `InitControl()` : 각종 Control의 초기값을 설정합니다.
- `RefreshList()` : 활성화 내역 Grid (왼쪽)의 List를 출력합니다.
- `RefreshHistList()` : 왼쪽 Grid에서 선택된 항목에 대한 상세 이력을 오른쪽 Grid에 출력합니다.
- `btn_Search_Click()` : 검색 버튼 Click Event
- `view_List_FocusedRowChanged()` : 왼쪽 Grid에서 항목을 선택하면 실행되는 Event
- `view_Detail_FocusedRowChanged()` : 오른쪽 Grid에서 항목을 선택하면 실행되는 Event
- `view_Detail_DataSourceChanged()` : 오른쪽 Grid의 항목이 바뀔경우 실행되는 Event
- `XUCC_FindAll_CheckedChanged()` : 전체기간 Checkbox를 눌렀을 때 실행되는 Event
- `btn_ManualActivation_Click()` : `Manual Activation` 버튼 Click Event

#####1.2.3.7 CR_EMP
- 직원 관리 Form인데, 현재 사용하지 않습니다.

#####1.2.3.8 CR_GRADE
- 등급 관리 From인데, 현재 사용하지 않습니다.

####1.2.4 ES
- Dialog(Pop-up 형식으로 동작하는 Form)들을 모아두었습니다.

#####1.2.4.1 ES_ACC
- `3.1 계약관리` 에서 협력업체, 고객사의 `Sale 담당자`, `Billing 담당자`, `Tech 담당자`를 눌렀을 때 실행됩니다.
- 담당자를 선택 하는 Dialog 입니다.
- `btn_Cancel_Click()` : 취소 버튼 Click Event
- `btn_Save_Click()` : 저장 버튼 Click Event
- `grid_List_DoubleClick()` : Grid에서 더블 클릭시 Event

#####1.2.4.2 ES_ACT
- `4.1 활성화 관리`에서 `Manual Activation` 버튼을 눌렀을 때 실행됩니다.
- 수동 활성화 작업 기능을 제공하는 Dialog 입니다.
- `ParseJson()` : 입력받은 JSON 형식의 string을 Parsing 하여 화면상에 표시합니다.
- `GetJsonString()` : `ParseJson()`의 sub-method. JSON Object에서 특정 field의 값을 string으로 return합니다.
- `btn_open_Click()` : 파일 오픈 Click Event
- `ClearLabels()` : 화면상 모든 Control의 값들을 삭제
- `btn_make_Click()` : Make Response File 버튼 Click Event
- `btn_deact_Click()` : Apply Deactivation 버튼 Click Event
- `GetResponseJson()` : MFC DLL의 함수입니다.
- `GetResActJson()` : `GetResponseJson()`의 결과를 C# string으로 return 합니다.
- `btn_act_Click()` : Apply Activation 버튼 Click Event 입니다.

#####1.2.4.3 ES_ADD_CONTPRD
- `ES_CONTPRD`에서 `추가`,`수정` 버튼을 눌렀을 때 실행됩니다.
- 계약 제품 입력 기능을 제공하는 Dialog 입니다.
- `InitControl()` : 각종 Control의 초기값을 설정합니다.
- `applyModification()` : Form 생성시 추가일 경우 S/N 값을 출력해주며, 수정일 경우 해당 제품에 관한 정보를 화면에 출력합니다.
- `combo_product_ComboChanged()` : 제품 ComboBox를 선택했을 때 발생하는 Event
- `combo_edition_ComboChanged()` : Edition ComboBox를 선택했을 때 발생하는 Event
- `combo_version_ComboChanged()` : ver. ComboBox를 선택했을 때 발생하는 Event
- `priceChanged()` : List Price 와 Net Price 값이 바뀔 경우 발생하는 Event
- `save()` : 저장 버튼 Click Event
- `check_upgrade_CheckedChanged()` : Upgrade 계약 CheckBox 선택시 발생하는 Event
- `check_maintc_CheckedChanged()` : 유지보수계약 CheckBox 선택시 발생하는 Event
- `btn_cancel_Click()` : 취소 버튼 Click Event
- `licenseTypeChanged()` : License 타입 Radio Button 선택시 발생하는 Event
- `startDateChange()` : 시작일 변경시 발생하는 Event
- `endDateChange()` : 종료일 변경시 발생하는 Event
- `check_manual_CheckedChanged()` : 키 수동입력 Checkbox 선택시 발생하는 Event
- `btn_orangeKey_Click()` : 키 생성 버튼 Click Event
- `SaveKey()` : 생성된 License Key를 database에 저장하는 기능
- `GetLicenseKey()` , `GetLicenseText()` : MFC DLL 함수입니다.
- `GetKey()` , `GetText()` : MFC 합수의 결과를 C# string으로 return 합니다.

#####1.2.4.4 ES_CONTPRD
- `3.1 계약관리`에서 `제품상세`버튼을 눌렀을 때 실행됩니다.
- 해당 계약에 포함되는 제품 및 License Key 정보를 등록하는 Dialog 입니다.
- `InitControl()` : 각종 Control의 초기값을 설정합니다.
- `RefreshPrdList()` : 제품정보 Grid (위쪽)를 출력합니다.
- `ModifyContQtyInfo()` : 사용되지 않는 함수입니다.
- `RefreshKeyList()` : 제품키 Grid (아래쪽)을 출력합니다.
- `btn_add_Click()` : 추가 버튼 Click Event
- `btn_modify_Click()` : 수정 버튼 Click Event
- `btn_delete_Click()` : 삭제 버튼 Click Event
- `btn_key_Click()` : 키 발행 버튼(사용되지 않음) Click Event 
- `DeleteKey()` : 키 삭제 버튼(사용되지 않음) Click Event 
- `view_List_FocusedRowChanged()` : 제품 정보 Grid를 선택했을 경우 발생하는 Event
- `view_keyList_CustomDrawCell()` : Grid의 Cell 색상을 변경해주는 Event

#####1.2.4.5 ES_CUST
- `3.1 계약관리` 에서 협력업체, 고객사의 `업체명`을 눌렀을 때 실행됩니다.
- 업체명을 선택 하는 Dialog 입니다.
- `btn_Cancel_Click()` : 취소 버튼 Click Event
- `btn_Save_Click()` : 저장 버튼 Click Event
- `view_List_DoubleClick()` : Grid에서 더블 클릭시 Event

#####1.2.4.6 ES_DETAIL_ACC
- `3.1 계약관리` 에서 협력업체, 고객사의 `Sale 담당자`, `Billing 담당자`, `Tech 담당자`를 눌렀을 때 실행됩니다.
- 선택된 담당자의 상세정보를 표시합니다.

#####1.2.4.7 ES_DETAIL_CUST
- `3.1 계약관리` 에서 협력업체, 고객사의 `업체명`을 눌렀을 때 실행됩니다.
- 선택된 업체의 상세정보를 표시합니다.

#####1.2.4.8 ES_GENKEY
- 현재 사용되지 않는 Dialog 입니다.

#####1.2.4.9 ES_LOGIN
- 처음 실행시 수행되는 Dialog 입니다.
- 사용자 ID, Password를 입력합니다.
- `btn_conn_Click()` : 접속 버튼 Click Event
- `xucEdit_password_TextKeyPress()` : password 란에 키 입력시 발생하는 Event

#####1.2.4.10 ES_PRODHIST
-  `3.1 계약관리`에서 `제품 계약 내역`을 눌렀을 때 실행됩니다.
-  제품 계약 내역을 출력합니다.
-  `RefreshList()` : Grid에 내용을 출력합니다.
-  `btn_excel_Click()` : Excel 저장 버튼 Click Event

#####1.2.4.11 ES_PWD
- `5.1 패스워드 변경`을 누르면 실행됩니다.
- 사용자 패스워드를 변경하는 기능을 제공합니다.
- `btn_Save_Click()` : Apply 버튼 Click Event
- `btn_Cancel_Click()` : Cancel 버튼 Click Event

#####1.2.4.12 ES_ZIP
- `2.1 고객 관리`에서 주소 입력시 우편번호 번호를 눌렀을 경우 실행됩니다.
- 우편번호 목록을 보여주며 선택하는 기능을 제공합니다.
- `RefreshGrid()` : Grid에 내용을 출력합니다.
- `UC_Text_TextKeyPress()` : 동이름 Edit에 키 입력시 발생하는 Event
- `OK()` : Apply 버튼 Click Event
- `Cancel()` : Cancel 버튼 Click Event

####1.2.5 SM/SM_ENV
- `5.2 환경 설정`을 누르면 실행됩니다.
- Skin 변경 및 접속정보를 수정 할 수 있습니다.
- `init()` : 처음 실행시 초기화 method 입니다.
- `BVBtn_Save_ItemClick()` : Save 버튼 Click Event
- `BVBtn_Cancel_ItemClick()` : Cancel 버튼 Click Event

###1.3 Globals
- 전역 변수 class들을 저장해 놓은 폴더입니다.

####1.3.1 Consts
- const 변수들을 설정해 두었습니다.
- `INFO.xml` 파일명 및 field명을 저장해 두었습니다.

####1.3.2 InitMgr
- xml 파일을 읽어서 Statics class에 기록하는 기능을 제공합니다.
- Statics class를 읽어서 xml 파일에 기록하는 기능을 제공합니다.

####1.3.3 Statics
- 전역으로 선언된 static 변수를 모아두었습니다.
- 환경 변수 및 database 접속 정보용 변수들이 있습니다.

###1.4 MFCDLL
- MFC에서 build한 dll 파일들을 모아두었습니다.
- Setup 파일 생성할때 여기에 있는 dll 파일을 포함시킵니다.
- debug시 여기의 파일들을 `bin/Debug` 안으로 복사해 주어야 합니다.
- 개발망 내의 MFC License Solution 중 아래 Project들을 Release 모드로 빌드해서 복사해주시면 됩니다.
  - ORestful
  - OLM
  - SCitrus
  - SLicense

###1.5 Util/XMLParser
- `MENU.xml`을 읽어서 MDI의 메뉴를 구성해주는 기능을 제공합니다.
- LunaStar에서 편의상 복사한 파일입니다.
- 자세한 설명은 생략하겠습니다.

###1.6 XML/MENU.xml
- MDI의 메뉴를 xml 형식으로 저장해 두었습니다.
- 새로운 Form 추가시 해당 xml을 수정하여야 메뉴상에 표시됩니다.
- Setup 파일 생성할때 여기에 있는 xml 파일을 포함시킵니다.
- debug시 여기의 파일을 `bin/Debug` 안으로 복사해 주어야 합니다.

##2. LunaStar
- Library Project로 여러 편의 기능을 제공합니다.
- WVMIS 작업 이전에 작업된 Project이며, 특별한 일이 없는 경우 고칠 일이 없습니다.
- 간단하게 class별로 어떤 기능을 제공하는지에 대해서만 설명드리겠습니다.

###2.1 DBA
- Oracle database server에 접속을 하여 SQL문을 실행하는 기능을 제공합니다.

###2.2 UserControls
- 사용자 정의 Control들을 모아두었습니다.

###2.3 Util/FileIO
- File 입출력 관련 기능을 제공합니다.

##3. Setup
- WVMIS를 배포하고자 할때 Setup 파일을 생성해줍니다.
- project를 선택하시고 build를 선택하면 setup 파일이 생성됩니다.
