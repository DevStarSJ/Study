---
layout: post
title:  "AWS Lambda + API Gateway Binary Response 예제"
subtitle:  
categories: cloud
tags: aws
comments: true
---

# AWS Lambda + API Gateway Binary Response 예제


**API Gatewa**y의 Binary Response가 가능하기 때문에 이미지 파일(png, jpg)나 pdf 다운로드 같은걸 **Lambda**를 이용해서 구현이 가능하다.
AWS 에서 제공해주는 예제는 AWS Compute Blog에 있는 [Binary Support for API Integrations with Amazon API Gateway](https://aws.amazon.com/blogs/compute/binary-support-for-api-integrations-with-amazon-api-gateway) 란 포스팅이 있는데 이것을 읽고 실제로 구현을 하기에는 조금 부족하다.

그래서 바로 사용 가능한 예제 코드를 작성해 보았다.

이번에 회사(직방)에서 `html to pdf` API 내재화 (예전에는 외부 유료 서비스 사용) 작업을 진행하면서 Binary Response에 대해서 경험을 하게 되었다.
그 과정에서 많은 삽질(?)을 하게 되었는데, 이런 예제 코드만 하나 검색으로 찾을 수 있었어도 시간을 많이 아낄수 있었을 꺼란 생각이 들었다.

## 1. Lambda 코드 작성

Node.JS를 이용해서 작성하였다.

```JavaScript
"use strict";

const fs = require("fs");
const qs = require("querystring");

const FILE = {
    JPG: "test.jpg",
    PNG: "test.png",
    PDF: "test.pdf"
};

const CONTENT_TYPE = {
    JPG: "image/jpg",
    PNG: "image/png",
    PDF: "application/pdf"
};

exports.handler = (event, context, callback) => {

    console.info(JSON.stringify(event,null,2));

    const qs = event.queryStringParameters || {};
    const path = event.pathParameters.proxy;
    const body = getBody(event);

    const KEY = path.indexOf("jpg") >= 0 ? "JPG" :
                path.indexOf("png") >= 0 ? "PNG" :
                                           "PDF";

    const content = fs.readFileSync(FILE[KEY]);

    const response = {
        statusCode: 200,
        headers: {
            "Content-Type": CONTENT_TYPE[KEY],
            "Content-Disposition": `inline; filename="${FILE[KEY]}"`
        },
        body: new Buffer(content).toString("base64"),
        isBase64Encoded: true
    }

    callback(null, response);
};

function getBody(event)
{
    if (!event.body)
        return null;

    const rawBody = event.isBase64Encoded ? new Buffer(event.body, "base64").toString() : event.body;

    const body = event.headers["Content-Type"] === "application/x-www-form-urlencoded" ?
        qs.parse(rawBody) : rawBody;

    return body;
}
```

코드 대해서는 간략하게만 설명하겠다.

경로상에 `pdf`, `png`, `jpg` 가 있는 경우 각각 그 예제 바이너리를 리턴해주는 간단한 API다.

API Gateway의 Lambda Proxy Integration를 이용해서 `event`를 받을 예정이다.
예전에는 `{proxy+}` 리소스를 사용해야지만 프락시 통합이 사용가능했지만, 이제는 각각의 리소스, 메서드를 직접 지정하더라도 프락스 통합 사용이 가능하므로 이걸 사용하지 않을 이유가 없다.

이번 예제에서 `body`를 사용하지는 않을 예정이라 `getBody` 함수가 사실상 필요는 없지만, 바이너리로 `body`를 받을 경우에는 해당 코드를 참고해서 처리하면 된다.

![](/images/BinaryResponse.00.png)

위 그림과 같이 `isBase64Encoded` 값을 보고 `body`를 인코딩 해줘야 한다.
인코딩 여부를 우리가 정할 수 있는지는 잘 모르겠지만, API Gateway에서 알아서 판단하여 인코딩 해주는것 같다.
여러 번의 테스트를 해보니 `isBase64Encoded`가 *false*로 계속 전달되다가 API Gateway deploy 이후 *true*로 바뀐적도 있다.

JavaScript에서의 switch-case 문에 대한 구현은 개인적으로 위와 같이 Object를 만들어서 key-value pair를 활용하는게 깔끔해 보인다.

## 2. Lambda 배포

위 작성한 코드와 `test.jpg`, `test.png`, `test.pdf` 를 같은 폴더에 복사한 뒤 같이 압축해 주자.

![](/images/BinaryResponse.01.png)

> zip -r test.zip .

그리고 AWS Lambda Console로 가서 **binaryTest** 란 이름으로 Function을 생성하자.

런타임은 **Node.js 6.10** 을 선택하고 해당 압축파일을 업로딩하자.

다른 설정은 적당히 알아서 하면 된다.

이 예제는 S3나 다른 AWS 상의 리소스를 사용하지 않으니 **Role** 설정도 따로 복잡하게 할 것이 없다.

단, 메모리와 타임아웃은 적당히 여유있게 주길 바란다.
바이너리 처리 자체가 파일을 읽고, 쓰는 작업이 필요하기 때문에 메모리가 많이 필요 할 수도 있고, 시간도 생각보다 오래 걸릴수 있기 때문이다.

## 3. API Gateway 생성 및 설정

### 3.1 일단 API 생성

![](/images/BinaryResponse.02.png)

그냥 `binaryTest`로 하나 생성한다.

### 3.2 리소스 추가

`Action` -> `Create Method` 를 누른 뒤 `proxy resource`를 체크하고 `Create Resource`를 눌러주자.

![](/images/BinaryResponse.03.png)

이번 예제에서는 모든 경로에 대해서 하나의 Lambda를 실행시킬 것이다.
단, 이 방법은 유효하지 않은 경로 등에 대해서도 모두 Lambda를 실행시키게 되므로 쓸데없는 비용이 발생 할 수도 있다는건 알아둬야 한다.
Lambda에서 처리 가능한 경로에 대해서만 호출을 할 것이라면 리소스를 유효한 것만 따로 생성하는게 좋다.

해당 프락시 리소스에서 실행시킬 Lambda를 설정해 주자.

![image](/images/BinaryResponse.04.png)

위에서 생성한 binaryTest Lambda Function으로 설정하자.

### 3.3 Binary Support 추가

API Gateway 상의 `Binary Support` 탭을 눌러서 들어가자.

![image](/images/BinaryResponse.05.png)

해당 API를 호출할 때 `headers`에서 `Accept`로 요청하는 형태들에 대해서 미리 정의해 줘야 한다.

만약 브라우저에서 url로 바로 호출할 것이라면 `*/*`를 추가해 줘야 한다.


그 밖의 다른 곳에서 요청시 `Accept`로 명시해주는 형태에 대해서 추가를 해줘야 `API Gateway`에서 바이너리 형태로 응답을 제공한다.

### 3.4 배포

다시 `Resources` 탭으로 가서 `Actions` -> `Deploy API`를 눌러서 배포를 하자.

![](/images/BinaryResponse.06.png)

그냥 늘 하던데로 `prod`라는 이름으로 배포를 했다.

## 4. 테스트

배포를 하면 **url**이 생성된다.

![](/images/BinaryResponse.07.png)

이 url 뒤에 `/pdf` , `/png` , `/jpg`를 붙여서 호출하여 바이너리 다운로드가 정상적으로 되는지 확인해 보자.

브라우저에서 직접 호출하면 바로 화면에 나타나겠고, `curl` 이나 `POSTMAN`을 사용할려면 `header`에 `Accept`값을 넣어서 호출하면 된다.

> curl -X GET -H “{Accept:application/pdf}”  https://xxx/prod/pdf > test.pdf

POSTMAN의 경우 이미지는 바로 화면에 보여주지만, pdf는 정상적으로 보여주지 못한다.

# Lambda Binary 작업 Tip(?) : Native Module 사용

Lambda로 binary response 작업을 할려면 몇가지만 미리 알아두더라도 삽질(?) 할 시간을 아낄 수 있다.


### Lambda가 실행되는 환경은 Linux 이다. 

[Lambda Execution Environment and Available Libraries](http://docs.aws.amazon.com/lambda/latest/dg/current-supported-versions.html) 에서 정확한 정보를 확인할 수 있다.

### Lambda에 50mb 정도의 디스크 사용이 가능하다.

`/tmp` 폴더내에 파일을 임시로 저장하고 사용하는게 가능하다.  
하지만 Lambda가 warm start로 실행될 경우 이미 만들어진 Lambda를 재사용하므로 해당 폴더에 임시로 만들어 놓은 파일은 계속 남아있게 된다.
임시로 파일을 만들어서 활용할 경우 동일한 이름을 사용해서 항상 덮어쓰거나 아니면 해당 파일을 다 사용한 후에는 지워주는 코드를 넣어주도록 하자.

### Native Module을 사용할 경우

바이너리 응답을 주는 기능 구현을 위해서는 native module을 사용하는 경우가 많다.

native module를 사용한다면, 기본적으로 아래와 같은 과정으로 개발을 할 것이다.

- 해당 native module을 설치한다. (macos의 경우 brew를 사용)
- 해당 모듈의 wrapper npm이 있는지 검색한다.
- 있다면 그걸 활용한다.
- 없다면 직접 shell에서 실행시켜주는 wrapper를 구현해서 사용한다.

이걸 Lambda로 배포하려면 해당 native module을 같이 배포해야한다.  
그래서 아래 과정이 추가된다.

- wrapper npm을 활용한 경우라면 그 소스코드를 살펴보면서 해당 모듈을 시스템 상에 설치된 것을 사용하는지, 아니면 npm으로 설치할때 같이 다운로드 되는지 살펴본다.
- 시스템상 설치된 것을 사용한다면 native module의 실행파일을 압축해 본다.
- 압축 후 용량이 50mb가 넘으면 포기한다. ㅠㅠ
- 50 mb 이하라면 Lambda 를 배포할 폴더 아래에 해당 파일을 복사한다.
- 옮긴 실행 파일을 실행하도록 wrapper를 수정한다.

여기서 반드시 명싱해야 할것은 Lambda의 실행환경은 Linux이다.  

지금 내 개발환경이 macos인 경우 이것을 그대로 Lambda로 배포하면 실행이 안된다.  

해당 native module을 Linux용으로 바꿔서 배포해야한다.

- wrapper npm에서 native module을 같이 다운로드 받게 되어 있다면, 코드를 살펴보자.
  - 분명 OS 타입별로 각각 다른 파일을 다운로드 하는 분기 코드가 있을 것이다. 그걸 보고 Linux용 실행파일을 다운로드 받자.
- 시스템 상에 설치된 실행파일을 사용하는 경우라면 따로 Linux용을 다운로드 받자.
- 로컬에서 테스트로 실행시켜볼 환경과 Lambda로 배포할 환경을 따로 만들어야 한다.
  - 배포 스크립트를 만들면 편하다.
    - 폴더 생성
    - Lambda 코드 복사
    - `npm i --only=production`
    - native module을 linux 용으로 복사
    - 배포

### OS에 따라 Native Module의 결과가 다를 수 있다.

같은 native module이라도 각 OS별로 다르게 동작할 수 있다.  
이 사실을 모르고 결과물을 개발 환경에 맞춰서 진행하다보면 Lambda 배포 후 결과가 다른걸 보고 또 다시 삽질을 해야할 수 있다.
그러니 일단 동작하는게 확인되면 Lambda로 배포한 후 그 결과를 확인해보고 진행하는게 좋다.

## 마치며...

잘못되었거나, 변경된 점, 기타 추가 사항에 대한 피드백은 언제나 환영합니다. - <seokjoon.yun@gmail.com>  
