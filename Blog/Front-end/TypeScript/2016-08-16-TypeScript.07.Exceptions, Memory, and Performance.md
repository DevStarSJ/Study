---
layout: post
title: "Chapter 7 Exceptions, Memory, and Performance"
subtitle:  
categories: development
tags: javascript
comments: true
---

# Chapter 7 Exceptions, Memory, and Performance

- 예외(Exception) 및 메모리 관리(MM : Memory Management)를 잘 알면 프로그램 작성에 도움이 됨
- TypeScript, JavaScript의 예외가 C#, Java, PHP 등 다른 언어를 다뤄본 개발자들에게는 친숙해 보이겠지만, 미묘한 차이가 있음
- 7장에서 MM 과 GC(Garbage Collection) 의 최적화 테스트를 위한 측정 방법에 대해서 다룰 예정

## 1. 예외 (Exceptions)

- 예외는 프로그램이나 모듈이 계속해서 처리하는게 불가능함을 나타내기 위해 사용됨
- 하지만, Program Logic 상의 문제를 예외를 통해서 처리하는 경우가 종종 있는데, 이 경우에는 예외처리 없이 Logic으로 검증하는게 더욱 바람직함
- 예외에 대해서 별도의 처리를 해주지 않으면 JavaScript 콘솔에 표시됨. (콘솔에는 개발자가 별도의 출력을 할 수도 있음)

 - 최신 브라우저 들은 콘솔 기능을 모두 제공함
 - Windows, Linux는 `Ctrl + Shift + I` 또는 `F12` , Mac은 `Cmd + Opt + I`를 누르면 개발자 도구, 브라우저 콘솔이 열림

### 1.1 예외 발생 (Throwing Exceptions)

- `throw` 키워드를 이용해서 예외를 발생시킴
- 예외로 어떤 타입의 객체라도 전달이 가능하지만, 가능하다면 `Error`객체에 메세지를 포함시키는 것이 바람직함

#####Listing 7-1. Using the throw keyword
```TypeScript
function errorsOnThree(input: number) {
    if (input === 3) {
        throw new Error('Three is not allowed');
    }

    return input;
}

var result = errorsOnThree(3);
```

`Error` 타입의 예외를 전달하는 예제인데, 사용자 정의 예외를 직접 구현하는 것도 가능합니다.
`toString()` 메서드를 구현해주면 콘솔에 출력되는 정보를 보기 좋게 할 수 있습니다.

#####Listing 7-2. Custom error
```TypeScript
class ApplicationError implements Error {

    public name = 'ApplicationError';

    constructor(public message: string) {
        if (typeof console != 'undefined') {
            console.log('Creating ' + this.name + ' "' + message + '"');
        }
    }

    toString() {
        return this.name + ': ' + this.message;
    }
}
```

- `InputError` 는 `ApplicationError`를 상속받아서 아무런 구현도 하지 않음
- `errorsOnThree` 함수에서 잘못된 입력에 대해서 `InputError`를 발생

#####Listing 7-3. Using inheritance to create special exception types
```TypeScript
class ApplicationError implements Error {

    public name = 'ApplicationError';

    constructor(public message: string) {
    }

    toString() {
        return this.name + ': ' + this.message;
    }
}

class InputError extends ApplicationError {
}

function errorsOnThree(input: number) {
    if (input == 3) {
        throw new InputError('Three is not allowed');
    }
    return input;
}
```

- `ApplicationError`를 사용하지 않고 `Error`를 바로 발생시켜도 되지만, 우리가 작성한 코드에서의 오류를 모두 `ApplicationError` 또는 이것을 상속받은 오류만 발생시킬 경우 우리가 작성한 코드 이외의 곳에서 발생한 오류와 구분이 쉬워짐

### 1.2 예외 처리 (Exception Handling)

- 예외발생시 별도의 처리를 하지 않으면 프로그램이 종료됨
- 예외를 처리하기 위해서는 예외가 발생한 곳을 `try-catch-finally` 블록으로 감싸줘야 함

#####Listing 7-4. Unconditional catch block
```TypeScript
try {
    var result = errorsOnThree(3);
} catch (err) {
    console.log('Error caught, no action taken');
}
```

