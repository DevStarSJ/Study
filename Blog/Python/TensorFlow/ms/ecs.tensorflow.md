- AWS ECS
  - Clusters
    - Create Cluster
      - Cluster name : test-ecs-cluster
      - EC2 instance type : t2.micro
      - Networking : VPC, Subnets, Security group 설정
      - Container Instance IAM role : S3, CloudWatch 등에 접근이 가능한 Role을 선택 or 생정 (Role 에 AmazonS3FullAccess Policy를 Attach)
      - Create
  - Repositories
    - Create repository
      - Repository name : tensorflow-test
      - Next Step
      - Build, tag, and push Docker image 의 설명이 나옴
        - AWS CLI 필요
        - 해당 pc에 AWS 계정이 여러개라면  `aws configure` 입력후 설정
        - 맥이라면 1, Windows라면 2 에 적힌 커맨드를 입력 : ex 맥일 경우 `aws ecr get-login --no-include-email --region ap-northeast-1`
          - 만약 오류가 나면 AWS CLI를 업데이트 해야함
        - 입력후 나온 커맨드를 복사후 실행 (로그인 스크립트)
      - 3번에 적힌 문장 실행 : 도커 빌드 `docker build -t tensorflow-test .`
      - 위까지 다 성공했으면 4번, 5번을 차례대로 실행 : 태깅하고 repository에 push
  - Task Definitions
    - Create new task definition
      - Task Definition Name : ts-test
      - Task Role : 선택하거나 생성 (Role 에 AmazonS3FullAccess Policy를 Attach)
      - Add container
        - Container name : ts-test-container
        - Image : Repository에서 tensorflow-test를 선택하여 Repository URI 에 적힌 값을 입력
        - Memory Limits 설정 : ex 128
        - CPU units 설정 : EC2 CPU 1개당 1024 개의 unit 이 생성됨. 할당한 숫자에 비례하여 실행됨
        - Log configuration : awslogs
          - awslogs-group : /aws/ecs/ts-test
          - awslogs-region : 각자 입력 (ex. ap-northeast-1)
        - Add
      - Create
    - ts-test 선택 후 Actions -> Run Task

만약 Log를 보고자 할 경우 CloudWatch 설정이 필요

- CloudWatch
  - Logs
    - Action -> Create Log Group
      - Name : /aws/ecs/ts-test


- Cluster
  - test-ecs-cluster 선택
    - Tasks
      - Run new Task
        - ts-test 선택
        - Run Task