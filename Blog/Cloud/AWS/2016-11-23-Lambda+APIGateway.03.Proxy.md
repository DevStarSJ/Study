---
layout: post
title: "AWS Lambda와 API Gateway를 이용해서 Serverless Web API 만들기 (3) - Proxy"
subtitle:  
categories: cloud
tags: aws
comments: true
---
# AWS Lambda와 API Gateway를 이용해서 Serverless Web API 만들기 (3)

## API Gateway Proxy Resource 활용

**API Gateway**에서 각각의 route path(API Gateway에서는 Resource로 불림) 및
http-method(API Gateway에서는 Method로 불림)에 대해서 **Lambda**를 설정하는 것은 여간 번거러운 작업이 아닙니다.
그 경우에 따라 각각 다른 **Lambda**로 연결이 되는 경우라면 당연히 따로 설정을 해야하지만,
하나의 **Lambda**로 연결하는 경우에 대해서라면 필요없는 번거로운 작업이 될 수도 있습니다.
앞 장에서 http-method에 대해서는 **ANY**를 이용해서 같은 **Lambda**로 모두 연결이 가능하도록 작성하였는데,
이번 장에서는 **Proxy Resource**를 이용해서 모든 Resource 및 Method를 같은 Lambda로 연결하는 방법에 대해서 익혀보겠습니다.

전편의 내용을 안다는 가정하에 진행하겠습니다.
처음 이 글부터 보시는 분들은 아래 Link에서 내용을 숙지한 후에 진행해 주세요.

- Lambda 와 API Gateway 연동 #1 (GET, POST) : <https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateWay.01.md>
- Lambda 와 API Gateway 연동 #2 (ANY, Deploy Staging, Node.JS Route) : <https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateway.02.Route.md>

## API Gateway 에 Proxy Resource 등록

먼저 **API Gateway**에 등록된 모든 Resource 및 Method를 삭제한 뒤 다음 단계로 진행해주세요.

- `/`에서 `Actions` -> `Create Resource`를 선택
  - `Configure as proxy resource` 를 체크한 후 `Create Resource`를 누름

<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/images/lambda_apigateway.proxy.01.png?raw=true">

그럼 다음 그림과 같이 설정 됩니다.

<img src="https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/images/lambda_apigateway.proxy.02.png?raw=true">


- `ANY` 선택
  - `Integration Request` 선택
    - **Integration type** : `Lambda Function`
      - **Lambda Region** : 람다를 생성한 지역 서버 선택
      - **Lambda Function** : 람다 명칭 기입

모든 설정이 끝났습니다.  
앞에서 해왔던 설정 중 mapping template를 설정하지 않았습니다.  
해당 설정을 하는 곳을 찾지 못했습니다.  
그게 없으면 요청이 어떤 모양으로 오는지 알기 힘든데...  
그냥 **Lambda**에서 출력해 보겠습니다.

**API Gateway**를 수정했으면 ???  
잊지말고 **Deploy**를 해줘야 적용됩니다.

- `Actions` -> `Deploy API` 선택 후 그냥 `prod`로 스테이징

## Lambda에서 요청을 그대로 출력

2편에서 작성한 코드를 그대로 두고 우선 실행해보도록 하겠습니다.
**API Gateway**의 **Invoke URL**을 그대로 브라우저에서 입력하니 오류가 발생합니다.


```JSON
{"message":"Missing Authentication Token"}
```

어라... 안되네요.

다른 분에게 도움을 요청하였더니, body에 JSON 형식의 string을 담아서 응답을 보내야 한다고 합니다.
네. 그렇답니다...

<http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-set-up-simple-proxy.html>

위 공식문서에 가면 자세한 내용이 있습니다.

그래서 다음과 같이 **hander**를 수정 후 실행해 보았습니다.

```JavaScript
exports.handler = (event, context, callback) => {
   let result = router(event, context);
   //let result = {"event" : event, "context" : context}
   callback(null, {body:JSON.stringify(result)});
}
```

결과는 똑같이 안됩니다. ;;;  
음... 그냥 요청을 그대로 출력해 보겠습니다.

```JavaScript
exports.handler = (event, context, callback) => {
   //let result = router(event, context);
   let result = {"event" : event, "context" : context}
   callback(null, {body:JSON.stringify(result)});
}
```

