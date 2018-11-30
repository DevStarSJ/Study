---
layout: post
title: "Monolith to Serverless using AWS Lambda (3)"
subtitle:  
categories: cloud
tags: aws
comments: true
---

# Monolith to Serverless using AWS Lambda

## 기존 모노리스 API 서버를 AWS Lambda를 이용하여 서버리스로 변경하기

[이전글 : 1편. 서버리스를 하려는 이유](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Serverless/2017-02-23-MonolithToServerless.01.md)  
[이전글 : 2편. 장애 대응 플랜](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Serverless/2017-02-25-MonolithToServerless.02.md)

### 3편. Lambda 배포 후 겪게되는 일들

서버리스를 가능하게 해주는 서비스 중 가장 많이 알려진게 AWS [Lambda](https://aws.amazon.com/lambda)이다.
간단하게 설명하자면 서버를 실행해 놓는게 아니라 실행될 코드를 올려놓고 해당 코드를 실행시킬 이벤트를 발생시키면 코드가 동작하는 것이다.
코드가 어느 PC에서 동작하는지에 대해서는 우리가 신경쓸 필요없이 AWS에 전적으로 맡겨놓는다.
과금은 Lambda 실행시간(100ms 단위)으로 한다.
1편 글에서 얘기했듯, EC2 서버로 운영할때는 갑자기 요청이 몰리는 경우 서버에 장애가 발생할 수 있는데 Lambda의 경우는 그런 상황자체를 전부 AWS에서 알아서 해달라고 위임하는게 된다.
이렇게 생각하는게 보다는 AWS에서 많은 사용자가 공통으로 사용할 굉장히 큰 서버를 띄워놓고 우리는 거기에서 우리 코드가 실제로 실행되는 시간만큼만 과금을 한다라고 생각하는게 더 쉬운가 ?

Lambda를 수행하기 위해서는 `aws-sdk`를 이용해서 호출을 하거나, AWS 내의 각종 서비스들 CloudWatch, SQS, SNS, Kinesis, DynamoDB 등에서 트리거를 통해서 실행되게 할 수 있다.
Lambda를 API로 사용하기 위해서는 API Gateway를 통해서 url 형식으로 외부 요청을 받아서 Lambda 실행이 가능하다.
서버리스를 구현하기 위해서는 주로 이 방법을 사용한다. 

## API 요청 정보 분석

기존의 EC2로 수행하던 API 서버를 CloudFront를 통해서 수행되도록 설정하였다.
CloudFront에서는 요청들에 대해서 S3로 로그를 생성해주는 기능을 제공한다.
2편에서 설명한 장애 대응 플랜을 수행하는 동안 로그를 계속 쌓아두어서 이걸 분석하여 Lambda로 옮길 API의 순서를 정했다.

전체적으로 옮길 API수는 100개가 살짝 넘는 수였다.
하지만 로그를 보니 이전체가 지금 사용되는 것은 아니었다.
3주 동안 호출된 API의 수는 50 정도가 되었으며, 이 중 많이 호출되고 내부 코드가 비교적 간단한 것부터 작업을 시작했다.

S3에 쌓아둔 로그는 python의 boto3를 이용해서 그냥 노트북으로 다운받아서 gz 압축을 풀고 내가 필요한 정보만 따로 추려서 csv로 만들어서 각 url path 별로 호출 빈도를 카운팅하였다.
그런데 path를 인자로 사용하는 경우는 전부 다른 path url로 인식되어서 간단하게 그런 경우만 따로 path pattern을 만들어서 csv 파일을 만들도록 수정했다.

S3에 쌓아둔 로그를 보니 querystring 정보는 볼 수 있었지만, POST 요청에 대한 body 정보는 없었다. headers의 정보가 전부 다 있는건 아니었지만 중요한 몇가지는 제공해주고 있었다.

첫번째로 옮길 API는 네번째로 자주 요청되는 사용자 정보를 JSON 형식으로 보내주는 API(/user/{id})로 정했다.
Lambda 명칭도 그냥 `api-user-id`로 지었다.  

## 첫번째 리미트 : Lambda 리미트

AWS Lambda 리미트의 기본값은 각 리젼 당 **100**번이다.
동시에 수행가능한 Lambda의 수를 뜻한다.
대략적으로 수행시간이 100ms인 Lambda인 경우 초당 1천번까지 호출해도 괜찮다.
물로 이 수치는 평균적인 것이지 이런 요청이 순간적으로 100번 이상 호출되면 실패가 발생한다.
Lambda 리미트가 발생한 것은 Lambda쪽 CloudWatch 로그에서는 확인이 되지 않는다.
왜냐면 수행 자체가 안되었기 때문에 Lambda에 로그가 발생하지 않는다.
해당 Lambda로 연결된 API Gateway의 오류를 CloudWatch로 로그를 남기도록 설정하면 확인이 가능하다.
정확인 오류 메세지는 기억이 나지 않지만 `exceed`로 검색을 한것 같다.

현재 회사 계정에서는 도쿄 리젼에 Lambda 리미트를 **200**개로 늘려놓은 상태였다.

`api-user-id`를 배포한 후 얼마 지나지 않아서 5XX 오류가 분당 150번 정도 계속 발생하였다.
일단 API를 원래대로 롤백한 후 로그를 보니 Lambda 리미트에 걸렸다.
처음부터 너무 요청이 많은 API를 옮긴것 같다.
AWS에 요청을 했다.
EC2로 되어있는 서버를 Lambda로 옮기고 있다.
100개가 넘는걸 모두 옮길려고 하는데 그 중 1개만 옮겼는데도 Lambda 리미트가 발생했다.
1 ~ 2k 정도로 좀 올려달라고 요청을 했더니 이틀 뒤 아침에 출근해서 확인하니 **2000**개로 리미트를 올렸다는 내용을 확인 할 수 있었다.

## 두번째 리미트 : Subnet Limit

Lambda 리미트가 2000개로 증가되었다는 소식을 듣고 API를 다시 배포하였다.
아침 일찍 배포했는데 정상적으로 잘 동작하고 있었다.
오후 4시에 앱 푸시가 나간 뒤 Lambda 수행이 분당 1만번을 넘기면서 5XX 오류가 지속적으로 발생했다.


다시 API를 롤백하고 API Gateway쪽 오류를 살펴보니 처음보는 메세지 였다.

```
Endpoint response body before transformations:
{
    "Message": "Lambda was not able to create an ENI in the VPC of the Lambda function because the limit for Network Interfaces has been reached.",
    "Type": "User"
}

Execution failed due to configuration error: Malformed Lambda proxy response

Method completed with status: 502
```

VPC에서 ENI를 만들지 못했단다.
Lambda를 VPC에서 수행되도록 설정할 필요는 없다.
하지만 보안을 위해서 그렇게 설정해 놓는 경우가 많다.
MySQL의 경우 사용자 ID, 비밀번호로만 보안을 설정해 놓는것 보다는 특정 대역대의 IP들만 접속을 허용해 놓는게 더 안전하다.
Lambda 같은 경우는 어떤 IP로 생성되는지 우리가 알 수가 없으므로 VPC 설정을 통해서 특정 대역대의 subnet 안에서 생성되도록 설정이 가능하다.
**AWS VPC** 서비스를 이용하여 생성된 VPC와 subnet을 설정해 두었다. subnet은 4000개짜리 2개를 설정했다.
합이 8000개인데, 동시 수행수가 2000개짜리 Lambda가 리미트에 걸려서 생성되지 않았다니...

그래서 16000개짜리 subnet을 하나 더 생성하였다.
기존에 수행중이던 Lambda도 많이 있었으므로, 이번에 새로 만든 api-user-id에는 기존의 4000개 subnet 하나와 새로만든 16000개 하나를 설정해 두었다.
합이 2만개인데 당연히 부족하지 않으리라 판단했다.

## 세번째 리미트 : Network Interface 리미트

사실상 두번째 리미트는 VPC 리미트가 아니라 Network Interface 리미트 였다.

이틀 뒤에 해당 API를 다시 배포했다.
그런데 비슷한 시기에 비슷한 빈도로 5XX 오류가 발생하였다.
분명 subnet의 수가 2배 이상으로 늘렸는데도 계속 오류가 발생하였다.
왜 그럴까 생각을 해봤는데, subnet 2개 (4000개, 16000개)를 합쳐서 2만개 중에 1개로 할당하는게 아니라 2개의 subnet 중 하나를 선택해서 거기에 할당을 하는 식을 동작하는게 아닌가라 판단된다.
그래서 바로 4000개의 subnet을 설정에서 삭제하였다.
삭제하자마자 요청 대비 오류가 50% 가까이로 발생했다.
다시 해당 API를 롤백했다.
그 뒤에 생각해보니 요청을 삭제한 subnet쪽 주소로 계속해서 보냈던 것으로 추정된다.
2개 중 1개를 삭제했으니 50% 정도의 오류가 발생한게 아닌가 생각된다.

그런데 문제는 subnet의 갯수가 부족해서가 아니라 다른 곳이었다.
AWS에 문의를 하니 <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Appendix_Limits.html#vpc-limits-enis> 링크를 보내주었다.
리전당 Network Interface가 최대 350개라고 설명이 되어 있다. 더 늘리고 싶으면 문의를 하라고 되어있다.
회사 동료분이 저 정보를 어디서 확인 가능한지 찾아주었다.


EC2로 들어가서 왼쪽에 보면 Network Interface라는 탭이 있다.
거기에 들어가보니 현재 사용중인 Network Interface가 341개 였고, 그중 Description이 AWS Lambda 로 시작하는게 240개가 넘었다.
다시 AWS에 문의를 하여 해당 리미트를 늘려달라고 하였더니 2000개로 늘려줬다는 답변이 왔다.

일단 subnet을 4000개 6개로 다시 할당을 하여서 배포를 했는데, 그 뒤로는 해당 오류가 더 이상 발생하지 않고 정상적으로 동작하였다.

## 네번째 리미트 : API Gateway 리미트

API Gateway에도 리미트가 있다.
기본적으로는 평균 초당 1000번, 최대 1초당 2000번의 요청을 처리 가능하도록 되어있다.

CloudWatch를 통해서 살펴보던 중 특정 시간대에 5XX 오류가 발생되었길래 그때를 살펴보니 1분에 2만번 정도의 요청이 있었다.
초당 요청으로 계산하면 API Gateway의 리미트보다 작았지만, 혹시 짧은 시간에 2000번 이상의 요청이 있지 않았나 판단되어 AWS에 요청하였으나,
API Gateway의 문제는 아니었고, Lambda 리미트가 발생한 것으로 판단되었다면서 Lambda 리미트를 3000개로 늘려주었다.

## 그 이후...

그 뒤 해당 API는 잘 동작하고 있다.
다른 API들도 작업해서 배포를 했는데 아무런 문제가 없다.
하지만 앞으로 몇 개의 API를 더 배포하면 현재의 리미트를 다시 넘기지 않을까 걱정이 된다.
그걸 미리 예측해서 AWS에 요청을 하면 과연 들어줄지 모르겠다.
그래서 항상 API를 배포하고는 Lambda 실행수, Network Interface 수 등에 대해서 모니터링을 하고 있다.

## 기타 작업하면서 겪은 일들

### 1. CloudFront

CloudFront에서 캐시설정 할 때 headers에 토큰 같은것을 전달하여 그것에 대해서 다른 값을 줘야할 경우에는 사용하면 안된다.
headers에 다른 정보를 전달하더라도 쿼리스트링이 동일한 경우 캐시에서 같은 값으로 응답한다.

CloudFront에서 API Gateway로 headers의 정보 중 포워드 할게 있는 경우 host 정보를 넘겨주면 CloudFront 오류가 발생한다.

### 2. Lambda

Lambda 작업시 `console.log` 같이 출력문을 넣어주면 해당 Lambda의 CloudWatch에서 출력문을 볼 수 있다.
이걸 이용해서 초반에 테스트 할 때는 필요한 모든 곳에 `console.log, console.info, console.dir` 등을 이용해서 확인이 가능하며,
서비스용으로 올릴때도 `event` 정보는 `console.info`로 출력을 해 놓으면 오류 발생시 뭐 때문이지 확인할때 편리하다.
API Gateway의 로그를 보면 event정보가 짤려서 출력되기 때문에 전체 다를 볼려면 Lambda쪽에서 출력해줘야 한다.
당연히 이렇게 하면 성능에 영향을 미치므로 그게 걱정스럽다면 최소한 `try-catch`를 이용해서 오류 상황에서만이라도 출력해 놓으면 나중에 디버깅 할 때 좋다.

TypeScript로 작업할 경우 Node 4.3에서 정상적으로 동작하는 코드라도 Lambda에 올렸을 경우 동작하지 않을 수도 있으니 꼭 테스트를 먼저 해보고 작업을 하는게 좋다.
class, async/await 등은 제대로 되지만 static, default parameter 등에 대해서는 제대로 동작하지 않는다.

### 3. API Gateway

API Gateway는 Lambda 호출후 30초 동안만 기다린다.
그러니 해당 Lambda 실행시간을 30초 이상으로 설정할 필요가 없다.

API Gateway를 {proxy+} 설정으로 사용하고, 1개의 Lambda에서 2가지 이상의 API 코드가 들어있더라도, Lambda를 다른 이름으로 배포하여 각 API별로 할당하는게 좋다.
만약 1개의 Lambda에 2개 이상의 API가 같이 처리 될 경우 오류 발생 상황에서 로그로 확인하는게 힘들다.
이게 맘에 안든다면 더 이상 오류가 발생하지 않고 안정적으로 서비스되고 있는 상황에서 Lambda 및 API Gateway의 {proxy+} 설정을 합치면 된다.

API Gateway에는 쿼리스트링을 파싱하여 JSON 형태로 Lambda에 전달된다.
그런데 그 과정에서 기존의 다른 웹 프레임워크랑 다르게 동작한다.
대표적인 예가 쿼리스트링의 경우 구분자로 `&`를 사용하는데 API Gateway에서는 `;`도 구분자로 인식은 한다.
그렇기 때문에 `?idList=1;2;3&filter=name;phone&flag=1;2`로 전달할 때 API Gateway는 `{IdList: 1, 2: , 3: , filter:name, phone: , flag: 1}` 식으로 해석을 해버린다.
저런 모양이라도 억지로 해석해서 사용하는 방법도 있지만 그 과정에서 idList의 2와 flag의 2개 같은 key로 인식이 되어서 해석이 애매모호해진다.
배열값을 `?id=1&id=2&id=3`의 모양으로 전달할 경우에도 `{id:3}`으로 마지막값 하나만 남겨두고 다 사라진다.
현재로서는 제대로 처리되도록 하는 방법을 찾지 못했다.
CloudFront상의 리퀘스트 로그를 살펴보면 쿼리스트링의 모양이 그대로 남아있는 것으로 봐서는 LambdaEdge를 사용해서 쿼리스트링을 수정한 뒤 API Gateway로 전달하여 처리하는 방법도 있겠지만,
현시점(2017년 2월) LambdaEdge는 프리뷰인데다가 리젼당 100개의 리미트 밖에 허용하지 않아서 실제 서비스에 사용하기에는 망설여진다.
당연한 이야기지만 요청하는 쪽에서 `;`를 인코딩하여 `%3B`로 전달하면 정상적으로 처리가 가능하다.


## Lambda와 API Gateway를 이용해서 Serverless Web API 만들기


- [Lambda 와 API Gateway 연동 #1 (GET, POST)](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateWay.01.md)
- [Lambda 와 API Gateway 연동 #2 (ANY, Deploy Staging, Node.JS Route)](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateway.02.Route.md)
- [Lambda 와 API Gateway 연동 #3 (Proxy Resource)](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateway.03.Proxy.md)
- [Lambda Node.JS Packaging](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda.Packaging.Node.md)
- [AWS Lambda에 Python Handler 만들기](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda.Python.md)
- [Lambda Python Packaging](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda.Packaging.Python.md)
- [Lambda C# Handler 만들기](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda.CSharp.md)




