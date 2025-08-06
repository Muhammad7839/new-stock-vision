<img src="New_Stock_Vision/notebooks/images/logo.png" alt="logo" width="360"/>

# StockVision: Forecasting Retail Stock Prices with Prophet and ARIMA

StockVision is a time series forecasting project that predicts future stock prices for two major retail companies, Amazon (AMZN) and Costco (COST). We compare two forecasting models, Facebook Prophet and ARIMA, using real stock data from 2022 to 2025.

## Project Goal

Our goal is to predict short-term stock price movements and compare how two different forecasting models perform,  
Facebook Prophet, which captures trends and seasonality,  
ARIMA, which is better for short-term patterns and noise.

## Dataset

Source: World-Stock-Prices-Dataset.csv  
Tickers used: AMZN and COST  
Date range: January 2022 to June 2025  
Target: Daily closing stock prices

## Project Steps

### 1. Data Preprocessing

We filtered for AMZN and COST, removed unrelated columns, reformatted for Prophet using `ds` and `y`, and handled missing values.

### 2. Prophet Forecasting

We trained Prophet separately on AMZN and COST, made 365-day forecasts, visualized trends and patterns, and calculated error metrics like MAE and RMSE.

Here is a Prophet forecast screenshot:

![Prophet Forecast](New_Stock_Vision/notebooks/images/prophet_cost_forecast.png)

### 3. ARIMA Forecasting

We used ADF tests to check stationarity, differenced the data, and estimated parameters using ACF and PACF plots. Then we trained ARIMA for both tickers, forecasted the next 30 days, visualized predictions, and evaluated errors.

Here is an ARIMA forecast screenshot:

![ARIMA Forecast](New_Stock_Vision/notebooks/images/arima_amzn_forecast.png)

### 4. Model Comparison

We compared both models using visual graphs and simple error metrics. Prophet tends to overpredict long-term, ARIMA is better for short-term forecasts.

Here are the model comparison screenshots:

![Error Bar Chart](New_Stock_Vision/notebooks/images/mae_rmse_barplot.png)

![Forecast Comparison](New_Stock_Vision/notebooks/images/comparison_arima_vs_prophet.png)

## Evaluation

| Ticker | Model   | MAE   | RMSE  |
|--------|---------|-------|--------|
| AMZN   | Prophet | 37.99 | 57.01 |
| AMZN   | ARIMA   | 3.26  | 4.06  |
| COST   | Prophet | 223.02| 236.57|
| COST   | ARIMA   | 5.34  | 7.16  |

## Conclusion

ARIMA performed better than Prophet for both tickers based on error values. Prophet captured patterns but often overpredicted when no growth cap was set. ARIMA stayed close to actual values and is better for short-term forecasts in this project.

## Lessons Learned

ARIMA is best for short-term retail stock prediction,  
Prophet gives great visuals and trend analysis but needs constraints for longer forecasts,  
Visualizing everything helped catch overfitting and patterns.

## Future Work

Add extra features like inflation or earnings,  
Try hybrid models using ARIMA and machine learning,  
Deploy the model on Streamlit for public use.

## Authors

Muhammad A, Dieunie G, Pallavi V  
AI4ALL Ignite Program, Summer 2025