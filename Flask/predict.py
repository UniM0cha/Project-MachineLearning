import pandas as pd
from prophet import Prophet


def predict_next_week(data):
    prophet = Prophet()
    prophet.fit(data)

    future = prophet.make_future_dataframe(
        periods=7, freq='D', include_history=False)

    forecast = prophet.predict(future)

    next_week_sum = sum(forecast['yhat'])

    return next_week_sum