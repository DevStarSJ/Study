-- http://blog.naver.com/oracledo/220731275842

create table cust_21 (
    custno number not null primary key,
    custnm varchar2(20),
    custtype varchar2(5),
    phone varchar2(30),
    regdate date
);

-- cust_21 : 100,000건
-- (custtype = 'AC' 10,000건)

create table custlogin_21 (
    logindate date not null,
    custno number not null,
    ip varchar2(50),
    pcnm varchar2(100)
);

alter table custlogin_21 add primary key (logindate, custno);


-- SELECT * FROM (
-- SELECT A.*, ROW_NUMBER() OVER(ORDER BY ID DESC) AS NUM
-- FROM OP_SAMPLE A
-- )
-- WHERE NUM BETWEEN 999991 AND 1000000;

-- custlogin_21 : 1,000,000건

CREATE INDEX IDX_CUST_21_01 ON CUST_21(custtype, regdate, custno);
CREATE INDEX INDX_CUSTLOGIN_21_01 ON CUSTLOGIN_21(custno, logindate);

-- ALL

SELECT /*+ INDEX(C IDX_CUST_21_01) */
       c.custno, c.custnm, c.phone, (SELECT /*+ INDEX(L INDX_CUSTLOGIN_21_01) */
                                            MAX(l.logindate)
                                       FROM custlonin_21 l
                                      WHERE l.custno = c.custno
                                       AND l.lastlogin >= add_months(sysdate, -1)) AS lastlogindata
  FROM cust_21 c
 WHERE c.custtype = 'AC'
 ORDER BY regdate, custno

 -- :page

SELECT n, c.custno, c.custnm, c.phone
  FROM (
        SELECT rownnum AS n, *
          FROM (
                SELECT c.custno, c.custnm, c.phone
                  FROM cust_21 c
                 WHERE c.custtype = 'AC'
                 ORDER BY regdate, custno
               )
        WHERE n <= :page * 10
       ) c
 WHERE n > (:page - 1) * 10

 -- page + lastlogin

 SELECT c.custno, c.custnm, c.phone, c.regdate, (
                                                  SELECT /*+ INDEX(L INDX_CUSTLOGIN_21_01) */
                                                         MAX(l.logindate)
                                                    FROM custlogin_21 l
                                                   WHERE l.custno = c.custno
                                                     AND l.lastlogin >= add_months(sysdate, -1)
                                                  ) AS lastlogindata
   FROM (
         SELECT n, c.custno, c.custnm, c.phone, c.regdate
           FROM (
                 SELECT /*+ INDEX(C IDX_CUST_21_01) */
                        rownum AS n,
                        c.custno, c.custnm, c.phone, c.regdate
                   FROM cust_21 c
                  WHERE c.custtype = 'AC'
                    AND n <= :page * 10
                  ORDER BY regdate, custno
                ) c
          WHERE n > (:page - 1) * 10
        ) c
 ORDER BY regdate, custno
