#Flask에서 HTML문서를 사용하는 방법
#플라스크의 경우, HTML문서를 보관하기 위한 디렉터리를 따로 만들어주어야 한다.
#그리고 해당 폴더의 위치는 반드시 플라스크를 실행시키는 코드와 같은 경료이고,
#templates라는 이름이여야 한다.

#locals() 메소드 활용해보기.
#웹 페이지 성격에 따라 HTML 문서에서 보여주어야 할 변수나 자료형이 매우 다양해진다.
#그래서 해당 함수 내의 지역 변수 전체를 인자로 보내주는 locals() 메소드를 사용하면 매우 편리하다.

from flask import Flask, flash, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App!"

@app.route("/user/")
def hello():
    users = ["Frank", "Steve", "Alice", "Bruce"]
    var = 1
    return render_template('user.html', **locals())
#locals() 메소드를 사용함으로 지역 내에서 선언된 users 리스트와 var 변수를 모두 render_template함수 내에 보내준다.

if __name__ == '__main__':
    app.run()