위 예제는 모든 종류의 예외에 대해서 처리를 하는 코드인데, 이런식의 처리는 좋은 방법이 아닙니다.
우리가 예상가능하고 처리가능한 예외에 대해서만 처리를 하고 나머지 예외에 대해서는 다시 발생시키는 것이 더 올바른 방법입니다.

#####Listing 7-5. Checking the type of error
```TypeScript
try {
    var result = errorsOnThree(3);
} catch (err) {
    if (!(err instanceof ApplicationError)) {
        throw err;
    }

    console.log('Error caught, no action taken');
}
```

위 예제는 `ApplicationError`와 이 것을 상속받은 오류에 대해서만 처리를 하고 나머지에 대해서는 처리를 하지 않는 코드입니다.

#####Figure 7-1. Error class hierarchy
<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Front-end/TypeScript/image/TypeScript.07.01.png?raw=true">

`ApplicationError` 대신 `InputError`에 대해서 처리하도록 했다면, 아래 그림과 같이 `InputError`, `BelowMinError`, `AboveMaxError`, `InvalidLengthError`에 대해서는 처리를 해주지만, 나머지에 대해서는 처리를 하지 않고 Call Stack에 오류를 전달하게 됩니다.

#####Figure 7-2. Handling InputError exceptions
<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Front-end/TypeScript/image/TypeScript.07.02.png?raw=true">

`ApplicationError`에 대해서는 아래 7가지 오류에 대해서 처리를 해줍니다.

#####Figure 7-3. Handling ApplicationError exceptions
<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Front-end/TypeScript/image/TypeScript.07.03.png?raw=true">

로우레벨 관련 코드를 작업하는 경우에는 예외의 타입을 정확하게 분류하여 작업을 할 필요가 있지만, UI 작업과 같은 경우에는 좀더 일반적인 예외 종류에 대해서 처리를 하여도 무방합니다.
예외는 성능 비용이 큰 편에 속하기 때문에 단순히 루프를 빠져나가기 위한 신호 같은 용도로 사용하는 것은 적절하지 않습니다.

## 2. 메모리 (Memory)

TypeScript 같은 고차원 언어에서는 메모리 관리가 자동으로 됩니다.
우리가 생성한 변수나 객체의 경우 범위를 넘어서 사용된다던지, 댕글링 포인트(dangling pointer)가 되지 않습니다.
대부분의 메모리 관련 오류는 자동으로 처리되지만 `Out of Memory`같이 처리가 되지 않는 오류도 있습니다.
이번 장에서는 어떻게 하면 그런 오류들을 피할 수 있을 것인지에 대해서 다뤄볼 예정입니다.

### 2.1 자원 해제 (Releasing Resources)

타입스크립트에서는 관리되지 않는 자원을 사용할 경우가 있습니다.
대부분의 API들은 작업이 완료되었을 경우 인자가 전달되는 비동기 패턴으로 되어 있습니다.
센서에 가까이 있을 때 검출되는 API에 대한 사용 예제를 보도록 하겠습니다.

#####Listing 7-6. Asynchronous pattern
```TypeScript
var sensorChange = function (reading) {
    var proximity = reading.near ?
        'Near' : 'Far';

    alert(proximity);
}

window.addEventListener('userproximity', sensorChange, true);
```

비동기 패턴을 통해 근접 센서로부터 정보를 얻어 올수 있지만, 통신 채널을 통한 응답을 보장해 주지는 못합니다.
오류가 발생할 경우에 대해서 대비하기 위해서 `try-finally` 블록을 이용해야 합니다.

#####Listing 7-7. Imaginary unmanaged proximity sensor
```TypeScript
var sensorChange = function (reading) {
    var proximity = reading.near ?
        'Near' : 'Far';

    alert(proximity);
}

var readProximity = function () {
    var sensor = new ProximitySensor();

    try {
        sensor.open();
        var reading = sensor.read();
        sensorChange(reading);
    } finally {
        sensor.close();
    }
}

window.setInterval(readProximity, 500);
```

`finally` 블록을 통해서 sensor의 `open`, `read`, `sensorChange` 중 어디에서 오류가 발생하더라도 `close`가 호출되는 것을 보장해 주게 됩니다.

### 2.2 가비지 콜렉션 (Garbage Collection)

메모리가 더 이상 사용되지 않을 경우 GC를 통해서 해제되게 됩니다.
예전 방식의 브라우저의 경우 참조 카운트(Reference Count)가 0이 되었을 경우 해제를 하게 되는데,
만약 2개의 객체가 서로 참조하는 경우에는 RC가 0이 되지 않아서 해제되지 않게 됩니다.

