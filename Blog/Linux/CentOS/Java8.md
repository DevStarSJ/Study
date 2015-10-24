### CentOS에 Java8 설치하기

- CentOS 6.7 버전에는 기본적으로 `Java7`이 설치되어 있습니다.

  ![CentOS Homepage](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.java.01.png?raw=true)

1. 먼저 Java7을 지웁니다.
  ```
yum remove java
```
  - 진짜로 잘 지워졌는지 확인해 보겠습니다.  

      ![CentOS Homepage](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.java.02.png?raw=true)

1. Java Homepage(<http://java.sun.com>) 에서 Java 8 버전을 다운로드 받습니다.

  ![CentOS Homepage](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.java.03.png?raw=true)

1. 다운로드 받은 file을 압축을 풀고 java란 이름으로 link를 생성합니다.
  ```
  cd 다운로드/
  mv jdk-8u60-linux-x64.tar.gz ~/
  cd ~
  tar zxvf jdk-8u60-linux-x64.tar.gz
  ln -s jdk1.8.0_60 java
```
  - `ls -al`명령어로 link가 제대로 생성되었는지 확인합니다.  

    ![CentOS Homepage](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.java.04.png?raw=true)

1. profile에 Java8 환경설정을 해줍니다.
  ```
vi .bash_profile
```
  - 아래의 내용들로 추가 및 수정을 합니다.  
    ```
export JAVA_HOME=~/java

PATH=$PATH:$HOME/bin:$JAVA_HOME/bin

export PATH
```
  - 바뀐 profile을 실행합니다.  
    ```
. .bash_profile
```

1. 바뀐 java 버전을 확인해 봅니다.  

  ![CentOS Homepage](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.java.05.png?raw=true)
