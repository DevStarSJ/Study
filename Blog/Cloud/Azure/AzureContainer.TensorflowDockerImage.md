---
title: Deploy Tensorflow Docker Image to Azure
date: 2017-07-26 17:41:00
categories:
- Azure
tags:
- Azure
- AzureContainerRegistry
- AzureContainerService
- AzureFileStorage
- Docker
- Python
- Tensorflow
- MachineLearning
---

# Deploy Tensorflow Docker Image to Azure

## 참고사항

똑같은 구성으로 **AWS**에 배포하는 글은 이전에 작성한게 있으니 참고하면 된다.

- [Deploy Tensorflow Docker Image to AWS ECS](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/TensorFlow/ms/ecs.tensorflow.md)

- [Using Tensorflow Predict on AWS Lambda Function](https://github.com/DevStarSJ/Study/blob/master/Blog/Python/TensorFlow/ms/lambda.tensorflow.md)

이 작업을 시작하게 된 이유와 개념적인 구성에 대한 설명은 위 Link의 글들을 참고하길 바란다
즉 학습, 저장, 서비스 를 어떻게 동작시키는 것을 목적으로 하였는지에 대한 설명은 이 글에서는 생략하겠다.

## 구성

이 글에서 다룰 내용은 위 Link에서 구성한 시스템을 **Microsoft Azure**에 그대로 구현하는 것을 그 목적으로 하였다. 최대한 **AWS**용으로 작성한 코드들을 그대로 쓸려고 노력하였으나 플랫폼 특성상 바뀐점이 있다. 크게 바뀐건 **AWS Lambda**에는 **Python**으로 예측 코드를 작성하였는데,**Azure Function**은 **C#** 으로 작성하였다. 그 이유는 뒤에 따로 설명하겠다.

### 사용한 Azure Service

- [Azure File Storage](https://azure.microsoft.com/services/storage/files) : 학습 데이터, 학습 결과를 저장
- [Azure Container Registry](https://azure.microsoft.com/services/container-registry) : 학습을 진행하는 Tensorflow Docker Image를 Upload할 공간
- [Azure Container Service](https://azure.microsoft.com/services/container-service) : Tensorflow Docker Image를 실행하는 환경
- [Azure Function](https://azure.microsoft.com/services/functions) : 예측 결과 제공 API


## Tensorflow 학습 코드

참고로 이 코드는 [김성훈 교수님의 모두를 위한 딥러닝 강좌](https://www.youtube.com/watch?v=BS6O0zOGX4E&list=PLlMkM4tgfjnLSOjrEJN31gZATbcj_MpUm) 에서 소개된 코드를 이용하였다.

동물의 여러가지 특징들에 대해서 입력받아서 이 동물의 종류가 무엇인가에 대한 학습데이터이다.

<https://archive.ics.uci.edu/ml/machine-learning-databases/zoo> 에서 해당 데이터 내용에 대해서 확인이 가능하다.

여기에는 김성훈 교수님이 미리 만들어 놓은 [data-04-zoo.csv](https://github.com/hunkim/DeepLearningZeroToAll/blob/master/data-04-zoo.csv) 파일을 이용하겠다.

## Azure File Storage 생성

Azure Portal(<https://portal.azure.com>)로 진입한다.

- 우측 상단 `+` 클릭
  - `Storage >` 선택
    - `Storage Account blob, file, table, queue` 선택
    - ![](images/azure.file.01.png)
      - `Name`: storage 이름 입력 (ex. tensorflowstorage)
      - `Replication` : 일단 테스트라 잴싼거 `LRS` 선택, 실제 서비스라면 접속 지역 분포에 맞게 적절하게 알맞은 것으로 선택
      - `Resource Group` : 새로 만들던지 이미 있는것을 사용하던지 판단하여 입력
      - `Location` : 기본적으로는 `East US`가 되어있는데, 해당 region과 비용도 같으면서 좀 더 가까운 `Japan West`로 선택했음
      - ![](images/azure.file.02.png)
      - `Pin to dashboard`를 선택하면 대쉬보드에 아이콘이 생성되어서 쉽게 진입이 가능하다.
      - `Create`를 눌러서 생성 한 후 다 생성되기를 기다린다.

생성이 끝나면 대쉬보드 화면에 아이콘이 하나 추가된다.

![](images/azure.file.03.png)

해당 아이콘을 눌러서 들어간다.





- `data-04-zoo.csv`를 **Azure File Storage**에 업로드
- 코드를 실행할 위치에 `saver`라는 폴더 생성 (`mkdir saver`)  


#### run.py
```Python
import tensorflow as tf
import numpy as np
import boto3
import datetime
import os

SAVER_FOLDER = "./saver"
BUCKET = 'S3버킷명칭'
TRAIN_DATA = "data-04-zoo.csv"

for file in os.listdir(SAVER_FOLDER):
    os.remove(SAVER_FOLDER + "/" + file);

s3_client = boto3.client('s3')
s3_client.download_file(BUCKET, TRAIN_DATA, TRAIN_DATA)

xy = np.loadtxt(TRAIN_DATA, delimiter=',', dtype=np.float32)
x_data = xy[:,0:-1]
y_data = xy[:,[-1]]
nb_classes = 7

X = tf.placeholder(tf.float32, [None, 16])
Y = tf.placeholder(tf.int32, [None, 1])

Y_one_hot = tf.one_hot(Y, nb_classes)
Y_one_hot = tf.reshape(Y_one_hot, [-1, nb_classes])

W = tf.Variable(tf.random_normal([16, nb_classes]), name='weight')
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')

logits = tf.matmul(X,W) + b
hypothesis = tf.nn.softmax(logits)
cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y_one_hot)
cost = tf.reduce_mean(cost_i)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)


prediction = tf.argmax(hypothesis, 1)
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for step in range(2001):
        sess.run(optimizer, feed_dict={X: x_data, Y: y_data})
        if step % 100 == 0:
            print(step, sess.run([cost, accuracy], feed_dict={X: x_data, Y: y_data}))

    saver.save(sess,"./saver/save.{}.ckpt".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    saver.save(sess,"./saver/save.last.ckpt")

    pred = sess.run(prediction, feed_dict={X: x_data})
    
    for p, y in zip(pred, y_data.flatten()):
        print("[{}] Prediction: {} True Y: {}".format(p == int(y), p, int(y)))


#s3_client = boto3.client('s3')
for file in os.listdir(SAVER_FOLDER):
    print(file)
    s3_client.upload_file(SAVER_FOLDER + "/" + file, 'dev-tensorflow-savedata', file)
``` 

PC에 tensorflow ,numpy, boto3가 설치된 상태라면 바로 실행해볼수도 있다.

```
pip install tensorflow numpy boto3

python run.py
```

## Docker 이미지 생성

Dokerfile을 생성한다.

#### Dockerfile
```Dockerfile
FROM python:3

RUN pip install tensorflow boto3 numpy

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./run.py" ]
```

```shell
docker build -t tensorflow-test .
```
커맨드를 입력하면 Docker Image가 생성된다. 시간이 많이 걸리는 작업이니 미리 실행해 두고 다음단계로 진행하는 것을 추천한다.

## EC2 Container Service 설정

Docker Image를 서비스해주는 AWS 기능이다. EC2 인스턴스를 띄워놓은 상태에서 ECS에 정의한 Docker Image를 수행시 EC2를 할당받아서 수행한다. 하나의 EC2에서 동시에 여러개의 Docker Image 실행이 가능하기때문에 자원을 더 효율적으로 사용할 수 있다.

ECS 설정에 대해서는 자세한 설명은 생략하고 작업 위주로만 순서대로 나열하겠다.

- 웹에서 AWS ECS 콘솔로 접근
  - Clusters 탭 선택
    - ![](images/ecs.tensorflow.01.png)
    - Create Cluster 버튼 클릭
      - Cluster name : `test-ecs-cluster`
      - EC2 instance type : t2.micro (가장 저렴한 인스턴스이다. 일단 테스트니깐 가장 저렴한걸로 구축하자.)
      - Networking : VPC, Subnets, Security group 설정 (먼저 설정된게 있으면 그것을 사용하면 되고 아니면 새로 생성)
      - Container Instance IAM role : S3, CloudWatch 등에 접근이 가능한 Role을 선택 or 생성 (Role 에 AmazonS3FullAccess Policy를 Attach)
      - Create 버튼 클릭
  - Repositories 탭 선택
    - Create repository 버튼 클릭
      - Repository name : `tensorflow-test`
      - Next Step 클릭
      - `Build, tag, and push Docker image 의 설명이 나옴`
        - AWS CLI 필요가 이미 설치되어 있어야 한다. 터미널 창을 연다.
        - 해당 PC에 AWS 계정이 여러개라면  `aws configure`를 이용해서 `[default]` 를 재정의 하던지 `aws` 명령어에 `--profile 프로필명`을 뒤에 붙여주어야 한다.
        - 맥이라면 1, Windows라면 2 에 적힌 커맨드를 입력 : ex 맥일 경우 `aws ecr get-login --no-include-email --region ap-northeast-1`
          - 만약 오류가 나면 AWS CLI를 업데이트 해야함
        - 입력후 나온 커맨드를 복사후 실행 (로그인 스크립트)
      - 3번에 적힌 문장 실행 : 도커 빌드 `docker build -t tensorflow-test .` (하지만 앞에서 미리 실행해 놓았다면 안해도 됨)
      - 위까지 다 성공했으면 4번, 5번을 차례대로 실행 : 태깅하고 Repository에 Push하는 기능이다.
  - Task Definitions 탭 선택
    - Create new task definition 클릭
      - Task Definition Name : `ts-test`
      - Task Role : 선택하거나 생성 (Role 에 AmazonS3FullAccess Policy를 Attach)
      - Add container 클릭
        - Container name : `ts-test-container`
        - Image : Repository 탭에서 `tensorflow-test`를 선택하여 `Repository URI`에 적힌 값을 입력
        - Memory Limits 설정 : ex) 128
        - CPU units 설정 : EC2 CPU 1개당 1024 개의 unit 이 생성됨. 할당한 숫자에 비례하여 실행됨
        - 로그를 남기고 싶다면 Log configuration 을 설정해야 한다.
          - Log configuration : `awslogs`
            - awslogs-group : `/aws/ecs/ts-test`
            - awslogs-region : 각자 입력 (ex. ap-northeast-1)
        - Add 클릭
      - Create 클릭

로그를 남기기로 설정했다면 아래와 같이 CloudWatch에 로그를 만들어야 한다.

- CloudWatch 콘솔로 접근
  - Logs 선택
    - Action -> Create Log Group
      - Name : /aws/ecs/ts-test

실행 방법이 여러가지가 있는데 일단 간단하게 콘솔에서 실행해 보겠다.

- Cluster 선택
  - `test-ecs-cluster` 선택
    - Tasks 탭
      - Run new Task 클릭
        - ts-test 선택
        - Run Task 버튼 클릭

작업이 정상적으로 수행완료가 되었다면 S3에 학습결과가 있는지 확인을 하면 된다.  

![](images/ecs.tensorflow.04.png)

CloudWatch에 로그를 남기기로 설정했다면 로그도 확인이 가능하다.

![](images/ecs.tensorflow.03.png)

### 다음글 Lambda를 이용하여 예측 서비스 제공하기

