#Problem Solving with Algorithm and Data Structures with Python

원서 : <http://interactivepython.org/runestone/static/pythonds/index.html>

## Chapter 01 Introduction

### 1.1 Objectives

### 1.2 Getting Started

### 1.3 What is Computer Science ?

`Computer Science`는 컴퓨터에 대해서 배우는 학문이 아니라 문제와 그 문제의 풀이방법에 대한 학문이다.
(하지만 이게 전부가 아니라고 뒤에서 말한다.)
여기에서 문제 풀이 방법을 우리는 `Algorithm`이라 부른다.
하지만 모든 문제가 다 컴퓨터로 쉽게 풀리지는 않는다.
컴퓨터로 해결가능한 알고리즘이 존재하는 문제들을 `Computerable`하다라고 한다.

`CS`는 또한 `Abstract`에 대한 학문이다.
여기에서 말하는 추상화의 의미는 알고리즘(문제를 푸는 과정)을 논리적이나 물리적 관점에서 분리하는 것이다.

`procedural abstraction`에서의 의미는 이것과 약간 다르다. 이말은 함수의 추상화를 의미하는데 그 뜻은 함수 내부에서 어떻게 구현되어 있는지에 대해서 몰라도 해당 함수를 호출해서 사용할 수 있다는 것을 의미한다.

```Python
import math
math.sqrt(16)
```

### 1.4 What is Programming ?

`Programming`은 알고리즘을 컴퓨터가 실행가능한 형태로 규칙에 맞게 작성하는 것이다.

### 1.5 Why Study Data Structures and Abstract Data Types ?

![image](image/01.01.adt.png)

사용자(개발자)는 `interface`에 대한 정보만 있으면 해당 기능을 사용할 수 있다.
내부적으로 어떻게 구현되어 있는지에 대해서는 알지 못하더라도 상관없다.
오히려 외부적으로 오픈해서 사용자가 수정가능하도록 하는게 잘못된 동작을 유발할 수 있는 경우도 생길 수 있으며,
사용자 입장에서도 굳이 신경안써도 되는 데이터에 대해서 열려 있으면 사용이 더 불편할 수 있다.
이렇게 추상화하는 과정을 `encapsulation`이라 부른다.
같은 말이지만 데이터나 기능을 외부에서 못보도록 숨긴다고 해서 `information hiding`이라고도 한다.

`Data Structure`란 실질적으로 데이터가 어떻게 저장되어 있는지, 어떻게 동작하는지에 대해서 사용자로부터 숨긴체 사용자가 편리하게 사용가능한 인터페이스만을 제공하는 형태를 뜻한다.

### 1.6 Why Study Algorithms ?

문제와 그 해법을 알고리즘이라 부른다.
그것들을 미리 익혀두면 다른 문제를 해결하고자 할때 그 해법들을 쉽게 찾을 수 있다.
그리고 알고리즘이 없는 문제(현실적인 시간내에 풀이가 불가능한 문제)를 좀 더 쉽게 찾을 수 있다.

### 1.7 Review of Basic Python

### 1.8 Getting Started with Data

Python은 `Object-Oriented Programming`을 지원한다.
OOP란 문제를 Object기반으로 해결하는 방법을 뜻한다.
Object는 `class`로 생성한 각각의 객체를 의미한다.
`class`란 관련있는 값(attribute)와 연산(behavior/method)들을 모아서 정의한 것이다.

#### 1.8.1 Built-in Atomic Data Types

##### 1.8.1.1 Numeric Types
  - `int` : 정수형
  - `float` : 부동소수점
  - 기본산술 연산 : + , - , * , / , ** (exponentiation) , % (remainder/modulo) , // (integer division)

```Python
print(2+3*4)
print((2+3)*4)
print(2**10)
print(6/3)
print(7/3)
print(7//3)
print(7%3)
print(3/6)
print(3//6)
print(3%6)
print(2**100)
```
```
14
20
1024
2.0
2.33333333333
2
1
0.5
0
3
1267650600228229401496703205376
```

##### 1.8.1.2 Boolean Type

- Python `bool` class
- value : `True` or `False`
- operator : `and`, `or` and `not`
- comparison operators
  - < : less than
  - > : greater than
  - <= : less than or equal
  - >= : greater than or equal
  - == : equal
  - != : not equal
  - and : logical and
  - or : logical or
  - not : logical not

```Python
print(5==10)
print(10 > 5)
print((5 >= 1) and (5 <= 10))
```
```
False
True
True
```

##### 1.8.1.3 Identifiers (Variables)

- 초기화없는 선언은 허용하지 않음
- 선언시 대입되는 값의 타입을 추론하여 해당 변수의 타입을 결정
- 결정된 타입은 언제든지 다른 타입으로 변경이 가능 (다른 타입의 값을 대입하면 됨)

![image](image/01.02.assignment2.png)

#### 1.8.2 Built-in Collection Data Types

##### list

- ordered collection of Python objects
- empty list : ``
- mutable

```Python
myList = [1,3,True,6.5]
```

- operations
  - [] : indexing
  - + : concatenation
  - * : repetition
  - in : contains
  - len : length
  - [:] : slicing

```Python
myList = [1,2,3,4]
A = [myList]*3
print(A)
myList[2]=45
print(A)
```
```
[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
[[1, 2, 45, 4], [1, 2, 45, 4], [1, 2, 45, 4]]
```

