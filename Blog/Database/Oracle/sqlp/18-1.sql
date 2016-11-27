-- http://blog.naver.com/oracledo/220488529134

SELECT B.ORD_NO, B.ORD_CD, ROUND(A.AVG_ORD_AMT, 2) 평균주문금액, A.SUM_ORD_AMT 주문금액합계
  FROM (
       SELECT ORD_CD,
              AVG(ORD_AMT) AVG_ORD_AMT,
              SUM(ORD_AMT) SUM_ORD_AMT
         FROM TB_ORD
        GROUP BY ORD_CD
       ) A, TB_ORD B
 WHERE B.ORD_CD = A.ORD_CD
 ORDER BY ORD_CD, ORD_NO;

----------------------------------------

SELECT ORD_NO, ORD_CD
       ROUND(AVG(ORD_AMT) OVER (PARTITION BY ORD_CD),2) 평균주문금액,
       SUM(ORD_AMT) OVER (PARTITION BY ORD_CD) 주문금액 합계
  FROM TB_ORD 
 ORDER BY ORD_CD, ORD_NO;