```
call svnindex.cmd -source="{SolutionFolder}" -symbols="{SolutionFolder}\bin\Unicode Release"
```

```
symstore.exe add /r /f "{SolutionFolder}\bin\Unicode Release\*.*" /s "{SymbolRepository}" /t "{Name}" /compress
```