왜 안될까 생각을 해보니... **API Gateway**상에 설정을 보면 `/`에는 아무런 method가 추가되어 있지 않고 `/{proxy+}`에 **ANY**가 등록되어 있습니다.
**Invoke URL**에 뭐라도 더 붙여서 보내니깐 정상적으로 동작합니다.

```
https://..../prod/test
```

뭔가 답변이 나옵니다.
좀 더 다양한 정보를 보기 위해서 쿼리스트링도 포함하여 보낸 다음 **JSON**을 살펴보도록 하겠습니다.

```
https://..../prod/test?id=123;name=Luna
```

```JSON
{
    "event": {
        "resource": "/{proxy+}",
        "path": "/test",
        "httpMethod": "GET",
        "headers": {
            ...
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        },
        "queryStringParameters": {
            "name": "Luna",
            "id": "123"
        },
        "pathParameters": {
            "proxy": "test"
        },
        "stageVariables": null,
        "requestContext": {
            ...
            },
            "resourcePath": "/{proxy+}",
            "httpMethod": "GET",
        },
        "body": null,
        "isBase64Encoded": false
    },
    "context": {
        ...
    }
}
```

2장 라우팅에서 사용한 변수들의 이름이 바뀌어 있습니다.
위 모양을 보고 그대로 수정을 해주면 되겠네요.
**POST**로 **body**값을 추가하여 보내보도록 하겠습니다.

```JSON
{
  "event": {
    "resource": "/{proxy+}",
    "path": "/test",
    "httpMethod": "POST",
    ...
    "queryStringParameters": {
      "name": "Luna",
      "id": "123"
    },
    "pathParameters": {
      "proxy": "test"
    },
    ...
    "body": "{\n  \"id\": \"123\",\n  \"age\": \"25\"\n}",
    ...
  }
  ...
}
```

## Lambda 코드 수정

위 결과를 보고 2장과 똑같은 기능을 하도록 **Lambda** 쪽의 **Node.JS**코드를 수정하려고 생각해보니
`/test/{userId}`와 같이 path parameter를 감안하여 path를 생성해주지 않으므로 그대로는 사용을 못하겠고 다르게 처리를 해줘야 합니다.
path parameter를 사용하지 않고 query string을 이용하는 방법도 있겠구요. 아니면 해당 패턴이 되도록 비교문을 이용해서 라우팅해야 합니다.

편의상 query string을 사용하도록 수정하였으며 `/`로 접근하던 부분은 삭제하였습니다.
코드에 대한 자세한 설명은 2장 포스팅을 참조해 주세요.

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
  '/test': {
    'GET': (event, context) => {
      const userId = event.queryStringParameters.id;
      return get(userId);
    },
    'POST': (event, context) => {
      const userId = event.queryStringParameters.id;
      const body = JSON.stringify(event.body);
      const header =  event.headers;
      return post(userId, header, body);
    }
  }
};

function router(event, context) {
  const controller = routeMap[event.path][event.httpMethod];

  if(!controller) {
    return {
      body: { Error: "Invalid Path" }
    };
  }

  return controller(event, context);
}

exports.handler = (event, context, callback) => {
   let result = router(event, context);
   callback(null, {body:JSON.stringify(result)});
}
```

## 결과 확인

- **GET** 요청 : `https://.../prod/test?id=2`

```JSON
{"body":{"id":"2","name":"test"}}
```

- **POST** 요청 : URL은 **GET**과 동일

```JSON
{
  "body": {
    "id": "2",
    "header": {
      ...
    },
    "body": "\"{\\n  \"id\": \"123\",\\n  \"age\": \"25\"\\n}\""
  }
}
```

## 마치며...

이번 포스팅에서 알아본 내용들은 다음과 같습니다.

- **API Gateway**에서 **{proxy+}**를 여러가지 **path**와 **http-method** 요청을 하나의 **Lambda**로 요청하는 방법
- **{proxy+}**로 접근할 경우 **Lambda**에서 필요한 요청값들의 변수명 

잘못되었거나, 변경된 점, 기타 추가 사항에 대한 피드백은 언제나 환영합니다. - <seokjoon.yun@gmail.com>  

### 다음글

- Lambda Node.JS Packaging : <https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda.Packaging.Node.md>
