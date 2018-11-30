---
layout: post
title: "aws-serverless-express 소개"
subtitle:  
categories: cloud
tags: aws
comments: true
---

# aws-serverless-express 소개

## aws-serverless-express ?

[aws-serverless-express](https://github.com/awslabs/aws-serverless-express) ?  
이름부터 좀 괴랄하다.  

- aws : [Amazon Web Service](https://aws.amazon.com)
- aws-serverless : AWS에서 제공해주는 serverless니깐 [AWS Lambda](https://aws.amazon.com/lambda/details) 라고 추측이 가능하다.
- aws-serverless-express: AWS Lambda에서 Express를 ? Node.js의 Web Framework인 그 [Express](http://expressjs.com)인가 ?

그 Express가 맞다.

**aws-serverless-express**는 기존에 Express로 동작하는 Web App을 그대로 AWS Lambda에서 동작하게 하는 Framework이다.

## aws-serverless-express 왜 써야하지 ?

**aws-serverless-express**는 어떤 장점이 있길래 써야 할까 ?
여기에 대해서 곰곰히 생각해보았다.

솔직히 **AWS Lambda**에 대해서 그 동안 쭉 작업을 해온 입장에서 **aws-serverless-express**로 작업을 처음 했을때 드는 생각은 다음과 같았다.

- 사용 전
  - 이거 없이도 이미 잘 쓰고 있다.
  - 굳이 **aws-serverless-express**를 왜 써야하는지 모르겠다.
- 사용 후
  - 이미 작성해 놓은 코드 들이 싹~ 필요없어 진다.
    - Route 기능
    - event를 전달받아서 해주는 전처리 기능들
    - Lambda Proxy Integration에 대한 구조들
    - Binary Response를 위해서 base64로 encoding하는 작업들
  - 기존에 Test를 위해서 **Lambda**에서 **API Gateway**로 부터 전달받은 **event**를 `console.log`를 이용해서 **CloudWatch**에 출력한 후 그걸 Local PC에 저장해두고 수정해가면서 했었는데, 일단 이걸 이제는 못쓰게 된다.
  - handler의 3번째 인자인 `callback`이 사라졌다. 기존 코드들 응답하는 것들을 다 수정해야 한다. 오류에 대한 처리 코드들 역시 다 수정해야 한다.

이 정도가 작업을 처음 했을때 드는 생각이었다.
이건 내 생각이었고, 그럼 그 특징들에 대해서 느낀 점들은 다음과 같다.

### 1. **Express**로 작성된 코드들을 전혀 고치지 않고 **AWS Lambda**에서 동작하도록 하는게 가능하다.

정말이다. **aws-severless-express**를 `npm`으로 설치하고 예제에서 제공해주는 `lambda.js`만 추가하면 끝이다. 
단, 기존의 `app.js` 파일을 `app.js`, `app.local.js`로 나누어야 한다.
`app.js`에는 app 설정 및 route 지정에 대한 내용만 남겨두고, `app.listen(port)` 이 한 줄만 `app.local.js`로 옮겨 놓으면 된다.
`lambda.js`와 `app.local.js`는 프로젝트마다 차이가 거의 없는 고정된 코드로 만들어도 될 정도로 아주 간단하다.

### 2. **AWS Lambda**의 event 구조에 대해서 알필요 없이 **Express**의 **Request**에서 필요한 값들을 읽어서 작업하면 된다.

기존에 **AWS Lambda**에서 작업할 경우 Template로 event를 정의한 경우 아래와 같은 형태로 전달된다.
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

하지만 요즘은 대부분 **Lambda Proxy Integration**를 사용하기 때문에 주로 아래와 같은 형태의 event를 전달받는다.

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

**AWS Lambda**에서 작업하기 위해서는 이런 구조들에 대해서 파악을 하고 작업을 해야한다.
**aws-serverless-express**에서는 이런것에 대해서 알 필요가 없이 Framework단에서 이런 event를 **Express**의 **Request** 타입으로 전달해준다.
**Lambda**에서 작업하기 위해서 event 형태에 대해서 배울 필요가 없어진다.
**Node.js** 개발자들이 **AWS Lambda** 개발을 하기위한 러닝커브가 많이 줄어든 것이다.

**Request** 뿐만 아니라 **Response** 또한 **Express**와 동일하게 작업이 가능하다.
Error 발생 사항에 대한 statusCode 전달 형태, Binary Response일 경우 Base64로 Encoding하여 body에 string 형태로 저장 등 Lambda만의 방식으로 작업을 할 필요가 없어진다.

### 3. **AWS Lambda**에 Deploy하지 않고도 Local PC에서 **Express**로 실행시켜서 API 테스트가 가능하다.

기존에는 Lambda Handler 함수에 **event, context, callback** 인자를 테스트용으로 생성하여 만들어서 전달하는 식으로 테스트를 하였다.
**event**는 실제 Lambda 상에서 CloudWatch로 출력한 내용을 복사한 뒤 그걸 수정하여 별도 *JSON* 파일로 저장을 하여서 활용을 하였으며,
**callback**은 2번째 인자로 전달받은 값을 화면에 `JSON.stringify`로 이쁘게 출력해주는 식으로 작성을 하여서 전달하였다.
**context**는 아에 사용을 하지 않아서 그냥 `null`로 전달하였다.
이런 식으로 실행을 해가면서 테스트를 했었는데, **aws-serverless-express**를 사용할 경우에는 그냥 `app.local.js`를 실행해서 **Express** 서버를 띄운 뒤 *Web Browser*나 *Postman*, *crul* 등으로 Request가 가능해진다.

위 3가지 특징들로 인하여 **AWS Lambda** 경험이 전혀 없는 **Node.js**의 **Express**로 Web Server를 개발하던 분들이 쉽게 작업이 가능해진다. 관련 개발자를 구하기도 좀 더 쉬워질 것이다.

위 특징은 **AWS Lambda**를 경험한 적이 없는 사람의 경우에 와닿는 이야기다. 그럼 **AWS Lambda**에서 작업이 능숙한 사람들 입장에서 한번 보자.

### 1. Route 코드 작업을 직접하지 않아도 된다.

**Express** 방식을 그대로 사용하면 된다.
**API Gateway**에서 `{proxy+}` 설정 방법에 따라 전달되는 `event`의 path parameter 가 달라지는 것도 신경쓰지 않아도 된다.
엄밀히 말하면 신경쓰지 않아도 되는거라기 보다는 **Express** 방식대로 작업하면 된다.

내가 작성한 코드가 많이 사라진다는건 어떤 의미일까 ?
이미 많은 사람들에게 검증된 코드들의 비중이 올라가고 내가 직접 작성한 코드가 적어지면 그만큼 버그 발생 가능성도 줄어드는 것으로 봐도 된다.
여기에 대해서는 반대 의견도 많긴 하지만, 이건 각자 판단에 맡기겠다.
이러한 기반 동작에 대한 코드들에 대해서 신경을 덜쓰고 그만큼 서비스 코드들에 대해서 더 작업 및 테스트 시간을 할애할수 있으면 더 좋지 않을까 ?

그럼에도 불구하고, 별로 그러기 싫다면 ??? 기존에 작업해 놓은 코드들을 수정하기가 죽어도 싫다면 ???

`Request.headers.x-apigateway-event`에 **API Gateway**의 event 값이 urlencoded 상태로 저장되어 있다.

```
'x-apigateway-event': '%7B%22resource%22%3A%22%2Fic%2F%7Bproxy%2B%7D%22%2C%22path%22%3A%22%2Fic%2Fusers%2F146150%2Fphotos%2Fuploads%2F0dce50a5319e92ee0700becde219bf0700003138.JPG%22%2C%22httpMethod%22%3A%22GET%22%2C%22headers%22%3A%7B%22Accept%22%3A%22text%2Fhtml%2Capplication%2Fxhtml%2Bxml%2Capplication%2Fxml%3Bq%3D0.9%2Cimage%2Fwebp%2Cimage%2Fapng%2C*%2F*%3Bq%3D0.8%22%2C%22Accept-Encoding%22%3A%22gzip%2C%20deflate%2C%20br%22%2C%22Accept-Language%22%3A%22ko-KR%2Cko%3Bq%3D0.8%2Cen-US%3Bq%3D0.6%2Cen%3Bq%3D0...
```

그냥 이걸 decoding하여 기존 코드에 event로 전달하면 된다.

### 2, Response 쪽 코드는 바뀌어야 한다.

이건 어쩔수 없다. 기존 `callback`을 사용할 수 있는 방법은 없다. 그럼에도 불구하고 기존 코드를 고치기 싫다면 **Express**의 **Response**를 이용해서 응답하는 `callback` 함수를 직접 만들어서 기존 handler로 전달해라. 선택은 본인의 몫이다.

**Binary Response**에 대해서 base64로 encode한 string값을 body에 저장하여 callback 함수의 2번째 인자로 전달하는게 편하면 그렇게 하면 된다.

#### Lambda의 Binary Response
```JavaScript
const content = fs.readFileSync(result.filename);
const response = {
    statusCode: 200,
    headers: {
        "Content-Type": result.contentType
    },
    body: new Buffer(content).toString("base64"),
    isBase64Encoded: true
}
callback(null, response);
```

#### Express의 Binary Response
```JavaScript
res.header('Content-Type', result.contentType)
   .sendFile(result.filename);
```

어느 코드가 더 작성도 편하고, 읽기도 편하게 보이는가 ?

### 3. Error 처리 코드를 변경할 수 있다.

이건 변경되어야 하는게 아니라 변경 할 수 있다고 썼다.
그렇다고 기존 `callback`을 그대로 쓸수 있다는 말은 아니다.

기존에 `callback`을 계속 인자로 전달하여 Error가 발생한 곳에서 실행을 했던 코드라면 `callback` 대신 `Response`를 계속 전달하여 `res.status(500).json({});`로 수정하면 된다.

Error를 최상단의 `catch { ... }`로 전달 받은뒤 처리하는 형태였다면 그것 역시 `callback`대신 `Response`로 변경하는 작업만 해주면 된다.

**Express**에는 이 방법 외에도 `app.use`에 Middleware로 등록해 놓는 것도 가능하다.

```TypeScript
app.use((err, req: Request, res: Response, next: NextFunction) => {
    console.info("error status = ", err.status);
    if (err.status && err.status < 500) {
        console.info("ExpectedError = " + err);
        res.status(err.status).json(err);
    } else {
        console.info("InternalServerError = " + err);
        if (!err)
            err = {status:599}
        raygun.Send(err);
        res.status(err.status).json(err);
    }
});
```

위 코드 형식으로 `app.js` 또는 `app.ts`에 등록해 두고 모든 Error를 여기서 처리하는 것도 가능하다.
단, 해당 app의 **Route**를 사용하는 것에 대해서만 처리가 가능하다. 만약 **Route** 되는 과정에서 따로 **class**를 생성하여 자체 **Route**를 가지는 곳으로 **Request**를 전달하여 처리하는 형태로 작성된 코드라면 해당 **Route**상의 Middleware로 등록하여야 한다.
어느게 더 좋은 방식이라는건 없다. 이건 설계의 문제이기 때문에 거기에 따라서 작업을 하면 된다.

<http://expressjs.com/guide/error-handling.html>에 Express Error Handling에 대한 내용이 있긴한데 그리 자세하지는 않다.

### 4. API Gateway StageVariable 사용이 조금 불편해진다.

이건 **Express**에는 없는 개념이라 어쩔 수 없다.
위에도 잠깐 언급했듯 `Request.headers.x-apigateway-event`에 **API Gateway**의 event 값이 urlencoded 상태로 저장되어 있다.
이 값을 다시 decode하여 `stageVariables`의 값을 읽어야 한다.

### 5. Lambda의 Environment variables는 쉽게 사용이 가능하다.

`.env`라는 파일에 `KEY=VALUE` 형태로 값들을 저장해 놓은 뒤 아래와 같이 사용이 가능하다.

```TypeScript
import * as dotenv from "dotenv";
dotenv.config({ path: ".env" });
const a = process.env.KEY;
```

그럼 Lambda 상에서와 동일하게 세팅해두고 Local PC에서 테스트가 가능하다.

## 3. 예제 코드

예제 코드를 따로 작성하려고 생각했었는데, 제공해주는 예제 코드가 너무나도 괜찮아서 따로 작성하지는 않겠다.

<https://github.com/awslabs/aws-serverless-express/tree/master/example>

위 Link 예제를 다운받아서 실행하면서 코드를 보면 쉽게 이해가 된다.

**Lambda** 배포시 실행할 함수를 `lambda.handler`로 설정해야 한다.

Local PC에서 테스트 할때는 `app.local.js`를 실행하면 된다.

```
node app.local.js
```

Error Handling 부분이 빠져 있는데, 그건 위에 설명하면서 적어놓은 코드 조각으로 충분할 거라 생각된다.

API Gateway 와 Lambda의 연결에 대해서는 예전에 포스팅 해놓은 글을 참고해 주길 바란다.

- [Lambda 와 API Gateway 연동 #1 (GET, POST)](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateWay.01.md)
- [Lambda 와 API Gateway 연동 #2 (ANY, Deploy Staging, Node.JS Route)](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateway.02.Route.md)
- [Lambda 와 API Gateway 연동 #3 (Proxy Resource)](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateway.03.Proxy.md)

그냥 `{proxy+}`로 배포를 하면 된다. path 별로 다른 **Lambda**를 실행하고 싶을 경우에도 기존과 동일하게 작업하면 된다.

## 4. TypeScript로 작성할 경우 참고할 내용들

주로 작업을 **TypeScript**로 많이 하는 편이라 거기에 관련된 Tip들만 몇개 적어보겠다.

### 1. **Express**용 Type에 대해서 정의하고 싶을 경우

express의 types를 설치

```
npm install @types/express --save-dev
```

```TypeScript
import {Router , Request , Response , NextFunction}  from 'express';
import * as express from 'express';
import * as asyncify from "express-asyncify";

const app = asyncify(express());
export default app;

app.get('/v1/*', index);

app.get('/v2/*', (req: Request, res: Response, next: NextFunction) => {
    req.query.version = v2;
    next();
}, index);

async function index(req: Request, res: Response, next: NextFunction) {
    ...
}
```

위 코드와 같은 Type을 사용할 수 있다.

### 2. 예제 js 코드를 ts로 고칠 경우 requre -> import로 수정

```JavaScript
const express = require('express')
```

위 코드와 동일하게 동작하게 하려면 아래와 같이 수정해야 한다.

```TypeScript
import * as express from 'express';
```

패키지로 제공받는 코드의 경우는 저렇게 사용하면 되며, 내가 작성한 코드는 `default` 키워드를 이용 할 수 있다.

#### app.ts
```TypeScript
import {Request , Response , NextFunction}  from 'express';
import * as express from 'express';
import * as asyncify from "express-asyncify";
import * as cors from 'cors';

const app = asyncify(express());
export default app;

...
```

#### lambda.ts
```TypeScript
import * as awsServerlessExpress from 'aws-serverless-express';
import * as awsServerlessExpressMiddleware from 'aws-serverless-express/middleware';
import app from './app';

const binaryMimeTypes = [
    'application/json',
    'image/jpeg',
    'image/png',
    'image/jpg',
    'image/webp'
];

app.use(awsServerlessExpressMiddleware.eventContext());
const server = awsServerlessExpress.createServer(app, null, binaryMimeTypes);
export const handler = (event, context) => awsServerlessExpress.proxy(server, event, context);
```

#### app.local.ts
```TypeScript
import app from './app';
const port = 3000;

app.listen(port);
console.log(`listening on http://localhost:${port}`)
```

위에 적어놓은 `app.local.ts`, `lambda.ts`는 거의 수정할 필요가 없다.
단 `lambda.ts`에서 `binaryMimeTypes`는 제공해주는 `Content-Type`에 맞게 추가 및 삭제하면 된다.

`app.ts`의 경우에도 해당 코드 아래에 `app.use`를 통한 Middleware 설정 및 `app.get`, `app.post` 등의 Route 설정을 하면 된다.

## 마치며...

그 동안 **AWS Lambda** 관련 작업을 많이해서 사실상 **aws-serverless-express** 없이도 작업하는데 큰 불편함이 없었다.
처음에는 **Lambda**에 배포하지 않고도 Local PC에서 Browser로 접속해서 테스트가 가능하는 점에서 시작하였다.
작업을 조금씩 하다보니 예전에 작성해 놓은 코드들이 많이 삭제되어야 해서 시원섭한한 느낌적인 느낌을 받았으며,
**Express** 형태에 맞게 수정되어야 할 코드들이 많이 생겨서 여간 귀찮은게 아니었다.
하지만 삭제 및 수정되어야 할 코드들은 대부분 중요한 로직 코드가 아니라서 앞으로 유지보수 차원에서 생각하자면 오히려 앞으로 코드 읽기도 편해지고, 버그가 발생한 가능성이 있는 코드를 보는 측면에서 생각하더라도 훨씬 봐야할 코드 량이 줄어들게 된다.

난 사실 **Express**에 대한 경험이 없고 바로 **Lambda**로 **Node.js** 및 **TypeScript** 작업을 처음 시작한 경우인데, **aws-serverless-express**를 사용하면서 **Express**를 경험하게 되어서 이제 **Express**를 이용한 **Node.js** Server 개발에 대한 기술도 확보하게 된 셈이다.

새로 합류하시는 분들에게도 **Lambda** 작업시 편리할 것 같단 생각이 든다.

아직 **aws-serverless-express**로 작업한 시간이 그리 길지 않으므로, 아직 확인되지 않은 사항들이 있을 수 있다.
새로운 공유할 사항이 발견되면 해당 글을 수정 또는 추가 글을 올리는 등의 방법으로 공유할 예정이다.

혹시 질문할 내용이 있는 경우에는 언제든지 문의해주길 바란다.