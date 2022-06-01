import pandas as pd


def predict_next_week(storeId, productId):
    data = pd.read_csv('./sales_modified.csv', index_col=0)
    data = data[(data['store_id'] == storeId) &
                (data['product_id'] == productId)]
    print(data)
    return data
