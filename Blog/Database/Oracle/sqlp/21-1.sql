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

-- custlogin_21 : 1,000,000건

-- ALL

SELECT c.custno, c.custnm, c.phone, (SELECT MAX(l.lastlogindate) FROM custlonin_21 l WHERE l.custno = c.custno) AS lastlogindata
  FROM cust_21 c
 WHERE c.custno = l.custno
 ORDER BY regdate, custno

 -- :page

SELECT n, c.custno, c.custnm, c.phone
  FROM (
        SELECT rownum AS n,
               c.custno, c.custnm, c.phone
          FROM cust_21 c
         WHERE c.custno = l.custno
         ORDER BY regdate, custno
         WHERE n <= :page * 10
       ) c
 WHERE n > (:page - 1) * 10

 -- page + lastlogin

 SELECT c.custno, c.custnm, c.phone, (
                                      SELECT MAX(l.lastlogindate)
                                        FROM custlonin_21 l
                                       WHERE l.custno = c.custno
                                         AND l.lastlogin >= add_months(sysdate, -1)
                                      ) AS lastlogindata
   FROM (
         SELECT n, c.custno, c.custnm, c.phone, c.regdate
           FROM (
                 SELECT rownum AS n,
                        c.custno, c.custnm, c.phone, c.regdate
                   FROM cust_21 c
                  WHERE c.custno = l.custno
                  ORDER BY regdate, custno
                  WHERE n <= :page * 10
                ) c
          WHERE n > (:page - 1) * 10
        ) c
 ORDER BY regdate, custno

 
