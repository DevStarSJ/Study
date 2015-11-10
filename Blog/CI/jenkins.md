###1. Jenkins 란 ?

Jenkins Server는 Open Source CI (Continuous Integration) 을 자동화해주는 Tool입니다. 대부분 다음과 같은 방식으로 Jenkins를 이용합니다.

1. Repository (SVN, Git)에서 source code를 가져옵니다.
2. 정해진 절차에 따라 build 및 unit test, integration test를 수행합니다. 수행 결과 이상이 있을 때 e-mail을 통해서 reporting해주는 역할까지 수행해 줍니다.
3. 정상적으로 build 되었으며, 모든 test 결과에 이상이 없는 경우 배포 파일(setup, update)을 생성합니다.

Jenkins 자체는 사용자가 입력한 command line 명령어들을 특정 조건에 맞게 또는 특정 시간이나 일정한 간격으로 수행해주는 역할을 해줍니다.
build 및 test, deploy하는 역할 자체는 command line에서 수행가능한 형태로 사용자가 직접 입력해 놓으면 그 명령어를 수행해주는 역할을 할 뿐이지, Jenkins 자체에 build tool이 있다던지 그러진 않습니다.

###2. 이번 Posting에서 다룰 내용

1. Jenkins download 및 설치 (Windows 기준)
2. MSBuild plugin 설치
3. Jenkins item 설정
  1. SVN Repository에서 source code 내려받기
  2. VisualStudio Solution (.sln)을 command line에서 실행시키기 (MSBuild 이용)
  3. Jenkins item에서 build 후 다른 item 실행

###3. Jenkins download 및 설치




