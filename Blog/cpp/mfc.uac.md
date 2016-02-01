##MFC UAC 관련 사항 정리

###Project의 UAC 설정

Project -> Properties -> Linker -> Manifest File -> `UAC Execution Level`

- asInvoker : 응용 프로그램을 시작한 프로세스와 동일한 권한으로 응용 프로그램이 실행됩니다. 관리자 권한으로 실행을 선택하면 응용 프로그램의 권한 수준을 높일 수 있습니다.
- requireAdministrator: 응용 프로그램이 관리자 권한으로 실행됩니다. 응용 프로그램을 시작하는 사용자는 관리자 그룹의 멤버이어야 합니다. 응용 프로그램을 여는 프로세스가 관리자 권한으로 실행되고 있지 않은 경우 자격 증명을 입력하라는 메시지가 표시됩니다.
- highestAvailable: 최대한 높은 권한 수준으로 응용 프로그램이 실행됩니다. 응용 프로그램을 시작하는 사용자가 관리자 그룹의 멤버이면 이 옵션은 requireAdministrator와 같습니다. 사용 가능한 가장 높은 권한 수준이 응용 프로그램을 여는 프로세스의 수준보다 높으면 자격 증명을 입력하라는 메시지가 표시됩니다.

###asInvoker 권한의 Application 에서 requireAdministrator를 호출하는 방법
