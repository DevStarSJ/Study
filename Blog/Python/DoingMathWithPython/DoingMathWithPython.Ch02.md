---
title: Doing Math with Python Chapter 2 Visualizing Data with Graphs
date: 2016-07-12 00:00:00
categories:
- Python
- DoingMathWithPython
tags:
- Python
- Math
---

# Doing Math with Python (파이썬으로 풀어보는 수학)

- 원서명 : Doing Math with Python: Use Programming to Explore Algebra, Statistics, Calculus, and More! (ISBN 9781593276409)
- 지은이 : 아미트 사하(Amit Saha)
- 원서 및 관련자료 : <https://www.nostarch.com/doingmathwithpython>
- 번역서 : <http://www.acornpub.co.kr/book/doing-math-with-python>

![](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/image/cover.jpg?raw=true)

This posting is made in `.ipynb`, so the original file can be modified and executed in the **Jupiter Notebook**.
- Location : <https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython>

## Chapter 2 Visualizing Data with Graphs

#### 카르테지안 좌표평면 (Cartesian coordinate plane)
수평선 값은 x축, 수직선 값은 y축 으로 부르는 좌표 평면 (통상적으로 많이 사용하는 2차원을 표현하는 좌표계)

이번 장에서의 진행을 위해서는 `matplotlib`를 설치해야 합니다.

```
pip install matplotlib-venn
```

필자는 `Windows`에서 현재 `Jupyter notebook`로 실행을 하고 있습니다.
윈도우즈 만의 문제인지 모르겠습니다만, 버전별로 실행 결과가 다르다던지, 팝업으로 뜨면서 응답없음으로 되는 경우가 있습니다.
`2016-08-15` 일자 아침에 아나콘다 업데이트를 모두 수행하니 많은 버그들이 잡혀서 정상적으로 수행됩니다.

```
conda update --all
```

기본적으로 `jupyter notebook`에서 실행을 하면 그래프 결과가 팝업으로 실행되어서 그림으로 저장 등 다양한 기능을 사용할 수 있습니다.
실행 결과를 팝업이 아닌 `notebook`안에 삽입하고 싶은 경우에는 아래 **magic command** `%matplotlib inline`을 입력하시면 됩니다.
그리고 `seaborn`이라는 시각화 툴을 **import**해주는 것 만으로도 `matplotlib`의 그래프들이 좀 더 블링블링 해집니다.

정리해 보겠습니다.

- 그래프를 Jupyter notebook 안에 그립으로 삽입하고 싶을 때


```python
%matplotlib inline
```

- 그래프를 팝업창으로 출력하고 싶을 때


```python
%matplotlib qt
```

- 점 더 이쁘고 블링블링한 그래프로 출력하고 싶을 때


```python
import seaborn
```

### 1. 맷플롭립을 이용한 그래프 그리기

##### step 1. X,Y 좌료를 이용하여 Show()

`plot()`에 인자로 X좌표들의 List, Y좌표들의 List를 차례대로 넣으면 `matplotlib.lines.Line2D` 라는 객체가 생성됩니다.
그런 다음에 `Show()`를 실행하면 팝업으로 그래프가 출력됩니다.
`Save`버튼을 눌러서 그림으로 저장이 가능합니다.


```python
x_numbers = [ 1, 2, 3 ]
y_numbers = [ 2, 4, 5 ]

from pylab import plot, show
plot(x_numbers, y_numbers)
show()
```


![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_8_0.png)


##### step 2. Marker 표시

그래프의 각 포인터에 마커를 표시하고 싶은 경우 세번째 인자로 `marker='o'`를 넣어주면 됩니다. ( `o`, `*`, `x`, `+` 등 여러가지가 있습니다.)


```python
plot(x_numbers, y_numbers, marker='o')
show()
```


![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_10_0.png)


##### Step 3. Line 지우기

세번째 인자에 `marker=`를 지우고 표시하고픈 마커만을 입력한 경우에는 선이 없이 마커만 출력됩니다.


