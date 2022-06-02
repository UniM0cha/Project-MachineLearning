from flask import Flask, request
import database
import predict
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 상품 번호를 전달받았을 때 그 상품의 일주일 뒤의 예상 판매량을 돌려준다.
@app.route('/predict', methods=['POST'])
def getPredict():
    value = request.form['item_id']
    print(value)
    return value


@app.route('/test', methods=['GET'])
def test():
    pred = predict.predict_next_week(1, 1)
    return {"holly": "shit"}


# 파이썬 명령어로 실행할 수 있음
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
