---
layout: post
title: "Introduce to AWS Batch"
subtitle:  
categories: cloud
tags: aws
comments: true
---

# Introduce to AWS Batch

## 1. Introduction to AWS Batch

**AWS batch**는 ECR (Amazon Elastic Container Registry)또는 EC2 AMI (Amazon Machine Image)를 이용해서 작업을 수행시키는 서비스이다.

[Amazon Batch](https://aws.amazon.com/batch)

ECS (Amazon Elastic Container Service)에서도 작업 수행이 가능하지만 몇가지 차이점이 있다.

1. **ECS**에서는 미리 **Cluster** (EC2)를 만들어 두고 **Task** (ECR)를 해당 Cluster에서 수행하는 방식이지만, **Batch**에서는 **Job queue** (EC2)를 만들어 두고 **Job**(ECS or EC2 AMI) 수행시 실행할 Job queue를 선택하면 런타임에 해당 instance가 생성된 후 job 실행이 끝나면 종료된다. instance가 실제 수행시에만 할당되므로 비용적인 면에서 유리하다. ECS, Batch 둘 다 Spot Instance를 지원한다.

2. **ECS**, **Batch** 모두  **Task** / **Job** 실행 후 종료와 **Service**형태로 계속 실행되는 방식이 둘 다 가능하다. 하지만 Batch의 경우 service 방식으로 실행하는게 원래 의도된 방법이 아니긴하다.

3. **Batch**의 경우 **Job**의 dependancy설정이 가능하다. 즉, 다른 job이 종류된 이후 수행하도록 설정이 가능하다. 이것이 **ECS**의 **Task**와 가장 큰 차이점이다.

4. **ECS**는 **ECR**의 docker image만을 지원히지만, **AWS Batch**는 **ECR** 과 **AMI** 모두를 지원한다. 단, AMI의 경우 Amazon Linux 1 or 2 OS에 별도의 docker agent가 설치되어 있어야 한다.

## 2. 설명 범위

**AWS Batch**를 수행하기 위한 최소한의 정의 및 실행 방법에 대해서 소개하겠다.

- ECR : Batch에서 실행할 docker image
- Batch Job : Batch에서 수행할 작업
- Batch Job queue : Batch가 수행될 instance 정의
- Batch Compute Environment : Job queue에서 포함시킬 instance들의 세부 정의
- AWS Lambda : Batch job의 dependancy 적용을 위한 간단한 코드
- CloudWatch : Batch job을 주기적으로 수행하기 위한 trigger

**AMI**를 활용하는 방법에 대해서는 설명은 하지 않을 것이며, **ECR**을 이용한 방법만을 다룬다.  

추가적으로 **Terraform**을 이용하여 인프라스트럭쳐를 배포하기 위한 최소한의 정의사항에 대해서도 소개를 하겠다.

## 3. Define AWS Batch Infrastructure

단 1개 Job을 AWS Batch를 수행하기 위해서 필요한 최소한의 AWS상의 infrastructure 는 다음과 같다.

- Job definitions
  - Job role : IAM role
  - Container image : ECR or AMI

- Computer environment
  - Service role : IAM role
  - Instance role : IAM role (profile)
  - EC2 key pair : IAM (optional)
  - Spot fleet role : IAM role (Provisioning model을 On-Demand가 아닌 Spot으로 설정할 경우)
  - VPC
  - Subnet
  - Security Group

- Job queue
  - Compute environment

각종 작업들을 위한 권한(IAM role)들과 수행할 작업(software)가 포함된 이미지(ECR or AMI), 수행될 instace에 필요한 network설정(VPC, Subnet, Security Group)들의 정의가 미리 이루어져야 한다. 해당 인프라의 정의는 이 글에서는 다루지 않겠다. **Terraform** 코드에서도 해당 인프라는 **resource**가 아닌 **data**로 정의하여 미리 정의된 내용을 사용하는 방향으로 진행하겠다.

**AWS Batch** console로 들어가면 왼쪽 목록에 5개의 메뉴를 볼 수가 있다.

- Dashboard : 정의된 Job queue와 Computer environment의 목록을 볼 수 있으며, 각각의 Job queue별로 Job의 Status(submitted, pending, runnable, starting, running, failed, succeeded) 상태를 볼 수 있다.
- Jobs : Job queue별로 Status별 job의 목록을 볼 수있다.
- Job definitions : 정의된 Job들을 볼 수 있으며, 생성 / 삭제가 가능하다. Job을 console상에서 실행할 경우 Dashboard, Jobs, Job definitions 3곳에서 모두 관련 버튼이 있으나 Job definitions에서만 원하는대로 Job 선택이 가능했다.
- Job queues : 정의된 Job queue 확인 및 생성 / 삭제가 가능하다. 삭제시 Disable -> Delete 순으로 작업해야 한다.
- Compute environments : 정의된 Compute environment 확인 및 생성 / 삭제가 가능하다. 삭제시 Disable -> Delete 순으로 작업해야 한다. 그리고 Job queue에서 사용중이지 않은 경우에만 삭제가 가능하다.

## 3.1 Job definitions

실행할 container image및 명령어를 정의하는 곳이다.

`Create`를 누르면 Job 정의가 가능하다.
- Create a job definition
  - Job definition name : Job difinition의 이름
  - Job attempts : Job 실패시 다시 시도해야 할 경우 몇 회까지 수행할 것인지에 대한 설정
  - Execution timeout : Job의 실행이 특정 시간내에 끝나야 할 경우 설정(초 단위)
- Environment
  - Job role : Job 수행을 위해서는 ECS IAM role이 필요하다. 해당 권한이 있는 role로 설정
  - Container image : 수행할 ECR or AMI 이미지의 url을 입력한다. ECR의 경우 version까지 입력할 경우 `{Repository URI}:latest`와 같은 형식으로 입력하면 된다.
  - Command : 실행할 명령어 `python src/run.py`와 같은식으로 띄워쓰기로 입력하면 된다.
  - vCPUs : Job 수행에 필요한 CPU수
  - Memory (MiB) : Job 수행에 필요한 메모리
- Environment variables : Job 실행시 참고할 환경변수들

나머지 값들은 필수값이 아니라 설명을 생략한다. 위에 소개한 특성들 중에서도 필수값이 아닌 것들이 존재하지만, 대부분의 작업에 필요해 보이는 것 위주로 나열하였다.

## 3.2 Compute environment

**Job queue**를 정의하기 전에 **Compute environment**를 먼저 정의해야 한다.  
Job queue에 포함될 instance에 대한 정의를 하는 곳이다.

`Creare environment`를 누르면 정의가 가능하다.
- Create a compute environment
  - Compute environment type : 그냥 `Managed`를 하자. AWS에서 관리를 해주는 것이다. `Unmanaged`를 선택하면 아래에 정의가능한 것들이 거의 없어진다.
  - Compute environment name : Compute environment의 이름
  - Service role : AWSBatchServiceRole IAM role이 필요하다.
  - Instance role : ecsInstanceRole IAM instance profile이 필요하다.
  - EC2 key pair : 해당 instance에 직접 접속할 필요가 있을 경우 그때 사용할 key-pair를 선택한다.
- Configure your compute resources
  - Provisioning model : On-Demand와 Spot 중 선택이 가능하다. Spot을 선택 할 경우 하위 항목을 2개 더 정의해야 한다.
    - Maximum Price : On-Demand 가격 대비 몇%의 가격까지 지불할 것인지를 정의한다.
    - Spot fleet role : Spot을 사용할 수 있는 IAM role이 필요하다.
  - Allowed instance types : 사용할 instance 타입들을 멀티로 선택이 가능하다.
  - Minimum / Desired / Maximum vCPUs : 최소/희망/최대 vCPU 개수에 대한 정의인데 그냥 모두 기본값으로 해도 무관하다.
- Networking
  - VPC Id
  - Subnets
  - Security groups
- EC2 tags

Networking 과 tags에 대해서는 따로 설명을 하지 않겠다. 일반적으로 EC2 정의에서 필요로하는 필수값들이다.

## 3.3 Job queue

**Job**이 수행되는 **Compute environment**들을 정의하는 곳이다.
`Creare queue`를 누르면 정의가 가능하다.
- Create a job queue
  - Queue name : Job queue의 이름
  - Priority : 우선순위
- Connected compute environments for this queue : 정의된 **Compute environment**를 순서대로 나열이 가능

만약 하나의 **Job queue**에 여러 개의 **Job**이 수행되도록 제출한 경우 정의된 Compute environment들의 범위 안에서만 동시에 수행이 가능하다.

예를 들어서 vCPU 10개가 필요한 Job 10개를 1개의 Job queue에 모두 할당 할 경우, 해당 Job queue에 정의된 Compute environment가 vCPU 36개일 경우 동시에 3개씩 밖에 수행을 할 수가 없다. 만약 정의된 Compute environment가 vCPU 36개, vCPU 24개 이렇게 2개가 있을 경우 먼저 제출된 3개는 앞의 머신에서 다음 2개는 뒤의 머신에서 수행되며, 마저미 5개는 먼저 제출된 Job중에 끝난 것이 있으면 해당 머신에 하나씩 할당이 된다.

## 4. Job 실행

### 4.1 Console에서 Job 실행

먼저 console에서 바로 실행시키는 방법이 있다.

- `Job definitions`에서 실행시킬 Job definition을 선택
  - `Revision X`와 같은 버전정보를 선택
    - 상위 `Action`버튼의 `Submit job`을 선택

- Job run-time
  - Job name : 실행 Job의 이름 (Job definition 이름과는 다름)
  - Job queue : 어느 Job queue에서 실행할지 선택
  - Job depends on : 다른 Job이 끝난 다음에 실행되어야 할 경우 해당 Job의 id를 입력

나머지 사항들은 `Job definitions`에서 이미 설정된 값을 따른다. 해당 Job에서만의 값으로 수정하는 것도 가능하다.

### 4.2 Python에서 AWS SDK(boto3)로 실행

아래 코드는 연속된 3개의 Job을 실행하는 예제 코드이다.  

```Python
import boto3
client = boto3.client('batch')

job_list = ['Job1', 'Job2', 'Job3']
env_list = ['queue_72', 'queue_simple', 'queue_72']

def make_request(name, env, depends_job=None):
    request = {'jobQueue': env, 'jobName': name,  'jobDefinition': name}
    if depends_job is not None:
        job_id = depends_job['jobId']
        request['dependsOn'] = [ {'jobId': job_id}]
    return request

response = None
for job, env in zip(job_list, env_list):
    response = client.submit_job(**make_request(job, env, response))
    print(job)
    print(response)
    print('')
```

3개의 Job은 각각 앞에 정의된 Job이 실행된 이후 실행되어야 한다.  
Job1, Job3는 vCPU가 72개 필요한 instance에서 실행되어야 하며, Job2는 vCPU 1개에서도 실행이 가능하므로 이 두 그룹의 Job queue를 다르게 설정하였다.

위 코드는 **AWS Lambda**에 정의헤 두고 실행하는 것이 가능하다. 이 경우 **AWS CloudWatch**에서 주기적으로 실행되로록 설정이 가능하다.

- `AWS CloudWatch` console
  - `Events` -> `Rules`
    - `Create rule`
      - Event Source : Schedule
        - 주기적으로 수행하도록 또는 Cron Express를 이용하여 수행하도록 설정
      - Add Target
        - Lambda Function 선택 후 정의된 Function name을 선택

**Job** 실행 결과는 **AWS Batch** Dashboard 상에서 세부정보로 들어가면 **CloudWatch** 링크가 보이는데 그것을 이용해서 로그 확인이 가능하다.

## 5. Terraform Code

**AWS Batch** 정의를 **Terraform**을 이용하여 정의한 예제코드이다.

**VPC**, **IAM Role**등 외부설정은 기존에 정의된 것을 사용한다는 전제하에 `data`로 정의하였으며 **Batch**상에서의 정의만 `resource`로 정의하였다.

참고로 현재(2018-11) 기준으로 **Compute Environment**가 설정된 상태에서 수정해서 `apply`할 경우 오류가 발생하며 `rollback`이 되지 않는다. 수동으로 작업을 하려고 해도 해당 리소스를 사용하고 있는 모든 **Job queue**를 모두 `Disable` -> `Delete`한 후에 **Compute Environment**를 `Disable` -> `Delete`하고 새로 만들어야 한다.

**CloudFomation**에서는 정상적으로 수정이 되는지 확인해보지는 않았다.

- role.tf
```HCL
data "aws_iam_instance_profile" "AWSEC2ContainerServiceForEC2Policy" {
    name = "AWSEC2ContainerServiceForEC2Policy"
}

data "aws_iam_role" "AWSBatchServiceRole" {
    name = "AWSBatchServiceRole"
}

data "aws_iam_role" "AWSServiceRoleForEC2SpotFleet" {
    name = "AWSServiceRoleForEC2SpotFleet"
}
```

- subnet.tf
```HCL
variable "subnet_id" {
    type = "string"
    default = "subnet-example"
  
}

data "aws_subnet" "subnet_default" {
    id = "${var.subnet_id}"
}
```

- security_group.tf
```HCL
variable "security_group_id" {
    type = "string"
    default = "sg-example"
}

data "aws_security_group" "default_sg" {
    id = "${var.security_group_id}"
}
```

- ecs.tf
```HCL
resource "aws_ecr_repository" "batch_image" {
  name = "batch_image"
}
```
**ECR**의 경우 미리 정의된 것을 사용할 경우 위 코드에서 `resource`만 `data`로 수정하면 된다.

- batch.tf
```HCL
resource "aws_batch_compute_environment" "env_72" {
  compute_environment_name = "env_72"

  compute_resources {
    instance_role = "${data.aws_iam_instance_profile.AWSEC2ContainerServiceForEC2Policy.arn}"
    spot_iam_fleet_role  = "${data.aws_iam_role.AWSServiceRoleForEC2SpotFleet.arn}"

    instance_type = [
      "c5.18xlarge",
      "m5.24xlarge",
      "m5.12xlarge"
    ]

    max_vcpus = 256
    min_vcpus = 0

    security_group_ids = [
      "${data.aws_security_group.default_sg.id}",
    ]

    subnets = [
      "${data.aws_subnet.subnet_default.id}",
    ]

    type = "EC2"
  }

  service_role = "${data.aws_iam_role.AWSBatchServiceRole.arn}"
  type         = "MANAGED"
}

resource "aws_batch_compute_environment" "env_simple" {
  compute_environment_name = "env_simples"

  compute_resources {
    instance_role = "${data.aws_iam_instance_profile.AWSEC2ContainerServiceForEC2Policy.arn}"
    spot_iam_fleet_role  = "${data.aws_iam_role.AWSServiceRoleForEC2SpotFleet.arn}"

    instance_type = [
      "r3.xlarge"
    ]

    max_vcpus = 256
    min_vcpus = 0

    security_group_ids = [
      "${data.aws_security_group.default_sg.id}",
    ]

    subnets = [
      "${data.aws_subnet.subnet_default.id}",
    ]

    type = "EC2"
  }

  service_role = "${data.aws_iam_role.AWSBatchServiceRole.arn}"
  type         = "MANAGED"
}

resource "aws_batch_job_queue" "queue_72" {
  name                 = "queue_72"
  state                = "ENABLED"
  priority             = 100
  compute_environments = ["${aws_batch_compute_environment.env_72.arn}"]
}

resource "aws_batch_job_queue" "queue_simple" {
  name                 = "queue_simple"
  state                = "ENABLED"
  priority             = 100
  compute_environments = ["${aws_batch_compute_environment.env_simple.arn}"]
}

resource "aws_batch_job_definition" "Job1" {
  name = "Job1"
  type = "container"

  container_properties = <<CONTAINER_PROPERTIES
{
    "command": ["python", "src/run1.py"],
    "image": "${data.aws_ecr_repository.batch_image.repository_url}:latest",
    "memory": 102400,
    "vcpus": 72
}
CONTAINER_PROPERTIES
}

resource "aws_batch_job_definition" "Job2" {
  name = "Job2"
  type = "container"

  container_properties = <<CONTAINER_PROPERTIES
{
    "command": ["python", "src/run1.py"],
    "image": "${data.aws_ecr_repository.batch_image.repository_url}:latest",
    "memory": 1024,
    "vcpus": 1
}
CONTAINER_PROPERTIES
}

resource "aws_batch_job_definition" "Job3" {
  name = "Job3"
  type = "container"

  container_properties = <<CONTAINER_PROPERTIES
{
    "command": ["python", "src/run3.py"],
    "image": "${data.aws_ecr_repository.batch_image.repository_url}:latest",
    "memory": 102400,
    "vcpus": 72
}
CONTAINER_PROPERTIES
}
```

## 6. 맺음말

**AWS Batch**를 이용하면 실제로 구동할때만 **EC2 Instance**를 띄워서 수행 할 수 있으며, **Job**의 dependency를 이용하여 workflow 관리도 가능하다. 그리고 **AWS Lambda**와 **CloudWatch**를 활용해서 주기적으로 실행하도록도 설정이 가능하다.

아쉬운 점으로는 첫째, dependency를 1개만 설정이 가능해서, 동시에 여러가지 일을 수행하고 그 모든게 다 끝난 후에 다음 Job을 수행하는 식의 정의는 안된다는 점이다. 최대한 병렬성을 높여서 전체 수행시간을 줄이는데에는 한계점이 보인다.

두번째 아쉬운 점으로는 Job간의 dependency를 run-time에 제출된 job id를 가지고 해야한다는 점이다. 미리 인프라 정의할때 Job의 default dependency를 걸어두고 job 제출시 dependency를 수정가능하도록 한다던지, 아니면 **Job Workflow definition**의 기능을 별도로 제공해서 미리 정의가능해서 그것만 수행하는 식으로 된다면 **AWS Lambda**를 따로 활용하지 않고 **CloudWatch**에서 바로 job workflow를 실행한다던지 아니면 workflow 정의시 실행주기까지 같이 설정이 가능하게 하면 훨씬 편리하겠다는 생각이 든다.

참고로 앞에서 설명한 예제와 같이 `Job1`과 `Job3`가 하나의 queue에서 수행되고 `Job2`가 다른 queue에서 수행될 경우, `Job1`의 실행이 끝난 시점에 `Job2`를 실행할 queue에 instance가 떠있지 않은 상태라면 instance가 할당될 동안 기다려야 한다. 그렇게 기다린 후 `Job2`의 실행이 끝난 시점에 `Job1`을 실행한 queue에 다른 job이 오랜시간동안 할당이 안되어서 내려갔을 경우 다시 `Job3` 수행전에 해당 queue상의 instance가 뜰동안 기다려야 한다. 만약 `Job2`가 너무나도 단순한 작업이어서 `Job1`을 실행시킨 고사양의 instance에서 수행되는게 낭비라고 생각해서 별도 queue에서 수행하도록 설정을 했다면 `Job1`의 수행이 종료되자마자 해당 queue의 instance가 내려가는 것이 아니라 다른 job을 기다리는 일정시간동안은 instance가 유지되므로 전체 수행시간도 더 길게되고, 비용도 오히려 더 나올 수가 있으니, 이점을 주의해야 한다.

## 마치며...

잘못되었거나, 변경된 점, 기타 추가 사항에 대한 피드백은 언제나 환영합니다. - <seokjoon.yun@gmail.com>  
