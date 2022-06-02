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
    data = database.select_sale(store_id=2, product_id=2)
    result = predict.predict_next_week(data=data)
    print(result['df'])
    print(result['sum'])
    return 'test'


# 파이썬 명령어로 실행할 수 있음
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
