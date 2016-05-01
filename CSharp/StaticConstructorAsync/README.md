#Using async method in static constructor

static constructor 내부에서 async 함수를 호출할 경우 제대로 동작을 하지 않습니다.  
왠만해서는 이런식으로 code가 이루어지지 않도록 해야하지만, 어쩔수 없이 

그 원인에 대해서는 몇 가지 생각해 볼 수 있습니다.  
(사실 저도 아직 정확히 이거 때문이다 라고 말하진 못하겠습니다.)

###1. `CLR-internal lock` 때문

`static constructor`는 정확히 1번만 실행되어야 합니다.  
그러므로 `static constructor`가 실행될 때는 내부적으로 `CLR-internal lock`으로 해당 code를 1번만 실행되도록 수행합니다.  