#####Table 7-1. Reference counting garbage collection
<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Front-end/TypeScript/image/TypeScript.07.04.png?raw=true">

최신의 브라우저의 경우에는 루트에 도달 가능한 모든 객체를 찾아낸 뒤, 나머지 객체에 대해서 마크앤스윕(mark-and-sweep) 알고리즘을 이용해서 해결합니다.
GC 수행 시간은 더 걸릴 수 있지만, 메모리 누수의 발생 가능성을 줄여 줍니다.

#####Figure 7-4. Mark and sweep
<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Front-end/TypeScript/image/TypeScript.07.05.png?raw=true">

`Table 7-1`과 `Figure 7-4`가 동일한 객체일 경우 RC를 사용하는 경우라면 `E`에 대해서만 해제를 하지만, MAS를 사용하는 경우라면 서로 참조하고 있는 `A`,`B`에 대해서도 해제가 가능합니다.

## 3. 성능 (Performance)

개발자들이 별로 중요하지도 않은 성능과 효율 등에 대해 고려하는 경우가 많습니다.
하지만 대부분의 경우(97%)는 고려하지 않아도 될만큼 효율이 작은 것입니다만,
치명적인 부분(3%)에 대해서는 간과하면 안됩니다.

측정 가능한 성능 문제가 발견되기 전까지는 최적화를 하지 않는게 좋습니다.
지역 변수는  객체의 속성보다 느리기 때문에 사용하지 말아야 한다는 주장이 있습니다.
이 말이 사실일 수는 있지만, 프로그램 디자인을 지저분하게 할 여지가 있기 때문에 조심해야 합니다.
최적화와 좋은 디자인은 트레이드-오프 관계에 있는 경우가 많기 때문에 신중하게 결정해야 합니다.

* TypeScript의 성능은 여러 브라우저에서 측정해봐야 합니다. 그렇지 않으면 특정 브라우저에서만 빠르고 다른 곳에서는 느려질 수도 있습니다.

아래 코드는 간단한 성능 테스트용입니다.
`CommunicationLines` 클래스는 팀 구성원 들 사이의 의사 소통 라인 수를 `N(N-1)/2` 알고리즘을 이용해서 구합니다.
`testCommunicationLines` 함수는 사이즈가 4, 10 인 경우에 대해서 계산하는 것으로 테스트 합니다.

#####Listing 7-8. Calculating lines of communication
```TypeScript
class CommunicationLines {
    calculate(teamSize: number) {
        return (teamSize * (teamSize - 1)) / 2
    }
}

function testCommunicationLines() {
    var communicationLines = new CommunicationLines();
    var result = communicationLines.calculate(4);

    if (result !== 6) {
        throw new Error('Test failed for team size of 4.');
    }

    result = communicationLines.calculate(10);

    if (result !== 45) {
        throw new Error('Test failed for team size of 10.');
    }
}

testCommunicationLines(); 
```

아래 코드는 함수와 실행 횟수를 인자로 받아서 성능을 테스트 해주는 클래스 입니다.
`performance.now()`로 전달받은 함수를 감싸고 있습니다.
기본적으로는 10,000번 실행을 해서 총 시간 및 평균 시간을 출력합니다.

#####Listing 7-9. Performance.ts runner
```TypeScript
class Performance {
    constructor(private func: Function, private iterations: number) {
    }

    private runTest() {
        if (!performance) {
            throw new Error('The performance.now() standard is not supported in this runtime.');
        }

        var errors: number[] = [];

        var testStart = performance.now();

        for (var i = 0; i < this.iterations; i++) {
            try {
                    this.func();
            } catch (err) {
                // Limit the number of errors logged
                if (errors.length < 10) {
                errors.push(i);
                }
            }
        }

        var testTime = performance.now() - testStart;

        return {
            errors: errors,
            totalRunTime: testTime,
            iterationAverageTime: (testTime / this.iterations)
        };
    }

    static run(func: Function, iterations = 10000) {
        var tester = new Performance(func, iterations);
        return tester.runTest();
    }
}

export = Performance;
```

앞에서 작성한 `CommunicationLines` 클래스에 대한 성능 측정을 `Performance`로 성능 측정을 하는 것에 대한 예제 입니다.

