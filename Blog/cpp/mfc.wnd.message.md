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

먼저 간단하게 Dialog 기반으로 MFC Application Project를 생성해주세요.

그런 다음 아래의 2개의 File을 추가합니다.

#####UserWnd.h
```C++
#pragma once
#include "afxwin.h"

#define WM_USER_WND		       WM_USER + 10001          // User-defined Message (#1)

class CUserWnd : public CWnd
{
public:
	HWND m_hwndDlg = nullptr;                               // HWND of Parent Dialog (#2)

protected:
	DECLARE_MESSAGE_MAP()                                   // Message Map Macro (#3)
	afx_msg void OnLButtonDown(UINT nFlags, CPoint point);  // Mouse left button click event (#4)
};
```

- #1 : 사용자 정의 메세지 입니다.
- #2 : 메세지를 보낼려면 해당 메세지를 받을 Dialog의 pointer나 HWND값이 필요합니다.
  - HWND를 알고 있는 경우 : `::SendMessage(m_hwndDlg, 메세지, WPARAM, LPARAM);`
  - Dialog의 pointer를 알고 있는 경우 : `pointer->SendMessage(메세지, WPARAM, LPARAM);`
- #3 : Message Map을 사용할려면 헤더파일에 선언해줘야할 매크로 입니다.
- #4 : 예제로 마우스 왼쪽 버튼을 눌렀을 경우 Dialog로 Message를 전달하기 위하여 해당 메세지를 사용했습니다.

#####UserWnd.cpp
```C++
#include "stdafx.h"
#include "UserWnd.h"

BEGIN_MESSAGE_MAP(CUserWnd, CWnd)                        // Message Map (#1)
	ON_WM_LBUTTONDOWN()                                  // Mouse left button click event (#2)
END_MESSAGE_MAP()

void CUserWnd::OnLButtonDown(UINT nFlags, CPoint point)  // Mouse left button click event (#3)
{
	HWND hWnd = GetSafeHwnd();

	if (hWnd == NULL) return;
	if (!::IsWindow(hWnd)) return;

	int nID = GetDlgCtrlID();

	if (m_hwndDlg != nullptr)
	{

	}
	
	CWnd::OnLButtonDown(nFlags, point);                  // Call Parent Function (#4)
}
```

- #1 : Message Map 정의 부분입니다.
  - 첫번째 인자 : 해당 class를 적어줍니다.
  - 두번째 인자 : 부모 class를 적어줍니다. 해당 class 내에 적어주지 않은 메세지에 대해서는 부모 class에서 처리하게 됩니다.
    - 만약 CXTPChartControl을 상속받아서 만든 사용자 정의 Control일 경우 두번째 인자에 CXTPChartControl을 적어줘야 합니다.
- #2 : MFC에서 미리 정의해놓은 것으로 마우스 왼쪽 버튼 눌렀을때 OnLButtonDown()을 실행하게 됩니다.
- #3 : 사용자 정의 메세지를 보내기위해 필요한 값들 HWND, ControlID를 가지고 있습니다. if 구문 안에서 각각의 메세지 타입에 따른 구현이 달라집니다.
- #4 : 부모 class에서 해당 메세지에 대한 동작을 계속 하도록 호출해 줍니다. 부모 class의 작업이 필요없다면 이 줄은 삭제하면 됩니다.



