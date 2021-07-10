# playwright-practice

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