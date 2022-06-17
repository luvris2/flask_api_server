from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add_two_nums', methods=['POST'])
def add() :
    # 클라이언트로부터 두 수를 받는다. request 라이브러리 사용
    data = request.get_json()
    ret = data['x'] + data['y']
    result = {'result' : ret}
    return jsonify(result)

if __name__ == '__main__' :
    app.run()