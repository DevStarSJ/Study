---
layout: post
title: "Chapter 3 Object Orientation in TypeScript"
subtitle:  
categories: development
tags: javascript
comments: true
---

# Chapter 3 Object Orientation in TypeScript

>소프트웨어를 디자인하는 방법 2가지가 있습니다.
하나는 간단하게 만들어서 명백하게 결함을 없게하는 것이고,
다른 방법은 복잡하게 만들어서 병백한 결함을 없게하는 것입니다.
전자가 조금 더 어렵습니다. 그것은 마치 복잡한 자연의 섭리와 같은 기술, 헌신, 통찰력, 영감 등을 요구합니다.
> - Tony Hoare

객체지향 프로그래밍은 현실 세계와 유사하게 데이터와 관련된 행위를 코드로 표현합니다.
이것을 보통 변수(property)와 함수(method)를 포함하는 클래스(class)로 표현하고 있으며,
해당 클래스로부터 객체(object)를 생성합니다.

<https://en.wikipedia.org/wiki/Object-oriented_programming>

<https://ko.wikipedia.org/wiki/객체_지향_프로그래밍>


## Obejct Orientation in TypeScript

타입스크립트는 다양한 OOP 개념들을 지원하고 있습니다.

- 클래스(Classes)
- 객체(Instance of classes)
- 함수(Methods)
- 상속(Inheritance) : <https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)>
- 열린 재귀(Open recursion) : <https://en.wikipedia.org/wiki/This_(computer_programming)#Open_recursion>
- 캡슐화(Encapsulation) : <https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)>
- 위임(Delegation) : <https://en.wikipedia.org/wiki/Delegation_(computing)>
- 다형성(Polymophism) : <https://en.wikipedia.org/wiki/Polymorphism_(computer_science)>

Classes, Instace of classes, Methods, Inheritacne는 Chapter.01에서 이미 살펴보았습니다.

## 열린 재귀(Open Recursion)

**열린 재귀**란 재귀의 조합과 늦은 바인딩입니다.
클래스 내에서 메서드가 자기자신을 호출한 경우, 서브클래스에 정의된 함수를 호출 할 수도 있습니다.
그냥 함수 **override**를 설명하는 개념인 것 같습니다.
*List 3-1*은 디렉토리의 내용을 읽는 클레스입니다.
`FileReader` 클래스는 입력받은 경로에서 내용들을 읽습니다.
모든 파일은 파일트리에 추가되지만, 디렉토리에 대해서는 `this.getFiles`를 재귀적으로 호출합니다.
이러한 재귀호출은 모든 하위 경로내의 파일들을 추가할때 까지 계속됩니다.
`fs.readdirSync`와 `fs.statSync` 메서드는 **NodeJS**에 있는 것 입니다.

#### List 3-1 Open Recursion
```TypeScript
interface FileItem {
	path: string;
	contents: string[];
}

class FileReader {
	getFiles(path: string, depth: number = 0) {
		var fileTree = [];
		var files = fs.readdirSync(path);
		
		for (var i = 0; i < files.length; i++) {
			var file = files[i];
			var stats = fs.statSync(file);
			var fileItem;
			if (stats.isDirectory()) {
				// Add directory and contents
				fileItem = {
					path: file,
					contents: this.getFiles(file, (depth + 1))
				};
			} else {
				// Add file
				fileItem = {
					path: file,
					contents: []
				};
			}
			fileTree.push(fileItem);
		}
		
		return fileTree;
	}
}

class LimitedFileReader extends FileReader {
	
	constructor(public maxDepth: number) {
		super();
	}
	
	getFiles(path: string, depth = 0) {
		if (depth > this.maxDepth) {
			return [];
		}
		return super.getFiles(path, depth);
	}
}

// instatiating an instance of LimitedFileReader
var fileReader = new LimitedFileReader(1);

// results in only the top level, and one additional level being read
var files = fileReader.getFiles('path');
```

예제에서는 간단한 *Sync* 함수를 사용했지만,
실제로 구현할때에는 `readdir`, `stat`와 같이 콜백함수를 사용하는 것이 좋습니다.

`LimitedFileReader`는 `FieReader`의 서브클레스입니다.
`LimitedFileReader`의 객체를 생성할 때 클레스에 표시되는 파일 트리의 깊이를 지정해야 합니다.
이 예제에서는 `this.getFiles`를 **열린재귀**로 어떻게 호출하는가를 보여줍니다.
`FileReader`로 객체를 생성한 경우 `this.getFiles`는 단순한 일반적인 재귀호출이 됩니다만,
`LimitedFileReader`로 인스턴스를 생성한 경우 `FileReader.getFiles` 메서드 내에서 `thid.getFiles`는 `LimitedFileReader.getFiles`를 호출하게 됩니다.

**열린재귀**는 부모클래스를 변경하지 할 필요도 없고, 서브클래스에 대한 사항을 몰라도 된다는 점입니다.
서브클래스는 부모클래스의 코드를 재사용하기 위해서 코드를 중복적으로 작성할 필요가 없습니다.

## 캡슐화(Encapsulation)

*타입스크립트*는 **캡슐화**를 완벽히 지원합니다.
클래스 객체는 변수과 함수를 가지고 있으며, `private` 제한자를 이용해 외부로부터 숨길 수 있습니다.
**캡슐화**란 데이터를 숨겨서 외부에서 해당 데이터에 대한 접근을 방지하는 것을 말합니다.

