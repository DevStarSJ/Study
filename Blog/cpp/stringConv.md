
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

* CStringW to std::string
```C++
CStringW CS;
std::wstring WS = CS.GetBuffer();
std::string S = "";
S.assign(WS.begin(), WS.end());
```

* std::string to CStringA
```C++
std::string S;
CString CS = S.c_str();
```

* std::string to CStringW
```C++
std::string S;
std::wstring WS = _T("");
WS.assign(S.begin(), S.end());
CString CS = WS.c_str();
```

