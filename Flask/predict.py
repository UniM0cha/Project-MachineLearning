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

    predict_result = predict_next_week_from_pickle(
        store_id, db_result_df['product_id'].to_list())

    all_list = predict_result['all_list']
    past_list = predict_result['past_list']
    future_list = predict_result['future_list']
    # print(future_list)

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
    # pred_sum_list = []
    # for future in future_list:
    #     pred_sum = round(sum(future['yhat']), 0)
    #     pred_sum_list.append(pred_sum)
    # pred_sum_list
    # # print(pred_sum_df)

    # db_result_df['predict'] = pred_sum_df

    # order = pd.DataFrame(
    #     db_result_df['predict'] - db_result_df['stock'], index=['order'])
    # order[order < 0] = 0
    # print("order :", order)
    # db_result_df['order'] = order['order']

    # print("db_result_df :", db_result_df)

    return {
        "chart_data": chart_data,
        "table_data": []
    }


def auto_order_list(store_id):
    db_result = database.select_product_stock(store_id=store_id)
    db_result_df = pd.DataFrame(
        db_result, columns=['product_id', 'product_name', 'stock'])

    pred_sum_list = []
    pred_list = []
    for product_id in db_result_df['product_id']:
        pred = pd.read_csv('data/pred_csv/pred_' +
                           str(store_id) + '-' + str(product_id) + '.csv')
        pred_sum_list.append(sum(pred['yhat'].iloc[21:]))
        pred_list.append(pred)

    db_result_df['pred_sum'] = pd.DataFrame(
        pred_sum_list, columns=['pred_sum'])
    db_result_df = db_result_df.sort_values(
        by='pred_sum', ascending=False).head(5)
    # print(db_result_df)

    # print(db_result_df['product_id'].iloc[0])
    # print(pred_list[db_result_df['product_id'].iloc[0]])

    pred_top5_list = []
    for i in db_result_df['product_id']:
        pred_top5_list.append(pred_list[i])

    # print(pred_list)

    # predict_result = predict_next_week(
    #     store_id, db_result_df['product_id'].to_list())

    # all_list = predict_result['all_list']
    # past_list = predict_result['past_list']
    # future_list = predict_result['future_list']
    # # print(future_list)

    # db_result = database.select_stock_product_id(
    #     store_id=store_id, product_id=1)

    # db_result_df = pd.DataFrame(
    #     db_result, columns=['product_id', 'product_name', 'stock'])
    # print("DB 데이터 :", db_result_df)

    # ############## chart_data를 만드는 과정 ###############
    product_name_list = db_result_df['product_name'].to_list()

    date_list = []
    pred_sale_list = []
    for pred in pred_top5_list:
        date_list.append(pred['ds'].to_list())
        pred_sale_list.append(pred['yhat'].to_list())

    chart_data = dict(
        상품명=product_name_list,
        날짜=date_list,
        판매량=pred_sale_list)

    ############### table_data를 만드는 과정 #################
    # pred_sum_list = []
    # for future in future_list:
    #     pred_sum = round(sum(future['yhat']), 0)
    #     pred_sum_list.append(pred_sum)
    # pred_sum_list
    # # print(pred_sum_df)

    # db_result_df['predict'] = pred_sum_df

    # order = pd.DataFrame(
    #     db_result_df['predict'] - db_result_df['stock'], index=['order'])
    # order[order < 0] = 0
    # print("order :", order)
    # db_result_df['order'] = order['order']

    # print("db_result_df :", db_result_df)

    return {
        "chart_data": chart_data,
        "table_data": []
    }


###########################################
## 일주일을 예측해서 csv로 저장하는 함수 ##
###########################################
def make_pred_csv():
    store_list = database.select_all_store()
    product_list = database.select_all_product()

    all_list = []
    past_list = []
    future_list = []

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


# #########################################
# ## 다음주까지의 판매량을 예측하는 함수 ##
# #########################################
# def predict_next_week(store_id, product_list=[]):

#     all_list = []
#     past_list = []
#     future_list = []

#     for product in product_list:
#         prophet = Prophet()

#         # 데이터베이스로부터 한 품목에 대한 판매량 받아옴
#         data = database.select_sale(store_id, product)

#         # 한 품목에 대하여 학습
#         prophet.fit(data)

#         pred_df = prophet.make_future_dataframe(
#             periods=7, freq='D', include_history=True)

#         forecast = prophet.predict(pred_df)

#         # pred = forecast.loc[data.shape[0]:]
#         # next_week_sum = sum(pred['yhat'])

#         # past_future = forecast.loc[data.shape[0]-21:][['ds', 'yhat']]

#         all = forecast.loc[data.shape[0] - 21:][['ds', 'yhat']]
#         all_list.append(all)

#         past = forecast.loc[data.shape[0] -
#                             21: data.shape[0]][['ds', 'yhat']]
#         past_list.append(past)

#         future = forecast.loc[data.shape[0]:][['ds', 'yhat']]
#         future_list.append(future)

#     return {
#         "all_list": all_list,
#         "past_list": past_list,
#         "future_list": future_list
#     }


# ##########################################
# ## 예측된 모델을 pickle로 저장하는 함수 ##
# ##########################################
# def make_model():
#     store_list = database.select_all_store()
#     product_list = database.select_all_product()

#     for store in store_list:
#         print("store :", store[0])
#         for product in product_list:
#             prophet = Prophet()

#             # 데이터베이스로부터 한 품목에 대한 판매량 받아옴
#             data = database.select_sale(store[0], product[0])

#             # 한 품목에 대하여 학습
#             prophet.fit(data)

#             pkl_dir = "data/pickle/"
#             with open(pkl_dir + 'prophet_' + str(store[0]) + '-' + str(product[0]) + ".pkl", "wb") as f:
#                 pickle.dump(prophet, f)
#     return


# #######################################################
# ## 모델을 불러와 다음주까지의 판매량을 예측하는 함수 ##
# #######################################################
# def predict_next_week_from_pickle(store_id, product_list=[]):

#     all_list = []
#     past_list = []
#     future_list = []

#     for product in product_list:
#         prophet = 0

#         pkl_dir = "data/pickle/"
#         with open(pkl_dir + 'prophet_' + str(store_id) + '-' + str(product) + ".pkl", "rb") as f:
#             prophet = pickle.load(f)

#         pred_df = prophet.make_future_dataframe(
#             periods=7, freq='D', include_history=True)

#         print('fdtetst')
#         forecast = prophet.predict(pred_df)

#         print(forecast)

#         # pred = forecast.loc[data.shape[0]:]
#         # next_week_sum = sum(pred['yhat'])

#         # past_future = forecast.loc[data.shape[0]-21:][['ds', 'yhat']]

#         # all = forecast.loc[data.shape[0] - 21:][['ds', 'yhat']]
#         # all_list.append(all)

#         # past = forecast.loc[data.shape[0] -
#         #                     21: data.shape[0]][['ds', 'yhat']]
#         # past_list.append(past)

#         # future = forecast.loc[data.shape[0]:][['ds', 'yhat']]
#         # future_list.append(future)

#     return {
#         "all_list": all_list,
#         "past_list": past_list,
#         "future_list": future_list
#     }
