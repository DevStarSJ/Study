-- http://blog.naver.com/oracledo/220860546323

SELECT O.ORDER_CD, O.ORDER_TP,
       (SELECT CUST_NM FROM CUST22 C WHERE C.CUST_ID = O.CUST_ID) AS CUST NM,
       S.SHIP_CD, S.SHIP_DT
  FROM ORDER22 O, SHIP22 S
 WHERE O.ORDER_NO = S.ORDER_NO
   AND O.ORDER_DT BETWEEN '20160101' AND '20160102';

-- BATCH 작업이란 말에 왠지 HASH JOIN을 써야한다는 느낌적인 느낌이...
-- PK_SHIP22에서 INDEX FULL SCAN : 2022027436 -> TABLE FULL SCAN
-- ORDER22 는 PATITION에서 TABLE FULL SCAN해서 2247건만 읽음... JOIN 방법을 다르게 ?
-- JOIN 조건인 S.ORDER_NO에 대한 INDEX가 필요, 해당 INDEX로 파티션 테이블에 대한 정보도 함께 있을수있으면 좋겠음

CREATE INDEX IDX_SHIP22_01 ON SHIP22 (ORDER_NO, SHIP_DT, SHIP_CD);

SELECT /*+ LEADING(O S C) USE_NL(S) USE_NL(C) INDEX(S INDEX_SHIP22_01) */
       O.ORDER_CD, O.ORDER_TP,
       C.CUST_NM,
       S.SHIP_CD, S.SHIP_DT
  FROM ORDER22 O, SHIP22 S, CUST22 C
 WHERE O.ORDER_NO = S.ORDER_NO
   AND O.ORDER_DT BETWEEN '20160101' AND '20160102'
   AND C.CUST_ID = O.CUST_ID;

-----------------------------------------

ALTER SESSION SET WORKAREA_SIZE_POLICY = MANUAL
ALTER SESSION HASH_AREA_SIZE = ~;
ALTER SESSION PGA_AGGREGATE_TARGET = ~~;

SELECT /*+ leading(o s c) full(o) parallel(o 8)
                          full(s) parallel(s 8)
                          use_nl(c) index (c idx_pk_cust_id)
                          use_hash_s */
       o.order_cd, o.order_tp, c.cust_nm, s.ship_cd, s.ship_dt
  FROM order22 o, ship22 s, cust22 c
 WHERE o.order_no = s.order_no
   AND c.cust_id(+) = o.cust_id
   AND o.order_dt BETWEEN '20160101' AND '20160102';