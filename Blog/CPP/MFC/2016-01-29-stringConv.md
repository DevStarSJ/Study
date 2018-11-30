---
layout: post
title: "MFC UAC 관련 사항 정리"
subtitle:  
categories: devlopment
tags: c++
comments: true
---

MFC (C++) 에서 여러가지 라이브러리를 사용하다보면
함수의 문자열을 받는 인자의 형식이 `Unicode/Ansi , std::string, char*, LPCTSTR` 등...
각각 제멋대로입니다.  

그래서 늘 해당 작업을 할때마다... 구글링...  
몇주 뒤에 또 이런 일이 있으면 또 구글링...

그래서 귀찮아서 정리해 봤습니다.

왠만한 조합은 다 있는듯 합니다.  
혹시 더 필요한 조합이나 아래 Code에 Error가 있으면 feedback 부탁드리겠습니다.  
(모든 조합을 다 Test해보진 않았습니다. ;;;)

처음엔 문제 많은 code였는데 feedback 주신분들이 친절히 가르쳐 주셔서 조금씩 보완하고 있는 중입니다.  
감사드립니다. ^_^

### CString (CStringA, CStringW) to std::string
```C++
std::string S2(CString& CS)
{
#ifdef _UNICODE
	USES_CONVERSION;
	std::string S = W2A(CS.GetBuffer());
#else
	std::string S = CS.GetBuffer();
#endif
	return S;
}
```

### std::string to CString (CStringA, CStringW)
```C++
CString S2(std::string& S)
{
#ifdef _UNICODE
	USES_CONVERSION;
	CString CS = A2W(S.c_str());
#else
	CString CS = S.c_str();
#endif
	return CS;
}
```

### std::wstring to CString (CStringA, CStringW)
```C++
CString S2(std::wstring& WS)
{
#ifdef _UNICODE
	CString CS = WS.c_str();
#else
	USES_CONVERSION;
	CString CS = W2A(WS.c_str());
#endif
	return CS;
}
```

### std::string to/from std::wstring
```C++
std::string S3(std::wstring& WS)
{
	USES_CONVERSION;
	return std::string(WA2(WS.c_str()));
}

std::wstring S3(std::string& S)
{
	USES_CONVERSION;
	return std::wstring(A2W(S.c_str()));
}
```

### CStringA to/from CStringW
```C++
CStringA CA
CStringW CS(CA);
CStringA _CA(CS);
```

### TCHAR* (char\*, wchat_t\*) to LPSTR, LPTSTR, LPCSTR, LPCTSTR
```C++
LPSTR S4_LPSTR(TCHAR * pChar)
{
#ifdef _UNICODE
	return (LPSTR)S3(std::wstring(pChar)).c_str();
#else
	return (LPSTR)pChar;
#endif
}

LPTSTR S4_LPTSTR(char * pChar)
{
	return (LPTSTR)S3(std::string(pChar)).c_str();
}

LPTSTR S4_LPTSTR(wchar_t * pChar)
{
	return (LPTSTR)pChar;
}

LPCSTR S4_LPCSTR(TCHAR * pChar)
{
	return (LPCSTR)S4_LPSTR(pChar);
}

LPCTSTR S4_LPCTSTR(TCHAR * pChar)
{
#ifdef _UNICODE
	return (LPCTSTR)pChar;
#else
	return (LPCTSTR)S4_LPTSTR(pChar);
#endif
}
```

### CString to char* buffer
```C++
void SMEMCPY(char* destBuf, CString & strSrc, int nSize)
{
	std::string str = CWVString::S2(strSrc);
	ZeroMemory(destBuf, nSize);
	memcpy(destBuf, &str[0], min(str.size(), (size_t)(nSize - 1)));
}
```

### 전체 Code

<https://gist.github.com/DevStarSJ/c68e55449dc6e68d7376>

