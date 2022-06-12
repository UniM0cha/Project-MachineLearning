import json
from flask import Flask, make_response, request
from matplotlib.font_manager import json_load
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
    # store_id = request.json['store_id']
    store_id = 1
    # page = request.json['page']
    result = predict.auto_order_list(store_id=store_id)

    return {
        "chart_data": result['chart_data'],
        "table_data": result['table_data']
    }


# 상품의 리스트 출력
@app.route('/product_list', methods=['POST'])
def get_product_list():
    result = database.select_all_product()
    return {"data": result}


# 상품 발주
@app.route('/order', methods=['POST'])
def order():
    store_id = 1
    # store_id = request.json['store_id']
    req_order_list = request.json['order']

    order_list = []
    for order in req_order_list:
        list = []
        list.append(order['product_id'])
        list.append(order['order'])
        order_list.append(list)

    print(order_list)
    database.update_stock(store_id=store_id, order_list=order_list)
    return make_response("처리 완료", 201)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
