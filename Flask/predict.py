import pandas as pd
from prophet import Prophet


def predict_next_week(data):
    prophet = Prophet()
    prophet.fit(data)

    future = prophet.make_future_dataframe(
        periods=7, freq='D', include_history=True)

    forecast = prophet.predict(future)

    pred = forecast.loc[data.shape[0]:][['ds', 'yhat']]
    print(pred)

    next_week_sum = sum(pred['yhat'])

    return {
        'df': future,
        'sum': next_week_sum
    }
