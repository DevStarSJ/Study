---
layout: post
title:  "AWS Lambda에 Python Handler 만들기"
subtitle:  
categories: cloud
tags: aws
comments: true
---

# AWS Lambda에 Python Handler 만들기

AWS Lambda 관련 5번째 포스트 입니다.  
지난 글들의 목록은 다음과 같습니다.

- [Lambda 와 API Gateway 연동 #1 (GET, POST)](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateWay.01.md)
- [Lambda 와 API Gateway 연동 #2 (ANY, Deploy Staging, Node.JS Route)](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateway.02.Route.md)
- [Lambda 와 API Gateway 연동 #3 (Proxy Resource)](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateway.03.Proxy.md)
- [Lambda Node.JS Packaging](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda.Packaging.Node.md)

이번에는 **Python**으로 구현해 보겠습니다.

## Previously on Lambda series

[Lambda 와 API Gateway 연동 #3 (Proxy Resource)](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateway.03.Proxy.md)까지 진행되었다는 가정하에 진행하겠습니다.  
아직 위 내용들을 보지 않으셨던 분은 아래대로 따라하시면 준비가 끝납니다.

그 과정을 간략하게 살없이 뼈만 간추리면 다음과 같습니다.
관련 내용은 위 포스트 들을 참조해주세요.
그냥 읽어봐서 이해가 안되신다면 한 번 아무생각없이 따라해 보시면 이해가 되실겁니다.

### Create Lambda

- `AWS` 로그인 후 `Lambda` 탭으로 이동
- `Create a Lambda Function` 선택
- Select blueprint에서 `Blank Function` 선택
- Configure function 에서 일단 바로 `Next` 선택 (미리 연결할 API Gateway가 있다면 여기서 연결하면 됨)
- `Configure function`에서 함수 정의
  - Name : `testLambda-luna`
  - Runtime : `Node.js 4.3`
  - Code : 일단 아무거나 입력
  - Role & Existing role : 일단은 적당히 선택 (만약 Lambda에서 다른 AWS 서비스 RDS, S3 등을 연동할려면 필요)
  - 아래 코드 입력 후 `Next` 선택
- `Create Function` 선택

### Set API Gateway

- `AWS` 메인 화면으로 이동 후 `API Gateway` 탭으로 이동
- `Create API` 선택
  - API name : `testAPI-luna`
  - `Create API` 선택
- `/`에서 `Actions` -> `Create Resource`를 선택
  - `Configure as proxy resource` 를 체크한 후 `Create Resource`를 누름
- `ANY` 선택
  - `Integration Request` 선택
    - **Integration type** : `Lambda Function`
      - **Lambda Region** : 람다를 생성한 지역 서버 선택
      - **Lambda Function** : 람다 명칭 기입
- `Actions` -> `Deploy API` 선택 후 그냥 `prod`로 스테이징

## Hello Python Lambda Handler

먼저 가장 기초적인 핸들러를 작성해보록 하죠.

앞서 생성한 **Lambda** 설정에 들어가셔서

- `Configuration` 탭
  - **Runtime** : `Python 2.7` 선택
  - **Handler** : `index.handler`라고 되어 있는지 확인
- `Code` 탭 으로 와서 아래 코드 입력  

```Python
def handler(event, context):
    return { 'event': str(event), 'context': str(context) }
```

그런 다음 **API Gateway**의 주소를 브라우저에서 입력하면 오류가 발생합니다.
주소 확인하는 법은 **API Gateway** 설정에서 **Stages**를 눌러서 해당 스테이징(**prod**)를 선택하면 **Invoke URL**에 표시됩니다

그 이유는 현재 `{proxy+}` 이하로는 **ANY**로 설정된게 있는데 `/`에는 아무것도 설정된게 없기 때문입니다.

- 좌측 해당 항목에서 `Resources`로 이동
  - `/`에서 `Actions` -> `Create Method`를 눌러서 `ANY`를 생성
    - 생성된 `ANY`를 눌러서
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

**API Gateway**는 설정 변경 후 반드시 **Deploy**해줘야만 적용됩니다.

- `Actions` -> `Deploy API` 선택 후 그냥 `prod`로 스테이징

이제 다시 **Invoke URL**로 접속하면 뭔가 화면에 결과가 나타나는 것을 볼 수 있습니다.

`{"event": "{u'body-json': {}, u'params': {u'path': {}, u'querystring': {}, ...}`

뭔가 이런 지저분한 모양입니다. `u`라고 따옴표 앞에 붙은것을 다 지우고 홀따옴표(`'`)를 쌍따옴표(`"`)로 수정한 뒤 **JSON** 모양으로 나타내 보면 아래와 같이 됩니다.
우리가 필요한 항목들만 적어봤습니다.

```JSON
{
  "event": {
    "body-json": {},
    "params": {
      "path": {},
      "querystring": {},
      "header": {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
      }
    },
    "stage-variables": {},
    "context": {
      "http-method": "GET",
      "resource-path": "/",
      "source-ip": "112.217.228.202",
    }
  },
  "context": "<__main__.LambdaContext object at 0x7f629a39aa10>"
}
```

**Node.JS**와 똑같은 모양으로 나옵니다.  
`context`는 뭔가 `dict`타입이 아니라서 그대로 출력이 되지 않는군요.
공식문서 (<http://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html>)를 보시면 `context` 오브젝트에 대한 자세한 내용이 나옵니다.

이제 기본 **Invoke URL** 뒤에 `/test?id=2`라고 적은 뒤 브라우저로 요청을 해보겠습니다.  

당연히 오류가 발생합니다.

`{proxy+}`로 요청하는 데이터의 형식도 다르며 여기에 대한 응답은 **JSON** 오브젝트 **body**에 **JSON** 형식의 문자열로 전달해야 합니다.

**Lambda**쪽 코드를 아래와 같이 수정 후 다시 요청해보면 정상적으로 답변이 오는 것이 확인 됩니다.  

**POSTMAN**을 통해서 `POST`로 요청을 해도 정상적으로 답변이 오는 것을 볼 수 있습니다.
(**JSON** 객체형태가 아니기 때문에 출력 형식을 **Text**로 해야 보입니다.)

그래서 JSON 형식으로 응답하도록 코드를 조금 수정해 봤습니다.

```Python
import json

def handler(event, context): 
    return { 'body' : json.dumps(event) }  
```

이제는 **JSON** 오브젝트로 응답하므로 **POSTMAN**에서도 바로 결과를 볼 수 있습니다.

## Python Routing Example

조금 더 복잡한 예제를 작성해 보겠습니다.
예제의 내용은 **Node.JS**로 진행한 예제와 같은 것입니다.

`/test?id=?` 라는 주소로 `GET`, `POST`요청에 대해서 각각 다른 작업을 하는 코드를 작성해 보겠습니다.

각각 함수에 대한 설명은 [Lambda 와 API Gateway 연동 #2 (ANY, Deploy Staging, Node.JS Route)](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateway.02.Route.md) 포스팅을 참고해 주세요.

바로 코드 들어갑니다.

```Python
import json

def get(event):
    user_id = event['queryStringParameters']['id']
    return { 'body': { 'id': user_id, 'name': "test" } }

def post(event):
    user_id = event['queryStringParameters']['id']
    body = event['body']
    header = event['headers']
    return { 'body': { 'id': user_id, 'header': header, 'body': body } }

route_map = {
    '/test': {
        'GET': get,
        'POST': post
    }
};

def router(event):
    controller = route_map[event['path']][event['httpMethod']];
    
    if not controller:
        return { 'body': { 'Error': "Invalid Path" } }
    
    return controller(event);

def handler(event, context):
    result = router(event);
    return { 'body' : json.dumps(result) }
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

**Node.JS** 와 똑같은 결과로 출력되는 것이 확인 가능합니다.

### 마치며...

**Python Packaging**는 나누어서 다음 포스팅에 작성하겠습니다.
간략하게 방법을 설명드리지만 `virtualenv`로 작업 환경을 만든 뒤 `pip install 모듈명 -t 프로젝트폴더`로 작업폴더에 모듈을 설치한 뒤 `.zip`파일로 압축하여 올리시면 됩니다.
(**Node.JS Packaging**과 크게 다르지 않습니다.)

이번 포스팅에서 알아본 내용들은 다음과 같습니다.

- **Lambda**에 **Python** 코드로 핸들러 작성
- **Python**에서 **API Gateway**의 `{proxy+}`요청에 대하여 구분해서 작업하는 방법

잘못되었거나, 변경된 점, 기타 추가 사항에 대한 피드백은 언제나 환영합니다. - <seokjoon.yun@gmail.com>  

### 참고

- AWS 공식 가이드 : <http://docs.aws.amazon.com/lambda/latest/dg/python-programming-model-handler-types.html>

### 다음글

- [Lambda Python Packaging](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda.Packaging.Python.md)

