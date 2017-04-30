
# 파이썬으로 풀어보는 수학

- 원서명 : Doing Math with Python: Use Programming to Explore Algebra, Statistics, Calculus, and More! (ISBN 9781593276409)
- 지은이 : 아미트 사하(Amit Saha)
- 원서 및 관련자료 : <https://www.nostarch.com/doingmathwithpython>
- 번역서 : <http://www.acornpub.co.kr/book/doing-math-with-python>

![책표지](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/image/cover.jpg?raw=true)

## 5장 집합과 확률

### 1. 집합은 무엇인가 ?

집합(set)은 개별 객체의 모음(collection)입니다.
통상 객체를 원소(element)나 구성원(member)라고 부릅니다.
집합과 모음의 다른점으로는 집합은 동일한 2개의 원소를 가질 수 없습니다.

`SymPy`를 사용해 파이썬에서 집합으로 작업하는 방법에 대해서 살펴보겠습니다.

### 2. 집합 생성

수학기호로 집합을 표현할 때는 `{ 2, 4, 6 }`와 같이 중괄호를 사용합니다.
파이썬에서는 `FiniteSet` 클래스를 사용하여 표현할 수 있습니다.


```python
from sympy import FiniteSet

s = FiniteSet(2, 4, 6)
s
```




    {2, 4, 6}




```python
type(s)
```




    sympy.sets.sets.FiniteSet



동일한 집합에 정수, 분수, 부동소수점수를 같이 저장할 수도 있습니다.


```python
from fractions import Fraction

FiniteSet(1, 1.5, Fraction(1,5))
```




    {1/5, 1, 1.5}



`카디널리티(cardinality)`란 집합의 구성원 수를 의미합니다.
`len()`함수를 이용해 계산이 가능합니다.


```python
len(s)
```




    3



`대상 집합에 숫자가 존재하는지 여부`는 `in`연산자를 사용해 알 수 있습니다.


```python
3 in s
```




    False




```python
4 in s
```




    True



`공집합(empty set)`을 생성하기 위해서는 인자가 없이 생성하면 됩니다.


```python
FiniteSet()
```




    EmptySet()



`리스트`나 `튜플`을 인자로 전달해서 집합을 생성할 수도 있습니다.


```python
members = [1, 2, 3]
FiniteSet(*members)
```




    {1, 2, 3}



앞서 언급했듯이 집합 내에는 중복된 값을 허용하지 않습니다.
같은 값을 여러번 넣어도 한 번만 추가되고 나머지는 모두 무시됩니다.


```python
s = FiniteSet(1, 3, 2, 3)
s
```




    {1, 2, 3}



그리고, 입력 순서와 저장되는 순서는 무관합니다.
집합 내의 구성원에 대한 순서는 별도로 저장하고 있지 않기 때문입니다.


```python
for m in s:
    print(m)
```

    1
    2
    3


두 집합의 구성원이 서로 다른 순서로 저장되더라도, 모든 요소들이 같다면 두 집합은 같은 집합으로 취급합니다.


```python
s = FiniteSet(3, 5, 7)
t = FiniteSet(5, 7, 3)
s == t
```




    True



###  3. 부분집합, 초집합, 파워집합

집합 s의 모든 구성원이 집합 t의 구성원일 경우 s는 t의 `부분집합(subset)`이라고 정의합니다.
파이썬에서는 `is_subset()` 함수를 사용해서 확인이 가능합니다.


```python
s = FiniteSet(1)
t = FiniteSet(1, 2)

s.is_subset(t)
```




    True




```python
t.is_subset(s)
```




    False




```python
s.is_subset(s)
```




    True



공집합은 모든 집합의 부분집합이며, 모든 집합은 자기 자신이 부분집합입니다.

`초집합(superset)`은 부분집합의 반대 개념으로 집합t가 집합s의 모든 구성원을 포함할 경우 집합t는 집합s의 초집합이라고 부릅니다.
파이썬에서는 `is_superset()` 함수를 사용해서 확인이 가능합니다.


