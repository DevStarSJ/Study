### VirtualBox VM Image 복사하기 (CentOS로 설명)

- VirtualBox VM Image를 그냥 file로 복사를 해서 사용해도 되지만, 그렇게 하면 `UUID`가 똑같은 VM이 2개가 되므로 따로 또 바꿔주는 작업을 해야 합니다.
  - VirtualBox의 Clone 기능 사용하기 : <http://icysword.blog.me/140139363644>
  - VirtualBox UUID 변경하기 : <http://icysword.blog.me/140139363863>

- Network를 안쓰는 VM Image라면 위 2가지 방법으로 복사하더라도 상관없지만, 사용할 경우에는 MAC Address도 변경해 줘야 합니다.

- 그래서 그냥 간단하게 VirtualBox의 기능을 활용하여 VM Image를 복사하고자 합니다.

1. 먼저 복사할 Image에서 마우스 우클릭을 한 뒤 `복제`를 선택합니다.
  -  아직 VM을 VirtualBox에 등록하지 않은 VDI 파일로 가지고 있다면 먼저 등록을 하세요.  
      ![CentOS Homepage](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/VirtualBox.CentOS.copy.01.png?raw=true)  
1. 복사할 VM의 이름을 입력해 줍니다.
  - 이 이름은 VirtualBox에서 구별하는 이름 및 복사할 file 및 폴더명이지 OS 상에 반영되지는 않습니다.  
      ![CentOS Homepage](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/VirtualBox.CentOS.copy.02.png?raw=true)  
1. 완전한 복제와 연결된 복제 중 뭐로 할 것인지 묻는데 당연히 `완전한 복제`를 선택해 줍니다.
  - 이 후 복사하는데 시간이 조금 걸립니다.  
1. 복사한 VM에서 우클릭하여 `설정`으로 들어갑니다.  
  ![CentOS Homepage](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/VirtualBox.CentOS.copy.03.png?raw=true)  
1. 원래 Internet을 사용할 경우 어뎁터1에서 NAT로 설정되어 있는 것을 사용합니다.
  - 거기에서 `고급`을 눌러서 MAC주소의 오른쪽 다시생성하는 버튼을 눌러줍니다.
  - 추가로 내부적으로 Network를 사용 (192.168.X.X 등...)할 필요가 있을 경우에는 어탭터 2에 `VirtualBox Host-Only Ethernet Adapter`를 선택하면 됩니다.
    - 이미 해당 카드로 설정한 Image를 복사한 경우에는 여기에서도 `고급`을 눌러서 MAC주소를 새로 생성해 줍니다.  
      ![CentOS Homepage](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/VirtualBox.CentOS.copy.04.png?raw=true)  
1. 해당 VM을 실행시켜도 복사할때 바꾼 이름이 아닌 원래 OS의 Host이름으로 나옵니다.  
  ![CentOS Homepage](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/VirtualBox.CentOS.copy.05.png?raw=true)  
1. `ifconfig`를 눌러서 네트워크 설정을 확인해 봅니다.  
  ![CentOS Homepage](https://github.com/DevStarSJ/Study/blob/master/Blog/Linux/CentOS/image/VirtualBox.CentOS.copy.06.png?raw=true)  
  - 네트워크 카드명 `eth0`, `eth1` 등은 VM 복사시 바뀔수가 있으므로 해당 명칭으로 설정한 것이 있으면 같이 바꿔줘야 합니다.
1. 참고로 Host명을 바꾸는 방법은 각 OS별로 다른데 CentOS 6버전에 대해서만 설명드리겠습니다.
  - `Terminal`을 실행해서 `setup`이라고 입력하신 후 `네트워크설정`으로 가시면 Host명칭을 바꿀 수 있습니다.
  - Host명칭이 제대로 바뀌었는지 확인하려면 `loggout`을 하시면 바뀐 Host명 확인이 가능합니다.
