---
layout: post
title:  "Deploy AWS Lambda using Python"
subtitle:  
categories: cloud
tags: aws
comments: true
---

# Deploy Lambda Python

**AWS Lambda**에 Tutorial에 대한 이전 글

- [Lambda 와 API Gateway 연동 #1 (GET, POST)](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateWay.01.md)
- [Lambda 와 API Gateway 연동 #2 (ANY, Deploy Staging, Node.JS Route)](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateway.02.Route.md)
- [Lambda 와 API Gateway 연동 #3 (Proxy Resource)](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda%2BAPIGateway.03.Proxy.md)
- [Lambda Node.JS Packaging](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda.Packaging.Node.md)
- [AWS Lambda에 Python Handler 만들기](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda.Python.md)
- [Lambda Python Packaging](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda.Packaging.Python.md)
- [Lambda C# ](https://github.com/DevStarSJ/Study/blob/master/Blog/Cloud/AWS/Lambda.CSharp.md)

AWS Lambda에서 Python 3.6 runtime을 지원하게 된 이후 Python을 이용해서 Lambda function을 구현하는 일이 더 많아졌다. 하지만 기존에 작업했던 Node.JS 와 Python 사이에는 차이점들이 있어서 개발 과정 및 배포에 대해서 고민을 좀 해야만 했다.



## Node.JS 와 Python의 차이

- 외부 라이브러리 사용 (import에 path를 따로 지정하지 않아도 되는 조건)
  - Node.JS
    - npm 설치시 기본적으로 현재 폴더 내에 npm_moudles 폴더를 생성한 후에 설치
    - packages.json 파일을 이용해서 npm으로 설치한 패키지에 대한 정보를 관리
  - Python
    - pip 설치시 기본적으로 Global로 설치됨
      - `pip install [패키지명] -t .` 으로 설치하면 현재 폴대 내에 패키지가 설치됨 (파일 구조가 많이 지저분해짐)
    - requirements.txt 파일을 이용하여 pip로 설치한 패키지에 대한 정보를 관리

- 응답 방식
  - Node.JS
    - handler에 세번째 인자로 callback을 전달받아서 그 함수 내에 인자로 Response Data를 넣어서 실행
  - Python
    - handler 내에서 return으로 Response Data를 전달

## Python 외부 라이브러리 관리에 대한 고민

응답 방식에 대해서는 별 다른 고민을 안해도 되지만, 외부 라이브러리 사용 방법에 대해서는 아무리 고민을 해도 완벽하게 깔끔한 방법이 떠오르지 않았다. pip 설치를 특정 폴더내에 넣으려니 import 할때마다 경로를 지정해야하는게 많이 불편했다.

그래서 든 생각이 작업공간과 배포공간을 분리하는 것이다. 기존에 TypeScript Node.JS로 AWS Lambda의 Binary Response 관련 작업을 할때에는 TypeScirpt의 컴파일된 js 파일과 원본 ts 파일에 대한 분리, 로컬에서 개발시에는 macos용 binary shell 실행파일을 사용해야 하며 배포시에는 AWS Lambda에서 실행가능한 linux용 binary shell 실행파일을 배포해야하는 것 등의 이유로 작업공간과 배포공간을 분리하였다.

apex를 이용해서 배포하였으며, 배포시 shell script를 이용하였다.

Python 작업을 할때에는 local에서 개발할때는 모든 pip 패키지들을 Global로 설치(또는 virtualenv를 활용하여 설치)하여 개발을 하였으며 배포할때 필요한 것들에 대해서는 requirements.txt에 기록하여서 해당 폴더 내에서 로컬에 설치한 후에 같이 배포를 하면 되겠단 생각이 들었다.

Global에 설치된 pip가 굉장히 많을텐데, 현재 배포할 AWS Lambda Function에 사용되는 pip 패키지들을 어떻게 requirements.txt에 정리를 할까 ? 이걸 자동으로 해주는게 가능할까 ? 란 생각이 들어서 찾아보니 가능했다.

`pipreqs`(<https://github.com/bndr/pipreqs>)를 이용하면 해당 폴더내의 py 파일들에 사용된 외부 라이브러리를 requirements.txt 파일로 자동으로 생성해 준다.

### Installation

```
pip install pipreqs
```

### Usage

```
Usage:
        pipreqs [options] <path>

    Options:
        --use-local           Use ONLY local package info instead of querying PyPI
        --pypi-server <url>   Use custom PyPi server
        --proxy <url>         Use Proxy, parameter will be passed to requests library. You can also just set the
                              environments parameter in your terminal:
                              $ export HTTP_PROXY="http://10.10.1.10:3128"
                              $ export HTTPS_PROXY="https://10.10.1.10:1080"
        --debug               Print debug information
        --ignore <dirs>...    Ignore extra directories
        --encoding <charset>  Use encoding parameter for file open
        --savepath <file>     Save the list of requirements in the given file
        --print               Output the list of requirements in the standard output
        --force               Overwrite existing requirements.txt
        --diff <file>         Compare modules in requirements.txt to project imports.
        --clean <file>        Clean up requirements.txt by removing modules that are not imported in project.
```

이것도 자동으로 매번 새로 생성하는 것으로 해도 되겠지만, AWS Lambda의 경우 `boto3`는 기본적으로 설치가 되어 있으므로 deploy할때 같이 올릴 필요가 없다. 더군다나 boto3는 압축을 하여도 6 MB의 용량이므로 꽤나 큰 편이다. 그래서 수동으로 필요할때마다 `pipreqs .`을 실행항 뒤 `boto3`를 지워주는 식으로 사용중이다.

## 예제 코드

`apex`가 설치되어 있고 local pc 에 (home)/.aws/credentials에 AWS 접속 정보가 저장되어 있다는 가정 하에 설명하겠다.

### 폴더구조
```
(작업폴더)
  - src (소스코드가 저장되어 있는 폴더)
    - lambda_test (AWS Lambda Function에 대한 작업 폴더)
      - index.py (예제 코드)
      - requirements.txt (pip 외부 패키지에 대한 정보)
      - function.json (apex 배포 설정)
  - deploy.sh (배포 스크립트)
  - project.json (apex 배포 설정)
```

### index.py
```Python
import requests

def handler(event, context):
    URL = 'http://www.zigbang.com'
    response = requests.get(URL)
    return { 'statusCode' : 200,
             'headers' : { 'Content-Type': 'text/html'},
             'body' : response.text }

if __name__ == '__main__':
    response = handler(None, None)
    print(response)
```

Local에서 `python index.py` 라고 실행시 html 파일 내용이 출력되면 성공한 것이다.

### requirements.txt

해당 폴더 내에서 `pipreqs .`로 실행하면 자동으로 생성된다.

```
requests==2.14.2
```

### function.json

배포 시 Lambda version에 description으로 보여지는 내용을 적어서 배포한다.

```JSON
{
  "description": "test depoly"
}
```

### project.json

```JSON
{
  "name": "test_deploy",
  "nameTemplate": "{{.Function.Name}}",
  "description": "Python Lambda Test Deploy",
  "role": "...",
  "handler":"index.handler",
  "runtime":"python3.6",
  "memory": 128,
  "timeout":30,
  "region": "...",
  "vpc": {
    "securityGroups":["..."],
    "subnets":[ ... ]
  }
}
```

### deploy.sh

```shell
rm -rf functions/lambda_test
cp -rf src/lambda_test functions/lambda_test
cd functions/lambda_test
pip install -r requirements.txt -t .
cd ../..

apex deploy
```

위 파일을 모두 생성한 후 배포 스크립트를 실행한다.

```
./deploy.sh
```

그럼 Lambda 가 배포될 것이며, AWS API Gateway로 연결하여 Browser에서 해당 staging의 url을 입력하면 결과를 볼 수 있다.

API Gateway와의 연동 방법에 대해서는 이 Post에서는 생략하겠다. 이 글 맨 위에 해당 Link로 들어가면 안내를 해놓은 글이 있으니 참고하길 바란다.

![](/images/Lambda.Python.Deploy.01.png)

## 마치며

Python으로 AWS Lambda에서 작업시 pip로 외부 패키지를 해당 폴더내에 설치를 해야만 해서 작업하는 동안 지저분한 폴더 및 파일들로 인하여 불편했다. 거기서부터 시작하여 나름 깨끗한 개발 환경을 만들고자 했다.

혹시 더 좋은 방법으로 작업하시는 분들은 피드백 부탁드립니다.
