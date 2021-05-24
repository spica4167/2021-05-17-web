from flask import Flask, render_template, request
from a import money_pung
app = Flask(__name__)

#   서버를 의미.
#   php와 같이 주소/에시.php 처럼 구분을 위한 페이지이름을 의미.
@app.route('/')
def hello():
    # 응답 및 첫페이지
    return 'Hello, World!'

@app.route('/money')
def money():
    return render_template("money.html")

@app.route('/show', methods=['GET', 'POST'])
def show():
    if request.method == 'GET':
        return "Get 으로 들어온 페이지"
    else:
    # form으로 전달된 데이터를 받아서 뻥튀기
        money = request.form['money']
        #money 의 값이 문자열이기 때문에 숫자로 변경
        print("전달된 값은 : ", int (money)*2)
        #돈을 이제 출력해줌.
    im = money_pung(int(money)) #뻥튀기 함수 사용
    return "당신의 능력을 보여줘~ 얍<br>{}원 드립니다.".format(im)
        #return "당신의 능력을 보여줘~ 얍<br>{}원 드립니다.".format(money_pung(int money))

@app.route('/showmoney')
def sm():
    #여러줄의 코드를 쓰고싶으면 따옴표(')을 3개 찍어서 작성해준다.
    #render_template 사용시 1번째줄에 import ~~ 뒤에 render_template을 꼭 작성하여 주어야한다.
    return render_template("showmoney.html")

if __name__ == '__main__':
    app.run()