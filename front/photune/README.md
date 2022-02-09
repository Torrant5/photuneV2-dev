# photune

## とりあえず起動させ方
1. node.jsが入っていない場合インストール
2. このディレクトリで `npm install`
3. .envがあるか確認。なければ、.envに以下を書く。

``` .env
   VUE_APP_API_BASE=https://ai.photune.net/
```

4. `npm run serve`でデバッグ用ローカルサーバ立ち上げ
5. http://localhost:8080/ あたりで見れるはず

.envでAPIを指定しているので、ローカルのVueでも一応getはできるはず。Postはそのうち直す。

下のコマンドでビルドなどが出来る。

main.js, App.vue, componentsでVueの処理を行っている。各コンポーネントを弄りたければcomponents内のやつを弄る。コンポーネントを配置するときののmarginなどを弄りたい場合はApp.vueかも。store.jsはデータの保持などをしている。


## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