```python
plot(x_numbers, y_numbers, '*')
show()
```


![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_12_0.png)


##### Step 4. 뉴욕시의  연간 평균온도 표시 (X축값을 주지 않고 출력)

이제는 예제 데이터가 아닌 실제 데이터를 가지고 작성해 보겠습니다.
뉴욕시의 2000년에서 2012년까지의 평균온도(화시)를 표시해보겠습니다.


```python
nyc_temp = [ 53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3 ]
plot(nyc_temp, marker='o')
show()
```


![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_14_0.png)


Y축의 값의 경우 0에서부터 시작을 한 것이 아니라 입력된 값의 최소값(53.4)에서 최고값(57.3)을 기준으로 표시된 것을 확인 할 수 있습니다.
X축의 값을 따로 주지 않은 경우 0부터 차례대로 번호가 매겨집니다.

X축 값을 2000 ~ 2012으로 주겠습니다.


```python
years = range(2000, 2013)
plot(years, nyc_temp, marker='o')
show()
```


![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_16_0.png)


##### Step 5. 뉴욕시의 월간 온도 비교 (한 그래프에 여러개의 시리즈 출력)

3개의 연도(2000, 2006, 2012)에 대해서 12개월에 대한 평균온도를 그래프로 표시해 보겠습니다.


```python
nyc_temp_2000 = [ 31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.3 ]
nyc_temp_2006 = [ 40.0, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6 ]
nyc_temp_2012 = [ 37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5 ]

months = range(1, 13)
```


```python
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
show()
```


![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_19_0.png)


3개의 시리즈가 하나의 그래프에 출력이 되었습니다.
각 시리즈별 라인의 색상은 특별히 신경쓰지 않아도 구분이 가능하도록 자동으로 설정되어 있습니다.

##### Step 6. 범주(Legend) 출력

한 그래프에 시리즈가 여러개일 경우 각각의 시리즈가 무엇을 의미하는지 범주를 추가해 주면 좀 더 알아보기 쉽습니다.
`legend()`에 각 시리즈별 명칭을 List로 전달하면 화면에 출력됩니다. 두번째 인자로 범주가 출력될 위치를 설정할 수 있습니다. 기본적으로는 우측상단에 출력되는데 `best`로 설정할 경우에는 그래프를 보는데 방해되지 않도록 적당한 위치에 알아서 위치시켜 줍니다.


```python
from pylab import legend
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
legend([ 2000, 2006, 2012 ])
show()
```


![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_21_0.png)


범주를 넣으니 각각의 색깔별 시리즈가 무엇을 의미하는지 확인이 가능해졌습니다.
가장 온도가 높은 7월의 경우를 보니 계속해서 증가하고 있는 것을 확인할 수 있습니다.

##### Step 7. 타이틀, 레이블 추가

`title()` : 타이틀 추가
`xlabel()` : X축 레이블 추가
`ylabel()` : Y출 레이블 추가


```python
from pylab import plot,show,title,xlabel,ylabel,legend
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
legend([ 2000, 2006, 2012 ])
title('Average monthly temperature in NYC')
xlabel('Month')
ylabel('Temperature')
show()
```


![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_23_0.png)


##### Step 8. 축 조정

기본적으로 축의 값은 전체 데이터의 최소값과 최대값을 그 범위로 하였습니다.
원하는대로 축의 값을 조정하려면 `axis()`를 이용하면 됩니다.

`axis()` : 현재 설정된 값을 출력해 줍니다.
`axis(ymin = ?)` : y최소값을 원하는 값으로 설정합니다. (같은 방법으로 ymax, xmin, xmax로 가능합니다.)
`axis([xmin, xmax, ymin, ymax])` : 4개의 숫자를 가진 `List`를 인자로 전달하여 한번에 모두 변경이 가능합니다.

- 현재 `%matplotlib inline`으로 실행하시는 분들께서는 아래의 `%matplotlib qt`를 먼저 실행하신 후 진행해주세요.


