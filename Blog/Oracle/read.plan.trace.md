#Oracle Plan, Trace 읽는 법

SQL Tuning을 하기 위해서 가장 기본으로 알아야 하는 것이 Plan과 Trce를 읽는 방법입니다.  
그래야 어느 곳이 비효율적인지를 알아내서 그 부분을 중심으로 Tuning 전략을 세울 수 있습니다.  

##1. Plan 읽는 법

- Plan은 SQL을 실행하기 전에 Optimizer에 의해 선택된 최적의 실행 경로 및 계산되어진 예상 Cost를 보여줍니다.

```SQL
*************************[Explain Plan Time: 2016/02/21 14:01:15]*************************
Execution Plan
-----------------------------------------------------------
   0      SELECT STATEMENT Optimizer=ALL_ROWS (Cost=5 Card=5 Bytes=325)
   1    0   SORT (ORDER BY) (Cost=9 Card=5 Bytes=325)
   2    1     UNION-ALL
   3    2       COUNT (STOPKEY)
   4    3         VIEW (Cost=5 Card=1 Bytes=65)
   5    4           SORT (ORDER BY STOPKEY) (Card=1 Bytes=14)
   6    5             FILTER
   7    6               TABLE ACCESS (FULL) OF 'BBS' (TABLE) (Cost=3 Card=10 Bytes=140)
   8    2       VIEW (Cost=4 Card=4 Bytes=260)
   9    8         SORT (ORDER BY) (Cost=4 Card=4 Bytes=56)
  10    9           COUNT (STOPKEY)
  11   10             TABLE ACCESS (FULL) OF 'BBS' (TABLE) (Cost=3 Card=5 Bytes=70)
-----------------------------------------------------------

Predicate information (identified by operation id):
-----------------------------------------------------------
   3 - filter(ROWNUM<=4)
   5 - filter(ROWNUM<=4)
   6 - filter(NULL IS NOT NULL)
   7 - filter("NUM"<10)
  10 - filter(ROWNUM<=4)
  11 - filter("NUM">10)
-----------------------------------------------------------
```
###1.1 실행순서 (access path)

- sibling 사이에서는 먼저 나온 것을 먼저 처리
- child가 있는 경우 child부터 다 처리하고 parent 처리하기

이 두가지만 기억하면 됩니다.

위 Plan을 기준으로 처리 순서는 다음과 같습니다.  
(0 ~ 11까지 있는 왼쪽의 Index를 사용하겠습니다.)

```
7 -> 6 -> 5 -> 4 -> 3 -> 11 -> 10 -> 9 -> 8 -> 2 -> 1 -> 0
```

- (4) UNION-ALL 아래에 2개의 child(3,8)가 있습니다.
- 이 둘중 위에 있는 (3)부터 처리를 해야하는데 (3)은 child가 있으므로 가장 안쪽부터 처리합니다.
- (3)의 child를 다 처리한 후에 자신의 sibling인 (8)을 처리해야하는데, (8)도 child가 있으므로 안쪽부터 처리합니다.
- (3, 8)이 모두 처리된 후에 (2)부터 쭉 처리하면 됩니다.

###1.2 예상 성능지표 (Cost-based Optimizer Mode에서만 표시)

- Cost : Cost 예상 지수. 클수록 성능상 (CPU 점유, Disk I/O, 수행시간 등...) 안좋다는 의미입니다.
- Card : (Computed Cardinality) : CBO상 계산된 예상되는 return row 입니다.
- Bytes : return row의 byte수 입니다.

###1.3 Predicate information

각 단계별 filter 조건이 어떻게 적용되었다는 정보를 보여줍니다.  

##2. Trace 읽는 법

- Trace는 실제 실행된 경로와 그 성능상 중요 수치들을 보여줍니다.

```SQL
Compile Time  : 2015/07/09 13:31:22
Trace File    : c:\oracle\diag\rdbms\orcl\orcl\trace\orcl_ora_11048.trc
Trace Version : 11.2.0.1.0
********************************************************************************

SELECT * FROM SCOTT.EMP
 WHERE DEPTNO = :"SYS_B_0"

Call     Count CPU Time Elapsed Time       Disk      Query    Current       Rows
------- ------ -------- ------------ ---------- ---------- ---------- ----------
Parse        1    0.000        0.000          0          0          0          0
Execute      1    0.000        0.001          0          0          0          0
Fetch        1    0.000        0.000          0          3          0          0
------- ------ -------- ------------ ---------- ---------- ---------- ----------
Total        3    0.000        0.001          0          3          0          0

Misses in library cache during parse   : 1
Optimizer Goal : ALL_ROWS
Parsing user : SYS (ID=0)


Rows     Row Source Operation
-------  -----------------------------------------------------------------------
      0  TABLE ACCESS FULL EMP (cr=3 pr=0 pw=0 time=0 us cost=2 size=190 card=5
```

