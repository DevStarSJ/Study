
# 파이썬으로 풀어보는 수학

- 원서명 : Doing Math with Python: Use Programming to Explore Algebra, Statistics, Calculus, and More! (ISBN 9781593276409)
- 지은이 : 아미트 사하(Amit Saha)
- 원서 및 관련자료 : <https://www.nostarch.com/doingmathwithpython>
- 번역서 : <http://www.acornpub.co.kr/book/doing-math-with-python>

![책표지](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/image/cover.jpg?raw=true)

이 포스팅은 ipynb 로 제작되어 있으므로 원본 파일을 Jupyter notebook 에서 수정 및 실행이 가능합니다.
- 원본파일 : <https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/DoingMathWithPython.Ch01.ipynb>

## 1장 숫자, 연산

### 1. 사칙연산

#### 1.1 기본연산 (더하기, 빼기, 곱하기)


```python
1 + 2
```




    3




```python
-1 + 3.5
```




    2.5




```python
100 - 45
```




    55




```python
3 * 2
```




    6




```python
3.5 * 1.5
```




    5.25




```python
3 / 2
```




    1.5




```python
4 / 2
```




    2.0



#### 1.2 나누기 ( 나누기, 나머지), 지수


```python
3 / 2
```




    1.5




```python
4 / 2
```




    2.0




```python
3 // 2 # 버림 나눗셈 : 소숫점 아래를 내림
```




    1




```python
-3 // 2 # 음수인 경우 원래 답보다 작거나 같은 값이므로 -1.5 -> -2.0이 됨
```




    -2




```python
9 % 2 # 나머지
```




    1




```python
2 ** 2 # 2의 2승
```




    4




```python
2 ** 10
```




    1024




```python
2 ** (0.5) # 2의 1/2 승이니 Root 2와 같음
```




    1.4142135623730951




```python
8 ** (1/3) # 8의 세재곱근
```




    2.0



### 2. 분수 (Fraction)

사용하기 위해서는 `fractions` 모듈에서 `Fraction` class를 임포트해야 합니다.

`Fraction(분자 , 분모)`의 형태로 입력합니다.


```python
from fractions import Fraction
f = Fraction(3, 4)
f
```




    Fraction(3, 4)




```python
Fraction(3,4) + 1 + 1.5
```




    3.25



### 3. 복소수 (Complex numbers)

문자 `j` 또는 `J`를 이용해서 허수부를 입력할 수 있습니다.


```python
c = 2 + 3j
type(c)
```




    complex



`complex` 객체를 이용해서도 가능합니다.


```python
c = complex(2,3)
c
```




    (2+3j)



`complex` 의 사칙연산입니다. ( 나머지 `%` 와 버림 `//`은 제공하지 않습니다. )


```python
b = 3 + 3j
b + c
```




    (5+6j)




```python
b - c
```




    (1+0j)




```python
b * c
```




    (-3+15j)



#### 복소수의 곱셈

$$
(a + bj) \times (c + dj) 
= ac + adj + bcj - bd 
= (ac - bd) + (bc + ad)j
$$

>$$(2 + 3j) \times (3 + 3j) = (6 - 9) + (6 + 9)j = -3 + 15j$$


```python
b / c
```




    (1.153846153846154-0.23076923076923078j)



#### 복소수의 나눗셈

$$ \frac {a + bj}{c + dj} 
= \frac {((a +bj)(c - dj))}{((c + dj)( c - dj))} 
= \frac{((ac + bd) + (bc - ad)j)}{({c}^{2} + {d}^{2}) + (cd - cd)j} 
= \frac{((ac + bd) + (bc - ad)j)}{{c}^{2} + {d}^{2}}
$$

>$$\frac{3 +3j}{2 + 3j} = \frac{6 + 9}{4 + 9} + (\frac{6 - 9}{4 + 9} ) j = \frac{15}{13} - \frac{3}{13}j$$

#### 컬레복소수(conjugate)
같은 실수부에 허수부의 부호가 반대인 경우를 말합니다.
바로 앞에서 본 것처럼 나누기 할때 분모의 컬레복소수를 분모 분자에 모두 곱해서 계산을 했습니다.


```python
c.conjugate()
```




    (2-3j)



#### 복소수의 값(magnitude)
절대치`abs() 함수`를 이용해서 구할수 있습니다.


```python
abs(c)
```




    3.605551275463989



계산 공식은 `(실수부의 제곱 + 허수부의 제곱)의 제곱근(루트)` 입니다.


```python
(c.real ** 2 + c.imag ** 2) ** 0.5
```




    3.605551275463989



### 4. 정수 팩터 계산
0이 아닌 정수 a를 다른 정수 b로 나누었을 때 나머지가 0인 경우 a는 b의 `팩터(Factor)`라 합니다.


```python
def is_factor(a, b):
    if a % b == 0:
        return True
    else:
        return False

if __name__ == '__main__':

    while True:
        a = input('Input a : ')
        a = float(a)
        if a.is_integer() and a > 0:
            break
        print('Please enter a positive integer for a')

    while True:
        b = input('Input b : ')
        b = float(b)
        if b.is_integer() and b > 0:
            break
        print('Please enter a positive integer for b')

    print(is_factor(a,b))        
```

    Input a : 8
    Input b : 2
    True


특정 정수에 대한 모든 팩터를 구하기 위해서는 어떻게 해야 할까요 ?
그 수보다 작은 모든 양의 정수에 대해서 검사를 하면 됩니다.