```python
%matplotlib qt
```


```python
from pylab import plot, axis, show
import seaborn

plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
axis()
```




    (0.0, 12.0, 30.0, 80.0)




```python
axis(ymin = 0)
```




    (0.0, 12.0, 0, 80.0)




```python
show()
```


![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_28_0.png)


`inline` 모드로 실행하실 경우에는 주의 사항이 하나 있습니다.

- `plot` 생성과 `show()` 실행이 하나의 `cell`안에 있어야 원하는대로 그래프가 출력됩니다.

위와 같이 3개의 `cell`로 되어 있는 경우 각각의 스텝마다 출력이 된 후 `plot`이 다시 초기화가 되므로 마지막 `show()`를 호출하였을 때 아무것도 보이지 않게 됩니다.

아래와 같이 하나의 `cell`에 모두 포함하면 정상적으로 출력 됩니다.


```python
%matplotlib inline
```


```python
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
axis()
axis(ymin = 0)
show()
```


![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_31_0.png)


### 2. pyplot을 이용한 그래프 그리기

지금껏 살펴본 `pylab`의 경우 *shell*환경에서 작업하기에 적합하지만, 비교적 규모가 있는 *Application*개발에는 `pyplot`가 더 효율적 입니다. 작업방법은 `pylab`과 거의 유사합니다.


```python
%matplotlib inline
```


```python
import matplotlib.pyplot as plt

def create_graph():
    nyc_temp_2000 = [ 31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.3 ]
    nyc_temp_2006 = [ 40.0, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6 ]
    nyc_temp_2012 = [ 37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5 ]

    months = range(1, 13)
    
    plt.plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
    plt.show()

if __name__ == '__main__':
    create_graph()
```


![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_34_0.png)


`savefig('저장할 파일 경로 및 이름')` : 그래프를 그림으로 저장 (PNG, PDF,SVG등 여러가지 타입을 지원) / `pylab`, `pyplot` 모두 가능


```python
import matplotlib.pyplot as plt

def create_graph():
    nyc_temp_2000 = [ 31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.3 ]
    nyc_temp_2006 = [ 40.0, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6 ]
    nyc_temp_2012 = [ 37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5 ]

    months = range(1, 13)
    
    plt.plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
    plt.savefig('d:/fig.png')

if __name__ == '__main__':
    create_graph()
```

### 3. 수식을 이용하여 그래프 그리기

#### 3.1 뉴턴의 만유인력의 법칙

![그림 3-1. 만류인력의 법칙(수식)](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/image/DoingMathWithPython.Ch02.equation.01.png?raw=true)

질량이 `m1`인 물체와 `m2`인 물체를 `F`의 힘으로 끌어당깁니다. (`G` : 중력상수, `r` : 두 물체간의 거리)

질량이 `0.5kg`인 물체와 `1.5kg`인 물체 사이의 중력을 구해보겠습니다.
거리는 19개의 구간에 대하여 구하며 100m 에서 50미터 간격으로 증가 (즉, 100m ~ 1000m)로 하며,
중력 상수는 `6.674 * 10**-11`을 사용하겠습니다.

![그림 3-2. 중력상수(수식)](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/image/DoingMathWithPython.Ch02.equation.02.png?raw=true)


```python
import matplotlib.pyplot as plt

def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitational force in newtons')
    plt.title('Gravirarional force and distance')
    plt.show()
    
def generate_F_r():
    r = range(100, 1001, 50)
    G = 6.674 * (10**-11)
    m1 = 0.5
    m2 = 1.5
    
    F = []
    
    for dist in r:
        force = G * m1 * m2 / (dist**2)
        F.append(force)
        
    draw_graph(r, F)

if __name__ == '__main__':
    generate_F_r()
```


![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_38_0.png)


#### 3.2 포물선 운동

