## Hadoop 설치하기

- 1대의 master와 3대의 datanode. 총 4대의 server를 구축하는 것을 기준으로 설명드리겠습니다.

###1. CentOS 6 및 Java8 준비 (4대 Server)

- CentOS 6 기준으로 설명드리겠습니다.
- CentOS 설치에 대해서는 다음 Posting을 참조하시기 바랍니다.
  - [CentOS 다운로드 받기](https://github.com/icysword/Study/wiki/Linux.CentOS.Download)
  - [VirtualBox에 CentOS 설치하기](https://github.com/icysword/Study/wiki/Linux.CentOS.VirtualBoxInstall)
  - [CentOS에 Java 8 설치하기](https://github.com/icysword/Study/wiki/Linux.CentOS.Java8)
- 위 과정까지 먼저 진행을 해 줍니다.
- 그런 다음 VM Image를 4개 복사합니다.
  - 복사 방법은 [VirtualBox image 복사하기](https://github.com/icysword/Study/wiki/Linux.CentOS.VMCopy)를 참조하세요.
    - 모두 내부망을 사용해야 하니 NAT말고 추가로 Network 카드를 추가해야 합니다.
  - 각각의 이름을 `hadoop.master` , `hadoop.slave.1` , `hadoop.slave.2` , `hadoop.slave.3` 으로 합니다.

###2. Network 설정

- 이 부분은 아래 설명한 것과 완벽하게 같게 되지는 않습니다.
  - 각자 Network 환경에 따라 수정하셔야 합니다.
- 먼저 `ifconfig`를 눌러서 확인해 줍니다.  
  ![CentOS Homepage](https://github.com/icysword/Study/wiki/Linux/CentOS/image/VirtualBox.CentOS.copy.06.png)  
  - VM Image를 복사한 경우 Network명칭이 `eth0` , `eth1`이 아니라 `eth2` , `eth5` 이런식으로 다를 수도 있습니다.
  - 위 정보에서 `Network 명칭` , `MAC Address (HWaddr)` , `IP (inet addr)` 정보를 다른 file에 설정해야 하니 어디 적어두시거나 다른 Terminal을 하나 띄우시길 추천 드립니다.
- `/etc/sysconfig/network-scripts` 내부에 있는 `ifcfg-네트워크명칭` 파일을 복사 및 편집해야 합니다.
  - `ifconfig`의 네트워크 명칭이 `eth2`이더라도 파일은 `ifcfg-eth0`만 있을 수 있습니다.
    - 그럴 경우에는 명칭을 `ifcfg-eth2`로 변경해 줍니다.
  - 추가로 설치한 Network카드에 대해서 내부IP 설정을 해줘야 합니다.
    - `ifcfg-eth0` 파일을 `Network명칭`에 맞게 복사 합니다.  
    ```
cd /etc/sysconfig/network-scripts
cp ifcfg-eth0 ifcfg-eth1
vi ifcfg-eth1
```
    - `ifcfg-eth0` 와 `ifcfg-eth1` 를 각각 아래의 내용으로 수정합니다.  
      - 수정시 위 `ifconfig`에서 확인한 내용을 토대로 수정을 합니다.  
      - ifcfg-eth0  
      ```
DEVICE=eth0
HWADDR=08:00:27:06:20:B7
TYPE=Ethernet
UUID=ab63ac3f-ab4c-46a7-baaa-9b36295aa7dd
ONBOOT=no
NM_CONTROLLED=yes
BOOTPROTO=dhcp
```  
      - ifcfg-eth1  
      ```
DEVICE=eth1
HWADDR=08:00:27:1D:34:59
TYPE=Ethernet
IPADDR=192.168.56.101
NETWORK=192.168.56.105
GATEWAY=192.168.56.1
NETMASK=255.255.255.0
ONBOOT=yes
NM_CONTROLLED=yes
BOOTPROTO=no
```
    - Network Restart를 해줍니다.
      - 하는 도중 오류가 발생한다면 file명, network명, file내의 설정 (DEVICE,HWADDR,IPADDR 등을 확인해 봅니다.)  
    ```
# /etc/init.d/network restart
```  
    - 위 과정과 같은 방법으로 다른 server 들도 설정합니다. (아래 IP는 필자의 경우에 저렇게 나왔습니다.)
      - hadoop.slave.1 : `192.168.56.105`
      - hadoop.slave.2 : `192.168.56.102`
      - hadoop.slave.3 : `192.168.56.103`

###3. Host 설정

- IP가 아닌 Host명칭으로 통신하기 위해서는 Host 설정을 해 줘야 합니다.
- 4대의 Server에 모두 동일 하게 설정하면 됩니다.

```
vi /etc/hosts
```

```
192.168.56.101 hadoop.master
192.168.56.105 hadoop.slave.1
192.168.56.102 hadoop.slave.2
192.168.56.103 hadoop.slave.3
```

####4. Hadoop 설치

1. Hadoop download 및 압축풀기, PATH 지정
  - Hadoop Download : <http://hadoop.apache.org> (2.6.1)
  - 홈 Directory로 이동 : `mv hadoop-2.6.1.tar.gz ~`
  - 압축 풀기 : `tar zxvf  hadoop-2.6.1.tar.gz`
  - Link 생성 : `ln -s hadoop-2.6.1 hadoop`
  - `.bash_profile`에 HADOOP_HOME 과 PATH 설정 : `vi .bash_profile`  
  ```
export JAVA_HOME=~/java
export HADOOP_HOME=~/hadoop

PATH=$PATH:$HOME/bin:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

export PATH
```

1. Hadoop 환경변수 설정
  - 환경설정 파일이 있는 경로 : `$HADOOP_HOME/etc/hadoop/`
    - hadoop-env.sh : Hadoop을 실행하는 shell-script로서, JDK path, classpath 등을 설정
    - slaves : data node들의 server를 지정
    - core-site.xml : HDFS와 MapReduce에서 공통적으로 사용할 정보 설정 , hdfs-site와 mapred-site의 공통 설정 부분
    - hdfs-site.xml : HDFS(Hadoop File System) 관련 환경 정보 설정
    - mapred-site.xml : MapReduce의 application 정보 설정
    - yarn-site.xml : Resource Manager, Node Manager 정보 설정
    - yarn-env.sh : Yarn을 실행하는 shee-script
    - 자세한 사항은 <http://hadoop.apache.org/docs/r2.6.1/hadoop-project-dist/hadoop-common/ClusterSetup.html> 를 참조하세요.
  - `hadoop-env.sh`최상단에 추가  
  ```
export JAVA_HOME=~/java
export HADOOP_HOME=~/hadoop
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_CONF_DIR = $HADOOP_HOME/etc/hadoop
export YARN_CONF_DIR=$HADOOP_HOME/etc/hadoop
```
  - `yarn-env.sh`최상단에 추가
  ```
export JAVA_HOME=~/java
export HADOOP_HOME=~/hadoop
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export YARN_CONF_DIR=$HADOOP_HOME/etc/hadoop
```
  - `slaves`에 노드들 저장
  ```
hadoop.slave.1
hadoop.slave.2
hadoop.slave.3
```
  - `core-site.xml`의 아래 tag 부분에 추가
  ```XML
<configuration>
  <property>
    <name>fs.default.name</name>
    <value>hdfs://hadoop.master:9000</value>
  </property>
  <property>
    <name>hadoop.tmp.dir</name>
    <value>~/hadoop/tmp/</value>
  </property>
</configuration>
```  
    - 필자의 경우 `hadoop.tmp.dir` property를 master에 설정하니 namenode가 생성되지 않았습니다.
      - 그렇다고 저 부분을 지우니 namenode는 뜨는데, slave 들에 datanode가 생성되지 않았습니다.
      - 정확한 원인은 아직 모르겠지만, `core-site.xml`을 내용을 master 와 slave를 다르게 설정하였습니다.
        - master에는 `hadoop.tmp.dir` 부분을 삭제하였으며, slave에는 추가하였습니다.
  - `~/hadoop/tmp` 라는 디렉토리 생성
    - 자세한 사항은 Link 참조 : <http://hadoop.apache.org/docs/r2.6.1/hadoop-project-dist/hadoop-common/core-default.xml>
  - `hdfs-site.xml`의 아래 tag 부분에 추가
  ```XML
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>3</value>
  </property>
  <property>
    <name>dfs.permissions.enabled</name>
    <value>false</value>
  </property>
  <property>
    <name>dfs.namenode.secondary.http-address</name>
    <value>hadoop.slave.1:50090</value>
  </property>
  <property>
    <name>dfs.namenode.secondary.https-address</name>
    <value>hadoop.slave.1:50091</value>
  </property>
</configuration>
```
    - 참조 : <http://hadoop.apache.org/docs/r2.6.1/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml>
  - `mapred-site.xml`의 아래 tag 부분에 추가
  ```XML
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
</configuration>
```
    - 참조 : <http://hadoop.apache.org/docs/r2.6.1/hadoop-mapreduce-client/hadoop-mapreduce-client-core/mapred-default.xml>
  - `yarn-site.xml`에 Resource Manager, Node Manager 정보 설정
  ```XML
<configuration>
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
  <property>
    <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
    <value>org.apache.hadoop.mapred.ShuffleHandler</value>
  </property>
  <property>
    <name>yarn.resourcemanager.resource-tracker.address</name>
    <value>hadoop.master:8025</value>
  </property>
  <property>
    <name>yarn.resourcemanager.scheduler.address</name>
    <value>hadoop.master:8030</value>
  </property>
  <property>
    <name>yarn.resourcemanager.address</name>
    <value>hadoop.master:8040</value>
   </property>
</configuration>
```
    - 참고 : <http://hadoop.apache.org/docs/r2.6.1/hadoop-yarn/hadoop-yarn-common/yarn-default.xml>

- 위에서 설정한 내용을 1대의 server에만 한 뒤에 다른 PC로 배포가 가능합니다.
  - 해당 방법은 ssh 연결 확인이 끝난 다음에 설명드리겠습니다.

###5. ssh 연결 확인

- ssh 연결 확인은 `hadoop.master`에서 3대의 slave node로만 설정하면 됩니다.

- ssh 연결 확인을 먼저 해봅니다.
  - 처음 연결시 인증을 받아야 합니다. (yes 입력)
  - 다음부터 연결 할때마다 password를 입력해야 합니다.
  - 그래서 인증 key를 생성해서 배포하는게 편리합니다.

```
ssh hadoop.slave.1     # yes 입력
ssh hadoop.slave.1     # root@hadoop.slave.1의 password 입력
ssh-keygen -t rsa      # enter 3번
```

- 실제 화면은 다음과 같습니다.

```
[root@hadoop network-scripts]# ssh hadoop.slave.1
The authenticity of host 'hadoop.slave.1 (192.168.56.105)' can't be established.
RSA key fingerprint is c4:29:35:8f:56:14:24:d6:0a:1e:ed:29:39:0e:98:be.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'hadoop.slave.1,192.168.56.105' (RSA) to the list of known hosts.
Connection closed by 192.168.56.105
[root@hadoop network-scripts]# ssh hadoop.slave.1
root@hadoop.slave.1's password: 
[root@hadoop ~]# ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
cd:8e:7e:e1:71:87:09:fd:e6:bb:a1:61:80:33:63:e3 root@hadoop.slave.1
The key's randomart image is:
+--[ RSA 2048]----+
|                 |
|                 |
|           .     |
|         +. .    |
|        S +. +   |
|       o Bo.+ +  |
|        E..+o+.  |
|       .  o. o.. |
|        ..  . oo |
+-----------------+
```

- ssh인증키가 생성되었습니다.
- 생성된 ssh 인증키를 배포해야 합니다.
- 인증키 생성 및 배포는 master에서 해야 합니다.
  - 그전에 test를 위해 slave로 ssh 접속을 한 상태라면 `exit`를 눌러서 다시 `master`로 돌아 온 뒤에 작업해야 합니다.
```
cd ~/.ssh/
scp id_rsa.pub ~/hadoop/.ssh/authorized_keys
scp id_rsa.pub root@hadoop.slave.1:~/hadoop/.ssh/authorized_keys
scp id_rsa.pub root@hadoop.slave.2:~/hadoop/.ssh/authorized_keys
scp id_rsa.pub root@hadoop.slave.3:~/hadoop/.ssh/authorized_keys
```
- 만약 `rsa.pub` 파일이 없다면 `ssh-keygen -t rsa`를 다시 실행하세요.

- 참고로 test를 할려면 hadoop이 아닌 ~/.ssh/authorized_keys에 추가한 뒤에 접속시 암호를 안묻는지 확인하면 됩니다.
```
scp id_rsa.pub root@hadoop.slave.1:~/.ssh/authorized_keys
ssh hadoop.slave.1
```

- 이후 `ssh hadoop.slave.1` 등으로 접속할 때 password를 묻지 않습니다.

####6. hadoop 배포

- hadoop 설치의 마지막 부분에 ssh 연결이 끝나고 방법을 알려준다고 언급하였습니다.
- ssh를 통해서 다른 server로 파일 복사 및 디렉토리를 복사, 명령어 실행이 가능합니다.

1. 파일 복사
  - 아래 문법을 참고하여 필요한 파일을 복사하면 됩니다.
  ```  
scp .bash_profile root@hadoop.slave.1:~
scp .bash_profile root@hadoop.slave.2:~
scp .bash_profile root@hadoop.slave.3:~
```
1. 디렉토리 복사
  - 아래 문법을 참고하여 필요한 폴더를 복사하면 됩니다. 
    - hadoop도 master에만 설치한 뒤에 slave에 복사하는 것이 가능합니다.
  ```
scp -r hadoop-2.6.1 root@hadoop.slave.1:~
```
1. 명령어 실행
  - 아래 문법을 참고하여 실행하면 됩니다.
    - 참고로 hadoop의 link를 생성하는 명령어 입니다.  
  ```
ssh root@hadoop.slave.1 "ln -s hadoop-2.6.1 hadoop"
```
####7. hadoop 실행

- 아래 명령어로 master에서 실행해 봅니다.
```
hadoop namenode -format
start-all.sh
```
  - `hadoop namenode -format`은 한번만 실행하면 됩니다.
  - 이후에는 `start-all.sh`로 실행하면 됩니다.

- hadoop을 종료하는 방법은 다음과 같습니다.
```
stop-all.sh
```

- jsp 명령어로 현재 어떤 process 들이 java VM 상에서 돌아가는지 확인이 가능합니다.
```
jsp
```

- 원래는 slave에 datanode 들이 자동으로 실행되어야 하는데, 실행되지 않은 경우 아래 명령어로 실행이 가능합니다.
```
hadoop datanode
```

- jsp 명령어로 확인인한 결과의 예제입니다.
  - hadoop.master
  ```
[root@hadoop ~]# jps
6070 Jps
3420 ResourceManager
8788 NameNode
```
  - hadoop.slave.1
  ```
[root@hadoop ~]# jps
6070 Jps
3420 NodeManager
3479 DataNode
```
  - hadoop.slave.2
  ```
[root@hadoop ~]# jps
3650 Jps
3419 DataNode
3501 NodeManager
```
  - hadoop.slave.3
  ```
[root@hadoop ~]# jps
5505 Jps
5274 DataNode
5371 NodeManager
```

- Web Interface로 상태를 확인해 보겠습니다.
  - <http://hadoop.master:50070> : HDFS 확인. NameNode가 안떠있으면 접속되지 않습니다.
      ![CentOS Homepage](https://github.com/icysword/Study/wiki/BigData/Hadoop/image/hadoop.50070.png)  
  - <http://hadoop.master:8088> : Resource & Node Manager 확인이 가능합니다.
      ![CentOS Homepage](https://github.com/icysword/Study/wiki/BigData/Hadoop/image/hadoop.8088.png)  