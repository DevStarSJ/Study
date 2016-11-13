-- http://blog.naver.com/oracledo/220415238007
-- http://blog.naver.com/qoop07

select o.order_qty , o.order_price, o.order_type, c.cust_nm, c.cust_addr, c.cust_cd, c.addr_cd
from cust16 c, order16 o
where c.cust_id = o.cust_id
and o.order_dt between to_date('20150101', 'yyyymmdd')
                   and to_date('20150315235959', 'yyyymmddhh24miss')
and c.addr_cd||c.cust_nm in ('02도날도', '05홍길동')
order by order_dt, c.cust_id;

- INDEX, HINT 사용하여 Query 재구성

(c.addr_cd, c.cust_nm) IN (('02','도날도'), ('05','홍길동'))

IDX_CUST_01 (addr_cd, cust_nm)
IDX_ORDER_01 (cust_id, order_dt)

/*+ LEADING (c o) INDEX(c IDX_CUST_01) INDEX(o IDX_ORDER_01) USE_NL(o) */
