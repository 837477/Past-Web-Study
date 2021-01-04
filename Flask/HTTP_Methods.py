from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
#기본적으로 Flask의 라우팅은 GET 메소드로 응답하지만, 필요한 경우 특정 메소드에만 응답하도록 선언할 수 있다.
#위의 코드의 경우 POST, GET 2개의 메소드에 대한 응답이 가능함.
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
        #이 코드는 해당 요청에서 입력된 form 정보의 'nm'필드 값을 가져오겠다는 뜻.
        #즉, 달랑 어떠한 폼이 있는 HTML파일속에서 서버로 요청한 form테그(필드) 속에 'nm'이라는 값을 가져오겠다는 뜻이다.
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))

if __name__ == '__main__':
    app.run(debug = True)
