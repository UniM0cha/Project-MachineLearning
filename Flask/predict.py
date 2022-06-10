import pandas as pd
from prophet import Prophet
import database


######################################################
## 자동 발주 페이지에 필요한 데이터를 생성하는 함수 ##
######################################################
def auto_order_list_page(store_id, page):
    db_result = database.select_product_stock_page(
        store_id=store_id, page=page)

    db_result_df = pd.DataFrame(
        db_result, columns=['product_id', 'product_name', 'stock'])
    print("DB 데이터 :", db_result_df)

    predict_result = predict_next_week(
        store_id, db_result_df['product_id'].to_list())

    all_list = predict_result['all_list']
    past_list = predict_result['past_list']
    future_list = predict_result['future_list']

    ############## chart_data를 만드는 과정 ###############
    product_name_list = db_result_df['product_name'].to_list()

    date_list = []
    pred_sale_list = []
    for all in all_list:
        date_list.append(all['ds'].to_list())
        pred_sale_list.append(all['yhat'].to_list())

    chart_data = dict(
        상품명=product_name_list,
        날짜=date_list,
        판매량=pred_sale_list)

    ############### table_data를 만드는 과정 #################

    return {
        "chart_data": chart_data,
        "table_data": []
    }


def auto_order_list(self, store_id, page):
    result = database.select_product_stock(store_id=store_id, page=page)

    products = []
    for i in result:
        products.append(i[0])

    predict_result = self.predict_next_week(store_id, products)

    future_list = predict_result['future_list']
    print(future_list)

    return


#########################################
## 다음주까지의 판매량을 예측하는 함수 ##
#########################################
def predict_next_week(store_id, product_list=[]):

    all_list = []
    past_list = []
    future_list = []

    for product in product_list:
        prophet = Prophet()

        # 데이터베이스로부터 한 품목에 대한 판매량 받아옴
        data = database.select_sale(store_id, product)

        # 한 품목에 대하여 학습
        prophet.fit(data)

        pred_df = prophet.make_future_dataframe(
            periods=7, freq='D', include_history=True)

        forecast = prophet.predict(pred_df)

        # pred = forecast.loc[data.shape[0]:]
        # next_week_sum = sum(pred['yhat'])

        # past_future = forecast.loc[data.shape[0]-21:][['ds', 'yhat']]

        all = forecast.loc[data.shape[0] - 21:][['ds', 'yhat']]
        all_list.append(all)

        past = forecast.loc[data.shape[0] -
                            21: data.shape[0]][['ds', 'yhat']]
        past_list.append(past)

        future = forecast.loc[data.shape[0]:][['ds', 'yhat']]
        future_list.append(future)

    return {
        "all_list": all_list,
        "past_list": past_list,
        "future_list": future_list
    }
