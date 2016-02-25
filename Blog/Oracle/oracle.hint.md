* Semi Join
  - NL_SJ, HASH_SJ, MERGE_SJ
* Subquery Unnesting 관련
  - UNNEST : 풀어서 JOIN 방식으로 유도
  - NO_UNNEST : 풀지말고 Filter 방식으로 최적화 유도
* View Merging
  - NO_MERGE(테이블) : main query 와 inline view를 JOIN으로 풀지말고 inline view를 먼저 실행
  - MERGE(테이블) : main query와 inline view를 JOIN으로 풀어서 최적화를 시도
* Push Predicate (조건절 Push)
  - PUSH_PRED(인라인뷰) : main query에서 먼저 filtering하여 그 결과를 inline view의 filter 조건으로 넣어라.
