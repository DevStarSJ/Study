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
