from flask import Flask, render_template
app = Flask(__name__)

#   서버를 의미.
#   php와 같이 주소/에시.php 처럼 구분을 위한 페이지이름을 의미.
@app.route('/')
def hello():
    # 응답
    return 'Hello, World!'

@app.route('/money')
def money():
    return '돈을 입력하세요.'

@app.route('/showmoney')
def sm():
    #여러줄의 코드를 쓰고싶으면 따옴표(')을 3개 찍어서 작성해준다.
    #render_template 사용시 1번째줄에 import ~~ 뒤에 render_template을 꼭 작성하여 주어야한다.
    return render_template("showmoney.html")

if __name__ == '__main__':
    app.run()