```python
s.is_superset(t)
```




    False




```python
t.is_superset(s)
```




    True




```python
s.is_superset(s)
```




    True



`파워집합(powerset)`은 모든 가능한 부분집합입니다.
모든 집합은 `2 ** cadinality` 만큼의 부분집합을 가집니다. (공집합, 자기자신을 포함)
파이썬에서는 `powerset()` 함수를 사용해 찾아낼 수 있습니다.


```python
s = FiniteSet(1, 2, 3)
ps = s.powerset()
ps
```




    {EmptySet(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}




```python
len(ps)
```




    8



동일하지 않은 집합t와 집합s가 있을 경우,
집합s가 집합t의 부분 집합일 경우 집합t는 집합s의 초집합이라고 할 수 있습니다.
`is_proper_subset()` , `is_proper_superset()` 함수를 사용해서 부분집합, 초집합 관계를 확인 할 수 있습니다.


```python
t = FiniteSet(1, 2, 3, 5)
s.is_proper_subset(t)
```




    True




```python
t.is_proper_superset(s)
```




    True




```python
s.is_proper_subset(s)
```




    False




```python
s.is_proper_superset(s)
```




    False



### 4. 집합 연산

#### 합집합

두 집합의 모든 구성원을 포함하는 집합입니다. (중복된 구성원은 하나만 포함됩니다.)


```python
from sympy import FiniteSet

s = FiniteSet(1, 2, 3)
t = FiniteSet(2, 4, 6)

s.union(t)
```




    {1, 2, 3, 4, 6}



#### 교집합

두 집합에 공통적으로 존재하는 구성원들로만 이루어진 집합입니다.


```python
s.intersect(t)
```




    {2}



#### 카르테지안 곱

두 집합의 구성원들을 택해 모든 가능한 쌍으로 구성된 집합입니다.

카르테지안 곱의 카디널리티는 개별 집합의 카디널리티의 곱입니다.


```python
p = s*t
p
```




    {1, 2, 3} x {2, 4, 6}




```python
for e in p:
    print(e)
```

    (1, 2)
    (1, 4)
    (1, 6)
    (2, 2)
    (2, 4)
    (2, 6)
    (3, 2)
    (3, 4)
    (3, 6)



```python
len(p) == len(s) * len(t)
```




    True



지수연산자를 이용해서 설정한 횟수만큼의 곱도 가능합니다.


```python
u = FiniteSet(1, 2)
p = u**3
p
```




    {1, 2} x {1, 2} x {1, 2}




```python
for e in p:
    print(e)
```

    (1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 2, 2)
    (2, 1, 1)
    (2, 1, 2)
    (2, 2, 1)
    (2, 2, 2)


#### 다중변수 집합에 공식 적용

다음 수식은 추의 길이별 주기값을 구하는 수식입니다.

![수식 추의주기](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/image/DoingMathWithPython.Ch05.equation.01.png?raw=true)

- T : 추가 한번 왕복하는데 소요되는 시간
- L : 추의 길이
- 상수값 : pi, g(지역의 중력가속도 : 대략 9.8 m/s^2)

길이에 따라 추의 주기가 어떻게 변하는지 알고 싶다면 위 수식에 `L`값을 변경해가면서 입력해보면 됩니다.


```python
from sympy import FiniteSet, pi

def time_period(length):
    g = 9.8
    T = 2 * pi * (length / g)**0.5
    return T

L = FiniteSet(15, 18, 21, 22.5, 25)
for e in L:
    t = time_period(e/100)
    print('Length: {0} cm Time Period: {1:.3f} s'.format(float(e), float(t)))
```

    Length: 15.0 cm Time Period: 0.777 s
    Length: 18.0 cm Time Period: 0.852 s
    Length: 21.0 cm Time Period: 0.920 s
    Length: 22.5 cm Time Period: 0.952 s
    Length: 25.0 cm Time Period: 1.004 s


입력으로 사용된 집합의 값이 cm 단위이기 때문에 함수에 전달시 100으로 나누어서 전달하였습니다.

서로 다른 3곳(중력이 다른 곳)에서 실험을 한다고 가정해 보겠습니다.
(적도 : 9.78 , 북극 9.83, 호주 9.8)


```python
def time_period(length, g):
    return 2 * pi * (length / g)**0.5

L = FiniteSet(15, 18, 21, 22.5, 25)
G = FiniteSet(9.8, 9.78, 9.83)

print('{0:^15}{1:^15}{2:^15}'.format('Length(cm)','Gravity(m/m^2)','Time Period(s)'))
for e in L * G:
    t = time_period(e[0]/100, e[1])
    print('{0:^15}{1:^15}{2:^15.3f}'.format(float(e[0]),float(e[1]), float(t)))
```

      Length(cm)   Gravity(m/m^2) Time Period(s) 
         15.0           9.78           0.778     
         15.0            9.8           0.777     
         15.0           9.83           0.776     
         18.0           9.78           0.852     
         18.0            9.8           0.852     
         18.0           9.83           0.850     
         21.0           9.78           0.921     
         21.0            9.8           0.920     
         21.0           9.83           0.918     
         22.5           9.78           0.953     
         22.5            9.8           0.952     
         22.5           9.83           0.951     
         25.0           9.78           1.005     
         25.0            9.8           1.004     
         25.0           9.83           1.002     


### 5. 확률

- **실험**(experiment) : 각각 가능한 확률에 대한 테스트, 실험을 한 번 실행하는 것을 시도(trial)이라고 함. 예를 들어 주사위 던지기, 카드 뽑기
- **표본공간**(`S`) : 모든 가능한 실험 결과들의 집합. 예를 들어  6면 주사위를 한 번 던진 경우 표본공간 `S = {1, 2, 3, 4, 5, 6}`
- **사건**(`E`) : 표본공간의 부분집합. 예를 들어 6면 주사위의 표본공간 중 숫자 3이 나올 확률

![수식 확률](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/image/DoingMathWithPython.Ch05.equation.02.png?raw=true)

특정 사건이 일어날 확률(`P(E)`)는 해당 사건의 개수(`n(E)`)를 전체 표본공간의 개수(`n(S)`)로 나눈 값입니다.
주사위를 던져서 3이 나올 확률은 다음과 같습니다.

> S = { 1, 2, 3, 4, 5, 6 }
E = { 3 }
n(S) = 6
n(E) = 1
P(E) = 1 / 6

이를 함수로 작성해 보겠습니다.


```python
def probability(space, event):
    return len(event) / len(space)
```

위 함수를 이용해서 1 ~ 20 사이의 숫자 중 소수(Prime number)일 확률을 구해보도록 하겠습니다.


```python
def check_prime(number):
    if number != 1:
        for factor in range(2,number):
            if number % factor == 0:
                return False
    else:
        return False
    return True

def get_primes(number):
    primes = [x for x in range(2, number + 1) if check_prime(x) ]
    
    return FiniteSet(*primes)

space = FiniteSet(*range(1,21))
event = get_primes(20)
probability(space, event)
```




    0.4




```python
event
```




    {2, 3, 5, 7, 11, 13, 17, 19}



#### 사건A나 사건B의 확률

A 사건과 B 사건의 집합을 합집합(`union`)한 다음에 확률을 계산하면 됩니다.

- S : 6면주사위를 1번 던짐 -> { 1, 2, 3, 4, 5, 6 }
- A : 소수 -> { 2, 3, 5 }
- B : 홀수 -> { 1, 3, 5 }

일 경우의 사건 A나 B일 확률은 다음과 같습니다.


```python
S = FiniteSet(*range(1,7))
A = FiniteSet(2, 3, 5)
B = FiniteSet(1, 3, 5)

len(A.union(B)) / len(S)
```




    0.6666666666666666



#### 사건 A 이면서 사건 B일 확률

두 집합의 교집합(`intersect`)의 확률을 계산하면 됩니다.


```python
len(A.intersect(B)) / len(S)
```




    0.3333333333333333



### 6. 랜덤 숫자 생성

파이썬에서 랜덤숫자를 생성하려면 먼저 표준 라이브러리 `random`을 포함시켜야 합니다.
주로 사용되는 랜덤함수는 다음의 2가지 정도만 알아도 됩니다.
- randint(from, to) : from 에서 to 사이의 숫자를 리턴합니다. int값을 넣어줘야 합니다.
- random() : 0에서 1사이의 부동소수점 숫자를 생성합니다.

주사위를 굴려서 총합이 20될 때까지 몇 번을 던져야 하는지를 랜덤을 통해서 구현해 보겠습니다.


```python
import random

target_score = 20

def roll():
    return random.randint(1,6)

def play_game():
    score = 0
    num_rolls = 0
    while score < target_score:
        dice = roll()
        num_rolls += 1
        print('Rolled: {0}'.format(dice))
        score += dice

    print('Score of {0} reached in {1} rolls'.format(score, num_rolls))

play_game()
```

    Rolled: 6
    Rolled: 6
    Rolled: 1
    Rolled: 5
    Rolled: 2
    Score of 20 reached in 5 rolls



```python
play_game()
```

    Rolled: 6
    Rolled: 4
    Rolled: 3
    Rolled: 1
    Rolled: 5
    Rolled: 6
    Score of 25 reached in 6 rolls


#### 목표점수 달성이 가능한가 ?

이번에는 목표로 한 점수가 최대던지기 횟수 내에 달성이 가능한지 그 여부 및 확률을 계산해주는 프로그램을 작성해 보겠습니다.


```python
from sympy import FiniteSet
from random import randint

def find_prob(target_score, max_rolls):
    dice = FiniteSet(*range(1,7))
    space = dice**max_rolls
    event_num = 0
    for e in space:
        n = sum(e)
        if (n >= target_score):
            event_num += 1
    return event_num / len(space)

find_prob(10,2)
```




    0.16666666666666666




```python
find_prob(20, 3)
```




    0.0



주사위를 3번 던져서 최고값은 18이므로 20이 나올 수 있는 확률은 0% 입니다.

위에서 사용한 랜덤은 균일 랜덤 숫자(uniform random number)였습니다.
비균일 랜덤을 생성하려면 어떻게 해야 할까요 ?
가장 간단하게 생각해 볼 수 있는 방법은 높은 확률에 더 넓은 영역을 지정하여 랜덤을 수행하는 것입니다.

>동전을 던졌을 때 앞면(True)이 나올 확률이 2/3이고, 뒷면(False)가 나올 확률이 1/3일 경우


```python
import random

def non_uniform_toss():
    if random.random() < 2/3:
        return True
    return False

true_num = 0
for i in range(10000):
    if non_uniform_toss() == True:
        true_num += 1
true_num
```




    6629



위 함수를 조금 더 일반적으로 구현하여 재사용 가능하도록 해보겠습니다.
인자로 확률값을 넣은 리스트를 전달받아서 호출시 마다 해당 **index**를 리턴받도록 하겠습니다


```python
import random

def get_index(probabilities):
    max = sum(probabilities)
    
    acc = 0
    rand = random.random() * max
    for idx, percent in enumerate(probabilities):
        acc += percent
        if rand < acc:
            return idx
    return len(probabilities)
```

이 함수를 이용해서 다음의 경우에 대해서 시뮬레이션 해보겠습니다.

다음 확률로 지폐를 배분하는 ATM기의 경우 만번의 지폐를 배분했을 때 각각 몇회 배분되었는지를 구해보겠습니다.

- $5 : 1/6
- $10 : 1/6
- $20 : 1/3
- $50 : 1/3


```python
from collections import defaultdict

d = defaultdict(int)
keys = ['$5', '$10', '$20', '$50']
probabilities = [ 1, 1, 2, 2 ]

for i in range(10000):
    d[keys[get_index(probabilities)]] += 1
d
```




    defaultdict(int, {'$10': 1639, '$20': 3322, '$5': 1733, '$50': 3306})



### 프로그래밍 연습

#### 1. 벤다이어그램을 사용하여 집합 간의 관계를 가시화

`matplotlib_venn` 패키지를 이용하여 벤다이어그램을 그릴 수 있습니다.

예를 들어서 20이하의 소수와 홀수를 그리는 벤다이어그램을 구현한 코드를 살펴보겠습니다.


```python
def get_odds(number):
    odds = [x for x in range(1, number + 1) if x % 2 == 1]
    return FiniteSet(*odds)

odds = get_odds(20)
odds
```




    {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}




```python
primes = get_primes(20)
primes
```




    {2, 3, 5, 7, 11, 13, 17, 19}




```python
from matplotlib_venn import venn2
import matplotlib.pyplot as plt

def draw_venn(sets, lables):
    venn2(subsets=sets, set_labels=lables)
    plt.show()

draw_venn([odds, primes], ['odds', 'primes'])
```

![벤다이어그램](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/image/DoingMathWithPython.Ch05.01.png?raw=true)

`(학번, 축구를 좋아하는지 여부, 다른 운동을 좋아하는지 여부)`의 3개의 컬럼을 가진 csv 파일을 읽어서 그 결과를 보여주는 벤다이어그램을 출력하세요.
좋아한다는 것은 `1`, 안 좋아한다는 것은 `0`으로 표시하도록 하겠습니다.
(**csv**를 읽어서 **list**를 리턴하는 함수는 Ch.03에서 작성해 놓은 함수를 재사용 하겠습니다.)


```python
import csv

def csv_to_list(filename, colHeaderLen, rowHeaderLen):
    reader = csv.reader(open(filename))                    
    columns = len(next(reader)) # pass column header
    
    for i in range(1, colHeaderLen):
        next(reader)
        
    data = []
    
    for i in range(rowHeaderLen, columns):
        data.append([])
    
    for row in reader:
        for i in range(rowHeaderLen, columns):
            data[i - rowHeaderLen].append(float(row[i]))
            
    return data
```


```python
lists = csv_to_list('files/ch05.venn.data.csv', 1, 0)
lists[2]
footballs = FiniteSet(*[ int(id) for id,football in zip(lists[0], lists[1]) if football == 1 ])
others = FiniteSet(*[ int(id) for id,other in zip(lists[0], lists[2]) if other == 1 ])
draw_venn([footballs, others],['Football','Other'])
```

![벤다이어그램2](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/image/DoingMathWithPython.Ch05.02.png?raw=true)


```python
sum(lists[1])
```




    1452.0




```python
sum(lists[2])
```




    1551.0



#### 2. 대수의 법칙 (기대값 계산)

기대값은 모든 경우의 수의 값에 그 확률을 곱한 값을 의미합니다.

![수식 기대값](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/image/DoingMathWithPython.Ch05.equation.03.png?raw=true)

그럼 주사위를 던졌을 경우의 기대값은 다음과 같습니다.


```python
e = 1*(1/6) + 2*(1/6) + 3*(1/6) + 4*(1/6) + 5*(1/6) + 6*(1/6)
e
```




    3.5



주사위를 던지는 회수를 늘려가면서 기대값대로 나오는지를 입증하는 프로그램을 작성하세요.

먼저, 재사용 가능한 형태로 기대값을 구하는 함수부터 구하는 만들어 보겠습니다.


```python
def get_expected_value(events, probabilities):
    elements = [x*p for x,p in zip(events, probabilities)]
    return sum(elements)   
```

위 함수가 제대로 동작하는지 앞에서 직접 계산해본 주사위를 던졌을 경우의 기대값을 함수를 통해서 구해보겠습니다.


```python
events = [1,2,3,4,5,6]
probabilities = [1/6,1/6,1/6,1/6,1/6,1/6]

get_expected_value(events, probabilities)
```




    3.5



그럼 이제 주사위를 던지를 횟수를 늘려가면서 실제로 비슷하게 나오는지 살펴보겠습니다.


```python
def get_expected_valueIn_multiple_drawing(num):
    acc = 0
    for i in range(num):
        acc += events[get_index(probabilities)]
    return acc / num
```


```python
get_expected_valueIn_multiple_drawing(100)
```




    3.42




```python
get_expected_valueIn_multiple_drawing(10000)
```




    3.4688




```python
get_expected_valueIn_multiple_drawing(100000)
```




    3.50564



#### 3. 돈이 떨어지기 전에 토스 시도 횟수는 ?

동전을 던져서 앞면이 나오면 $1를 얻고, 뒷면이 나오면 $1.5를 잃는 게임이 있습니다.
(누가봐도 불공평한 이딴 겜을 누가 할지는 모르겠습니다만... 어쨌든 하는 사람이 있다고 합시다.)
잔고가 0이 되면 게임이 끝납니다.
이 게임을 시뮬레이션하는 코드를 작성하세요.


```python
events = [1, -1.5]
probabilities = [0.5, 0.5]

def play_draw_game(balances):
    cnt = 0
    while balances > 0:
        index = get_index(probabilities)
        balances += events[index]
        cnt += 1
        print('{0:3} {1} ! Current amount: {2:.1f}'.format(cnt, 'Heads' if index == 0 else 'Tails', balances))
    
    print('Game Over ! Coin tosses {0:3} times'.format(cnt))
```


```python
play_draw_game(10)
```

      1 Tails ! Current amount: 8.5
      2 Tails ! Current amount: 7.0
      3 Tails ! Current amount: 5.5
      4 Heads ! Current amount: 6.5
      5 Tails ! Current amount: 5.0
      6 Tails ! Current amount: 3.5
      7 Tails ! Current amount: 2.0
      8 Tails ! Current amount: 0.5
      9 Heads ! Current amount: 1.5
     10 Heads ! Current amount: 2.5
     11 Tails ! Current amount: 1.0
     12 Tails ! Current amount: -0.5
    Game Over ! Coin tosses  12 times


#### 4. 카드뭉치 섞기

52장의 트럼프카드를 섞는(shuffling)하는 프로그램을 작성하세요.

먼저 파이썬 표준라이브러리의 `random` 모듈에 있는 `shuffle()`함수에 대해 살펴보겠습니다.


```python
import random
x = [1, 2, 3, 4]
random.shuffle(x)
x
```




    [4, 2, 3, 1]



트럼프에는 총 52장의 카드가 있으니 숫자 1 ~ 52를 이용해서 셔플을 한 후에 해당 숫자를 트럼프 카드와 매핑을 해주는 클래스를 이용하는 방식으로 구현해 보겠습니다.
먼저 1 ~ 52까지의 숫자를 트럼프 카드로 매핑하는 클래스를 만들어 보겠습니다.


```python
class Trump:
    suits = ['spades','diamonds','clubs','hearts']
    ranks = ['ace','two','three','four','five','six','seven','eight','nine','ten','jack','queen','king']
    
    def __init__(self, idx):
        self.suit = self.suits[idx // 13]
        self.rank = self.ranks[idx % 13]
    
    def print(self):
        print('{0} of {1}'.format(self.rank, self.suit))
```

이제 위 클래스를 이용해서 카드를 셔플해 보겠습니다.

먼저 0 ~ 52 사이의 숫자를 셔플하겠습니다.


```python
import random

cards = list(range(52))
random.shuffle(cards)

print(cards)
```

    [36, 5, 51, 37, 9, 25, 1, 33, 34, 40, 7, 43, 21, 48, 17, 50, 42, 49, 16, 15, 12, 23, 29, 27, 41, 35, 22, 4, 44, 19, 32, 13, 8, 2, 11, 39, 14, 0, 46, 10, 6, 38, 26, 24, 31, 20, 3, 28, 47, 45, 30, 18]


이 결과를 `Trump` 클래스를 이용해서 출력해 보겠습니다.


```python
trumps = [Trump(card) for card in cards]

for trump in trumps:
    trump.print()
```

    jack of clubs
    six of spades
    king of hearts
    queen of clubs
    ten of spades
    king of diamonds
    two of spades
    eight of clubs
    nine of clubs
    two of hearts
    eight of spades
    five of hearts
    nine of diamonds
    ten of hearts
    five of diamonds
    queen of hearts
    four of hearts
    jack of hearts
    four of diamonds
    three of diamonds
    king of spades
    jack of diamonds
    four of clubs
    two of clubs
    three of hearts
    ten of clubs
    ten of diamonds
    five of spades
    six of hearts
    seven of diamonds
    seven of clubs
    ace of diamonds
    nine of spades
    three of spades
    queen of spades
    ace of hearts
    two of diamonds
    ace of spades
    eight of hearts
    jack of spades
    seven of spades
    king of clubs
    ace of clubs
    queen of diamonds
    six of clubs
    eight of diamonds
    four of spades
    three of clubs
    nine of hearts
    seven of hearts
    five of clubs
    six of diamonds


#### 5. 원의 면적 추정

원의 면적은 `pi * r^2`이라는 공식이라는 것을 알고 있습니다만,
이것이 정말로 맞는지를 다른 방법으로 추정해 보고자 합니다.
한쪽면의 길이가 `2r`인 정사각형 안에 반지름 `r`인 원으로 구성된 다트보드가 있다고 생각해 봅시다.
여기에 다트를 던졌을 경우 원 안에 명중한 갯수를 `N`개라고 하고 나머지는 원 안이 아닌 정사각형 보드위에 맞췄다고 가정하겠습니다. (M)
정사각형 보드 밖으로 나가는 경우는 생각하지 않겠습니다.
이럴 경우 원안에 명중할 확률은 `f = N / (N + M)`이 됩니다.
정사각형의 면적이 `A`일 경우 `A * f`는 원의 면적과 같을 것입니다.

이것을 직접 프로그램으로 구현하여 던지는 횟수를 다르게 하여 실제 원의 면적과 얼마나 차이가 나는지를 살펴보세요.

먼저 실제 원의 면적을 구해보겠습니다.
(반지름이 2이라 가정하겠습니다.)


```python
from sympy import pi, N

r = 2
N(pi *r**2)
```




    12.5663706143592



이제 다트를 던졌을 때 원안에 맞은 확률을 구해야 합니다.
이 확률을 구하기 위해서 다트를 던지는 것의 시뮬레이션 결과 중 명중한 것을 `1`, 그렇지 않은 것을 `0`으로 하겠습니다.
그 결과에 정사각형의 면접과 곱한한 결과가 위에 계산결과와 맞는지를 비교해 보겠습니다.

원 안에 맞았다는 것을 어떻게 구현해야 할까요 ?
다트가 명중한 곳과 원의 중심간의 거리가 반지름(2)보다 작은 경우 명중했다고 생각하겠습니다.
계산상 편의를 위해 원의 중심을 `(0, 0)`으로 생각하고 좌표를 랜덤으로 생성하겠습니다. (`-2 ~ 2`)


```python
import random

def dart():
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    dist = (x*x + y*y)**0.5
    return True if dist < 2 else False

def probability_of_dart(number):
    shootings = [1 if dart() else 0 for x in range(number)]
    return sum(shootings) / number

def get_expected_of_dart(number, length):
    return probability_of_dart(number) * length * length 
```


```python
get_expected_of_dart(100, 4)
```




    11.68




```python
get_expected_of_dart(1000, 4)
```




    12.592




```python
get_expected_of_dart(10000, 4)
```




    12.6848




```python
get_expected_of_dart(100000, 4)
```




    12.56928