`List 3-2`의 예를 보면 `Totalizer` 클래스의 경우 `private`으로 `total` 변수를 가지고 있어서 외부에서는 수정을 할 수 없습니다.
수정하기 위해서는 클래스내에 선언된 함수 호출로 가능합니다.
이런 점은 다음의 위험을 제거합니다.

- `taxRebate`를 추가하지 않으면서 `amount`를 추가하는 외부 코드
- `amount`가 0보다 크지 않은 경우
- 코드 여러곳에서 호출되는 `taxRebate` 계산
- 코드 여러곳에 나타는 `taxRateFactor`

#### List 3-2 Encapsulation
```TypeScript
class Totalizer {
    private total = 0;
    private taxRateFactor = 0.2;

    addDonation(amount: number) {
        if (amount <= 0) {
            throw new Error('Donation exception');
        }
        var taxRebate = amount * this.taxRateFactor;
        var totalDonation = amount + taxRebate;
        this.total += totalDonation;
    }

    getAmountRaised() {
        return this.total;
    }
}

var totalizer = new Totalizer();
totalizer.addDonation(100.00);

var fundsRaised = totalizer.getAmountRaised();

// 120
console.log(fundsRaised);
```

**캡슐화**를 하면 프로그램상에서 중복 코드를 예방할 수 있는 도구로 보여지지만 사실상 그렇지 않습니다.
`private` 키워드를 사용하여 외부에서 값을 수정하는 것을 방지할 수 있습니다.
복제의 가장 일반적인 경우는 논리적 분리입니다.
예를 들어서 `if`나 `switch` 문의 경우 `private`에 숨겨진 요소를 바탕으로 프로그램을 제어 할 수 있습니다.
요소를 변경할 경우 이러한 논리적 분리 상에 있는 모든 코드들을 다 살펴봐야 할 필요가 있습니다.

## 위임 (Delegation)

프로그램 재사용 측면에서 가장 중요한 개념중 하나는 바로 **위임**입니다.
레퍼(Wrapper) 클래스가 위임한 클래스를 호출하기 위해 인자로 키워드를 전달해야하는 경우 위임한 클레스는 래퍼클레스의 메서드를 호출 할 수 있습니다.

이것은 레퍼와 위임한 클래스가 서브클레스와 부모클레스로 동작하는것을 가능하게 합니다.
레퍼가 자기자신에게 참조를 전달하지 못할 경우, 해당 작업은 위임보다는 전달(Forwarding)로 알려져 있습니다.
위임과 전달에서는 클래스의 함수를 호출할 수 있지만, 해당 클래스는 그것을 다른 클래스로 넘겨줍니다.
Listing 3-3이 거기에 대한 예제입니다.

위임과 전달은 두 클래스간의 관계가 `ia a` 테스트에 실패하여 상속이 안되는 경우 좋은 대안입니다.

#### Listing 3-3. Delegation
```TypeScript
interface ControlPanel {
    startAlarm(message: string): any;
}

interface Sensor {
    check(): any;
}

class MasterControlPanel {
    private sensors: Sensor[] = [];
    constructor() {
        // Instantiating the delegate HeatSensor
        this.sensors.push(new HeatSensor(this));
    }

    start() {
        for (var i= 0; i < this.sensors.length; i++) {
            // Calling the delegate
            this.sensors[i].check();
        }
        window.setTimeout(() => this.start(), 1000);
    }

    startAlarm(message: string) {
        console.log('Alarm! ' + message);
    }
}

class HeatSensor {
    private upperLimit = 38;
    private sensor =  {
        read: function() { return Math.floor(Math.random() * 100); }
    };

    constructor(private controlPanel: ControlPanel) {
    }

    check() {
        if (this.sensor.read() > this.upperLimit) {
            // Calling back to the wrapper
            this.controlPanel.startAlarm('Overheating!');
        }
    }
}

var cp = new MasterControlPanel();
cp.start();
```

List 3-3은 위임의 간단한 예제입니다.
`HeatSensor`의 생성자로 `ControlPanel` 객체를 전달합니다.
`HeatSensor` 클레스가 `ControlPanel`의 `startAlarm` 메서드를 필요할때 호출할 수 있습니다.

`ControlPanel`은 센서들의 갯수를 조정할수 있으며,
각각의 센서는 `ControlPanel`에 콜백을 통해서 문제가 발생했을때 경보를 알릴수 있습니다.

그림 3-1은 다양한 자동차 구성 요소 사이의 관계를 설명합니다.

새시는 자동차에 내장된 일반 골격입니다.
엔진, 구동샤프트, 트랜스미션이 섀시에 장착될 때, 그 결합을 롤링 섀시라고 합니다.

#### 그림 3-1 캡슐화와 상속
<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Front-end/TypeScript/image/TypeScript.03.01.png?raw=true">

## 다형성(Polymorphism)

**다형성**이란 하나의 시그너쳐를 여러가지 다른 형태로 구현하는 능력을 말합니다.
*타입스크립트*에서 **다형성**은 여러가지 다른 형태로 가능합니다.

- 많은 클래스에 의해 구현된 인터페이스
- 많은 개체에 의해 구현된 인터페이스
- 많은 함수에 의해 구현된 인터페이스
- 여러 서브 클래스를 가진 슈퍼 클래스
- 유사한 스트럭쳐를 많이 가진 스트럭쳐

