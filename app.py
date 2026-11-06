from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

PAGE = r"""
<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>生日快乐 🎂</title>
<style>
*{box-sizing:border-box}body{margin:0;min-height:100vh;font-family:system-ui,-apple-system,"Microsoft YaHei",sans-serif;color:#fff;overflow-x:hidden;background:radial-gradient(circle at 20% 20%,#ffb6c1 0,transparent 28%),radial-gradient(circle at 80% 10%,#a18cd1 0,transparent 30%),linear-gradient(135deg,#20123a,#54265f 55%,#1d3155);display:grid;place-items:center;padding:28px}
.card{width:min(720px,100%);text-align:center;padding:48px 28px;border:1px solid #ffffff45;border-radius:28px;background:#ffffff16;backdrop-filter:blur(12px);box-shadow:0 25px 80px #0005;position:relative;z-index:2}
.tag{letter-spacing:5px;color:#ffd9e2;font-size:12px}.cake{font-size:76px;margin:18px 0;animation:bounce 2s infinite}.title{font-size:clamp(38px,8vw,68px);margin:8px 0;color:#fff0b8;text-shadow:0 4px 24px #ff9acb80}.name{color:#ffd0e0}.message{font-size:18px;line-height:1.9;color:#f8eafa;max-width:540px;margin:18px auto 28px}.btn{border:0;border-radius:999px;padding:14px 28px;background:linear-gradient(90deg,#ff9a9e,#fad0c4);color:#54265f;font-weight:700;font-size:16px;cursor:pointer;box-shadow:0 8px 24px #ff9a9e55}.btn:hover{transform:translateY(-2px)}.wish{min-height:30px;margin-top:18px;color:#ffe7a8;font-size:17px}.footer{margin-top:30px;font-size:12px;color:#ffffff9c}
.star{position:fixed;top:-20px;z-index:1;animation:fall linear infinite;pointer-events:none}@keyframes fall{to{transform:translateY(110vh) rotate(360deg)}}@keyframes bounce{50%{transform:translateY(-10px) rotate(3deg)}}
</style></head>
<body>
<div class="card">
<div class="tag">A DAY FULL OF LOVE & JOY</div>
<div class="cake">🎂</div>
<div class="title">生日快乐</div>
<h2 class="name">{{ name }}</h2>
<p class="message">愿新的一岁，<br>有数不尽的快乐，遇见更多美好；<br>心中有梦，眼里有光，脚下有路。<br>愿所有期待都能如约而至！</p>
<button class="btn" onclick="makeWish()">✨ 点击收下祝福</button>
<div class="wish" id="wish">今天，你是全世界最闪亮的主角！</div>
<div class="footer">Made with ❤️ · 祝你生日快乐</div>
</div>
<script>
const wishes=["愿你平安喜乐，万事胜意！","愿每一个愿望都慢慢实现！","愿你所行皆坦途，所遇皆温柔！","新的一岁，继续闪闪发光！"];
function makeWish(){document.getElementById('wish').textContent=wishes[Math.floor(Math.random()*wishes.length)];for(let i=0;i<24;i++){let e=document.createElement('span');e.className='star';e.textContent=['✨','💖','🎉','🌸'][Math.floor(Math.random()*4)];e.style.left=Math.random()*100+'vw';e.style.animationDuration=(2+Math.random()*3)+'s';e.style.fontSize=(16+Math.random()*20)+'px';document.body.appendChild(e);setTimeout(()=>e.remove(),5200)}}
</script></body></html>
"""

@app.route("/")
def home():
    name = request.args.get("name", "亲爱的你")
    return render_template_string(PAGE, name=name[:30])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
