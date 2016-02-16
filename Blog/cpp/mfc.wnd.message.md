#사용자 정의 MFC Control의 Message 처리

CWnd를 상속받아서 사용자가 작성한 MFC Control의 메세지 처리하는 방법을 소개해드리겠습니다.  

통상적으로 Dialog, View, FormView (앞으로 편의상 Dialog라 칭함)에 Control을 올려서 사용하는데, 
그 구현자체를 Control안에서 하는 경우도 있지만,  
해당 Control을 사용하고 있는 Dialog에서 구현을 해야하는 경우도 있습니다.  
2개 이상의 Control을 같이 활용하려면 그렇게 해야 하죠.

```
Textbox에 숫자를 적어두고 Button을 눌렀을 경우 해당 숫자를 화면에 AfxMessageBox로 출력하는 경우  
해당 처리는 Button에서 하는게 아니라 Textbox와 Button을 가지고 있는 Dialog에서 하는게 편합니다.
```

3가지 방법이 있습니다.

1. Message로 처리
2. Command로 처리
3. Notify로 처리

각각에 대해서 소개해 드리겠습니다.

###1. 준비사항

사용자 정의 Control에서는 Message를 보낼 Dialog의 HWND을 알고 있어야 합니다.  
먼저 사용자 정의 Control에 자신을 포함하고 있는 Dialog의 HWND를 보관하는 멤버변수를 생성합니다.

```C++
public:
    HWND m_hwndDlg;
```

HWND를 알고 있어야 Message를 보낼 수 있습니다.

```C++
::SendMessage(m_hwndDlg, 메세지, WPARAM, LPARAM);
```

HWND가 아니라 Dialog의 pointer를 직접 가지고 있을 수도 있습니다.

```C++
pointer->SendMessage(메세지, WPARAM, LPARAM);
```



