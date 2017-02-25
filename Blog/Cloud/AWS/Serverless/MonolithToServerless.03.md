# Monolith to Serverless using AWS Lambda

## 기존 모노리스 API 서버를 AWS Lambda를 이용하여 서버리스로 변경하기

[이전글 : 1편. 서버리스를 하려는 이유](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Serverless/MonolithToServerless.01.md)
[이전글 : 2편. 장애 대응 플랜](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Serverless/MonolithToServerless.02.md)

### 3편. 람다 배포 후 겪게되는 일들

서버리스를 가능하게 해주는 서비스 중 가장 많이 알려진게 AWS [Lambda](https://aws.amazon.com/lambda)이다.
간단하게 설명하자면 서버를 실행해 놓는게 아니라 실행될 코드를 올려놓고 해당 코드를 실행시킬 이벤트를 발생시키면 코드가 동작하는 것이다.
코드가 어느 PC에서 동작하는지에 대해서는 우리가 신경쓸 필요없이 AWS에 전적으로 맡겨놓는다.
과금은 람다 실행시간(100ms 단위)으로 한다.
1편 글에서 얘기했듯, EC2 서버로 운영할때는 갑자기 요청이 몰리는 경우 서버에 장애가 발생할 수 있는데 람다의 경우는 그런 상황자체를 전부 AWS에서 알아서 해달라고 위임하는게 된다.
이렇게 생각하는게 보다는 AWS에서 많은 사용자가 공통으로 사용할 굉장히 큰 서버를 띄워놓고 우리는 거기에서 우리 코드가 실제로 실행되는 시간만큼만 과금을 한다라고 생각하는게 더 쉬운가 ?

람다를 수행하기 위해서는 `aws-sdk`를 이용해서 호출을 하거나, AWS 내의 각종 서비스들 CloudWatch, SQS, SNS, Kinesis, DynamoDB 등에서 트리거를 통해서 실행되게 할 수 있다.
람다를 API로 사용하기 위해서는 API Gateway를 통해서 url 형식으로 외부 요청을 받아서 람다 실행이 가능하다.
서버리스를 구현하기 위해서는 주로 이 방법을 사용한다. 

## API 요청 정보 분석

기존의 EC2로 수행하던 API 서버를 CloudFront를 통해서 수행되도록 설정하였다.
CloudFront에서는 요청들에 대해서 S3로 로그를 생성해주는 기능을 제공한다.
2편에서 설명한 장애 대응 플랜을 수행하는 동안 로그를 계속 쌓아두어서 이걸 분석하여 람다로 옮길 API의 순서를 정했다.

전체적으로 옮길 API수는 100개가 살짝 넘는 수였다.
하지만 로그를 보니 이전체가 지금 사용되는 것은 아니었다.
3주 동안 호출된 API의 수는 50 정도가 되었으며, 이 중 많이 호출되고 내부 코드가 비교적 간단한 것부터 작업을 시작했다.

S3에 쌓아둔 로그는 python의 boto3를 이용해서 그냥 노트북으로 다운받아서 gz 압축을 풀고 내가 필요한 정보만 따로 추려서 csv로 만들어서 각 url path 별로 호출 빈도를 카운팅하였다.
그런데 path를 인자로 사용하는 경우는 전부 다른 path url로 인식되어서 간단하게 그런 경우만 따로 path pattern을 만들어서 csv 파일을 만들도록 수정했다.

S3에 쌓아둔 로그를 보니 querystring 정보는 볼 수 있었지만, POST 요청에 대한 body 정보는 없었다. headers의 정보가 전부 다 있는건 아니었지만 중요한 몇가지는 제공해주고 있었다.

첫번째로 옮길 API는 네번째로 자주 요청되는 사용자 정보를 JSON 형식으로 보내주는 API(/user/{id})로 정했다.
람다 명칭도 그냥 `api-user-id`로 지었다.  

## 첫번째 리미트 : 람다 리미트

AWS 람다 리미트의 기본값은 각 리젼 당 **100**번이다.
동시에 수행가능한 람다의 수를 뜻한다.
대략적으로 수행시간이 100ms인 람다인 경우 초당 1천번까지 호출해도 괜찮다.
물로 이 수치는 평균적인 것이지 이런 요청이 순간적으로 100번 이상 호출되면 실패가 발생한다.
람다 리미트가 발생한 것은 람다쪽 CloudWatch 로그에서는 확인이 되지 않는다.
왜냐면 수행 자체가 안되었기 때문에 람다에 로그가 발생하지 않는다.
해당 람다로 연결된 API Gateway의 오류를 CloudWatch로 로그를 남기도록 설정하면 확인이 가능하다.
정확인 오류 메세지는 기억이 나지 않지만 `exceed`로 검색을 한것 같다.

현재 회사 계정에서는 도쿄 리젼에 람다 리미트를 **200**개로 늘려놓은 상태였다.

`api-user-id`를 배포한 후 얼마 지나지 않아서 5XX 오류가 분당 150번 정도 계속 발생하였다.
일단 API를 원래대로 롤백한 후 로그를 보니 람다 리미트에 걸렸다.
처음부터 너무 요청이 많은 API를 옮긴것 같다.
AWS에 요청을 했다.
EC2로 되어있는 서버를 람다로 옮기고 있다.
100개가 넘는걸 모두 옮길려고 하는데 그 중 1개만 옮겼는데도 람다 리미트가 발생했다.
1 ~ 2k 정도로 좀 올려달라고 요청을 했더니 이틀 뒤 아침에 출근해서 확인하니 **2000**개로 리미트를 올렸다는 내용을 확인 할 수 있었다.

## 두번째 리미트 : Subnet Limit

람다 리미트가 2000개로 증가되었다는 소식을 듣고 API를 다시 배포하였다.
아침 일찍 배포했는데 정상적으로 잘 동작하고 있었다.
오후 4시에 앱 푸시가 나간 뒤 람다 수행이 분당 1만번을 넘기면서 5XX 오류가 지속적으로 발생했다.


다시 API를 롤백하고 API Gateway쪽 오류를 살펴보니 처음보는 메세지 였다.

```
Endpoint response body before transformations:
{
    "Message": "Lambda was not able to create an ENI in the VPC of the Lambda function because the limit for Network Interfaces has been reached.",
    "Type": "User"
}

Execution failed due to configuration error: Malformed Lambda proxy response
```

VPC에서 ENI를 만들지 못했단다.
람다를 VPC에서 수행되도록 설정할 필요는 없다.
하지만 보안을 위해서 그렇게 설정해 놓는 경우가 많다.
MySQL의 경우 사용자 ID, 비밀번호로만 보안을 설정해 놓는것 보다는 특정 대역대의 IP들만 접속을 허용해 놓는게 더 안전하다.
람다 같은 경우는 어떤 IP로 생성되는지 우리가 알 수가 없으므로 VPC 설정을 통해서 특정 대역대의 subnet 안에서 생성되도록 설정이 가능하다.
**AWS VPC** 서비스를 이용하여 생성된 VPC와 subnet을 설정해 두었다. subnet은 4000개짜리 2개를 설정했다.
합이 8000개인데, 동시 수행수가 2000개짜리 람다가 리미트에 걸려서 생성되지 않았다니...

그래서 16000개짜리 subnet을 하나 더 생성하였다.
기존에 수행중이던 람다도 많이 있었으므로, 이번에 새로 만든 api-user-id에는 기존의 4000개 subnet 하나와 새로만든 16000개 하나를 설정해 두었다.
합이 20000만개인데 당연히 부족하지 않으리라 판단하고 이틀 뒤에 다시 배포했다.

## 세번째 리미트 : Network Interface 리미트

사실상 두번째 리미트는 VPC 리미트가 아니라 Network Interface 리미트 였다.


