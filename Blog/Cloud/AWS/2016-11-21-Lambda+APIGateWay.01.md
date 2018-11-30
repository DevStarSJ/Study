---
layout: post
title: "AWS Lambda와 API Gateway를 이용해서 Serverless Web API 만들기"
subtitle:  
categories: cloud
tags: aws
comments: true
---
# AWS Lambda와 API Gateway를 이용해서 Serverless Web API 만들기

**[AWS Lambda](https://aws.amazon.com/ko/lambda/details)** 란 코드를 AWS 내에 올려두고 필요할 때에만 해당 코드를 실행해주는 서비스를 말합니다.
서버를 24시간 가동시키게 아니라, 그냥 해당 코드가 실행되면서 사용하는 컴퓨팅 시간에 대해서만 과금을 하는 방식입니다.
즉, 서버없이 서비스를 할 수 있는 편리한 구조면서도 실제로 코드가 동작하는 만큼만 과금이 되다보니 보통의 경우 서버를 띄워놓는거보다 훨씬 저렴한 비용으로 서비가 가능하며 스케일링에 대한 관리를 해줄 필요가 없습니다.

람다에 올려둔 코드는 AWS 내의 다른 서비스에서 이벤트 형식으로 해당 코드가 실행되게 할 수 있는데, **[API Gateway](https://aws.amazon.com/ko/api-gateway)** 를 붙이면 웹서비스로 활용이 가능합니다.

이 두가지 AWS의 서비스를 이용해서 서버없이 API 서비스를 구축하는 튜토리얼을 진행하겠습니다. 아무 생각없이 그냥 따라하시다 보면 그 과정과 원하는 값을 전달하고 받는 것에 대해서 이해가 되실 겁니다.

## Lambda 생성

- `AWS` 로그인 후 `Lambda` 탭으로 이동

<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/images/lambda_apigateway.01.png?raw=true">

- `Create a Lambda Function` 선택

<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/images/lambda_apigateway.02.png?raw=true">

- Select blueprint에서 `Blank Function` 선택

<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/images/lambda_apigateway.03.png?raw=true">

- Configure function 에서 일단 바로 `Next` 선택 (미리 연결할 API Gateway가 있다면 여기서 연결하면 됨)
- `Configure function`에서 함수 정의
  - Name : `testLambda-luna`
  - Runtime : `Node.js 4.3`
  - Code : 아래 코드를 입력
    - 참고로 `callback(null, result);`와 `context.succeed(result);`는 둘 다 결과를 return 해주는 코드로 아무거나 사용해도 됨
  - Role & Existing role : 일단은 적당히 선택 (만약 Lambda에서 다른 AWS 서비스 RDS, S3 등을 연동할려면 필요)
  - 아래 코드 입력 후 `Next` 선택

```JavaScript
'use strict';

exports.handler = (event, context, callback) => {
    let result = {"event" : event, "context" : context}
    context.succeed(result);
    //callback(null, result);
};
```

- `Create Function` 선택
- `Action` -> `Configure test event` 선택
- 원하는 값으로 수정 후 `Save and test` 선택하면 아래와 같이 나옴.

```JSON
{
  "event": {
    "key3": "value3",
    "key2": "value2",
    "key1": "value1"
  },
  "context": {
    "callbackWaitsForEmptyEventLoop": false,
    "logGroupName": "/aws/lambda/testLambda-luna",
    "logStreamName": "2016/11/16/[$LATEST]3906ef41b5df4f1d89c6501dda78253c",
    "functionName": "testLambda-luna",
    "memoryLimitInMB": "128",
    "functionVersion": "$LATEST",
    "invokeid": "be8f2961-aba7-11e6-8ffb-6d91b83819cf",
    "awsRequestId": "be8f2961-aba7-11e6-8ffb-6d91b83819cf",
    "invokedFunctionArn": "arn:aws:lambda:ap-northeast-1:768556645518:function:testLambda-luna"
  }
}
```

- 만약 `name`이란 값을 `event`로 넘겨서 `Hello` + `name` 을 출력하고 싶다면 위 Lambda Code를 아래와 같이 수정



```JavaScript
'use strict';

exports.handler = (event, context, callback) => {
    let result = {"event" : event, "context" : context}
    let name = event.name || 'no name';
    context.succeed('Hello ' + name);
};
```

- 그런 다음 `Configure test event`에 `name`을 넣어주면 아래와 같이 출력됨.

```JSON
{
  "name" : "Luna"
}
```

```
"Hello Luna"
```

## API Gateway 생성 & Lambda 연결

- `AWS` 메인 화면으로 이동 후 `API Gateway` 탭으로 이동

<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/images/lambda_apigateway.04.png?raw=true">

- `Create API` 선택
  - API name : `testAPI-luna`
  - `Create API` 선택
- `Actions` -> `Create Resource` 선택 (API Path를 추가)
  - Resource name : `test`
  - Resource Path : `test`
  - `Create Resource` 선택
- `/test`가 선택된 상태에서 `Actions` -> `Create Resource` 선택
  - Resource name : `name`
  - Resource Path : `{name}` (Path Variable 추가)
  - `Create Resource` 선택
- `/{name}`이 선택된 상태에서 `Actions` -> `Create Method` 선택
  - `GET` 선택 후 확인
    - Lambda Region : 람다를 생성한 region 선택
    - Lambda Function : `testLambda-luna` (좀 전에 생성한 람다명 입력)

<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/images/lambda_apigateway.05.png?raw=true">

  - `Integration Request` 선택
    - `Body Mapping Templates` 선택
      - `Add mapping template` 선택
        - `application/json` 입력
           - `No, use current settings` 선택
        - Generate template: `Method Request passthrough` 선택
          - `Save` 선택
- `/test/{name} [GET]` 선택
  - `TEST` 선택
    - Path {name} : 원하는 값 입력
    - `Test` 버튼 선택
    - 아래와 같이 출력되면 성공

```JSON
{
  "event": {
    "body-json": {},
    "params": {
      "path": {
        "name": "Luna"
      },
      "querystring": {},
      "header": {}
    },
    "stage-variables": {},
    "context": {
      ...
    }
  },
  "context": {
    "callbackWaitsForEmptyEventLoop": true,
    "logGroupName": "/aws/lambda/testLambda-luna",
    ...
  }
}
```

## 배포

- `Actions` -> `Deploy API` 선택
  - Deployment Stage : `[New Stage]` 선택
  - Stage name : `prod` 입력
  - `Deploy` 버튼 선택
  - `Invoke URL` 복사

<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/images/lambda_apigateway.06.png?raw=true">

## 테스트

-  `Invoke URL` + `/test/luna` 로 Web Browser에서 주소 입력
  - 위 **JSON** 같은 모양으로 출력되면 성공
- `Invoke URL` + `/test/luna?id=345;dept=개발팀`과 같이 **QueryString** 을 포함하여 호출
  - 아래와 같이 **querystring** 에서 확인되면 성공

```JSON

{
  "event": {
    "body-json": {},
    "params": {
      "path": {
        "name": "Luna"
      },
      "querystring": {
        "dept": "개발팀",
        "id": "345"
      },
      ...
    }
  }
}
```

## POST로 배포

- `API Gateway`에 `testAPI-luna`로 이동
- `/{name}`이 선택된 상태에서 `Actions` -> `Create Method` 선택
  - `POST` 선택 후 확인
    - Lambda Region : 람다를 생성한 region 선택
    - Lambda Function : `testLambda-luna`
  - 바로 `Test` 버튼을 눌러서 확인
    - Path {name} : 원하는 값 입력
    - Request Body에 아래 **JSON** 값 입력

```JSON
{
  "id": "123",
  "age": "25"
}
```

- 결과

```JSON
{
  "event": {
    "id": "123",
    "age": "25"
  },
  "context": {
    ...
  }
}
```

- `name` 값이 정상적으로 전달되지 않았으므로 `GET` 작업한것 처럼 **template** 설정
  - `Integration Request` 선택
    - `Body Mapping Templates` 선택
      - `Add mapping template` 선택
        - `application/json` 입력
           - `No, use current settings` 선택
        - Generate template: `Method Request passthrough` 선택
          - `Save` 선택
  - `Test` 로 들어가서 위와 같은 `JSON` 입력

```JSON
{
  "event": {
    "body-json": {
      "id": "123",
      "age": "25"
    },
    "params": {
      "path": {
        "name": "Luna"
      },
      "querystring": {},
      "header": {}
    },
    ...
  }
}
```

## 다시 배포

- `Actions` -> `Deploy API` 선택
  - Deployment Stage : `[New Stage]` 선택
  - Stage name : `prod` 입력
  - `Deploy` 버튼 선택
  - `Invoke URL` 복사



## Postman 을 통해서 테스트

- 만약 설치되지 않았다면, Chrome App `Postman` 설치 후 실행
- `POST` 메서드로 선택
- 주소에 `Invoke URL` + `/test/luna?id=345` 입력
- `Headers` 탭 선택
  - `headerValue1` : `123` 입력

<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/images/lambda_apigateway.07.png?raw=true">

- `Body` 탭 선택
  - 위 예제의 **JSON** 입력

<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/images/lambda_apigateway.08.png?raw=true">

- `Send` 선택
- 결과

```JSON
{
  "event": {
    "body-json": {
      "id": "123",
      "age": "25"
    },
    "params": {
      "path": {
        "name": "luna"
      },
      "querystring": {
        "id": "345"
      },
      "header": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4",
        ...
        "Content-Type": "application/json",
        "headerValue1": "123",
        ...
      }
    },
    "stage-variables": {},
    "context": {
      ...
      "http-method": "POST",
      ...
      "source-ip": "112.217.228.202",
      "user": "",
      "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
      ...
      "resource-path": "/test/{name}"
    }
    }
  },
  "context": {
    ...
  }
}
```

## 활용

- `Lambda`에서 전달받은 값 활용
  - `event`
    - `body-json` : BODY에서 전달해온 값
    - `params`
      - `path` : URL 상에서 경로로 얻어오는 변수들
    - `header` : HEADER에서 전달해온 값
    - `querystring` : URL 상의 QueryString로 전달된 변수들
    - `context`
      - `http-method` : 호출한 METHOD (GET, POST, ...)
      - `resource-path` : 하나의 Lambda에서 여러 URL을 처리할 경우 경로 정보

## 참고

- 아웃사이더님 Blog : <https://blog.outsider.ne.kr/1205> , <https://blog.outsider.ne.kr/1206>
- AWS : <http://docs.aws.amazon.com/ko_kr/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html>


- 원문 : <https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateWay.01.md>

잘못되었거나, 변경된 점, 기타 추가 사항에 대한 피드백은 언제나 환영합니다. - <seokjoon.yun@gmail.com>

### 다음글

- Lambda 와 API Gateway 연동 #2 (ANY, Deploy Staging, Node.JS Route) : <https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateway.02.Route.md>
