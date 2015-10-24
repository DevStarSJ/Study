#### Hive 설치

- Hive Download : <http://spark.apache.org>
- $HOME로 이동 : `mv spark-1.5.1-bin-hadoop2.6.tgz ~`
- 압축풀기 : `tar zxvf spark-1.5.1-bin-hadoop2.6.tgz`
- link 생성 : `ln -s apache-hive-1.2.1-bin hive`
- .bash_profile에 경로 추가  
  ```
export JAVA_HOME=$HOME/java
export HADOOP_HOME=$HOME/hadoop
export HIVE_HOME=$HOME/hive

export HADOOP_OPTS=$HADOOP_OPTS

PATH=$PATH:$HOME/bin:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$HIVE_HOME/bin

export PATH
```

#### MySQL 설치

- MySQL 설치 : `yum install mysql-server`
- MySQL Demon 실행 : `service mysqld start`
- root password 변경 : `mysqladmin -u root password XXXX`
  - 확인   
  ```
[root@hadoop ~]# mysql -u root -p
Enter password: 

mysql> exit
Bye
```
- 부팅시 실행 추가 : `chkconfig mysqld on`
  - 확인  
  ```
[root@hadoop ~]# chkconfig --list mysqld
mysqld         	0:해제	1:해제	2:활성	3:활성	4:활성	5:활성	6:해제
```

#### MySQL - Hive 연동

- MySQL Connector 설치 : `yum install mysql-connector-java`
- MySQL Connector.jar 을  hadoop 아래로 복사 : `cp /usr/share/java/mysql-connector-java.jar ~/hive/lib/mysql-connector-java.jar`

- 접속 후 metastore DB 생성
```
[root@hadoop ~]# mysql -u root -p
Enter password: 

mysql> create database metastore;
Query OK, 1 row affected (0.00 sec)

mysql> use metastore;
Database changed
```

- hive 사용자 추가 및 권한 할당 (hive/hive로 설정)
```
mysql> create user 'hive'@'%' identified by 'hive';
Query OK, 0 rows affected (0.00 sec)

mysql> grant all privileges on metastore.* to 'hive'@'%';
Query OK, 0 rows affected (0.00 sec)

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)

mysql> exit
Bye
```

#### Hive 환경설정

- hive-env.sh
```
cd ~/hive/conf
cp hive-env.sh.template hive-env.sh
chmod 755 hive-env.sh
vi hive-env.sh
```

- `HADOOP_HOME=${bin}/../../hadoop` 의 주석만 풀어줍니다.

- hive.log4j.properties
```
cp hive-log4j.properties.template hive-log4j.properties
mkdir ../logs
vi hive-log4j.properties
```

```
hive.root.logger=WARN,DRFA
hive.log.dir=~/hive/logs
hive.log.file=hive2.log
```

- hive-site.xml

```
cp hive-default.xml.template hive-site.xml
vi hive-site.xml
```

- 무지 긴 파일이니깐 각 name 을 찾아서 수정합니다.
```
  <property>
    <name>javax.jdo.option.ConnectionURL</name>
    <value>jdbc:mysql://hadoop.master/metastore?createDatabaseIfNotExist=true</value>
    <description>JDBC connect string for a JDBC metastore</description>
  </property>

  <property>
    <name>javax.jdo.option.ConnectionDriverName</name>
    <value>com.mysql.jdbc.Driver</value>
    <description>Driver class name for a JDBC metastore</description>
  </property>

  <property>
    <name>javax.jdo.option.ConnectionUserName</name>
    <value>hive</value>
    <description>Username to use against metastore database</description>
  </property>

  <property>
    <name>javax.jdo.option.ConnectionPassword</name>
    <value>hive</value>
    <description>password to use against metastore database</description>
  </property>

  <property>
    <name>hive.metastore.uris</name>
    <value>thrift://hadoop.master:9083</value>
    <description>Thrift URI for the remote metastore. Used by metastore client to connect to remote metastore.</description>
  </property>
```
