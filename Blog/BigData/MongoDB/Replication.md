### Replication - 2015.10.17 - 이보용님  

- 11번가 : MongoDB  
- GS홈쇼핑 : 하둡, MongoDB, Unix Oracle -> OpenSource : 오픈한 뒤 문제없이 사용하고 있음, MariaDB
- 카디날정보기술 : MongoDB를 applicance로 판매
  - 관련 내용 참조 (좋은 내용이 많음) : <http://mongodb.citsoft.net>  

#### Replication 개요

- 각각의 Server가 storage를 공유하는 것은 안되는 것으로
- 고가용성의 기능 (미러링)
- 복제 셋 (replica set)
  - 표준, 수동 결정권자 노드
- Master/slave replication : 주종 관계, 실제로는 M/S 로 쓰는 경우는 거의 없음. 유연성이 떨어짐. Master가 망가지면 쫑!
- Oplog와 heartbeat, priority

###3 Replication 종류

- Replica set : 복제셋
  - 자동장애 조치
  - 12개 Node까지 가능
  - 홀수 Node로 구성 권장 : 처음 구동시 Primary를 선출해야 하는데, 짝수인 경우 투표결과 1위가 2개가 되어버리면 구동이 안되고 멍때려버림 -> 이 경우 Abitor 서버를 두어서 투표를 참여하게 하는 방법도 있음

- Master/Slave
  - 자동 장애조치 불가능 (수동) : 사용자가 개입하여 Slave -> Master로 승격해야함
  - 13개 이상 Node 구성 가능
  - 홀수 Node로 구성 권장

- Oplog : 트랜잭션 Log
  - Capped collection
  - local database 내에 저장
  - Collcection 이름, timestamp, 변경된 document 저장

- Headtbeat
  - 2초마다 각각 Server들에게 ping 전달
  - Server 상태 check

- Priority
  - Server 내 우선순위
  - 기본값은 1
  - 0일 경우 수동모드 Node
  - 권장값은 별로도 수정하지말고 그냥 1로 사용하도록 

###4. Member 종류 : blog 참조

###5. 실습 (Master & Slave)

```
MongoD --dbpath C:/MongoDB/data/R0 --port 50000 --master
MongoD --dbpath C:/MongoDB/data/R1 --port 50001 --slave --source localhost:50000
MongoD --dbpath C:/MongoDB/data/R2 --port 50002 --slave --source localhost:50000
```

- Master / Slave를 명시적으로 지정했으므로 Master가 죽을시 Slave로 자동으로 Fail-over가 되지 않습니다.
  - Slave의 source를 모두 50000 으로 고정했기 때문에 모든 Slave를 다 내리고 다른 Master를 source로 다시 지정해야 합니다.

```
mongo localhost:50000
db.emp.save( { empno : 7707, ename : 'Luna' , dept :'Develop' } )
show dbs
show collections
db.emp.find()
exit

mongo localhost:50001
db.emp.find()
show dbs # 오류 발생 slave에서는 실행 불가
rs.slaveOk() # 이 명령을 내리면 이제 slave에서도 위 문장 실행가능
show dbs
show collections
exit
```

- Master/Slave는 내가 접속한 Node가 Master인지 Slave인지 구분 할 수가 없습니다.

###6. Replica Set

- Master, Slave, Abitor로 구성되었다고 생각하면 편합니다. (나머지 member들은 거의 안씁니다.)

- 실습

- `--rest` 를 붙이면 Web-interface의 관리상태, Log등의 조회가 가능합니다. port는 지정한 port + 1000 입니다.

### Sharding 과 Replica Set을 같이 적용할려면

- 크게 Sharding 을 구축을하고
  - 각각의 Shade Node를 Replica Set으로 구성

### Replica 구축 예제

- 통상적으로 Service 망과 Backup 망은 별도로 운영
  - Service망으로 Backup등과 같은 대용량 트래픽이 몰리면 Service가 중단 될 수 있음

