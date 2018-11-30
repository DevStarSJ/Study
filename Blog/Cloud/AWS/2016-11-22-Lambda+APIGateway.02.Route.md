---
layout: post
title: "AWS Lambda와 API Gateway를 이용해서 Serverless Web API 만들기 (2) - Route"
subtitle:  
categories: cloud
tags: aws
comments: true
---
# AWS Lambda와 API Gateway를 이용해서 Serverless Web API 만들기 (2)

## Routing 예제

Web API를 구현하기 위해서는 여러가지 URL에 대해서 각각 다른 기능을 구현하는것은 필수적입니다.
각각의 URL을 별도의 Lambda로 구현하여 API Gateway에서 연결하는 방법도 있지만 하나의 Lambda에서 처리하는 방법에 대해서 알아 보도록 하겠습니다.
이번에는 전편과는 다르게 약간의 설명을 하면서 진행하겠습니다.
전편의 내용을 안다는 가정하에 진행하겠습니다.
처음 이 글부터 보시는 분들은 아래 Link에서 내용을 숙지한 후에 진행해 주세요.

<https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateWay.01.md>

## API Gateway 설정

아래와 같이 API Gateway를 설정해 주세요.

<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/images/lambda_apigateway.route.01.png?raw=true">


1편에서 설정한 Path를 그대로 두셔도 되지만, **ANY** 에 대해서 연습할겸 모든 Resource, Method를 삭제한 후 다음 단계대로 추가해 주세요.

**ANY**는 모든 http-method (GET, POST, PUT, DELETE, ...) 를 모두 같은 Lambda로 연결하게 해주는 역할을 합니다.
**ANY**와 같은 위치에 다른 method를 추가하면 그것을 제외한 나머지에 대해서만 **ANY**로 연결합니다.
 (ex. **ANY**, **GET**을 같은 위치에 선언하면 **GET**을 제외한 나머지 연결에 대해서는 **ANY**가 처리)

- `/`에서 `Actions` -> `Create Method`를 눌러서 `ANY`를 생성
- `/`에서 `Actions` -> `Create Resource`를 눌러서 `test`를 추가
- `/test`에서 `Actions` -> `Create Resource`를 눌러서 `{userId}`를 추가
- `/{userId}`에서 `Actions` -> `Create Method`를 눌러서 `ANY`를 생성

위까지 한 다음에 `ANY`로 된 2 곳을 각각 눌러서

- **Integration type** : `Lambda Function`
  - **Lambda Region** : 람다를 생성한 지역 서버 선택
  - **Lambda Function** : 람다 명칭 기입
- `Save`를 누른 뒤 화면이 바뀌면
- `Integration Request` 선택
  - `Body Mapping Templates` 선택
    - `Add mapping template` 선택
      - `application/json`이라고 입력한 뒤 적용
        - **Generate template** : `Method Request passthrough` 선택
        - `Save` 선택

**API Gateway**는 수정한 후 반드시 Deploy를 해주어야만 적용이 됩니다.
`Actions` -> `Deploy API`를 선택하면 **Deployment stage**를 입력하여야하는데 기존에 동일한 이름으로 하면 해당 설정을 덮어쓰게 되며,
`[New Stage]`를 선택한 후 다른 이름을 입력하면 기존의 설정상태를 남겨둔체 새로운 이름으로 생성이 가능합니다.
앞에서의 예제에서 **prod**로 생성을 하였는데 이번에는 `test`로 생성해 보겠습니다.
`[New Stage]`를 선택한 후 `test`를 입력하고 `Deploy` 버튼을 누릅니다.

`Invoke URL`에 연결가능한 주소가 나오는데, 기존과 달라진 점이 마지막에 **/prod** 대신에 **/test**가 붙었다는것 밖에 없습니다.
브라우저에서 해당 주소로 접속을 하면 2가지 주소가 다 동작한다는 것이 확인됩니다.
**API Gateway** 상에서도 **Stages** 메뉴로 들어가서 각각의 스테이징 명칭을 누르면 설정된 내용들을 볼 수 있습니다.

## Lambda 의 Node.JS 코드 수정

**API Gateway**에서 여러 경로로 들어오면 요청들을 모두 하나의 **Lambda**로 연결하였으니,
이젠 **Lambda** 상에서 여러 경로에 대해서 각각 다른 기능을 하도록 구현해보겠습니다.

가장 중요한 것이 어떤 경로(`resource-path`)로 들어왔는지 어떤 메서드(`http-method`)로 요청했는지에 대해서 알아야 합니다.
**JSON object**로 전달된 `event` 안에 2가지 정보가 모두 있는데
각각의 위치가 `event.context.resource-path` 와 `event.context.http-method`에 있습니다.
그런데 **-**(dash)가 포함된 명칭이 있어서 **.**(dot)을 이용하여 읽으려면 오류가 발생하므로 
`event.context["resource-path"]` , `event.context["http-method"]` 식으로 접근해야 합니다.
**API Gateway**에서의 template에서 **-**(dash)가 없는 명칭으로 수정한 뒤  **.**(dot)을 이용하여 읽어도 됩니다만
일단 여기서는 기본설정 그대로 진행하겠습니다.

3가지 경로에 대해서 각각 기능을 구현해보겠습니다.

- `/`로 `GET` 요청 : 요청한 **JSON Object**를 그대로 응답
- `/test/{userId}`로 `GET` 요청 : **{ id: userId, name: "test" }**로 응답
- `/test/{userId}`로 `POST` 요청 : **{ id: userId, header: header, body: body }**로 응답

