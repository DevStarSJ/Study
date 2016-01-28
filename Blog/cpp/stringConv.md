MFC (C++) 에서 여러가지 라이브러리를 사용하다보면
함수의 문자열을 받는 인자의 형식이 Unicode/Ansi , std::string, char*, LPCTSTR 등...
각각 제멋대로입니다.  

그래서 늘 해당 작업을 할때마다... 구글링...  
몇주 뒤에 또 이런 일이 있으면 또 구글링...

그래서 귀찮아서 정리해 봤습니다.

왠만한 조합은 다 있는듯 합니다.  
혹시 더 필요한 조합이나 아래 Code에 Error가 있으면 feedback 부탁드리겠습니다.  
(모든 조합을 다 Test해보진 않았습니다. ;;;)

###CString (CStringA, CStringW) to std::string
```C++
std::string S2(CString CS)
{
#ifdef _UNICODE
	std::wstring WS = CS.GetBuffer();
	std::string S = "";
	S.assign(WS.begin(), WS.end());
#else
	std::string S = CS.GetBuffer();
#endif
	return S;
}
```

###std::string to CString (CStringA, CStringW)
```C++
CString S2(std::string S)
{
#ifdef _UNICODE
	std::wstring WS = _T("");
	WS.assign(S.begin(), S.end());
	CString CS = WS.c_str();
#else
	CString CS = S.c_str();
#endif
	return CS;
}
```

###std::wstring to CString (CStringA, CStringW)
```C++
CString S2(std::wstring WS)
{
#ifdef _UNICODE
	CString CS = WS.c_str();
#else
	std::string S = "";
	S.assign(WS.begin(), WS.end());
	CString CS = S.c_str();
#endif
	return CS;
}
```

###std::string to/from std::wstring
```C++
std::string S3(std::wstring WS)
{
	std::string S = "";
	S.assign(WS.begin(), WS.end());
	return S;
}

std::wstring S3(std::string S)
{
	std::wstring WS = L"";
	WS.assign(S.begin(), S.end());
	return WS;
}
```

###CStringA to/from CStringW
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

###CString to char* buffer
```C++
void SMEMCPY(char* destBuf, CString & strSrc, int nSize)
{
	std::string str = CWVString::S2(strSrc);
	ZeroMemory(destBuf, nSize);
	memcpy(destBuf, &str[0], min(str.size(), (size_t)(nSize - 1)));
}
```