리스트 중 마지막 부분에 보면 *"유사한 스트럭쳐를 많이 가진 스트럭쳐"*란 형태가 같은 *타입스크립트 스트럭쳐 타입*을 말합니다.

#### Listing 3-4. Polymorphism
```TypeScript
interface Vehicle {
    moveTo(x: number, y: number);
}

class Car implements Vehicle {
    moveTo(x: number, y: number) {
        console.log('Driving to ' + x + ' ' + y);
    }
}

class SportsCar extends Car {
}

class Airplane {
    moveTo(x: number, y: number) {
        console.log('Flying to ' + x + ' ' + y);
    }
}

function navigate(vehicle: Vehicle) {
    vehicle.moveTo(59.9436499, 10.7167959);
}

var airplane = new Airplane();
navigate(airplane);
var car = new SportsCar();
navigate(car);
```

`navigate`함수는 `Vehicle`인터페이스와 호환되는 어떤 타입이라도 다 받아들입니다.
2개의 `number`타입을 인수로 받는 `moveTo` 메서드를 가진 어떠한 클래스나 객체라도 다 가능합니다.

예제의 모든 타입은 `Vehicle`의 정의와 호환됩니다.
`Car`는 명시적으로 인터페이스를 구현한 것이며,
`SportsCar`는 `Car`를 상속받았으므로 `Vehicle`인터페이스를 구현하였습니다.
`Airplane`는 명시적으로 `Vehicle` 인터페이스를 구현하지 않았지만, `moveTo` 메서드 가지고 있으므로 `navigate` 함수에 호환됩니다.

## SOLID Principles

<https://en.wikipedia.org/wiki/SOLID_(object-oriented_design)>

#### 1. 단일 책임 원칙 (Single responsibility priciple)
클레스는 오직 한 가지 작업만 수행하며, 단 한 가지 이유에 의해서만 변경되는 코드를 작성하도록 권장하는 원칙이다.

#### 2. 개방/폐쇄 원칙 (Open/closed principle)
클래스 내부를 수정하지 않고서도 확장할 수 있어야 한다. (여기에 대해서는 사람마다 해석하는 방법이 다르다.)
- 확장에 대한 개방 : 새로운 요구 사항 발생시 추가가 가능해야 한다. 
- 수정에 대한 폐쇄 : 수정될때 그 결과 인해 모듈의 소스 혹은 바이너리 코드가 변경되어서는 안된다.

#### 3. 리스코프 치환 원칙 (Liskov substitution principle)
슈퍼 클래스가 사용되는 곳에 서브 클래스로 치환하더라도 문제를 일으키지 않고 동작해야 한다.

#### 4. 인터페이스 분리 (Interface segregation principle)
작은 인터페이스로 많이 분리하는 것이 일반적인 경우에도 다 사용가능한 하나의 인터페이스보다 더 좋다.

#### 5, 의존성 주입 (Dependency inversion principle)
직접적으로 의존하지 말고 추상화에 의존하라.

### 단일 책임 원칙 (Single responsibility priciple)

클레스가 변경되는 이유는 딱 한가지여야 합니다.
클레스 설계시 통상 관련있는 항목 들을 같이 넣어서 변경시 관련 있는 것들을 모아둡니다.
이러한 프로그램은 매우 결합력이 있을수 있습니다.

여기에서의 결합력의 의미는 클래스나 모듈에서 기능의 관련성을 의미합니다.
기능들이 관련성이 낮으면 클래스는 낮은 결합력을 가지는 것이며 여러가지 이유에 의해서 변경 될 수 있습니다.
높은 응집력은 `SRP`의 결과입니다.

코드를 추가할 경우 어디에 추가할지에 대해서 결정을 해야 하는데 대부분의 명백히 맞다, 틀리다라고 말하기 애매한 경우가 많습니다.
클래스는 시간이 지날수록 점점 더 원래의 목적과 멀어지는 경우가 많습니다.

**SRP**를 클래스에 적용한다고 생각할 것이 아니라
함수를 만들때도 그것은 한가지 일만 수행해야 하고, 한가지 이유에 의해서만 수정해야 합니다.
모듈 또한 마찬가지고 한가지 목적을 가지고 있는 것들의 집합으로 생성해야 합니다.

*List 3-5*는 **SRP**에 어긋한 사례를 보여줍니다.
언뜻보면 모든 함수들이 `Movie` 클래스의 속성을 사용하여 작업하므로 맞게 된 것으로 보이지만,
`Movie` 객체를 사용하는 것과 Repository로 사용하는 것 사이에서 그 경계가 애매모호 한 점이 보입니다.

#### Listing 3-5. Single responsibility principle (SRP) violation

```TypeScript
class Movie {
    private db: DataBase;
    constructor(private title: string, private year: number) {
        this.db = DataBase.connect('user:pw@mydb', ['movies']);
    }
    getTitle() {
        return this.title + ' (' + this.year + ')';
    }
    save() {
        this.db.movies.save({ title: this.title, year: this.year });
    }
}
```

이 클래스가 더 커지기전에 수정하고자 한다면,
`Movie`에 관련된 것과 `MovieRepository`에 관련된 것으로 구분이 가능합니다.
`Movie`에 관련된 기능을 추가할 경우 `MovieRepository`는 변경할 필요가 없습니다.
반대로 `MovieRepository`를 변경한 경우 `Movie`는 변경할 필요가 없습니다.

