
* CStringA to std::string
```C++
CStringA CS;
std::string S = CS.GetBuffer();
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