```python
def is_factor(a, b):
    if a % b == 0:
        return True
    else:
        return False

def factors(value):
    result = []
    for i in range (1, value + 1):
        if is_factor(value, i):
            result.append(i)
    return result

if __name__ == '__main__':
    
    while True:
        a = input('input a : ')
        a = float(a)
        if a.is_integer() and a > 0:
            a = int(a)
            break;
        print('Please enter a positive integer for a')
    
    print(factors(a))

```

    input a : 16
    [1, 2, 4, 8, 16]


### 5. 측정 단위 변환

#### 센티미터 to 인치
1인치는 `2.54`센티미터입니다.


```python
37.5 * 2.54
```




    95.25



#### 마일 to 킬로미터
1마일은 `1.609`킬로미터와 같습니다.


```python
320 * 1.609
```




    514.88



#### 화씨 to 섭씨
```
C = (F - 32) * 5 / 9
```


```python
F = 98.6
(F - 32) * 5 / 9
```




    37.0



반대로는 위 수식의 역수를 취하면 됩니다.
```
F = C * 9 / 5 + 32
```


```python
C = 37
C * 9 / 5 + 32
```




    98.6



### 6. 이차방정식 근 구하기

${ax}^{2} + bx + c$라는 식에 대한 x의 근은 다음과 같이 2개가 존재합니다.

$$
x = \frac{- b \pm \sqrt{{b}^{2} - 4ac}}{2a}
$$


```python
def roots(a, b, c):
    D = ( b ** 2 - 4 * a * c ) ** 0.5
    result = [ (-b + D) / (2 * a) , (-b - D) / (2 * a) ]
    return result

if __name__ == '__main__':
    a = float(input('Enter a :'))
    b = float(input('Enter b :'))
    c = float(input('Enter c :'))
    rootList = roots(a, b, c)
    
    for i in rootList:
        print('{0:.2f}'.format(i))
```

    Enter a :1
    Enter b :2
    Enter c :1
    -1.00
    -1.00


## 프로그래밍 연습

### 1. 짝수,홀수 자판기

- 입력한 숫자가 `짝수`인지 `홀수`인지 출력합니다.
- 입력한 숫자 다음으로 오는 `짝수` 또는 `홀수`를 같이 출력합니다.
- `is_integer()`를 이용하여 유효하지 않은 입력에 대해서는 오류 메세지를 출력하세요.


```python
def is_odd(val):
    if val % 2 == 0:
        return False
    else:
        return True

if __name__ == '__main__':
    try:
        inputNum = float(input('Enter number: '))
    except:
        print('You must input number')
    if inputNum.is_integer():
        val = int(inputNum)
        print(val, 'is','odd' if is_odd(val) else 'even', ':')
        seq = list(range(val, val + 20, 2))
        print(seq)
    else:
        print('You input invalid number')
```

    Enter number: 2
    2 is even :
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


### 2. 개선된 곱 테이블

X 단을 Y 개까지 출력하는 방식으로 구현하세요.


```python
try:
    val = int(input('Enter start number :'))
    num = int(input('Enter number of step :'))
except:
    print('Invalid number entered')

for i in range(1, num + 1):
    print(val, '*', i, '=', val * i)
```

    Enter start number :9
    Enter number of step :15
    9 * 1 = 9
    9 * 2 = 18
    9 * 3 = 27
    9 * 4 = 36
    9 * 5 = 45
    9 * 6 = 54
    9 * 7 = 63
    9 * 8 = 72
    9 * 9 = 81
    9 * 10 = 90
    9 * 11 = 99
    9 * 12 = 108
    9 * 13 = 117
    9 * 14 = 126
    9 * 15 = 135


### 3. 개선된 단위 변환

아래 변환이 모두 가능한 프로그램을 작성하세요.
- 거리(킬로미터 <-> 마일)
- 무게(킬로그램 <-> 파운드)
- 온도(섭씨 <-> 화시)


```python
def km_to_mile(km):
    return km / 1.609

def mile_to_km(mile):
    return mile * 1.609

def kg_to_pound(kg):
    return kg * 2.20462

def pound_to_kg(pound):
    return pound / 2.20462

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

if __name__ == '__main__':
    try:
        order = int(input('Enter command (1.KM To Mile, 2.Mile To KM, 3.KG To Pound, 4.Pound To KG, 5.Celsius To Fahrenheit, 6.Fahrenheit To Celsius) : '))
        val = float(input('Enter value : '))
    except:
        print('Invalid command')

    task = [km_to_mile, mile_to_km, kg_to_pound, pound_to_kg, celsius_to_fahrenheit, fahrenheit_to_celsius]
    result = task[order-1](val)
    print('Result : ', result)
```

    Enter command (1.KM To Mile, 2.Mile To KM, 3.KG To Pound, 4.Pound To KG, 5.Celsius To Fahrenheit, 6.Fahrenheit To Celsius) : 5
    Enter value : 46.5
    Result :  115.7


### 4. 분수계산기
2개의 분수를 입력받아서, 4칙연산을 수행하는 프로그램을 작성하세요.


```python
from fractions import Fraction

a = Fraction(input('Enter first fraction : '))
b = Fraction(input('Enter second fraction : '))
op = input('Operation to perform - [A]dd, [S]ubtract, [D]ivide, [M]ultiply : ')

cmd = op.lower()[0]

if cmd == 'a':
    print(a, '+', b, '=', a + b)
elif cmd == 's':
    print(a, '-', b, '=', a - b)
elif cmd == 'd':
    print(a, '/', b, '=', a / b)
elif cmd == 'm':
    print(a, '*', b, '=', a * b)
else:
    print('Invalid Operation')
```

    Enter first fraction : 3/4
    Enter second fraction : 2/6
    Operation to perform - [A]dd, [S]ubtract, [D]ivide, [M]ultiply : M
    3/4 * 1/3 = 1/4

