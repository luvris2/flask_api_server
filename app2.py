from flask import Flask, jsonify
from http import HTTPStatus

# API 서버를 구축하기 위한 기본 구조
app = Flask(__name__)

# API는 함수로 처리
@app.route('/', methods=['GET'])
def hello_world() :
    return 'Hello World!'

@app.route('/hithere', methods=['GET'])
def hi_there() :
    return 'Hithere~'

@app.route('/add', methods=['GET'])
def add():
    data = 283 + 111
    return str(data) # 반환값은 문자열로 반환해야 함

@app.route('/act/data', methods=['GET'])
def act() :
    ret = { 'count' : 2 ,
            'students' : [ { 'name' : '홍길동', 'age' : 38 } ,
                           { 'name' : '김나나', 'age' : 25 } ]}
    return jsonify(ret)

if __name__ == '__main__' :
    app.run()