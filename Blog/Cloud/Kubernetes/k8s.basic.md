# Kubernetes 기본

EKS Cluster 기준

## 기본 명령어
- kubectl get all : 실행중인 모든 resource 확인
- kubectl get po octopos-pod -o yaml : octopos-pod 라는 이름의 pod에 대한 상태를 yaml로 출력
- kubectl get po --show-labels : pod 목록을 label과 함께 확인
- kubectl exec -it octopos-rs-7rhw5 -- ls : pod에서 직접 실행. `--` 이후 명령어는 pod에서의 command

## 준비 Terraform에서 생성한 config_map_aws_auth.yaml을 실행

```shell
aws eks update-kubeconfig --name octopos_server --region ap-northeast-2
kubectl apply -f config_map_aws_auth.yaml

kubectl get all
kubectl get no --show-labels
```

## 1. Pod 배포

##### pod.yaml
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: octopos-pod
  labels:
    creation_method: manual
    env: develop
spec:
  containers:
  - image: 025325660074.dkr.ecr.ap-northeast-2.amazonaws.com/octopos_server:latest
    name: octopos 
    ports:
    - containerPort: 3000
      protocol: TCP
```

```shell
kubectl create -f pod.yaml

kubectl get po --show-labels
kubectl get po octopos-pod -o yaml
```

실행 여부를 확인하기 위해서는 pod의 3000 포트를 local의 8080으로 port-forward하여 확인
```shell
kubectl port-forward octopos-pod 8080:3000
```

<http://localhost:8080>

pod 삭제
```shell
kubectl delete po --all
```

## 2. Node Label을 이용하여 pod을 특정 node에 배포하기

```shell
kubectl label node ip-172-31-1-65.ap-northeast-2.compute.internal gpu=true

kubectl get no --show-labels
```

##### pod-gpu.yaml
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: octopos-pod-gpu
  labels:
    creation_method: manual
    env: develop
    gpu: "true"
spec:
  nodeSelector:
    gpu: "true"
  containers:
  - image: 025325660074.dkr.ecr.ap-northeast-2.amazonaws.com/octopos_server:latest
    name: octopos 
    ports:
    - containerPort: 3000
      protocol: TCP
```

```shell
kubectl create -f pod-gpu.yaml
```

## 3. namepsace 생성

namespace 확인
```shell
kubectl get ns
kubectl get po -n kube-system
```

##### namespace.yaml
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: octopos-namespace
```

```shell
kubectl create -f namespace.yaml
kubectl create -f pod.yaml -n octopos-namespace

kubectl get po
kubectl get po -n octopos-namespace
```

namespace삭제 (내부 resource도 다 같이 삭제)
```shell
kubectl delete ns octopos-namespace
```

현재 namespace의 모든 resource 삭제
```shell
kubectl delete all --all
```

## 4. Pod livenessProbe 와 readinessProbe

- livenessProbe : 컨테이너가 살아 있는지 확인. 실패할 경우 컨테이너를 다시 시작.
- readinessProbe : 서비스할 준비가 되었는지 확인. 실패할 경우 request가 못가도록 설정.

readinessProbe는 Replication 단위의 동작과 관련이 있으므로 추후 다시 설명

##### pod.yaml
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: octopos-pod
spec:
  containers:
  - image: 025325660074.dkr.ecr.ap-northeast-2.amazonaws.com/octopos_server:latest
    name: octopos 
    livenessProbe:
      httpGet:
        path: /v1/menus
        port: 3000
      initialDelaySeconds: 15
    ports:
    - containerPort: 3000
      protocol: TCP
```

위 파일에서 path 부분을 비정상적인 값으로 수정한 후 1분 뒤에 확인하면 RESTARTS 수치가 증가한 것을 확인할 수 있다.  

로그 확인
```shell
kubectl logs octopos-pod --previous
```

## 5. ReplicaSet

- ReplicationController 설명은 생략. RS가 RC의 모든 기능을 포함

