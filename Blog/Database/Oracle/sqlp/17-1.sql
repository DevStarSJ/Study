-- http://blog.naver.com/oracledo/220425668814

CREATE INDEX IDX_EMP_P_01 ON EMP_P(empcd);
CREATE INDEX IDX_ORDER_P_01 ON ORDER_P(empid, orderdt);

SELECT a.empid, cnt, price, qty, dt, b.empnm, b.addr, b.phone
  FROM (
        SELECT empid, COUNT(*) cnt, SUM(orderpic) price, SUM(orderqty) qty, MAX(orderdt) dt
          FROM order_p p
         WHERE orderdt BETWEEN '20140901' AND '20140901'
         GROUP BY empid
       ) a, emp_p b
 WHERE a.empid = b.empid
   AND b.empcd = 'z0005';

- order_p 전체에 대해서 수행을 하고 있는데, empcd = 'z0005'에 해당하는 empid에 대해서만 하면 된다.
- 
