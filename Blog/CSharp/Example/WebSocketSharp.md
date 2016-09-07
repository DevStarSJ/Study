`checkIfAvailable` : true로 들어간 인자에 대해서는 허용이 안됨
ex. connecting : true 인 경우 현재 상태가 connecting이면 오류
- connect() : connecting, closed 일때만 가능 (open, closing은 안됨)