#####Listing 7-10. Running the performance test
```TypeScript
import perf = require('./performance');

class CommunicationLines {
    calculate(teamSize: number) {
        return (teamSize * (teamSize - 1)) / 2
    }
}

function testCommunicationLines() {
    var communicationLines = new CommunicationLines();
    var result = communicationLines.calculate(4);

    if (result !== 6) {
        throw new Error('Test failed for team size of 4.');
    }

    result = communicationLines.calculate(10);
    if (result !== 45) {
        throw new Error('Test failed for team size of 10.');
    }
}

var result = perf.run(testCommunicationLines);

console.log(result.totalRunTime + ' ms');
```

위 테스트 결과가 `2.73ms`로 나왔습니다. (`communicationLines.calculate()`를 2만번 호출)
이런식으로 테스트는 최적화 위치를 적절하게 찾는 것에 도움이 됩니다.

하지만 아래 코드와 같이 예외가 발생하게 된다면 전혀 다른 결과가 나옵니다.

#####Listing 7-11. Running the performance test with exceptions
```TypeScript
import perf = require('./performance');

class CommunicationLines {
    calculate(teamSize: number) {
        return (teamSize * (teamSize - 1)) / 2
    }
}

function testCommunicationLines() {
    var communicationLines = new CommunicationLines();
    var result = communicationLines.calculate(4);

    // This test will now fail
    if (result !== 7) {
        throw new Error('Test failed for team size of 4.');
    }

    result = communicationLines.calculate(10);
    if (result !== 45) {
        throw new Error('Test failed for team size of 10.');
    }
}

var result = perf.run(testCommunicationLines);

console.log(result.totalRunTime + ' ms');
```

위 테스트 결과는 `214.45ms` 즉 78배나 더 느려졌습니다.

다양한 조건 및 실행회수로 테스트를 해 볼 수 있습니다.

다음 결과는 `Performance` 클래스를 통해 여러가지 다른 방법으로 구현했을 떄의 수치입니다.

- Iteration : 0.74ms
- Global variables: 0.80 ms (0.06 ms slower per iteration)
- Closures: 1.13 ms (0.39 ms slower per iteration)
- Properties: 1.48 ms (0.74 ms slower per iteration)

이렇듯 어떻게 구현하냐에 따라 실행결과가 각각 다르게 나타나기 때문에, 최적화를 하기 전에 이런식으로 측정을 해보고 결정을 하는 것이 좋습니다.

## Summary

- 중요한 3가지 점에 대해서 살펴보았는데, 이런 것을 잘 고려하면 좀 더 쉽게 지름길로 가듯 코드를 작성 할 수 있습니다.
- 예외 처리를 잘하면 프로그램이 비정상적으로 종료되는 현상을 방지할 수 있습니다.
사용자 정의 예외를 작성하면 각각 오류에 대해서 구분을 할 수 있어서 도움이 되며,
해결 가능한 예외만 `catch`절에서 처리해야 합니다.
- 요즘의 브라우저들은 `mark-and-sweep` 알고리즘을 이용하므로 순환 참조에 대한 메모리 누수는 신경을 쓸 필요가 없습니다.
가비지 컬렉터에 대해서는 신경쓰지 않고 작업을 하면 됩니다만, 성능을 측정한다던지 가비지 컬랙터에 문제가 있는 경우에는 좀 더 작은 객체를 생성하는 것이 좋습니다.
- 최적화 작업을 하기전에는 반드시 성능측정을 하는 것이 좋습니다.
여러 가지 환경에서의 성능을 측정한 뒤에 모든 상황에 대해서 고려하여 최적화 작업을 해야 합니다.

## Key Points

- `throw`로 모든 종류의 객체를 전달하는게 가능은 하지만, 되도록이면 사용자 지정 `Error`의 서브클래스를 사용하는 것이 좋습니다.
- `try-catch-finally` 블록으로 예외를 직접 처리할 수 있습니다.
- 특정 예외만 `catch` 블록으로 잡을 수는 없지만, 그 안에서 예외의 타입을 체크할 수 있습니다.
- 대부분의 API가 비동이 패턴이므로 `try-finally` 블록을 이용해서 자원을 관리하는게 좋습니다.
- 성능 최적화 작업을 할때는 코드 변경 전후에 대해서 수치적으로 측정을 하는게 좋습니다.

