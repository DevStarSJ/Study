### 1. VirtualBox 설치

- 자세한 내용은 생략하겠습니다.
  - VirtualBox Download
  - VirtualBox Extention Pack Download
  - VirtualBox 설치
  - CentOS 설치용 가성머신 생성

### 2. CentOS Image Download

- 아래 Link 참조 바랍니다.

#### [CentOS 다운로드 받기](https://github.com/DevStarSJ/Study/tree/master/Blog/Linux/CentOS/Download.md)

- VirtualBox에 설치시 다운로드 받은 Image를 mount 시켜서 진행합니다.

### 3. CentOS 설치

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.01.png?raw=true)

#### 3.1 `Install`을 눌러서 진행합니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.02.png?raw=true)

#### 3.2 media test는 과감하게 `Skip` 합니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.03.png?raw=true)

#### 3.3 설치언어는 당연히 `한국어`로 해줍니다. 다른 언어가 편하시면 그걸로 하셔도 됩니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.04.png?raw=true)

#### 3.4 키보드도 `한국어`로 합니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.05.png?raw=true)

#### 3.5 VirtualBox 환경이니 그냥 `기본 저장 장치`로 선택합니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.06.png?raw=true)

#### 3.6 방금 만든 이미지니 `모든 데이터를 삭제합니다.`를 선택합니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.07.png?raw=true)

#### 3.7 호스트명은 원하는 걸로 해주면 됩니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.08.png?raw=true)

#### 3.8 시간대는 그냥 서울로 해주시구요.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.09.png?raw=true)

#### 3.9 Root 계정의 암호를 설정해 줍니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.10.png?raw=true)

#### 3.10 어차피 VM으니 공간을 적게 할당하였을 것이고 그냥 `모든 공간 사용`을 선택합니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.11.png?raw=true)

#### 3.11 `디스크에 변경 사항 기록`을 눌러줍니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.12.png?raw=true)

#### 3.12 설치하려는 Software들을 선택합니다.  

- 일반적으로 사용하실 경우에는 `Desktop`을 설정하시면 편합니다.
- `Basic Server`로 까시면 GUI Desktop이 없습니다.
  - 필자는 'Basic Server`를 선택하고, GUI 관련된 것만 추가로 선택하기 위해서 추가 소프트웨어 선택의 '지금 선택'을 선택했습니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.13.png?raw=true)

#### 3.13 추가로 설치할 Software를 선택합니다.  

- 앞 화면에서 `지금 선택`을 눌렀을 경우에만 이 화면이 나옵니다.
- 필자는 GUI 환경을 위해서 데스크탑에서 KDE 데스크탑 을 제외한 나머지를 모두 선택하였습니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.14.png?raw=true)

#### 3.14 사용자를 생성합니다.  

- 계속 `앞으로`를 누르다보면 사용자 생성이 나옵니다.
- 필자의 경우 별로 사용자를 사용하지 않고 `root`계정만 사용할 것이라서 그냥 여기서도 `앞으로`를 눌렀습니다.

#### 3.15 설치가 되는 것을 기다린 후 `재부팅` 해줍니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.15.png?raw=true)

#### 3.16 `root` 또는 `사용자 계정`으로 로그인을 합니다.  

### 4. VirtualBox Extension Pack 설치 설치

- 필요없으면 설치하지 않으셔도 되지만 설치하면 다음의 기능이 가능합니다.
  - VM 창 크기를 변화하면 거기에 자동으로 맞춰서 해상도가 적용됩니다.
  - Clipboard 가 Host Windows 와 Guest VM이 공유합니다.
  - File 을 drag&drop으로 Host Windows 와 Guest VM 으로 복사가 가능합니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.16.png?raw=true)

#### 4.1 VirtualBox 메뉴바에서 `장치` 아래에 있는 `게스트 확장 CD 이미지 삽입...`을 누릅니다.

- VirtualBox 옵션에서 미리 설정하지 않았다면 파일 위치를 물어봅니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.17.png?raw=true)

#### 4.2 `확인`을 눌러서 실행합니다.

- 정상적으로 설치가 종료되면, Reboot을 하면 됩니다.
- 하지만 제대로 설치가 안되면 4.3 이하 부분을 해주셔야 합니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.18.png?raw=true)

#### 4.3 Guest Additions module의 build가 실패하였던 메세지가 뜬 경우 제대로 설치되지 않은 것입니다.

- 이 경우 Network를 통해서 프로그램들을 설치해야 합니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.22.png?raw=true)

- 만약 위 그림과 같이 Network가 연결이 안되어 있다면, `System eth0`를 눌러서 연결을 해줘야 합니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.19.png?raw=true)

- 정상적으로 연결되었을 경우 위와 같이 표시됩니다.

#### 4.4 `yum` 명령어를 이용해서 아래와 같이 실행합니다.

```
$ yum install gcc dkms make kernel-devel
$ yum install kernel sources
$ yum install kernel-headers
$ yum groupinstall "Development Tools"
```

#### 4.5 `Reboot` 한 후 다시 설치를 시도합니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.20.png?raw=true)

- 위와 같이 OpenGL 에서 나는 오류는 무시하셔도 됩니다.
- 어쨌든 VirtualBox Guest Addition의 Start가 성공하면 됩니다.

#### 4.6 다시 `Reboot` 합니다.

![CentOS Install](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/CentOS.install.21.png?raw=true)

#### 4.7 상단 메뉴의 `장치`의 `클립보드 공유` 와 `드래그 앤 드롭` 을 둘 다 `양방향`으로 해서 Test를 해봅니다.  

- 창 크기를 변화 시켰을때 VM 내의 해상도가 바뀌는지 확인 합니다.
- File을 drag 하여 다른 쪽으로 넘겨봅니다. (Windows -> CentOS , CentOS -> Windows)
- 파일을 하나 열어서 내용을 Copy 한 후 다른 쪽에서 Paste 해봅니다. (Windows -> CentOS , CentOS -> Windows)
- 위 과정이 모두 정상적으로 수행되었다면 제대로 설치된 것입니다.


