# 生日快乐 Python 网站 🎂

一个使用 Python + Flask 制作的生日祝福网页，带有渐变星空背景、祝福按钮和飘落特效。

## 本地运行

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS / Linux:
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

浏览器打开 http://127.0.0.1:5000

## 自定义名字

访问 `http://127.0.0.1:5000/?name=林倩` 即可显示指定名字。

## 部署

可部署到支持 Python/Flask 的平台。启动命令：`python app.py`。
