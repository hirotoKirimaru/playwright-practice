# playwright-practice

# ビルドする

Microsoftから提供されているDockerイメージにはplaywrightそのものは入っていない。ですので、pipやnpm等で明示的に入れてあげる必要がある。
  
その一連のコマンドをDockerfileにしているので、```build.sh```を実行してイメージを作成する。
  
# コンテナにログインする

```run.sh```を使用して、ログインする。シナリオファイルをマウントさせたいので、ディレクトリを変更すること。```GitHub Codespaces```が動くようにしている。
  
# シナリオを実行する

```python sample.py```を実行すればOK。

# 備考

```playwright codegen```に関しては、コンテナに画面表示機能が無いため難しそうだ。
  
コード生成を使うときはローカルに環境構築を行い、実行するときだけこちらをじっこうする、というので十分カバーはできる。




```python
pip install playwright
playwright install
```

# Docker動作環境

```bash
docker pull mcr.microsoft.com/playwright:focal
```

ログイン？

```bash
docker run -it --rm --ipc=host mcr.microsoft.com/playwright:focal /bin/bash
# Codespacesにマウントさせる
docker run -v /workspaces/playwright-practice:/var/scenario -it --rm --ipc=host mcr.microsoft.com/playwright:focal /bin/bash
```

```
pip install playwright
```



## nodeでも確認してみる

```bash
npm i -D playwright
```

これで実行。
```bash
node sample-node.js 
```