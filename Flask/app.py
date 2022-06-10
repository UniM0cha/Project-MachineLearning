from flask import Flask, request
import database
import predict
import pandas as pd
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 자동발주 홈화면
@app.route('/auto_order_list', methods=['POST'])
def auto_order_list():
    store_id = request.json['store_id']
    # page = request.json['page']
    result = predict.auto_order_list(store_id=store_id)

    return {
        "chart_data": result['chart_data'],
        "table_data": result['table_data']
    }


@app.route('/make_pred_csv', methods=['POST'])
def make_pred_csv():
    predict.make_pred_csv()
    return 'success'


# 상품 번호를 전달받았을 때 그 상품의 일주일 뒤의 예상 판매량을 돌려준다.
@app.route('/get_one_predict', methods=['POST'])
def getPredict():
    store_id = request.json['store_id']
    product_id = request.json['product_id']

    # data = database.selectSale(store_id=store_id, product_id=product_id)
    result = predict.predict_next_week(
        store_id=store_id, product_list=[product_id])
    # result = predict.next_week(data=data)

    past_ds = result['past_list'][0]['ds'].to_list()
    past_yhat = result['past_list'][0]['yhat'].to_list()
    future_ds = result['future_list'][0]['ds'].to_list()
    futrue_yhat = result['future_list'][0]['yhat'].to_list()

    return {
        'past_ds': past_ds,
        'past_yhat': past_yhat,
        'future_ds': future_ds,
        'futrue_yhat': futrue_yhat,
    }


# 모든 상품의 예측값을 반환한다.
@app.route('/get_all_predict', methods=['POST'])
def getAllPredict():
    store_id = request.json['store_id']

    all_product = database.selectAllProduct(store_id)

    result = predict.predict_next_week(
        store_id=store_id, product_list=all_product)


@app.route('/product_list', methods=['POST'])
def getProductList():
    store_id = request.json['store_id']
    product_id = request.json['product_id']

    data = database.select_stock
    return


# 파이썬 명령어로 실행할 수 있음
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
