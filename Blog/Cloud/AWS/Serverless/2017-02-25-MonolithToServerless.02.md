---
layout: post
title: "Monolith to Serverless using AWS Lambda (2)"
subtitle:  
categories: cloud
tags: aws
comments: true
---

# Monolith to Serverless using AWS Lambda

## 기존 모노리스 API 서버를 AWS Lambda를 이용하여 서버리스로 변경하기

[이전글 : 1편. 서버리스를 하려는 이유](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Serverless/2017-02-23-MonolithToServerless.01.md)

### 2편. 장애 대응 플랜

기존에 잘 돌아가고 있는 API 서버 (EC2)를 서버리스(Lambda)로 변경하고자 한다.
만약 람다로 구현한 API가 정상동작하지 않는 경우 기존의 EC2 서버로 되돌리면 된다.
이게 끝. 심플하지 않은가 ?
이 심플함을 구현하기 위해 얼마나 컴플랙스한 일들이 필요한지에 대한 것이 2편의 전반적인 내용이다.

## 기존 API 서버에 대한 정보

만약 `api.luna.com`이란 이름의 API 서버를 EC2에 올려놓고 오토 스케일링 ([AWS의 Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk) 을 통해 서비스하고 있는 경우라면,
ELB에서 제공해 주는 url은 `api-luna.elasticbeanstalk.com`과 같은 이름이 된다. 이것을 `api.luna.com`란 이름의 도메인을 쓰기 위해서는 **DNS** 서비스를 이용해야 한다.
회사에서는 [CloudFlare](https://www.cloudflare.com)라는 서비스를 이용하는데 **CDN**은 거의 사용하지 않고 **DNS**로만 사용한다.

즉, 아래와 같은 모양으로 되어 있다.

```
- C#으로 되어 있는 API Server : ELB(api-luna.elasticbeanstalk.com) <- DNS(api.luna.com)
```

만약 API의 url이나 파라메터 정보들을 수정하게 된다면, 해당 API를 사용하는 웹, 앱(안드로이드, 아이폰)도 함께 수정해서 배포를 해야하니 일이 커진다.
그리고 만약 장애시 다시 되돌리지도 못한다.
그래서 기존 url은 바꾸지 않고 가야한다.
같은 url에 path 정보가 다른 것들에 대해서 서로 다른 엔드포인트로 보낼려면 어떻게 해야할까 ? (람다는 서버가 아니므로 그냥 엔드포인트(endpoint)로 하겠다.)


[AWS CloudFront](https://aws.amazon.com/cloudfront)라는 **CDN**을 사용하면 각 path 별로 캐시 정책, 엔드포인트 등의 설정을 다르게 할 수 있다.
일단 기존에 ELB에서 돌아가는 서버를 CloudFront를 통해서 서비스 되도록 설정을 변경하였다.

```
- 기존 API Server의 DNAME 변경 : ELB(api-luna.elasticbeanstalk.com) <- DNS(api-origin.luna.com)
- 기존 주소를 CloudFront로 연결 : CloudFront(cf1.cloudfront.net) <- DNS(api.luna.com)
- CF의 Default(*) Origin을 api-origin.luna.com 으로 설정
```

하나의 흐름으로 그려보면 아래와 같이 된다.

```
ELB(api-luna.elasticbeanstalk.com) <- DNS(api-origin.luna.com) <- CloudFront(cf1.cloudfront.net) <- DNS(api.luna.com)
```

새로만드는 람다를 API Gateway를 통해서 서비스 할 경우 CloudFront에서 해당 path에 대해서만 람다를 보도록 설정을 붙이기만 하면 된다.
(람다로 만든 API의 path가 `api.luan.com/user/{id}`라고 가정하고, 람다명칭을 `api-user-id`라고 할 경우)

```
ELB(api-luna.elasticbeanstalk.com) <- DNS(api-origin.luna.com)     <- CloudFront(cf1.cloudfront.net) <- DNS(api.luna.com)
Lambda(api-user-id) <- API Gateway(exec-api.amazonaws.com/service) <-
```

이런 모양으로 구성이 된다.
이건 API를 어떻게 구상하냐는 것에 대한 것이고 장애대응에 대한건 아직 고려되지 않은 형태이다.

## 장애대응

앞에서 얘기했듯이 API가 정상적으로 동작하지 않아서 장애가 났을 때는 해당 API 대신 그냥 기존의 EC2(api-origin.luna.com)을 바라보게하면 된다.
아주 심플하다.
그럼 이 심플함을 어떻게 구성해야 할까.

### 첫번째 생각 : CloudFront에서 Behavior 삭제

CloudFront에서 람다로 향하는 **Behavior**를 삭제한다.
그러면 **api-origin**을 바라볼 것이다. 끝 ?

하지만...
CloudFront는 특정 지역(region)별로 서비스되는게 아니라 글로벌로 서비스된다.
그리고 설정을 변경하면 전체적으로 반영되는데 40분 정도의 시간이 걸린다.
40분동안 장애난 상황을 멀뚱멀뚱 지켜만 봐도 될까 ?
당연히 난리난다.
일단 이 방법은 안된다.

테스트 해볼 가치도 없다.
그냥 패스하자.

### 두번째 생각 : DNS만 살짝 바꿔서 다른 CloudFront를 바라보게 설정

CloudFront를 2개를 만든다.
위에서 설정한 **cf1** 과 api-origin만 바라보는 **cf2**.
`api.luna.com`은 **cf1**을 향하게 하다가 장애 발생시 **cf2**를 바라보게 설정하면 된다.
DNS 바꾸는건 바로 반영되기 때문에 장애 대응 시간을 2분 정도로 줄일 수 있다.

일정 기간동안 정상적으로 서비스되었다고 판단이 되는 api에 대해서는 **cf2**의 behavior에도 추가를 해놓으면 된다.
그러면 장애 발생시 **cf2**로 되돌리더라도 새로 추가한 api에 대해서만 롤백이 된다.

```
ELB(api-luna.elasticbeanstalk.com) <- DNS(api-origin.luna.com)     <- CloudFront(cf1.cloudfront.net) <- DNS(api.luna.com)
Lambda(api-user-id) <- API Gateway(exec-api.amazonaws.com/service) <-

ELB(api-luna.elasticbeanstalk.com) <- DNS(api-origin.luna.com)     <- CloudFront(cf2.cloudfront.net)
```

위 그림과 같이 서비스하다가 장애 발생시 `api.luna.com`의 주소만 **cf2**로 변경하면 된다.
일단 **cf2**를 만들어 보았다.
안만들어진다.
CloudFront에서 DNS를 사용하기 위해서는 **CNAMEs**를 설정해야 한다.
그런데 서로 다른 CloudFront가 같은 CNAME을 가지도록 설정이 안된다.
왜 안된다는 건지 이해가 안된다.
어차피 실제로 같은 DNS가 동시에 2개의 CloudFront를 바라보고 있다는거 자체가 말이 안되는데 그렇게 설정하게 좀 해줘도 상관없지 않나 ?
일단 안된다니깐 이 방법은 사용할 수 없다.

### 세번째 생각 : 그럼 DNS를 여러개 설정

CloudFront가 같은 CNAME으로 설정이 안되니 DNS를 여러개 만들어서 DNS단에서 스와핑을 하면 해결되지 않을까 ?

```
ELB(api-luna.elasticbeanstalk.com) <- DNS(api-origin.luna.com)     <- CloudFront(cf1.cloudfront.net) <- DNS(api1.luna.com)
Lambda(api-user-id) <- API Gateway(exec-api.amazonaws.com/service) <-

ELB(api-luna.elasticbeanstalk.com) <- DNS(api-origin.luna.com)     <- CloudFront(cf2.cloudfront.net) <- DNS(api2.luna.com)

DNS(api1.luna.com) <- DNS(api.luna.com)
```

이렇게 DNS 끼리 연결해두고 장애 발생시 api.luna.com 이 api2.luna.com 을 바라보게 설정하면 된다.
너무 쉽다.


그런데...
CloudFront의 CNAME에 `api1.luna.com` 이라 설정해두고, `api1.luna.com <- api.luna.com`으로 설정을 하면 `api.luna.com`은 CNAME으로 설정되어 있지 않다고 오류가 발생한다.
음... 어쨌든 안된단다. 다른 방법을 또 생각해 봐야지.

### 네번째 생각 : API Gateway에서 EC2를 바라보게 설정

이 방법만은 사용하지 않으려 했는데...
이 방법 밖에 없는것 같다.

```
ELB(api-luna.elasticbeanstalk.com) <- DNS(api-origin.luna.com)     <- CloudFront(cf1.cloudfront.net) <- DNS(api1.luna.com)
Lambda(api-user-id) <- API Gateway(exec-api.amazonaws.com/service) <-
```

위의 형태로 서비스를 하다가 `api-user-id`에 장애가 발생한 경우

```
ELB(api-luna.elasticbeanstalk.com) <- DNS(api-origin.luna.com)     <- CloudFront(cf1.cloudfront.net) <- DNS(api1.luna.com)
ELB(api-luna.elasticbeanstalk.com) <- API Gateway(exec-api.ama...) <-
```

이렇게 API Gateway에서 람다 대신에 `api-origin`을 바라보게 설정을 변경한다.
먼저 이렇게 해서 장애 상황을 일단 해결한 후 CloudFront에서 behavior를 삭제하고 40분뒤에 적용되면 다시 API Gateway를 람다를 바라보도록 수정하고 API를 수정하는 식으로 작업을 진행하면 된다.

### 네번째 생각의 보완점들

테스트해보니 원하는대로 동작한다.
하지만 뭔가 찜찜한게 몇 가지 있다.

그 중 첫번째는 장애 발생시 마우스 클릭이나 미리 설정해놓은 스크립트 실행 같은 방법이 아니라 AWS 콘솔로 접속해서 설정을 하나하나 바꿔주면서 `api-luna.elasticbeanstalk.com/user/{proxy}` 또는 `api-origin.luna.com/user/{proxy}` 이렇게 입력해줘야 한다.
완벽한 해결방법은 아니지만, API Gateway를 발행할때 먼저 `api-origin`을 바라보게 배포하고, 다시 수정해서 람다를 바라보게 배포하면 된다.
그럼 해당 스테이징에 가보면 2가지 경우가 모두 `Deployment History`에 남아있어서 과거 버전을 선택한 후 `Change Deployment` 버튼을 누르면 된다.

두번째는 API Gateway url끝에 스테이지명을 항상 붙여줘야 한다.
만약 스테이지를 `service`로 설정했다면 `exec-api.amazonaws.com/service`이런식의 url을 가지게 된다.
url을 줄여주기 위해서 DNS를 설정하려고 해도 `/service` 때문에 원하는대로 설정이 안된다.
그렇다고 DNS에서 주는 이름 뒤에  `/service`를 붙이는 것으로 `CloudFront`에서 behavior를 설정하려는 순간 막막해진다.

API Gateway에 `Custom Domain Names` 탭으로 가면 이름을 이쁘게 지어줄수 있다.
하지만 SSL용 인증서를 등록해야 하는데, AWS의 인증서는 또 지원을 해주지 않는다.
그래서 무료 인증서인 [Lets' Encrypt](https://letsencrypt.org)에서 발급받으면 된다.
발급받는것도 쉽지는 않다. 인증서 발급을 위해서 현재 해당 주소의 서버를 사용중이라 것을 증명해야하는데 API Gateway에서 그 인증을 해줄수가 있나 ?
발급받은 방법이 여러가지 있는데...
그 중 하나를 대충 설명하자면 `nginx`를 이용해서 임시로 서버를 하나 띄워서 DNS에서 그 서버를 바라보게 설정한 후 인증서를 발급받아서 사용하면 된다.
구글에서 검색해보면 관련 방법 및 코드들이 쭉 나온다. 회사 동료분중 이미 해당 작업을 위한 코드를 만들어두고 발급받고 계신분이 있어서 그 분 도움을 받아서 쉽게 발급 받을 수 있었다.

처음엔 SSL 인증서 발급받는게 귀찮아서, **Custom Domain Name**을 사용하지 않을려고 그 과정 자체를 `API Gateway <- CloudFront <- DNS` 식으로 몇 단계를 더 거치게 했었는데
그 과정에서도 CloudFront에서 SSL 인증서를 써야하고... (기존 서비스에 쓰던걸 같이쓰면 되긴 했다.) 설정 자체도 너무 복잡해져서 다시 **Custom Domain Name**을 사용하기로 결정했다.

### 실제로 적용

처음 API를 배포할때는 네번째 방법(장애발생시 API Gateway에서 EC2를 바라보게 설정)을 사용했지만, 지금은 그냥 첫번째 방법(CloudFront에서 behavior를 삭제)을 사용한다.
사실 삭제도 아니고 그냥 url 앞에 `/test` 이런걸 붙여서 주소만 바꿔버린다.
40분동안 장애가 나도록 그냥 내버려 두고 있냐고 ?
그건 당연히 아니다.
CloudFront의 설정을 수정하면 그게 완벽하게 적용되었다고 콘솔상에 표시되는건 40분 정도가 걸리지만, 실제로 적용되는건 평균 1분 정도, 아무리 길어도 3분 이내에는 바뀌는게 확인되었다.
내부적으로 어떻게 동작하는지 알 수는 없지만 현재 AWS 도쿄 리전만 사용을 하다보니 CloudFront에서도 일단 가장 많이 사용하는 도쿄 리전부터 적용해주는 것으로 보인다.

어떻게 이 사실을 알수가 있었냐면 새로운 API 배포시 해당 람다, API Gateway에 대한 주요 수치들에 대해서 **CloudWatch Metrics**에 미리 등록해두고 모니터링을 했다.
배포전에 먼저 CloudWatch부터 띄워둔체로 배포를 하고 계속 수치 및 그래프를 확인하고 있으니깐 거의 바로 람다로 호출이 들어오는 것이 확인되었다.
API 배포 초반에는 거의 배포하자마자 바로 장애가 났었다. 그래서 2주 동안은 배포, 롤백을 몇 번씩 겪었다. 그러면서 CloudWatch 상의 각종 수치들을 보고 어떻게 해석해야하는지에 대해서 자연스럽게 잘 알게 되었다.
네번째 방법이 아무래도 첫번째 방법보다는 손이 많이 간다. 그렇게 해서 되돌리는 시간과 그냥 첫번째 방법으로 behavior만 삭제한 후 적용되는 시간의 차이가 거의 없었다. 오히려 첫번째 방법이 더 빠르게 적용되 되는 것으로 판단되었다.

#### 다음 글에 계속...

다음 글에는 람다 배포 후 들이닥치게 되는 각종 리미트들... 리미트 뒤에 숨어있는 또 다른 리미트들에 대한 이야기를 쓸 예정이다.

[다음글 : 3편. Lambda 배포 후 겪게되는 일들](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Serverless/2017-02-26-MonolithToServerless.03.md)
