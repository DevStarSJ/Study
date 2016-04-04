### Symbol 등록

```
call svnindex.cmd -source="{SolutionFolder}" -symbols="{SolutionFolder}\bin\Unicode Release"
```

```
symstore.exe add /r /f "{SolutionFolder}\bin\Unicode Release\*.*" /s "{SymbolRepository}" /t "{Name}" /compress
```

### symstore 사용법 (Symbol 삭제 포함)
<https://msdn.microsoft.com/en-us/library/windows/desktop/ms681378(v=vs.85).aspx>
