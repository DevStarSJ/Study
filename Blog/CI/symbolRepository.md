### Symbol 등록

```
call svnindex.cmd -source="{SolutionFolder}" -symbols="{SolutionFolder}\bin\Unicode Release"
```

```
symstore.exe add /r /f "{SolutionFolder}\bin\Unicode Release\*.*" /s "{SymbolRepository}" /t "{Name}" /compress
```

>e.g.  
call svnindex.cmd -source="d:\svn\trunk" -symbol="d:\svn\trunk\bin\Unicode Release"
symstore add /r /f "d:\svn\trunk\bin\Unicode Release\*.*" /s "d:\symbol" /t "MyApp" /compress

### 저장된 Symbol 확인

- `{SymbolRepository}\000Admin\server.txt`에서 확인
- 각 ID별 Build일시. 이름 (/t 옵션 뒤에 이름) 확인이 가능

### Symbol 삭제

```
symstore del /i ID /s "{SymbolRepository}"
```

>e.g.  
symstore del /i 142 /s "d:\symbol"

### symstore 사용법 (Symbol 삭제 포함)
<https://msdn.microsoft.com/en-us/library/windows/desktop/ms681378(v=vs.85).aspx>
