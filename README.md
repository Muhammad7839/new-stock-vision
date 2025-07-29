# StockVision: Forecasting Retail Stock Prices with Prophet and ARIMA

**StockVision** is a time series forecasting project that predicts future stock prices for two major retail companies: **Amazon (AMZN)** and **Costco (COST)**. We compare two forecasting models — **Facebook Prophet** and **ARIMA** — using visualizations, evaluation metrics, and real stock data from 2022 to 2025.

---

## 📊 Project Goal

Predict short-term stock price movements and compare the performance of two beginner-friendly models:
- **Facebook Prophet** – easy to use, captures trends and seasonality
- **ARIMA** – statistical model that handles patterns and noise in time series data

---

## 📁 Dataset

- **Source**: World-Stock-Prices-Dataset.csv
- **Tickers Used**: AMZN (Amazon), COST (Costco)
- **Date Range**: January 2022 to June 2025
- **Target**: Daily closing stock prices

---

## 🔧 Steps and Structure

### 1. Data Preprocessing
- Filtered for AMZN and COST
- Removed unnecessary columns
- Formatted for Prophet (`ds`, `y`)
- Checked missing values

### 2. Facebook Prophet Notebook
- Trained one Prophet model for each ticker
- Forecasted 365 days into the future
- Plotted:
  - Full forecast
  - Trend and seasonal components
  - Zoomed-in actual vs predicted
  - Moving averages (30-day, 90-day)
- Calculated MAE and RMSE for evaluation

### 3. ARIMA Notebook
- Checked stationarity using ADF test
- Differenced data where needed
- Used ACF and PACF plots to estimate (p, d, q)
- Trained separate ARIMA models for AMZN and COST
- Forecasted 30 future days
- Plotted:
  - Actual vs predicted
  - Residual diagnostics (histogram, Q-Q plot)
- Calculated MAE and RMSE

### 4. Model Comparison Notebook
- Pulled final predictions from Prophet and ARIMA
- Compared visual forecasts side-by-side
- Plotted bar charts for:
  - MAE (Mean Absolute Error)
  - RMSE (Root Mean Squared Error)
- Graphed daily forecast errors
- Wrote a summary of which model performed better

---

## 📈 Evaluation Metrics

| Ticker | Model   | MAE   | RMSE  |
|--------|---------|-------|--------|
| AMZN   | Prophet | 37.99 | 57.01 |
| AMZN   | ARIMA   | 3.26  | 4.06  |
| COST   | Prophet | 223.02| 236.57|
| COST   | ARIMA   | 5.34  | 7.16  |

---

## ✅ Conclusion

- **ARIMA outperformed Prophet** on both AMZN and COST in terms of error metrics.
- Prophet overpredicted in some periods due to long forecast range and no growth cap.
- ARIMA stayed closer to real values, making it more reliable for short-term retail stock forecasting.
- Both models were trained and evaluated separately to follow mentor guidelines.

---

## 🧠 Lessons Learned

- ARIMA is strong at short-term, trend-based forecasting.
- Prophet is easy to use and offers rich visual outputs but can overfit without constraints.
- Always visualize predictions and residuals to catch major issues.

---

## 🔍 Future Improvements

- Add external regressors (e.g., inflation, earnings) to Prophet
- Try hybrid models (ARIMA + XGBoost)
- Deploy the forecasts with Streamlit for interactive use

---

## 👨‍💻 Author

Muhammad A. , Dieunie G. , Pallavi V.  
AI4ALL Ignite Program, Summer 2025  