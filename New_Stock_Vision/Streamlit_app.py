# Streamlit_app.py

import streamlit as st
import pandas as pd
from scripts.model import forecast_stock

st.set_page_config(page_title="StockVision", layout="centered")
st.title("📈 StockVision: Costco & Amazon Forecast")

# --- Stock selector ---
ticker = st.selectbox("Choose a stock", ["COST", "AMZN"])
data_path = f"New_Stock_Vision/Data/{ticker}.csv"

# --- Load and forecast ---
try:
    df = pd.read_csv(data_path)
    st.success(f"Loaded {ticker} data")

    forecast = forecast_stock(df)

    # Display chart
    st.subheader("📊 Forecasted Prices")
    st.line_chart(forecast.set_index("ds")[["yhat"]])

    # Show table
    st.subheader("📄 Forecast Table")
    st.dataframe(forecast.tail(7).set_index("ds").style.format("{:.2f}"))

except Exception as e:
    st.error(f"Error: {e}")
