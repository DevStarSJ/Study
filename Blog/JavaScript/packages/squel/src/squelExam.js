var squel = require("squel");

var q = squel
  .select()
  .from("emp", "e")
  .field("*")
  .toString();

console.log(q);

var idList = [ 1, 2, 3];

var s = squel
  .select()
  .from('emp', 'e')
  .where('e.id IN ?', idList)
  .where('e.sal > ?', 2000)
  .join('dept', 'd', 'e.deptno = d.id')
  .field('e.name')
  .field('d.name')
  .toString();

console.log(s);

var is = squel
  .insert()
  .into('emp')
  .fromQuery(
    ['id', 'name'],
    squel
      .select()
      .from('candidates')
      .field('id')
      .field('name')
  )
  .toString();

console.log(is);

var im = squel.insert()
  .into('emp')
  .setFieldsRows([{id:1, name:"Luna"}, {id:2, name:"Star"}])
  .toString();

console.log(im);

var uf = squel.update()
  .table('emp')
  .set('hire_date', 'GETDATE()', { dontQuote: true })
  .where('dept = ?', 10)
  .toString();

console.log(uf);
