import pandas as pd
import database


def auto_order_list(store_id):
    db_result = database.select_product_stock(store_id=store_id)
    db_result_df = pd.DataFrame(
        db_result, columns=['product_id', 'product_name', 'stock'])

    print(db_result_df)

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
    db_result_df['pred_sum'] = db_result_df['pred_sum'].round()

    pred_top5_list = []
    for i in db_result_df['product_id']:
        pred_top5_list.append(pred_list[i])

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
    order = db_result_df['pred_sum'] - db_result_df['stock']
    order[order < 0] = 0
    db_result_df['order'] = order

    db_result_df_tolist = db_result_df.values.tolist()

    return {
        "chart_data": chart_data,
        "table_data": db_result_df_tolist
    }
