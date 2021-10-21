from flask import *

# Flaskオブジェクトの生成
app = Flask(__name__)

# ルート( / )へアクセスがあった時 --- (*1)
@app.route("/")
def root():
    # HTMLでWebフォームを記述 --- (*2)
    return """
    <html><body>
    <form action="/calc" method="post">
      <input type="text" name="num">
      <input type="submit" value="素数判定">
    </form>
    """

# フォームの値を受け取って結果を表示 --- (*3)
@app.route("/calc", methods=["post"])
def calc():
    num = int(request.form.get("num"))
    icount = 0
    for i in range(2,num):
        if num%i == 0:
            icount =  1
            break
        #else:#何もせず

    if icount == 0:
        r = "素数です"
    else:
        r = "合成数です"
    return "<h1>" + str(num) + "は..." + str(r) + "</h1>"    

# サーバーを起動
if __name__ == "__main__":
    app.run(debug=True, port=8888)

# https://news.mynavi.jp/article/zeropython-64/
# https://www.sejuku.net/blog/68423