# ![StockVision Logo](New_Stock_Vision/notebooks/images/logo.png)

# StockVision: Forecasting Retail Stock Prices with Prophet and ARIMA

**StockVision** is a time series forecasting project that predicts future stock prices for two major retail companies: **Amazon (AMZN)** and **Costco (COST)**. We compare two forecasting models — **Facebook Prophet** and **ARIMA** — using visualizations, evaluation metrics, and real stock data from 2022 to 2025.

---

## Project Goal

Predict short-term stock price movements and compare the performance of two beginner-friendly models:
- **Facebook Prophet** – captures trends and seasonality automatically
- **ARIMA** – a statistical model good at handling patterns in historical data

---

## Dataset

- **Source**: World-Stock-Prices-Dataset.csv
- **Tickers Used**: AMZN (Amazon), COST (Costco)
- **Date Range**: January 2022 to June 2025
- **Target**: Daily closing stock prices

---

## Steps and Structure

### 1. Data Preprocessing
- Selected AMZN and COST data
- Cleaned and formatted datasets for both models
- Renamed columns to fit Prophet’s format (`ds`, `y`)

### 2. Facebook Prophet Modeling
- Trained separate Prophet models for AMZN and COST
- Forecasted 365 days into the future
- Plotted:
  - Full forecast
  - Trend and seasonal components
  - Zoomed actual vs predicted
  - Moving averages (30-day, 90-day)

![AMZN Prophet Forecast](New_Stock_Vision/notebooks/images/prophet_amzn_forecast.png)

![COST Prophet Forecast](New_Stock_Vision/notebooks/images/prophet_cost_forecast.png)

### 3. ARIMA Modeling
- Ran Augmented Dickey-Fuller (ADF) tests for stationarity
- Differenced data as needed
- Used ACF/PACF plots to estimate ARIMA parameters
- Trained ARIMA models separately for each ticker
- Forecasted 30 days
- Checked residuals with histogram and QQ plots

### 4. Model Comparison
- Pulled latest forecast arrays from both models
- Plotted actual vs forecast for last 5 days

![ARIMA vs Prophet Comparison](New_Stock_Vision/notebooks/images/comparison_arima_vs_prophet.png)

- Plotted MAE and RMSE comparison bar charts

![MAE RMSE Comparison](New_Stock_Vision/notebooks/images/mae_rmse_barplot.png)

---

## Evaluation Metrics

| Ticker | Model   | MAE   | RMSE  |
|--------|---------|-------|--------|
| AMZN   | Prophet | 37.99 | 57.01 |
| AMZN   | ARIMA   | 3.26  | 4.06  |
| COST   | Prophet | 223.02| 236.57|
| COST   | ARIMA   | 5.34  | 7.16  |

---

## Conclusion

- **ARIMA performed better than Prophet** in short-term forecasting for both tickers.
- Prophet overshot future prices, especially on longer horizons.
- ARIMA was more stable and followed real stock movements more closely.
- Model separation, visualizations, and metrics followed mentor guidelines.

---

## Lessons Learned

- Visualizing forecasts helps catch large errors quickly
- ARIMA requires more setup but gives better short-range performance
- Prophet is user-friendly but needs tuning for real-world accuracy

---

## Future Work

- Add features like market news, earnings reports, and inflation
- Explore hybrid models combining ARIMA + ML models (e.g., XGBoost)
- Deploy with Streamlit for interactive exploration

---

## Team

Muhammad A. , Dieunie G. , Pallavi V.  
AI4ALL Ignite Program – Summer 2025