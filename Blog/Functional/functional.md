### Step 1

(take 25 (squares-of (integers)))

### Step 2

(defn squint [n]
    (take n (squares-of (integers))))

(println (squint 25))

### Step 3

(defn square [n]
    (* n n))

(defn squares-of [list]
    (map square list))

(defn integers []
    (integers-starting-at 1))

(defn integers-starting-at [n]
    (cons n (lazy-seq (integers-starting-at (inc n)))))

(defn map [f l]
    (if (empty? l)
        []
        (cons (f (first l)) (lazy-seq (map f (rest l))))))

(defn take [n l]
    (if (zero? n)
        []
        (cons (first l) (take (dec n) (rest l)))))

### ex : n = 2

(squint 2)

(take 2 (squares-of (integers)))

(if (zero? 2) -> 가 아니므로
    

(cons (first (squares-of (integers)) (take (dec 2) (rest (squares-of (integers))))))

(cons (first (squares-of (integers)) (take 1 (rest (squares-of (integers))))))

(cons (2 of (squares-of (integers)) (cons (1 of (squares-of (integers)) []))))

