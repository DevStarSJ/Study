[SQLP] 실기시험 기출문제 복구(60%) 2014.09.20 

<http://faust86.tistory.com/entry/SQLP-%EC%8B%A4%EA%B8%B0%EC%8B%9C%ED%97%98-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-%EB%B3%B5%EA%B5%AC60-20140920>


◎ 실기시험1번

* 쿼리

```SQL
select a.고객번호, a.주문건수, a.총금액, a.할인금액, a.최근주문일시, b.고객명, b.고객주소
from 
(
 select 고객번호, count(*) 주문건수, sum(금액) 총금액, sum(할인금액) 할인금액, max(주문일시) 최근주문일시
 from 주문
 where 주문일시 >= trunc(sysdate-3)
 group by 고객번호 
) a, 고객 b
where a.고객번호 = b.고객번호
and b.고객등급 = 'Z001'
```
* 위 쿼리의 sql trace   
인라인 뷰의 where 주문일시 >= trunc(sysdate-3) 부분에서  
 access rowid cr=28xxx , pr=28xxx <-엄청난 수로 늘었음.  
 index range scan 주문일시idx cr=380, pr=작은수..  


1) 쿼리를 튜닝하시오 (sql재작성 or 힌트추가)

2) 쿼리를 작성관련 인덱스 구성안

 

◎ 실기시험2번
```
* 테이블 (월별로 파티션 되어있음) 
상담
----------------
상담번호
상담일자(yyyymmdd)
상담원ID
상담시각(hh24miss)
상담시간
타부서이관코드 (00: 이관x , 01 : 상급이관, 02:또다른곳이관(ㅋㅋ))
.
.
.
```
1) 상담원별로,

상담일자, 시각은 조회하고자 하는 날의 첫날 0시부터 현재날짜 12시까지 기준으로 함.
(예를들어, 금일(9월20일) 기준으로 2014년9월01일 0시 부터 9월20일 12시까지)
아래의 record를 조회하는 sql작성.
```
- 상담원id
- 총건수
- 타부서이관건수
- 중복제거 건수
(...더이상 생각이...한 7개됐음 ㅋㅋ)
```
2) 쿼리작성을 위한 인덱스 구성안 ( 4갠가 5갠가임)
```
- 파티션키
- 인덱스
- 파티션 인덱스 
  local prefix
  local nonprefix
  global prefix
  global nonprefix 이런거..
```
- 하나더있었는데 먼지 생각안남 ㅋㅋ
