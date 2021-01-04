# routes.py
from flask import Flask
app = Flask(__name__)
#app 객체에 Flask객체를 선언했다. 그럼 해당 app객체를 통해 플라스크를 사용할 수 있게 되었다.
#__name__의 경우 이 routes.py를 실행시키면 "__main__"이라는 문자열이 들어가게 된다.

@app.route('/')
#데코레이터를 사용하여 hellow_world 함수를 wrapping되었음을 알 수 있다.
#데코레이터를 통해 웹으로 접근한 사용자가 어떤 URL에 따라 어떤 함수를 실행시켜야 할지 정해주게 된다.
#현재 '/'의 경우, 메인페이지가 URL 파라미터인 셈이다.
#즉 데코레이터 인자 속이 URL인 느낌이다.
def hellow_world():
    return 'Hello, World!'

#ex) user/837477, user/ash123
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
#URL에 route()인자인 <>안에 있는 것과 같은 이름의 변수를 인자로 받아온다.
#즉, user/837477 이라는 인자로 입력받게 되면 <username>에 위치한 837477이라는 문자열을 코드에서 사용할 수 있게 하는 것이다.

#ex) post/123
@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show the post with the given id, the id is an integer
    return 'Post %d' % post_id
#이 함수도 위에 함수랑 같지만, 인자에 <int>를 넣어서 정수 값 만 입력되었을 때, 해당 함수를 실행시킨다.
#만약 정수 값이 아닌 경우, 해당 페이지를 찾을 수 없다고 뜰 것이다.

#인자로 받을 변수 규칙에는 %s, %d, %f 등이 있고, 아무것도 안 적으면 자동으로 string 인자를 주게된다.


#또한, 특정 함수 1개에 2개이상의 데코레이터를 덮어 씌울 수 있다.
#예를들어 아래코드를 보면
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#2개의 데코레이터를 씌어준 후, 기본 함수 인자 설정을 None으로 해주면,
#인자가 없을 경우 첫 번째 URL이고, 있을경우 두 번째 URL이 되는 것이다.



if __name__ == '__main__':
    app.run()

#app.run()에서 사용할 수 있는 인자들
#port (ex: port = 5000)
#host (ex: 0.0.0.0, 127.0.0.1, ...)
#debug(true or False)
