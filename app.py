from flask import Flask

# API 서버를 구축하기 위한 기본 구조
app = Flask(__name__)

# API는 함수로 처리
@app.route('/', methods=['GET'])
def hello_world() :
    return 'Hello World!'

if __name__ == '__main__' :
    app.run()