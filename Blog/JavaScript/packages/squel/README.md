# Squel.js

*JavaScropt* 의 `SQL query string`의 작성을 도와주는 package 입니다.
*C#* 의 `LINQ`와 비슷한 형식으로 함수들의 체인을 이용해서 정의하면 해당 기능을 동작하는 `query string`을 작성해 줍니다.

단순히 `query string`만을 만들어 주는 역할만을 합니다.
이게 장점일수도 단점일수도 있는데, *C#* 의 `LINQ`의 경우에는 `Inline View`나 `Subquery`, `JOIN`을 표현하기가 상당히 복잡했습니다. 그래서 단순한 문장이 아닌 경우는 그냥 `raw query`로 작성하는게 더 편했습니다.
하지만 `squel`의 경우에는 어차피 결과물은 `String`이기 때문에 이것들을 잘 조합하면 얼마든지 복잡한 문장도 표현이 가능합니다.


여기에서는 자주 사용되는 간단한 예제들을 중심으로 소개를 드릴 예정이며,
자세한 내용은 공식 사이트 <https://hiddentao.com/squel> 를 참조해주세요.

## 설치

### Node.js

```
npm install squel
```

```JavaScript
var squel = require("squel");
```

### Browser

```HTML
<script type="text/javascript" src="/your/path/to/squel.min.js"></script>
<script>
  console.log( squel.VERSION );    /* version string */
</script>
```

## 사용법

### SELECT 문장

- `select()` : `SELECT`에 대한 query builder 인스턴스를 생성합니다.
- `from("table", alias = null)` : `FROM`절에 해당하는 테이블을 지정합니다. `alias` 생략 가능
- `field("column")` : 읽어올 컬럼들을 지정합니다. `field`절을 실행한 순서대로 왼쪽부터 출력됩니다.
- `where("condition")` : `WHERE`절 조건을 지정합니다.
- `distinct()` : `DISTINCT`한 결과로 출력합니다. (중복제거)
- `order("column", ASC = true)` : `ORDER BY`절에 해당하는 sorting연산을 수행합니다. `order`절을 수행한 순서대로 왼쪽부터 기술되며 `ASC`, `DESC`여부를 2번째 인자에 `true`,`false`로 전달이 가능합니다.
- `group()` : `GROUP BY`절에 해당하는 그룹화 기능을 수행합니다.
- `having("condition")` : `HAVING`절에 해당하는 조건을 지정합니다.
- `limit(number)` : `TOP-N` query를 수행합니다. 앞서 지정한 `limit`기능을 제거하고 싶으면 `.limit(0)`을 수행하면 됩니다.
- `offset(number)` : `SKIP`연산을 수행합니다. `limit`와 마찬가지로 `.offset(0)`을 수행하면 앞서 지정한 `offset`기능을 제거할 수 있습니다.
- `function('string')` : Scalar 값이나 DB Function 수행시 활용이 가능합니다.
- JOIN
  - `join("table", alias = null, onCondition = null)` : INNER JOIN을 수행합니다. `alias`와 `ON절`은 필요없을시 생략이 가능합니다.
  - `outer_join(...)` : 해당 하수에서 지정한 테이블을 OUTER JOIN으로 지정
  - `left_join(...)` : LEFT OUTER JOIN
  - `right_join(...)` : RIGHT OUTER JOIN
- `union('squel select instance')` : `UNION`연산을 수행합니다.

- 모든 필요한 기능을 다 수행한 후 `toString()`를 실행하면 `query string`이 생성됩니다.

- `UNION ALL` 연산에 대한 대해서는 현재 제공되고 있지 않습니다. 필요할 경우 그냥 `string concatenation`을 해야합니다.

- 모든 조건(`condition`)에 대해서는 `string format`형식으로 입력이 가능합니다. (ex. `where('id = ?', 1)`)

- 관련 예제들

```javascript
var squel = require("squel");

var q = squel
  .select()
  .from("emp", "e")
  .field("*")
  .toString();
```

```SQL
SELECT * FROM emp `e`
```

```javascript
var s = squel
  .select()
  .from('emp', 'e')
  .where('e.id IN ?', idList)
  .where('e.sal > ?', 2000)
  .join('dept', 'd', 'e.deptno = d.id')
  .field('e.name')
  .field('d.name')
  .toString();
```

```SQL
SELECT e.name, d.name FROM emp `e` INNER JOIN dept `d` ON (e.deptno = d.id) WHERE (e.id IN (1, 2, 3)) AND (e.sal > 2000)
```
