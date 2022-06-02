import pandas as pd
from prophet import Prophet


def predict_next_week(storeId, productId):
    data = pd.read_csv('./sales_modified.csv', index_col=0)
    data = data[(data['store_id'] == storeId) &
                (data['product_id'] == productId)]

    prophet = Prophet()
    prophet.fit(data)

    future = prophet.make_future_dataframe(periods=7, freq='D')

    forecast = prophet.predict(future)

    prophet.plot(forecast)
    print(data)
    return data