##### rs.yaml
```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: octopos-rs
  labels:
    tier: backend
spec:
  replicas: 3
  selector:
    matchLabels:
      tier: backend
  template:
    metadata:
      labels:
        tier: backend
    spec:
      containers:
      - name: octopos
        image: 025325660074.dkr.ecr.ap-northeast-2.amazonaws.com/octopos_server:latest
        livenessProbe:
          httpGet:
            path: /v1/menus
            port: 3000
          initialDelaySeconds: 15
        ports:
        - name: http-server
          containerPort: 3000
          protocol: TCP
```

## 6. Service

- ReplicaSet에 대한 단일 end-point를 제공
- Load Balancer 역할

##### service.yaml
```yaml
kind: Service
apiVersion: v1
metadata:
  name: octopos-service
spec:
  selector:
    tier: backend
  ports:
  - protocol: TCP
    port: 80
    targetPort: http-server
  type: LoadBalancer
```

- `type: LoadBalancer`를 설정할 경우 cloud service의 external load balancer를 사용함

## 7. ReadinessProbe

서비스할 준비가 되었는지 확인. 실패할 경우 Replica에서 request를 전송하지 않음.

##### rs.yaml
```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: octopos-rs
  labels:
    tier: backend
spec:
  replicas: 3
  selector:
    matchLabels:
      tier: backend
  template:
    metadata:
      labels:
        tier: backend
    spec:
      containers:
      - name: octopos
        image: 025325660074.dkr.ecr.ap-northeast-2.amazonaws.com/octopos_server:latest
        livenessProbe:
          httpGet:
            path: /v1/menus
            port: 3000
          initialDelaySeconds: 15
        readinessProbe:
          exec:
            command:
            - ls
        ports:
        - name: http-server
          containerPort: 3000
          protocol: TCP
```

## 8. Deployment

1. 오래된 pod 삭제 후 새로은 pod로 교체
  - pod template를 수정 후 pod를 삭제하면 모두 새것으로 교체됨. down-time 발생.
2. 새 pod를 올린 후 오래된 pod 삭제
  - pod를 새로 올린 후 selector를 변경하고, 기존 pod 삭제. 추가적인 하드웨어 리소스 필요.
3. Rolling Update

##### deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: octopos-v1
  labels:
    app: octopos
spec:
  replicas: 3
  selector:
    matchLabels:
      app: octopos
  template:
    metadata:
      labels:
        app: octopos
    spec:
      containers:
      - name: octopos
        image: 025325660074.dkr.ecr.ap-northeast-2.amazonaws.com/octopos_server:latest
        livenessProbe:
          httpGet:
            path: /v1/menus
            port: 3000
          initialDelaySeconds: 15
        readinessProbe:
          exec:
            command:
            - ls
        ports:
        - name: http-server
          containerPort: 3000
          protocol: TCP
```

##### service.yaml
```yaml
kind: Service
apiVersion: v1
metadata:
  name: octopos-service
spec:
  selector:
    app: octopos
  ports:
  - protocol: TCP
    port: 80
    targetPort: http-server
  type: LoadBalancer
```

```shell
kubectl create -f deployment.yaml --record

kubectl rollout status deployment octopos-v1
```

- `--record`를 포함하면 revision history를 기록

위 명령을 실행하면 replicaset을 만든 후 해당 replicaset의 pod를 생성. pod명으로 확인이 가능

### 새로운 이미지로 배포

- image url을 수정 

```
025325660074.dkr.ecr.ap-northeast-2.amazonaws.com/octopos_server@sha256:ffc92415b718a868b55a6d5b2cd81154bc60eff4ea01a54e552f425a4585d0ac
```

```shell
kubectl apply -f deployment.yaml
```

새로운 replicaset을 생성후 pod를 생성하고, ready 상태가 되면서 기존 pod들이 삭제

### Undo

```shell
kubectl rollout undo deployment octopos-v1
```

### 특정 Revision으로 돌리기

```shell
kubectl rollout history deployment octopos-v1

kubectl rollout undo deployment octopos-v1 --to-revision=1
```

## 아직까지 다루지 않은 내용

- Batch & CronJob