먼저 위 3가지 기능에 대해서 각각 구현을 해보겠습니다.

`/`로 `GET` 요청에 대해서는 앞 장에서 사용했던 코드 그대로 전달을 하면 됩니다.

```JavaScript
  return {"event" : event, "context" : context};
```

`/test/{userId}`로 `GET`, `POST` 요청에 대해서는 각각 `get`, `post`라는 이름의 함수로 생성하겠습니다.

```JavaScript
function get(userId) {
  return {
    body: { id: userId, name: "test" }
  };
}

function post(userId, header, body) {
  return {
    body: { id: userId, header: header, body: body }
  };
}
```

다음 순서로 위 3가지 기능을 담은 **Map**을 생성하겠습니다.
**JavaScript**이기 때문에 그냥 간단하게 **JSON Object**형식으로 생성을 하면 됩니다.
`event.context["resource-path"]` -> `event.context["http-method"]` -> `각각의 기능` 순서대로 접근하면 되도록 생성하였습니다.

```JavaScript
const routeMap = {
  '/': {
    'GET': (event, context) => {
      let  result = {"event" : event, "context" : context}
      return result;
    }
  },
  '/test/{userId}': {
    'GET': (event, context) => {
      const userId = event.params.path.userId;
      return get(userId);
    },
    'POST': (event, context) => {
      const userId = event.params.path.userId;
      const body = JSON.stringify(event["body-json"]);
      const header =  event.params.header;
      return post(userId, header, body);
    }
  }
};
```

이제 실질적으로 **Router**기능을 수행하는 함수를 생성해 보겠습니다.
`event`와 `context`를 전달받아 `routeMap`에서 해당 기능들을 수행하고 그 결과를 다시 전달하는게 이 함수 기능의 전부입니다.

```JavaScript
function router(event, context) {
  const controller = routeMap[event.context["resource-path"]][event.context["http-method"]];

  if(!controller) {
    return {
      body: { Error: "Invalid Path" }
    };
  }

  return controller(event, context);
}
```

이제 모든 기능 구현은 끝났습니다.
**Lambda**의 진입점인 `exports.handler`에서 `router` 함수를 호출해주기만 하면 됩니다.

```JavaScript
exports.handler = (event, context, callback) => {
   let result = router(event, context);
   callback(null, result);
}
```

### 전체 코드

앞에 설명한 내용들을 실제 소스코드로 작성하면 아래와 같이 됩니다.

```JavaScript
'use strict';

function get(userId) {
  return {
    body: { id: userId, name: "test" }
  };
}

function post(userId, header, body) {
  return {
    body: { id: userId, header: header, body: body }
  };
}

const routeMap = {
  '/': {
    'GET': (event, context) => {
      let  result = {"event" : event, "context" : context}
      return result;
    }
  },
  '/test/{userId}': {
    'GET': (event, context) => {
      const userId = event.params.path.userId;
      return get(userId);
    },
    'POST': (event, context) => {
      const userId = event.params.path.userId;
      const body = JSON.stringify(event["body-json"]);
      const header =  event.params.header;
      return post(userId, header, body);
    }
  }
};

function router(event, context) {
  const controller = routeMap[event.context["resource-path"]][event.context["http-method"]];

  if(!controller) {
    return {
      body: { Error: "Invalid Path" }
    };
  }

  return controller(event, context);
}

exports.handler = (event, context, callback) => {
   let result = router(event, context);
   callback(null, result);
}
```

**Lambda**에 위 코드를 입력한 후 저장하면 됩니다.

## 결과 확인

 **API Gateway**의 **Invoke URL**을 이용하여 호출하여 그 결과값을 확인해 보겠습니다.

 - `/`로 `GET` 요청 : **Invoke URL** 을 브라우저에 입력 

 요청 JSON을 그대로 응답한 것으로, 앞장에서 살펴본 예제의 결과와 동일하게 나옵니다.

 - `/test/{userId}`로 `GET` 요청 : **Invoke URL**에 `/test/LunaStar`를 붙여서 브라우저에 입력

 ```JSON
{
  "body": {
    "id": "LunaStar",
    "name": "test"
  }
}
 ```

- `/test/{userId}`로 `POST` 요청 : **POSTMAN**에서 **Invoke URL**에 `/test/LunaStar`를 붙이고 적당히 header, body를 입력하여 요청

```JSON
{
  "body": {
    "id": "LunaStar",
    "header": {
      ...
    },
    "body": "{\"id\":\"123\",\"age\":\"25\"}"
  }
}
```

### 마치며...

이번 포스팅에서 알아본 내용들은 다음과 같습니다.

- **API Gateway**에서 **ANY**를 이용해서 여러가지 **http-method** 요청을 하나의 **Lambda**로 요청하는 방법
- **API Gateway**에서 **Staging**을 나누어 **Deploy**하여 각각의 **Staging**으로 접근하는 방법
- **Lambda**내에서 요청한 **URL** 및 **http-method** 별로 다른 작업을 하는 **Node.JS** 코드 작성법 

잘못되었거나, 변경된 점, 기타 추가 사항에 대한 피드백은 언제나 환영합니다. - <seokjoon.yun@gmail.com>

### 다음글

- Lambda 와 API Gateway 연동 #3 (Proxy Resource) : <https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateway.03.Proxy.md>
