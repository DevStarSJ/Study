-- http://blog.naver.com/oracledo/220406979657

SELECT * FROM
(
SELECT CASE WHEN no = 1 THEN '전체'
            WHEN no = 2 AND 상품코드 = 'R' THEN '냉장고',
            WHEN no = 3 AND 상품코드 IN ('R', 'T', 'A') THEN '가정',
            WHEN no = 4 AND 상품코드 NOT IN ('R', 'T', 'A') THEN '가전외'
       END 상품코드,
       SUM(NVL(판매수량, 0)) 판매수량
  FROM 상품판매내역, (SELECT LEVEL NO FROM DUAL CONNECT BY LEVEL <= 4)
 WHERE 판매일자 BETWEEN '20151201' AND '20141231'
 GROUP BY CASE WHEN no = 1 THEN '전체'
               WHEN no = 2 AND 상품코드 = 'R' THEN '냉장고',
               WHEN no = 3 AND 상품코드 IN ('R', 'T', 'A') THEN '가정',
               WHEN no = 4 AND 상품코드 NOT IN ('R', 'T', 'A') THEN '가전외'
          END
)
 WHERE 상품코드 IS NOT NULL

- 한달평균 30만건 (파티션은 구성 안해도 될 정도)
- 비효율 설명
- 튜닝 방법 설명
- 튜닝 쿼리 작성

1. SUM안에 NVL이 있으면 모든 요소마다 NVL 함수를 실행함. NVL(SUM(...))으로 수정
2. 냉장고, 냉장고외 가전, 가전외 3개로 구분하여 합을 계산한 후 원하는 모든 경우에 대해서 출력하는 것도 가능함
3. Table Full Scan -> 판매일자에 대한 INDEX가 없다면 생성하는게 좋음
4. 상품코드 IS NOT NULL 조건을 INLINE VIEW 안으로 넣어서 필요없는 것에 대한 조회를 하지 않도록
5. 4배로 뻥튀기 하고 GROUP BY 되어 있음. 먼저 GROUP BY 하고 뻥튀기 하도록

SELECT CASE WHEN no = 1 THEN '전체'
            WHEN no = 2 THEN '냉장고'
            WHEN no = 3 THEN '가전'
            WHEN no = 4 THEN '가전외'
       END AS 상품코드,
       CASE WHEN no = 1 THEN 냉장고 + 냉장고외가전 + 가전외
            WHEN no = 2 THEN 냉장고
            WHEN no = 3 THEN 냉장고 + 냉장고외가전
            WHEN no = 4 THEN 가전외
       END AS 판매수량
  FROM
(
SELECT NVL(SUM(CASE WHEN 상품코드 = 'R' THEN 판매수량 END),0) '냉장고',
       NVL(SUM(CASE WHEN 상품코드 IN ('T', 'A') THEN 판매수량 END),0) '냉장고외가전',
       NVL(SUM(CASE WHEN 상품코드 NOT IN ('R','T','A') THEN 판매수량 END),0) '가전외'
  FROM 상품판매내역
 WHERE 판매일자 BETWEEN '20151201' AND '20141231'
   AND 상품코드 IS NOT NULL
) A,
(
SELECT LEVEL NO FROM DUAL CONNECT BY LEVEL <= 4
) B
