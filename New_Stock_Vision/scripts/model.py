# New_Stock_Vision/scripts/model.py

import pandas as pd
from prophet import Prophet

def forecast_stock(df, periods=7):
    # Rename columns for Prophet
    df = df[['Date', 'Close']].rename(columns={'Date': 'ds', 'Close': 'y'})
    
    # Convert 'ds' to datetime and remove timezone
    df['ds'] = pd.to_datetime(df['ds'], utc=True).dt.tz_localize(None)
    
    # Initialize and fit Prophet model
    model = Prophet()
    model.fit(df)

    # Create future dataframe for forecasting
    future = model.make_future_dataframe(periods=periods)
    # Ensure future dates are also timezone-naive
    future['ds'] = future['ds'].dt.tz_localize(None)
    
    forecast = model.predict(future)

    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]