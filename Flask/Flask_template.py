#Flask에서 HTML문서를 사용하는 방법
#플라스크의 경우, HTML문서를 보관하기 위한 디렉터리를 따로 만들어주어야 한다.
#그리고 해당 폴더의 위치는 반드시 플라스크를 실행시키는 코드와 같은 경료이고,
#templates라는 이름이여야 한다.

from flask import Flask, render_template
app = Flask(__name__)

#ex)hello/837477
@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name = user)

#render_template('hello.html', name=user)
#플라스크에서 외부의 html파일을 불러오기 위해 사용하는 !메소드!
#templates폴더에서 인자로 받은 hello.html 파일을 탐색한 후,
#name인자를 건네주며 페이지를 실행.

#<h1>Hello {{ name }}!</h1>
#인자로 받은 name 변수는 이런 형태로 html 문서에서 출력할 수 있다. 이렇게 { } 등을 사용하여 html 문서 내에서 직접 코드를 실행시키는 문법을 Template Engine이라고 부르며, 이 템플릿 엔진의 이름은 Jinja2라고 한다.

#Jinja2
#이 템플릿 엔진을 사용하여 HTML 문서에서 몇 가지 파이썬 구문을 작성하고 실행시킬 수 있다. (if 문, for 문 및 일부 메소드들 사용가능) 코드에 용도에 따라 적절한 괄호를 감싸주어서 사용하면 된다.
# {% ... %} for Statements
# {{ ... }} for Expressions to print to the template output
# {# ... #} for Comments not included in the template output
# # ... ## for Line Statements

if __name__ == '__main__':
    app.run(debug = True)
