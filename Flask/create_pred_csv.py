from prophet import Prophet
import database


###########################################
## 일주일을 예측해서 csv로 저장하는 함수 ##
###########################################
def make_pred_csv():
    store_list = database.select_all_store()
    product_list = database.select_all_product_id()

    for store in store_list:
        print("store :", store[0])
        for product in product_list:
            prophet = Prophet()

            # 데이터베이스로부터 한 품목에 대한 판매량 받아옴
            data = database.select_sale(store[0], product[0])

            # 한 품목에 대하여 학습
            prophet.fit(data)

            pred_df = prophet.make_future_dataframe(
                periods=7, freq='D', include_history=True)

            forecast = prophet.predict(pred_df)

            all = forecast.loc[data.shape[0] - 21:][['ds', 'yhat']]
            all.to_csv('data/pred_csv/pred_' +
                       str(store[0]) + '-' + str(product[0]) + '.csv')
    return


make_pred_csv()
