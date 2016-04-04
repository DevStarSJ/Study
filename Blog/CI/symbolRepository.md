```
call svnindex.cmd -source="{SolutionFolder}" -symbols="{SolutionFolder}\bin\Unicode Release"
```

```
symstore.exe add /r /f "{SolutionFolder}\nim\Unicode Release\*.*" /s "{SymbolRepository}" /t "{Name}" /compress
```
