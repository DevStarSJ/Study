
* CString (CStringA, CStringW) to std::string
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

* std::string to CString (CStringA, CStringW)
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

* std::wstring to CString (CStringA, CStringW)
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

