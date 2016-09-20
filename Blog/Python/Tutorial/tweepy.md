### tweepy 를 이용해서 파이썬으로 트위터 분석하기

####  Twitter Application Management 에 등록

1. twitter 에 가입하기 (생략)
  - 단, 모바일 인증까지 한 상태여야 함
2. 트위터 개발자 사이트(<https://apps.twitter.com>) 에 API 접근 권한 생성
  - `Create New App` 클릭
  - 앱 개발 정보 입력
    - Name : application 이름. 아무거나 입력
    - Description : application 설명. 아무거나 입력
    - Website : 소유한 도메인. 아무거나 입력
    - Callback URL : 인증된 후 연결될 URL. OAuth를 사용하는 앱일 경우 반드시 이 URL을 입력해야 함. 이것도 임의로 입력 가능.
    - Developer Agreement : 체크
    - `Create your Twitter application` 클릭
3. 생성된 정보 확인
  - `Keys and Access Tokens` 또는 `Test OAuth` 클릭
    - Consumer key : API 키 값
    - Consumer secret : API 비밀번호
  - `Keys and Access Tokens`에서 `Create My Access Token` 클릭
    - Access token : API 접근용 Token
    - Access token secret : API Token 비밀번호

#### tweepy 설치

 - <https://github.com/tweepy/tweepy>

```
pip install tweepy
```

