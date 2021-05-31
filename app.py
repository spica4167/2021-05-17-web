from flask import Flask, render_template, request, Response, redirect #21-05-31 response, redirect 추가
from a import money_pung, logincheck # 21-05-31 logincheck 추가
app = Flask(__name__)

#   서버를 의미.
#   php와 같이 주소/에시.php 처럼 구분을 위한 페이지이름을 의미.
@app.route('/')
def hello():
    # 응답 및 첫페이지
    return render_template("main.html")

@app.route('/money')
def money():
    return render_template("money.html")

@app.route('/signup')
def su():
    return render_template("signup.html")

@app.route('/login')
def lg():
    return render_template("login.html")

# 회원가입 페이지
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    else:
        email = request.form['email']
        pswd = request.form['pswd']
        username = request.form['username']
        return "{}</br>{}</br>{}</br> 회원 정보".format(email, pswd, username)
        #결과값은 페이지이후에 적은 이메일 패스워드 이름 회원 정보 라고 출력이 된다. 이부분을 나중에 SQL연동해서 사용.

# 로그인 페이지
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        email = request.form['email']
        pswd = request.form['pswd']
        #a.py에서 logincheck를 불러서 사용함.
        #msg는 메시지를 의미함
        msg = logincheck(email,pswd)
        return "{}</br>{}</br>{}".format(email, pswd, msg) #{}순서대로 email, pswd, msg가 출력된다.
        # 가입과 마찬가지로 페이지 이후 적은 이메일 패스워드 로그인처리 라고 출력이 된다.

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