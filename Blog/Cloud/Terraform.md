## Terraform 이란 ?

- Google Translate에서의 정의

> (especially in science fiction) transform (a planet) so as to resemble the earth, especially so that it can support human life.

- [**Hashicorp**](https://www.terraform.io)에서 만든 Cloud Infrastructure as Code 관리 툴 (Amazon Web Service, MS Azure, Google Cloud Platform)
  - Write
  - Plan
  - Create

- [Terraform 소개 관련 영상 및 Slide](https://www.slideshare.net/awskorea/configuring-practical-aws-based-infrastructure-as-code-using-terraform-byoun-jeonghun) bt Outsider

## 특징

1. [HCL (HashiCorp configuration Language)](https://github.com/hashicorp/hcl)로 작성

```hcl
resource "aws_instance" "jenkins_master" {
    ami                         = "${var.ami_jenkin_master_id}"
    ebs_optimized               = false
    instance_type               = "t3.medium"
    monitoring                  = false
    key_name                    = ""
    subnet_id                   = "${var.subnet_id}"
    vpc_security_group_ids      = ["${aws_security_group.ci_master.id}"]
    iam_instance_profile        = "${var.ec2_instance_profile_name}"
    associate_public_ip_address = true
    source_dest_check           = true

    root_block_device {
        volume_type           = "gp2"
        volume_size           = 20
        delete_on_termination = true
    }

    tags {
        "Name" = "Jenkins Master"
    }
}
```

2. Resource 간의 Defendency가 관리 된다.
3. Code로 정의하기 때문에 변경 내역에 대한 이력관리(Git)가 된다.
4. 자동화 가능 (CI 연동)
5. tfstate로 변경된 최종 상태가 관리. 모든 명령은 최종 tfstate와의 변경 사항을 적용

## 주의 사항

1. Apply시 오류가 나도 Rollback이 안된다. 성공한것까지만 tfstate에 기록.
2. Modify로 Plan되는 것이 정상동작 하지 않을 때가 많다. Delete 후 다시 Create 되도록 유도.
3. 최근 새로 생성된 AWS Resource에 대해서는 레퍼런스가 부족하다.
4. 임의로 AWS 콘솔에서 Resource를 조작할 경우 tfstate가 꼬여버린다.
5. 동일한 자원을 Module / Project 간 이동시 tfstate를 직접 수정해야 한다.

## [aws-infra](https://bitbucket.org/jtnetco/aws-infra/src/master/)

- tfstate는 S3에 보관
  - backend.tf에 정의
- 모든 자원은 Module로 정의
  - 새로운 Module을 추가할때마다 `terraform init`을 해주어야 함
  - 모든 Env에서 사용하는 자원에 대해서는 Module로 정의
  - 특정 Env에서 사용(ex. CI)는 해당 기능별로 정의
- 각 Env 별로 Terraform Project 생성
  - `credential.tf` : 접속 계정에 대한 정보 (삭제해야 함)
  - `global.tf` : Region별 자원이 아닌 Global 자원에 대한 정의. ex IAM, CloudFront
  - `지역이름.tf` : 해당 Region내의 자원을 정의
  - `variable.tf`, `variable.tfvars` : Env별로 다르게 정의해야하는 place-holder 관리
- Env별 tfstate에서 관리되면 안되는 자원에 대해서는 `/backend` 폴더내에 정의. tfstate도 해당 폴더내의 file로 관리
- Yarn Script로 명령어 관리