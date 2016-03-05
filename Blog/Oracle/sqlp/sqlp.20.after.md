#20회 SQLP 시험후기

----
###1. 시험일시
>2016년 3월 5일 오후 1시부터 4시까지

###2. 학습기간
>2016년 1월 10일경부터 약 2달간

###3. 공부방법

- SQLP 가이드 1번 읽기 : 2주  
- SQLP 가이드 Blog에 정리 : 3주 (정리 후 다시 읽어보진 않았음)  
- 기출문제 풀이 : 나머지 기간동안
  - devdo님 blog의 서술형 기출문제 5회 가량 풀이 : <http://blog.naver.com/oracledo>

###4. 본인소개
- 나이 : 40세
- IT경력 : 8년차
- 현재 WareValley에서 Orange라는 DB 관리툴 개발팀에 소속

----

솔직히 위에 적은 것은 별로 안 궁금하시죠 ?
20회 시험 문제에 대해 말씀드리겠습니다.  

잊어버리기 전에 서술형 부터 먼저 설명드릴께요.  

서술형 1번은 SQL문과 Trace 결과를 주고 Tuning하라는 문제였습니다.  
정확한 복기는 힘들듯 하고, 그냥 제가 문제를 풀면서 든 생각을 적겠습니다.  

Table a, b, c가 있고 3개를 NL Join 한 것으로 Trace 결과가 나왔습니다.  
a 와 b 를 먼저 join 했는데,
a의 column 하나를 `like 'ZZ%'`로 비교를 했습니다. 
cr=2에 rows도 100건 정도여서 별로 비효율이 없어보였습니다.  
c의 index range scan에서 cr=2300 가량에 rows 가 50건 정도로 여기 index를 수정해야 겠구나 생각이 들었습니다.  
그래서 index 추가하고 해당 index 사용하는 것으로 sql을 시험지에 작성한 뒤에 2번 문제를 풀었습니다.  
1번 문제를 답안지에 옮겨 적는 중 이상한걸 하나 발견했습니다.  

```SQL 
SELECT b. ... , c. ...
  FROM a, b, c
 WHERE a.ProdCode LIKE 'ZZ%'
   AND b.ContCode = a.ProdCode
...
```

가만히 보니 저런식으로 되어 있었습니다.  
a의 column은 출력안하고... 심지어 a와 b의 join 조건이 달랑 1개의 column인데 그마저 따로 조건이 있다보니  
그냥 바로 `b.ContCode LIKE 'ZZ%'`로 하면 되겠구나 생각이 들었습니다.  
이미 답안지를 엄청 작성한 뒤라서 다시 답안지를 받아서 작성했습니다. ㅠㅠ  

서술형 2번은 UNION ALL을 이용하여 서로 다른 조건이 입력된 경우 나누어서 실행하는 방식의 문제였습니다.  
Table 2개를 JOIN 하는데 위와 아래의 SELECT 문에서 a와 b의 JOIN 칼럼이 다릅니다.  
대충 SQL문을 복기하자면 다음과 같은 모양입니다.

```SQL
SELECT ...
  FROM a, b
 WHERE a.ContCode = b.ProdCode
   AND SUBSTR(a.dt,1,6) = SUBSTR(b.dt,1,6)
   AND b.id = :id
   AND b.ProdCode IS NOT NULL
   AND a.code IN (1,2,3,4,5,6)
UNION ALL
SELECT ...
  FROM a, b
 WHERE a.ContCode = b.UserCode
   AND SUBSTR(a.dt,1,6) = SUBSTR(b.dt,1,6)
   AND b.id = :id
   AND b.ProdCode IS NULL
   AND a.code IN (1,2,3,4,5,6)
```
- a Table은 500만건
- b Table은 5000만건
- a.ContCode의 Cardinality가 10
- b.ProdCode의 Cardinality가 50
- a.code는 7개가 있으며 균등분포

위의 조건이었습니다. SELECT의 ... 부분이 엄청 길고 복잡해서 답안지 작성하는데 시껍했습니다. 욕나오더군요 ;;;

제가 작성한 답은
b의 INDEX로 b1 (id, ProdCode, dt) , b2 (id, UserCode, dt) 이렇게 2개를 추가하고,  
a의 INDEX로 (ContCode, code)를 추가하여서 위 SQL에서는 b1과 a의 index를 아래에서는 b2와 a의 index를 사용했으며,

```SQL
AND b.dt LIKE SUBSTR(a.dt,1,6) || '%'
```
로 비교를 하였습니다.  
처음 생각에는 a.code 를 NOT IN 으로 고칠까 생각했는데... 그렇게 하면 INDEX를 사용못하기 때문에 저건 함정일꺼라 생각하고 그냥 두었습니다.
