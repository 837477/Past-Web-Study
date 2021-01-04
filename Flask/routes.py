# routes.py
from flask import Flask
app = Flask(__name__)
#app 객체에 Flask객체를 선언했다. 그럼 해당 app객체를 통해 플라스크를 사용할 수 있게 되었다.
#__name__의 경우 이 routes.py를 실행시키면 "__main__"이라는 문자열이 들어가게 된다.

@app.route('/')
#데코레이터를 사용하여 hellow_world 함수를 wrapping되었음을 알 수 있다.
#데코레이터를 통해 웹으로 접근한 사용자가 어떤 URL에 따라 어떤 함수를 실행시켜야 할지 정해주게 된다.
#현재 '/'의 경우, 메인페이지가 URL 파라미터인 셈이다.
def hellow_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

#app.run()에서 사용할 수 있는 인자들
#port (ex: port = 5000)
#host (ex: 0.0.0.0, 127.0.0.1, ...)
#debug(true or False)