- methods
  - append(item) : Add a new item to the end of a list
  - insert(n, item) : Insert an item at the nth position in a list
  - pop(n = last) : Removes and returns the nth item in a list
  - sort() : Modifies a list to be sorted
  - reverse() : Modifies a list to be in reverse order
  - del (del alist[n]) : Deletes the item in the nth position
  - index(item) : Returns the index of first occurrence of item
  - count(item) : Returns the number of occurrences of item
  - remove(item) : Removes the first occurrence of item

##### String

- sequential collections of letters
- using single or double quotation marks
- immutable

```Python
myName = 'SeokJoon.Yun'
```

##### Tuple

- immutable list
- using ( )

```Python
myTuple = (2,True,4.96)
```

##### Set

- unordered collection of non-duplicate immutable Python objects
- empty set : `set()`

```Python
mySet = {3,6,"cat",4.5,False, 5,6}
print(mySet)
```
```
{False, 4.5, 3, 5, 6, 'cat'}
```

##### Dictionary

- associated pairs of a key and a value
- empty dictionary : {}

```Python
capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
```

### 1.9 Input and Output

- Input from Keyboard : `input`

```Python
aName = input('Please enter your name: ')
```

- Output to Display : `print`

```Python
print(aName)
```

#### 1.9.1 String Formatting

```Python
print('My', 'age', 'is', 19, 'years old.')
```
```
My age is 19 years old.
```

- Formatted String (old style)

```Python
print('%s age is %d years old.' % ('My', 19 ))
```

- New Style String Format

<https://pyformat.info>

```Python
print('{} age is {} years old.'.format('My', 19))

print('{1} age is {0} years old.'.format(19, 'My'))
```

### 1.10. Control Structures

#### Iteration

- `while`

```Python
counter = 1
while counter <= 5:
    print('Hello World')
    counter += 1
```
```
Hello World
Hello World
Hello World
Hello World
Hello World
```

- `for`
```Python
for item in [1,3,6,2,5]:
    print(item)
```
```
1
3
6
2
5
```

#### Selection Statements

- `if`

```Python
if score >= 90:
   print('A')
elif score >=80:
   print('B')
elif score >= 70:
   print('C')
elif score >= 60:
   print('D')
else:
   print('F')
```

### 1.11. Exception Handling

- `Exception` : runtime에 발생하는 예상치 못한 오류

```Python
n = -1
try:
    if n < 0:
        raise RuntimeError('Negative Value')
except:
    print('Negative Value')
```

### 1.12. Defining Functions

- `def` 키워드를 이용해서 정의
- `return`을 해주지 않으면 `None`을 반환

```Python
def square(n):
   return n**2
```

### 1.13. Object-Oriented Programming in Python: Defining Classes

OOP의 핵심은 사용자가 자신만의 class를 만들수 있다는 점이다.
이렇게 만든 클래스를 이용해서 문제를 푸는데 활용할 수 있다.

#### 1.13.1 A `Fraction` Class

- `Magic Method` : `__add__`와 같이 2개의 언더바로 시작과 끝이 나는 모양의 메서드. 파이썬에서 연산자나 기타 기본 함수 실행시 각각의 클래스에 미리 정의해 놓은 스페셜 메서드를 찾아서 실행시킨다.

<http://www.rafekettler.com/magicmethods.html>

```Python
# The Greatest Common Divisor
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn

    return n

class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, '/', self.den)

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)

        return Fraction(newnum//common, newden//common)

    def __eq__(self other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum
```

#### 1.13.2 Inheritance : Logic Gates and Circuits

- `상속(Inheritance)`
  - `superclass`의 특성을 모두 가지면서 추가적인 특성 (또는 일부 변경한 특성)을 가지는 `subclass`를 생성.
  -  `IS-A Relationship` : 상속은 IS-A 관계에 있는 것에 사용해야 한다. *list* is a *sequential collection**. 이므로 상속관계로 나타낼수 있다.
    - `HAS-A Relationship` : 포함하는 관계에 대해서는 상속보다는 `위임(Delegation)`으로 그 관계를 표현하는게 좋다. *Car* has a *Engine*. 이라고 해서 *Engine* 을 상속받아서 *Car* 를 구현하는 것 보다는 *Car* 내부에 *Engine* 객체를 두고 사용하는게 더 좋다.

```Python
class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.out
```

`performGateLogic` 함수는 아직 구현하지 않았다.
세부적인 구현에 대해서 부모 클래스에서는 모른다.
부모 클래스에서는 단지 해당 함수를 이용해서 output을 구한다는 것만 명시해주고, 해당 기능에 대한 구현은 실제로 동작하는 클레스에게 그 책임을 넘긴다.
(다른 언어에서는 모든 구현이 완료되지 않은 클래스를 `abstract class`라 부르며, 여기에서 사용하는 메서드에 대한 선언을 반드시 해주어야 한다.)

```Python
class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate" + self.getLabel() + "-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate" + self.getLabel() + "-->"))

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
               raise RuntimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)
        #super(UnaryGate, self).__init__(n)
        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate" + self.getLabel() + "-->"))
```

```Python
class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0
```


```Python
class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate
```