![그림 3-4. 포물선 운동](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/image/DoingMathWithPython.Ch02.12.jpg?raw=true)
그림출처 : [Naver지식백과 Basic 고교생을 위한 물리 용어사전 : 포물선 운동](http://terms.naver.com/entry.nhn?docId=941198&cid=47338&categoryId=47338)

한 지점에서 공을 던지게되면 포물선을 그리면서 이동하게 됩니다.
이것을 그래프로 표현하기 위해서는 포물선 운동방적식을 이용하여 공이 지면에 도달할때 까지 공의 위치를 계산해야 합니다.

공의 초기 속도를 `u`라고 하고 그때의 각도를 `θ`라고 할 경우 이 속도를 2개로 분리하여 생각할 수 있습니다.
- x 방향 : `ux = u cosθ`
- y 방향 : `uy = u sinθ`

시간이 지날수록 속도는 변하게 됩니다. 변화된 속도를 `V`로 표시하는 경우,
x축 방향으로는 계속 변하지 않고 동일한 속도가 유지되는데, y축 방향으로는 중력의 영향을 받아서 감소하게 됩니다.
- x 속도 : `Vx = u cosθ`
- y 속도 : `Vy = u singθ - gt`

이동 거리(`S`)는 `속도 x 시간`이므로 아래와 같이 표현이 가능합니다.
- x 이동거리 : `Sx = u cosθ t`
- y 이동거리 : `Sy = u sinθ t - (1/2) gt^2`

이제 포물선 운동을 표현하는데 필요한 수식은 완성이 되었습니다.
그래프로 표현하기 위해서는 그려질 영역을 어느 정도 알아야 하는데, 그러기 위해서 공이 지면에서 얼마나 오랫동안 공중에 있는지를 계산해야 합니다.
이를 위해서는 우선 공이 어느 시점에 지면에서 최고 지점에 위치하는지를 알아야 합니다.
공의 수직속도 요인 (`Vy`)가 0이 되는 시점이 됩니다.

![수식 3-3. Tpeak 수식](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/image/DoingMathWithPython.Ch02.equation.03.png?raw=true)

비행시간은 그 시간동안 다시 내려와서 지면에 닿는시간 까지이므로 2배를 해주면 됩니다.

![수식 3-4. Tflight 수식](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/image/DoingMathWithPython.Ch02.equation.04.png?raw=true)

초기 속도(`u`)를 `5m/s`로 하고 각도(`θ`)를 45도로 던진경우 대입하면 아래와 다음과 같은 수식이 됩니다. (`g = 9.8`로 가정)

![수식 3-5. Tflight 수식 예제](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/image/DoingMathWithPython.Ch02.equation.05.png?raw=true)


```python
from math import sin, radians
2 * 5 * sin(radians(45)) / 9.8
```




    0.7215375318230076



계산을 공의 체공시간이 나옵니다.
최대한 자주 계산할수록 더 정확한 결과가 나오므로 `0.001`초마다 해당 좌료를 계산해 보겠습니다.

동일 간격으로 부동소수점 숫자를 생성해야하는데, 정수 간격은 `range()`를 이용해서 바로 생성이 가능하지만, 부동소수점을 만들어주는 내장 함수가 없으므로 직접 생성해야 합니다.


```python
from matplotlib import pyplot as plt
import math

def frange(start, end, step): #부동소수점 배열 생성
    numbers = []
    while start < end:
        numbers.append(start)
        start += step
    return numbers

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')

def draw_trajectory(u, theta, interval):
    theta = radians(theta)
    g = 9.8
    
    t_flight = 2 * u * math.sin(theta) / g #체공시간
    
    intervals = frange(0, t_flight,interval)
    
    x = []
    y = []
    
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
        
    draw_graph(x,y)
    
if __name__ == '__main__':
    try:
        u = float(input('Enter the initial velocity(m/s): '))
        theta = float(input('Enter the angle of projection (degrees): '))
        interval = float(input('Enter the time intervals to draw points (s): '))
    except ValueError:
        print('You Entered an invalid input')
    else:
        draw_trajectory(u, theta, interval)
        plt.show()
```

    Enter the initial velocity(m/s): 10
    Enter the angle of projection (degrees): 45
    Enter the time intervals to draw points (s): 0.001



![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_42_1.png)


만약 서로 다른 속도로 던진 공들에 대한 궤적을 비교하고 싶으면 어떻게 해야 할까요 ?


```python
if __name__ == '__main__':
    u_list = [20, 40, 60]
    theta = 45
    interval = 0.01
    
    for u in u_list:
        draw_trajectory(u, theta, interval)
    
    plt.legend(['20','40','60'])
    plt.show()
```


![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_44_0.png)


## 프로그래밍 연습

### 1. 낮 동안 온도는 어떻게 변화하는가 ?

다른 2개의 도시에 대해서 낮 온도의변화를 표시한 그래프를 작성하세요.


```python
from matplotlib import pyplot as plt
seoul_temp = [ 24, 23, 21, 23, 25, 27, 27, 25 ]
taegu_temp = [ 23, 22, 22, 25, 27, 28, 28, 26 ]
hours = range(2, 24, 3)

plt.plot(hours,seoul_temp, hours, taegu_temp, marker='o')
plt.legend(['Seoul', 'Taegu'], loc = 2)
plt.xlabel('Hours')
plt.ylabel('Temperature')
plt.axis([0, 24, 20, 30])

plt.show()
```


![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_46_0.png)


### 2. 이차방정식을 그림으로 탐색해보기

>$y = {x}^{2} + 2x + 1$

위 방적식에서 x에 10개의 값을 대입하여 `(x,y)`를 화면에 출력하세요.
그 과정에서 해 (`y = 0 이되는 값`)를 찾고 그래프의 변동 패턴이 선형인지 비선형인지를 분석하세요.


```python
x = list(range(-5, 6))
y = list(map(lambda x : x**2 + 2*x + 1, x))
print(y)

from matplotlib import pyplot as plt
plt.plot(x, y, marker='o')
plt.show()
```

    [16, 9, 4, 1, 0, 1, 4, 9, 16, 25, 36]



![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_48_1.png)


### 3. 투척 궤적 비교 프로그램 개선

#### 3.1 속도, 투척각도를 입력받아서 체공시간, 최대 수평이동거리, 최대 수직이동거리를 계산하여 출력


```python
from math import sin, cos, radians

def get_parabolic_movement(u, theta):
    g = 9.8
    theta = radians(theta)
    durationOfFlight = 2 * u * sin(theta) / 9.8
    horizontalDistance = u * cos(theta) * durationOfFlight
    
    t = durationOfFlight / 2
    verticalDistance = u * sin(theta) * t - g / 2 * t**2
    
    return durationOfFlight, horizontalDistance, verticalDistance

if __name__ == '__main__':
    u = float(input('Input u :'))
    theta = float(input('Input theta :'))
    t, h, v = get_parabolic_movement(u, theta)
    print('Duration Of Flight : ', u, 's')
    print('The Maximum horizontal distance traveled : ', h, 'm')
    print('The Maximum vertical distance traveled : ', v, 'm')
```

    Input u :70
    Input theta :37.5
    Duration Of Flight :  70.0 s
    The Maximum horizontal distance traveled :  482.9629131445341 m
    The Maximum vertical distance traveled :  92.64761936218493 m


#### 3.2 여러개의 속도, 투척각도를 입력받아서 그래프로 출력하세요.


```python
from matplotlib import pyplot as plt
from math import sin, cos, radians

def frange(start, end, step): #부동소수점 배열 생성
    numbers = []
    while start < end:
        numbers.append(start)
        start += step
    return numbers

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')

def draw_trajectory(u, theta, interval):
    theta = radians(theta)
    g = 9.8
    
    t_flight = 2 * u * sin(theta) / g #체공시간
    
    intervals = frange(0, t_flight,interval)
    
    x = []
    y = []
    
    for t in intervals:
        x.append(u*cos(theta)*t)
        y.append(u*sin(theta)*t - 0.5*g*t*t)
        
    draw_graph(x,y)
    
if __name__ == '__main__':
    interval = 0.01
    num = int(input('How many trajectories ? '))
    u = []
    theta = []
    for i in range(1,num+1):
        ue = float(input('Enter the initial velocity for trajectory ' + str(i) + '(m/s) :'))
        te = float(input('Enter the angle of projection for trajectory ' + str(i) + '(degrees) :'))
        draw_trajectory(ue, te, interval)
    
    plt.legend(list(range(1, num+1)))
    plt.show()
```

    How many trajectories ? 4
    Enter the initial velocity for trajectory 1(m/s) :10
    Enter the angle of projection for trajectory 1(degrees) :60
    Enter the initial velocity for trajectory 2(m/s) :8
    Enter the angle of projection for trajectory 2(degrees) :45
    Enter the initial velocity for trajectory 3(m/s) :20
    Enter the angle of projection for trajectory 3(degrees) :15
    Enter the initial velocity for trajectory 4(m/s) :12
    Enter the angle of projection for trajectory 4(degrees) :70



![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_52_1.png)


#### 수평막대 차트 예제


```python
import matplotlib.pyplot as plt

def create_bar_chart(data, labels):
    num_bars = len(data)
    positions = range (1, num_bars+1)
    plt.barh(positions, data, align='center')
    plt.yticks(positions, labels)
    plt.xlabel('Steps')
    plt.ylabel('Day')
    plt.title('Number of steps walked')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    steps = [6534, 7000, 8900, 10786, 3467, 11045, 5059]
    labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    create_bar_chart(steps, labels)
```


![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_54_0.png)


#### 4. 비용 가시화

각 항목별 사용금액을 입력받아서 막대차트로 표시하세요.


```python
import matplotlib.pyplot as plt

def create_bar_chart(amounts, labels):
    num_bars = len(amounts)
    positions = range (1, num_bars+1)
    plt.barh(positions, amounts, align='center')
    plt.yticks(positions, labels)
    plt.xlabel('Amount')
    plt.ylabel('Categories')
    plt.title('Weekly expenditures')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    num = int(input('Enter the number of categories : '))
    
    amounts = []
    labels = []
    for i in range(0,num):
        labels.append(input('Enter category : '))
        amounts.append(int(input('Expenditure : ')))
        
    create_bar_chart(amounts, labels)
```

    Enter the number of categories : 4
    Enter category : Food
    Expenditure : 70
    Enter category : Entertainment
    Expenditure : 50
    Enter category : Movement
    Expenditure : 30
    Enter category : Development
    Expenditure : 100



![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_56_1.png)


#### 5. 피보나치 순열과 황금비 간의 관계 탐색

피보나치 순열은 수치적으로 황금비(1.61803398...)을 가진 숫자의 집합입니다.
100개의 피보나치 숫자 간의 비를 그래프상에 그리세요.


```python
import matplotlib.pyplot as plt

def fibonacci_series(n):
    series = []
    current = 1
    if n < 1:
        return series
    else:
        series.append(1)
    
    if n >= 2:
        series.append(1)
    
    if n > 2:
        for i in range(2,n):
            current = series[i-1] + series[i-2]
            series.append(current)
            
    return series

def ratio_of_front(series):
    ratio = []
    for i in range(1,len(series)):
        ratio.append(series[i] / series[i-1])
    return ratio

def draw_graph(series):
    plt.plot(series)
    plt.ylabel('Ratio')
    plt.title('Ratio between consecutive Fibonacci numbers')
    plt.show()
    
if __name__ == '__main__':
    draw_graph(ratio_of_front(fibonacci_series(100)))          
```


![png](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/DoingMathWithPython/md_files/DoingMathWithPython.Ch02_58_0.png)

