from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name =='admin':
        return redirect('/admin')

    else:
       return redirect(url_for('hello_guest',guest
       = name))

if __name__ == '__main__':
    app.run(debug = True)

#위의 코드는 /user/<name> URL에 입력된 name 값에 따라 다른 URL로 향하게 되어 있다. name 값이 admin일 경우, /admin URL(hello_admin())를 실행시키고, 나머지는 guest/<guest> URL(hello_guest)를 실행시키는 구조이다.

#즉, 127.0.0.1:5000/user/admin 이면
#hello_admin() 함수가 실행돼서, 'Hello Admin'이 출력.
#이외에 127.0.0.1:5000/user/XXXX <-아무 값 이면,
#hello_guest() 함수가 실행 됨.

# return redirect('/admin')  == return redirect(url_for("hello_admin"))
#해당 URL로 리다이렉트시키는 함수이다. URL을 줘도 되고, url_for() 메소드를 사용하여 실제 함수 이름을 인자로 주어도 된다.

# return redirect(url_for('hello_guest',guest = name))
#url_for의 경우, 나머지 인자를 넘겨 줄때, 위 코드처럼 변수로 나눠서 넘겨줄 수 있다. 파이썬은 문자열 접근이 워낙 편하니까 실제 URL로 줘도 비슷하니, 편한걸 쓰도록 하자.