#### Listing 3-6. Separate reasons for change
```TypeScript
class Movie {
    constructor(private title: string, private year: number) {
    }
    getTitle() {
        return this.title + ' (' + this.year + ')';
    }
}

class MovieRepository {
    private db: DataBase;
    constructor() {
        this.db = DataBase.connect('user:pw@mydb', ['movies']);
    }
    save(movie: Movie) {
        this.db.movies.save(JSON.stringify(movie));
    }
}

// Movie
var movie = new Movie('The Internship', 2013);

// MovieRepository
var movieRepository = new MovieRepository();

movieRepository.save(movie);
```

**SRP**를 클래스 레벨에 대해서 고려하는 것은 개념적으로 생각하기 쉽습니다.
하지만 함수 레벨에 적용을 하는게 더 중요합니다.
각각의 함수는 한가지 작업만을 수행하며, 함수명은 그 의도를 명확히 보여주어야 합니다.
*Uncle Bob* (<http://blog.cleancoder.com>)은 *당신이 떨어져 나갈때까지 분리하라.*고 하였습니다.
즉, 함수가 몇줄 안될때까지 한가지 작업만 할 수 있도록 리팩토링을 하라는 의미입니다.
이러한 함수를 리팩토링하는 방법은 전체적인 디자인을 재구성할 경우 쉽게 가능하도록 하는데 큰 도움이 됩니다.

### 개방/폐쇄 원칙 (Open/closed principle)
**OCP**는 다음 문장으로 요약됩니다.

>소프트웨어는 확장에 대해서는 개방적이어야 하지만, 수정을 하는데는 폐쇄적이어야 한다.

실질적으로 아무리 설계를 잘하더라도, 수정으로부터 완벽하게 보호하는 것은 힘듭니다.
그러나 아무리 사소한거라도 기존 코드를 변경하는 것은 위험합니다.

**OCP**를 따를려면 프로그램의 변경가능성을 고려해야 합니다.
예를 들어, 나중에 교체되거나 확장가능한 함수를 포함하는 클래스들을 식별해야 합니다.
하지만, 미래를 예측하는 것은 가능한 일이 아니며, 나중을 위해 생성한 코드는 거의 대부분 사용되지 않습니다.
무슨 일이 일어날지 예측하는 것은 까다롭습니다.
이 코드가 나중에 필요없게 될수도 있고, 예측한 것과는 다른 방향으로 흘러 갈 수도 있습니다.
그래서 실제로 문제가 일어났을 때만 해결하려고 노력을 한다는 것을 윈칙으로 하는것이 좋습니다.

**OCP**를 따르는 방법중 가장 일반적인 것은 필요할 경우 클래스를 다른 클래스도 대체할 수 있도록 구현하는 것입니다.
객체지향 언어로 이렇게 구현하는 것은 그렇게 어려운 일이 아닙니다.
물론 타입스크립트도 예외는 아닙니다.
목록 3-7은 `RewardPointsCalculator`라는 포인트 카드의 리워드를 계산해주는 클래스를 보여줍니다.
보통의 경우 달러 당 4점의 포인트를 보상해 줍니다.
VIP 손님과 같이 2배로 포인트를 보상해 주려고 할때 `DoublePointsCalculator`라는 서브클래스로 대체할 수 있습니다.
`getPoints()`함수 호출하면 슈퍼클래스의 함수가 무시되고 서브클레스에서 수행합니다.

#### Listing 3-7. Open–closed principle (OCP)
```TypeScript
class RewardPointsCalculator {
    getPoints(transactionValue: number) {
        // 4 points per whole dollar spent
        return Math.floor(transactionValue) * 4;
    }
}

class DoublePointsCalculator extends RewardPointsCalculator {
    getPoints(transactionValue: number) {
        var standardPoints = super.getPoints(transactionValue);
        return standardPoints * 2;
    }
}

var pointsCalculator = new DoublePointsCalculator();

alert(pointsCalculator.getPoints(100.99));
```

`RewardPointsCalculator`의 기능을 대체하기 위해서 해당 클래스에 대한 수정 없이 서브클래스를 생성하여 원래 기능을 대체함으로써 구현을 하였습니다.
**OCP**를 잘 지키면 유지 보수 및 재사용 가능한 코드로 작성되는 경향이 높습니다.
변화가 필요한 경우에도 기존에 잘 동작하는 코드는 수정하지 않으면서 새로운 코드를 요구 사항에 맞게 처리하도록 추가할 수 있습니다.

### 리스코프 치환 원칙 (The Liskov Substitution Principle) (LSP)

바바라 리스코프(Barbara Liskov)가 1988년에 `데이터 추상화와 계층구조`(Data Abstraction and Hierarchy)라는 제목의 기조연설에서 이런말을 했습니다.

> S가 T의 하위속성이라면 프로그램의 변경없이 T의 객체를 S로 교체(치환)할 수 있어야 한다.

서브클레스가 슈퍼클래스를 대체할 경우 클래스를 사용하는 코드가 대체한다는 사실을 알 필요가 없다는 것입니다.
개체의 타입에 대해서 테스트하는 코드가 있는 경우에는 **LSP**를 위반하고 있을 가능성이 높습니다.

- 서브타입에서의 함수 인자 호환성 :
 슈퍼클래스에 `Cat`을 입력받는 함수가 있는 경우, 서브클레스는 `Cat` 혹은 `Animal`을 인자로 받을수 있어야 합니다.
- 서브타입에서의 리턴 타입 호환성 :
 슈퍼클래스에 `Animal`을 리턴하는 함수가 있는 경우, 서브클레스는 `Animal`이나 `Animal`의 서브클래스 (`Cat`)를 반환할 수 있어야 합니다.
- 서브타입에서의 발생 예외 호환성 :
 서브클래스가 예외를 발생할 경우, 슈퍼클래스와 같은 예외이거나 그 예외의 서브타입을 발생시켜야 합니다.
타입스크립스의 경우에는 예외 클래스 뿐만 아니라 단순한 예외를 문자열로 `throw`하게 지정할 수 있습니다.
`List 3-8`과 같이 오류 클래스를 생성할 수도 있습니다.
여기서 말하고자하는 것은 예외 처리 코드의 경우 서브클레스라고 해서 다르게 처리되어서는 안된다는 뜻입니다.

#### Listing 3-8. Error classes
```TypeScript
class ApplicationError implements Error {
    constructor(public name: string, public message: string) {
    }
}

throw new ApplicationError('Example Error', 'An error has occurred');
```

**LSP**는 새로운 함수를 추가할 때 예전에 사용되던 함수 대신 사용이 가능하다는 것을 보장해 줌으로 OCP를 지원합니다.
서브클래스가 직접 슈퍼클래스를 대체할 수 없는 경우,
서브클래스를 추가하는 작업은 기존에 잘 작동하던 코드를 수정해야 한다는 뜻이며,
객체 타입에 따라 실행이 나뉘게 되는 식으로 프로그램을 작성해야 할 수도 있다는 말이 됩니다.

책에서는 소개되지 않았지만 **LSP**를 제대로 지키기 위한 가이드 라인을 소개해 드리겠습니다.

- 계약 규칙
  - 서브타입에서 더 강력한 사전 조건을 정의할 수 없다.
  - 서브타입에서 더 완화된 사후 조건을 정의할 수 없다.
  - 슈퍼타입의 불변식(항상 참으로 유지되는 조건들)은 서브타입에서도 반드시 유지되어야 한다.
- 가변성 규칙
  - 서브타입의 메서드 인수는 반 공변성(contravariance)을 가져야 한다. (더 작은 파생형식을 사용할 수 있다.)
  - 서브타입의 리턴 타입은 공변성(variance)을 가져야 한다. (더 많은 파생형식을 사용할 수 있다.)
  - 서브타입은 슈퍼타입이 발생시키는 것과 동일한 타입 예외나 그 보무 타입의 예외 혹은 자식 타입의 예외만 사용해야 한다.

### 인터페이스 분리 (The Interface Segregation Principle) (ISP)

인터페이스를 통해 클래스가 어떤 역할을 하는지를 알 수 있습니다.
통상적으로 클래스를 먼저 생성한 후에 인터페이스를 작성합니다.
`List 3-9`는 복사,출력, 분류 작업을 하는 `Printer` 인터페이스입니다.
이 인터페이스는 프린터 동작을 단순히 포함하는 식이기 때문에 폴딩, 봉투 입력, 팩스, 스캔, 이메일 전송 등의 작업을 추가하는 식으로 점점 더 커질 수 있습니다.

#### Listing 3-9. Printer interface
```TypeScript
interface Printer {
    copyDocument();
    printDocument(document: Document);
    stapleDocument(document: Document, tray: number);
}
```

**ISP**는 큰 인터페이스를 만드는 대신 더 작고 구체적인 인터페이스로 분리하는 것을 권장합니다.
각각의 인터페이스는 필요한 함수만을 제공하도록 정의합니다.
이렇게 함으로써 클래스 내에 인터페이스를 구현할 때 필요없는 기능에 대해서 구현할 필요가 없게 할 수 있습니다.

`List 3-9`의 `Printer` 인터페이스를 구현할때 인쇄, 복사는 구현이 가능한데 분류가 불가능할 경우 해당 함수에 대해서는 오류를 발생시키도록 해야 할 수도 있습니다.
추후에 `Printer` 인터페이스에 새로운 함수를 추가할 경우 이미 구현된 클래스들에 영향을 주기 때문에 추가 자체가 어려워 집니다.
`List 3-10`은 기존의 `Printer` 인터페이스를 나눠서 `SimplePrinter`와 `SuperPrinter`에서 구현을 다르게 한 것을 보여줍니다.

#### Listing 3-10. Segregated interfaces
```TypeScript
interface Printer {
    printDocument(document: Document);
}

interface Stapler {
    stapleDocument(document: Document, tray: number);
}

interface Copier {
    copyDocument();
}

class SimplePrinter implements Printer {
    printDocument(document: Document) {
        //...
    }
}

class SuperPrinter implements Printer, Stapler, Copier {
    printDocument(document: Document) {
        //...
    }
    copyDocument() {
        //...
    }
    stapleDocument(document: Document, tray: number) {
        //...
    }
}
```

**ISP**를 잘 지키면 클라이언트 코드는 사용하지 않는 함수에 대해서 구현할 필요가 없습니다.

### 의존성 주입 (The Dependency Inversion Principle) (DIP)

전통적인 OOP에서는 상위 컴퍼넌트는 계층구조 상의 하위 컴퍼넌트들에게 의존적입니다.
컴퍼넌트간의 결합으로 인해 시스템을 수정하기 힘들게 됩니다.
또한 해당 모듈을 재사용하기 위해서는 의존 관계에 있는 모든 컴퍼넌트들을 다 신경써야 하므로, 결과적으로 재사용성을 떨어트립니다.

`List 3-11`은 전통적인 종속성을 보여주는 예제입니다.
`LightSwitch` 클래스는 `Light` 클래스에 의존성을 가지고 있습니다.

#### Listing 3-11. High-level dependency on low-level class
```TypeScript
interface LightSource {
    switchOn();
    switchOff();
}

class Light {
    switchOn() {
        //...
    }
    switchOff() {
        //...
    }
}

class LightSwitch {
    private isOn = false;
    constructor(private light: Light) {
    }
    onPress() {
        if (this.isOn) {
            this.light.switchOff();
            this.isOn = false;
        } else {
            this.light.switchOn();
            this.isOn = true;
        }
    }
}
```

**DIP**는 **OCP**와 **LSP**를 확장한 개념입니다.
추상화에 의존하게 함으로써, 구체적인 클래스와의 결합성을 낮출수 있습니다.
이 원리를 따르는 가장 간단한 방법은 *클래스*가 아닌 *인터페이스*에 의존적으로 구현하는 것입니다.

## 디자인 패턴 (Design Patterns)

디자인 패턴이란 이미 알려진 문제점들에 대해서 그 해결책을 디자인을 통해서 제공해주는 것을 의미합니다.
하지만 패턴이 과도하게 사용되어서는 안됩니다.
디자인 패턴에 관해 가장 알려진 것은 `Gang of Four`의 `Design Patterns: Elements of Reusable Object-Oriented Software (Gamma, Helm, Johnson,
& Vlissides, Addison Wesley, 1995)`가 있습니다.

디자인 패턴들을 자바스크립트에서도 적용이 가능합니다.
`Diaz and Harmes`의 `Pro JavaScript Design Patterns, Apress, 2007`란 책도 나와 있습니다.
자바스크립트에서 가능한 것은 타입스크립트에서도 물론 가능합니다.
타입스크립트는 클래스 기반의 객체 지향을 사용하기 때문에 전통적인 디자인 패턴 예제를 타입스크립트로 적용하는 것이 가능합니다.
몇 가지 디자인 패턴 샘플들에 대해서 소개해 드리겠습니다.
(`전략 패턴`, `추상 팩토리 패턴`)
GOF의 디자인패턴에는 총 23가지 패턴이 있습니다.

### 전략 패턴 (The Strategy Pattern)

**전략패턴**은 알고리즘을 캡슐화하는 방법을 제공합니다.
그림 3-2에서 `Context` 클래스는 인터페이스의 구체적인 구현을 제공하는 `Strategy`에 의존적입니다.
인터페이스를 구현하는 클래스는 런타임에 `Context`에 제공되어 집니다.

#### 그림 3-2 전략 패턴
<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Front-end/TypeScript/image/TypeScript.03.02.png?raw=true">

### 추상 팩토리 패턴 (The Abstract Factory Pattern)

추상 팩토리 패턴은 창조적인 디자인 패턴입니다.
개체 생성을 위해서 구체적인 클래스를 지정하지 않고 인터페이스로 지정할 수 있습니다.
그래서 런타임시 구체적인 클래스를 전달하는 것입니다.

#### 그림 3-3 추상 팩토리 패턴
<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Front-end/TypeScript/image/TypeScript.03.03.png?raw=true">

### 예제

새차 시스템에 전략 패턴과 추상 팩토리 패턴을 이용한 예를 살펴보겠습니다.
가격에 따라 다른 서비스를 제공하는 시스템입니다.
`List 3-13`은 휠청소 클래스에 대한 인터페이스와 2가지 기본, 고급의 2가지 전략을 보여줍니다.

#### Listing 3-13. Wheel cleaning
```TypeScript
interface WheelCleaning {
    cleanWheels(): void;
}

class BasicWheelCleaning implements WheelCleaning {
    cleanWheels() {
        console.log('Soaping Wheel');
        console.log('Brushing wheel');
    }
}

class ExecutiveWheelCleaning extends BasicWheelCleaning {
    cleanWheels() {
        super.cleanWheels();
        console.log('Waxing Wheel');
        console.log('Rinsing Wheel');
    }
}
```

`List 3-14`는 차체 청소를 위한 전략을 보여줍니다.

#### Listing 3-14. Body cleaning
```TypeScript
interface BodyCleaning {
    cleanBody(): void;
}

class BasicBodyCleaning implements BodyCleaning {
    cleanBody() {
        console.log('Soaping car');
        console.log('Rinsing Car');
    }
}

class ExecutiveBodyCleaning extends BasicBodyCleaning {
    cleanBody() {
        super.cleanBody();
        console.log('Waxing car');
        console.log('Blow drying car');
    }
}
```

`List 3-15`는 추상 팩토리 패턴이 사용되기 전의 `CarWashProgram`입니다.
세척 클래스들과 강력한 결합을 가지고 있으며, 선택된 것에 대하여 클래스를 생성합니다.

#### Listing 3-15. CarWashProgram class before the abstract factory pattern
```TypeScript
class CarWashProgram {
    constructor(private washLevel: number) {
    }
    runWash() {
        var wheelWash: WheelCleaning;
        var bodyWash: BodyCleaning;
        switch (this.washLevel) {
            case 1:
                wheelWash = new BasicWheelCleaning();
                wheelWash.cleanWheels();
                bodyWash = new BasicBodyCleaning();
                bodyWash.cleanBody();
                break;
            case 2:
                wheelWash = new BasicWheelCleaning();
                wheelWash.cleanWheels();
                bodyWash = new ExecutiveBodyCleaning();
                bodyWash.cleanBody();
                break;
            case 3:
                wheelWash = new ExecutiveWheelCleaning();
                wheelWash.cleanWheels();
                bodyWash = new ExecutiveBodyCleaning();
                bodyWash.cleanBody();
                break;
        }
    }
}
```

추상 팩토리란 구체적인 팩토리들이 수행가능한 인터페이스 입니다.
`List 3-16`에서 `ValetFactory` 인터페이스는 `WheelCleaning`와 `BodyCleaning`를 얻을 수 있는 기능을 제공합니다.
휠청소와 차체청소를 필요로하는 클래스는 이 인터페이스에 의존적일 수 있습니다.
또한 각각의 청소를 클래스로 부터 해제하는 일이 필요할 수도 있습니다.

#### Listing 3-16. Abstract factory
```TypeScript
interface ValetFactory {
    getWheelCleaning() : WheelCleaning;
    getBodyCleaning() : BodyCleaning;
}
```

`List 3-17`에서 금,은,동 등급의 3개의 팩토리를 선언합니다.
각각의 팩토리는 해당 등급에 맞는 청소클래스를 제공합니다.

#### Listing 3-17. Concrete factories
```TypeScript
class BronzeWashFactory implements ValetFactory {
    getWheelCleaning() {
        return new BasicWheelCleaning();
    }
    getBodyCleaning() {
        return new BasicBodyCleaning();
    }
}

class SilverWashFactory implements ValetFactory {
    getWheelCleaning() {
        return new BasicWheelCleaning();
    }
    getBodyCleaning() {
        return new ExecutiveBodyCleaning();
    }
}

class GoldWashFactory implements ValetFactory {
    getWheelCleaning() {
        return new ExecutiveWheelCleaning();
    }
    getBodyCleaning() {
        return new ExecutiveBodyCleaning();
    }
}
```

`List 3-18`은 추상 팩토리 패턴이 사용된 예제입니다.
`CarWashProgram` 플래스는 더이상 구체적인 클래스에 대해서 알 필요가 없습니다.
이제는 각각의 청소 클래스를 제공하는 팩토리로 구성되어 있습니다.
이것은 컴파일 타임이나 런타임에 수행됩니다.

#### Listing 3-18. Abstract factory pattern in use
```TypeScript
class CarWashProgram {
    constructor(private cleaningFactory: ValetFactory) {
    }
    runWash() {
        var wheelWash = this.cleaningFactory.getWheelCleaning();
        wheelWash.cleanWheels();
        var bodyWash = this.cleaningFactory.getBodyCleaning();
        bodyWash.cleanBody();
    }
}
```

## Mixins

<https://en.wikipedia.org/wiki/Mixin>

`Mix-in`은 디자인 패턴에서는 다루지 않는 응용 프로그램을 구성하는 다른 방법입니다.
믹스인은 미사추세츠, 소머빌에 있는 시트브 아이스크림이란 가게에서 고객이 고를수 있는 아이스크림 디저트의 이름을 따왔습니다.
아이스 크림을 고른 뒤 막대 사탕 같은 다른 기호에 맞는 것들을 추가할 수가 있습니다.

프로그래밍의 믹스인도 이와 유사합니다.
인자로 재사용 가능한 클래스들을 받아서 그것들을 조합하여 사용합니다.
믹스인 클래스의 일부는 인터페이스이며 일부는 구현입니다.

### TypeScript Mixins

아직 타입스크립트에서 **믹스인**이 완벽하게 지원되지는 않습니다만, 간단한 정도는 구현이 가능합니다.
`List 3-19`에 **믹스인**을 적용한 함수가 있습니다.
이 함수는 각각의 *증강 클래스*(augumented class) 배열을 baseCtors로 전달하고 *구현할 클래스*를 derivedCtor로 전달합니다. 
이 함수를 통해서 **믹스인**을 적용하고 싶을 때는 언제든지 적용이 가능합니다.

#### Listing 3-19. Mixin enabler function
```TypeScript
function applyMixins(derivedCtor: any, baseCtors: any[]) {
    baseCtors.forEach(baseCtor => {
        Object.getOwnPropertyNames(baseCtor.prototype).forEach(name => {
            if (name !== 'constructor') {
                derivedCtor.prototype[name] = baseCtor.prototype[name];
            }
        })
    });
}
```

`Listing 3-20`에는 재사용 가능한 *증강 클래스*가 정의 되어 있습니다.
구체적인 구분은 없지만, `Sings`, `Dances`, `Acts`에 대해서 정의했습니다.
이러한 클래스는 서로 다른 조합으로 구성되어 실행이 가능합니다.

#### Listing 3-20. Reusable classes
```TypeScript
class Sings {
    sing() {
        console.log('Singing');
    }
}

class Dances {
    dance() {
        console.log('Dancing');
    }
}

class Acts {
    act() {
        console.log('Acting');
    }
}
```

이 클래스들은 **SRP**를 매우 잘 지키고 있습니다.
타입스크립트에서는 `implements` 키워드 뒤에 믹스인 리스트(*증강 클래스*)를 콤마로 나열해서 클래스를 구성할 수 있습니다.

#### Listing 3-21. Composing classes
```TypeScript
class Actor implements Acts {
    act: () => void;
}

applyMixins(Actor, [Acts]);

class AllRounder implements Acts, Dances, Sings {
    act: () => void;
    dance: () => void;
    sing: () => void;
}

applyMixins(AllRounder, [Acts, Dances, Sings]);
```

`Actor`와 `AllRounder` 클래스에는 구현되어 있는게 아무것도 없습니다.
*증강 클래스*에서 제공받을 수 있는 공간만을 할당해놓고 있습니다.
이 클래스를 사용하는 것은 다른 클래스를 사용하는 것과 다르지 않습니다.

#### Listing 3-22. Using the classes
```TypeScript
var actor = new Actor();
actor.act();

var allRounder = new AllRounder();
allRounder.act();
allRounder.dance();
allRounder.sing();
```

타입스크립트에서 다중 상속은 허용되지 않습니다.
마치 다중 상속처럼 보이겠지만, `extends`를 사용한 것이 아닌 `impliments`를 사용했다는 것이 중요합니다.

### 언제 믹스인을 써야 하는가

**믹스인**을 타입스크립트에서 일부 지원하지만, 사용할때 무엇을 염두해 두어야 할까요 ?
무엇보다도, 구현이 클래스에 주입되었는지에 대해서 확인하는 방법이 없으므로 `applyMixins` 함수를 정확한 클래스 명의 리스트로 호출하는것을 신경써야 합니다.
그렇지 않으면 테스트 할때 제대로 잘 안되더라도 원인을 찾기 힘들 것입니다.

믹스인을 사용할지 일반적인 클래스를 사용할지는 클래스간의 관계를 보고 결정을 해야 합니다.
**상속**에는 통상 `is a`를 사용하고 **위임**에서는 `has a`를 사용합니다.
- A car has a chassis.
- A rolling chassis is a chassis.

믹스인에서는 `can do`를 사용하는 것으로 그 관계를 설명할 수 있습니다.
- An actor can do acting  
or
- An actor acts.

`Acting`과 `Acts`와 같이 이름 지정으로서 믹스인 관계를 식별하도록 할 수 있습니다.
그렇게 하면 클래스 선언이 마치 문장 처럼 보일 수 있습니다. (`Actor implements Acting`)
**믹스인**은 작은 단위가 합쳐서 큰 것으로 되는 것이 가능하기 때문에, 다음에 열거한 시나리오들은 믹스인으로 구성되기 좋은 것들입니다.

- 추가적인 옵션을 갖는 클래스 (*믹스인 함수*를 옵션으로 구현)
- 여러 클래스에서 동일한 함수를 재사용
- 비슷한 기능들의 조합으로 여러 가지 클래스를 만들어야 할 경우

### 제한점

*믹스인 함수*를 `private` 멤버로 사용하면 안됩니다.
왜냐면 컴파일러가 *증강 클래스*가 구현이 안되었을 경우 오류를 발생합니다.
또한 *믹스인 함수*와 *증강 클래스*가 둘 다 동일한 이름의 `private` 멤버를 가지고 있는 경우에도 오류를 발생합니다.

**믹스인**의 또다른 제한점은 함수는 *증강 클래스*로 매핑되지만, 속성은 안됩니다. (`List 3-23`)
*증강 클래스* 안에 속성을 구현한 경우 *믹스인 함수*에서 초기화해줘야 합니다.
실수를 방지하기 위해서는 *증강 클래스* 안에 있는 속성에 대해서는 디폴트값을 정의하지 않는 것이 좋습니다.

#### Listing 3-23. Properties not mapped
```TypeScript
class Acts {
    public message = 'Acting';
    act() {
        console.log(this.message);
    }
}

class Actor implements Acts {
    public message: string;
    act: () => void;
}

applyMixins(Actor, [Acts]);

var actor = new Actor();

// Logs 'undefined', not 'Acting'
actor.act();
```

속성이 특정 개체에 종속되지 않는다면 `static`으로 선언하는 방법도 있습니다.
`List 3-24`는 `List 3-23`의 문제점을 `static` 요소로 선언하는 것으로 해결한 것입니다.
객체마다 다른 값이 필요한 경우 해당 요소는 *믹스인 함수*에서 초기화해줘야 합니다.

#### Listing 3-24. Static properties are available
```TypeScript
class Acts {
    public static message = 'Acting';
    act() {
        alert(Acts.message);
    }
}
```

### Summary

- 타입스크립트에는 객체 지향적인 요소들을 대부분 포함하고 있습니다.
- SOLID 이론은 코드가 계속 유지될 수 있도록 해주는 것을 그 목표로 하고 있습니다.
- 디자인 패턴은 일반적으로 알려준 문제들에 대한 해법이 될 수 있습니다.
- 디자인 패턴에서 설명한 그대로 구현할 필요는 없습니다.
- 믹스인은 각 가수어품들을 대체 할수 있는 방법을 제공합니다.















