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


# 상품의 리스트 출력
@app.route('/product_list', methods=['POST'])
def get_product_list():
    result = database.select_all_product()
    return {"data": result}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
