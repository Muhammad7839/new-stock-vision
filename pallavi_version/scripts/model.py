import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import os

df = pd.read_csv("../Data/Cleaned_Stock_Data.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Create output folders
os.makedirs("forecast_plots", exist_ok=True)
os.makedirs("forecast_csvs", exist_ok=True)

forecast_horizon = 30  # predict next 30 days
tickers = df['Ticker'].unique()
print(f"Total tickers found: {len(tickers)}")

# Loops through tickers
for ticker in tickers:
    print(f"\n🔄 Processing ticker: {ticker}")
    ticker_df = df[df['Ticker'] == ticker].copy()

    # Prepares Prophet dataframe
    prophet_df = ticker_df[['Date', 'Close']].rename(columns={'Date': 'ds', 'Close': 'y'})
    prophet_df['ds'] = pd.to_datetime(prophet_df['ds'], utc=True).dt.tz_localize(None)

    # Fits Prophet model
    model = Prophet()
    model.fit(prophet_df)

    # Creates future dataframe & forecast
    future = model.make_future_dataframe(periods=forecast_horizon)
    forecast = model.predict(future)

    # Saves forecast CSV
    csv_path = os.path.join("forecast_csvs", f"{ticker}_forecast.csv")
    forecast.to_csv(csv_path, index=False)
    print(f" Forecast CSV saved: {csv_path}")

    # Saves forecast plot
    fig1 = model.plot(forecast)
    plt.title(f'{ticker} Stock Price Forecast')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.grid(True)
    plt.tight_layout()
    fig_path = os.path.join("forecast_plots", f"{ticker}_forecast.png")
    plt.savefig(fig_path)
    plt.close(fig1)

    # Saves components plot
    fig2 = model.plot_components(forecast)
    plt.tight_layout()
    fig_path_comp = os.path.join("forecast_plots", f"{ticker}_components.png")
    plt.savefig(fig_path_comp)
    plt.close(fig2)

    print(f"Forecast plots saved for {ticker}")

