## 1. Hadoop Download

- <http://hadoop.apache.org> 에서 다운로드 받습니다.
  - source 버전이 아닌 binary를 받습니다.
- `C:/hadoop`에 압축을 풉니다.
- <https://github.com/prabaprakash/Hadoop-2.3-Config/archive/master.zip>에서 `Pre Configured file`을 다운로드 받습니다.
- 다운로드 받은 `Pre Configured file`의 압축을 풀어서 bin 폴더내의 `yarn.cmd`를 `hadoop/bin`에 덮어씁니다.
- `etc/hadoop` 안의 파일들도 덮어씁니다.

## 2. 환경 변수 설정

- `HODOOP_HOME` = `C:/hadoop`
- `JAVA_HOME` 이 설정되어 있지 않다면 환경변수에 Java가 설치된 폴더로 설정
- `Path` 에 `;C:\hadoop\bin` , `JAVA_HOME` 안의 `bin` 폴더 추가
- `cmd`를 관리자 권한으로 실행하여 `java -version` , `javac -version` 에서 버전정보가 제대로 보이나 확인
  - 제대로 나오지 않는다면 Java를 다시 설치

## 3. Hadoop 환경 설정

- `ect/hadoop/hadoop-env.cmd` 의 25번째 줄을 `JAVA_HOME`의 위치와 같게 수정
- `C:/hadoop/bin` 으로 이동하여 `hadoop namenode -format` 실행

```
메세지 들이 우루루 나오고...
SHUTDOWN_MSG: Shutting down NameNode at SJ-ATIV/192.168.56.1
위 메세지 출력 후 종료
```

- `C:/hadoop/sbin`으로 이동하여 `start-yarn` 실행

--------------------------------------------

- Cygwin 2.774
- Java 1.7.0
- Hadoop 0.20.2

- Cygwin Install
  - default로 쭉쭉쭉 하다가 select packages 에서 openssh 로 검색 모두 다운
  - openssl로 검색 모두 다운로드
  - tcp_wrappers 모두 다운로드
  - diffutils
  - 넥스트 넥스트

- Cygwin 실행
  - ssh-host-config -> yes 엔터 3번 -> blank 엔터 -> no 엔터 -> yes -> password 입력
  - 
