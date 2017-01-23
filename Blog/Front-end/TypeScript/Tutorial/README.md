# Install

- `npm -g typescript` : 설치
- `tsc -version` : 버전확인

# Test

## app.ts
- `tsc app.ts` : app.js로 생성
- `tsc --out bundle.js app.ts` : bundle.js로 생성
- `tsc --watch --out bundle.js app.ts` : app.ts가 바뀌면 자동으로 bubdle.js 생성
- `tsc --init` : tsconfig.jso 생성
- `tsc` : 해당 폴더의 모든 파일 컴파일

## tsconfig.json
- `"compilerOptions" : { ... }`
  - `"outDir": "./dist"` : 컴파일 후 js 파일들을 해당 폴더내에 생성
  - `"noEmitOnError": true` : 컴파일 오류시 js 파일을 생성하지 않음
  - `"rootDir" : "./src"` : 시작 폴더
- `"exclude" : [ "node_modules"]` : 해당 폴더/파일은 컴파일시 제외
- `"files" : [ "src/main.ts" ]` : 해당 파일들을 포함 (와일드카드 `*.ts`를 지원하지 않음)


```
{
    "compilerOptions": {
        "module": "commonjs",
        "target": "es5",
        "noImplicitAny": false,
        "sourceMap": false
    }
}
```

```
    "exclude" : [ "node_modules"]
```

## Typings

The Typescript Definition Manager

<https://www.npmjs.com/package/typings>

```
npm install typings --global
typings install lodash --save
npm install --save lodash
```

npm install --save rxjs : es6 로 세팅 변경하면 오류가 안나긴함

typings install es6-shim --save --global
