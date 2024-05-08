# MGT4250 Course Project
Author: Aidan Fulton (afulton7@elon.edu)

This is my Senior course Project for MGT4250 at Elon Univeristy

[Link to Visualization Dashboard](https://mgt4250sping2024-msv4h2cqbdprhvbrweqbqv.streamlit.app)

## Project Description: 
### Questions of interest
1. Is there a correlation between NVDA's price increase and overall market performance
2. What are the trends in trading volume for S&P 500 and NVIDIA, and how do they correlate with stock price movements?
3. How has the stock price of NVDA evolved over time, and are there specific months with notable price fluctuations?
### Importance Statement
These questions are relevant because:
1. Unicorn stocks are becoming more prevelent as tech start-ups are breaking the $1B dollar barrier. It is important to identify trends, and with the correct data predictive model, unicorn ups can be identified before there $1B dollar valuation.
2. Nvidia has become a market leader in the tech industry
3. Reason 3

[Investopedia Unicorn Stocks Article](https://www.investopedia.com/terms/u/unicorn.asp)
[Investor's Business Daily](https://www.investors.com/research/swing-trading/nvidia-stock-earnings-report-swing-trade-success/)
## Data Description

1. Yahoo Finance
   - Open Link to YahooFinance
   - Apply 5 year under time period with daily trading frequency
   - Select Download button located above Volume
   

[Link to NVDA YahooFinance Historical Data](https://finance.yahoo.com/quote/NVDA/history)

[Link to S&P 500 YahooFinance Historical Data](https://finance.yahoo.com/quote/%5EGSPC?.tsrc=fin-srch)

2. FactSet:
   - Open FactSet Link
   - Select Index Base as 5 years ago and daily trading frequency
   - Select Download in top right corner

[Link to NVDA FactSet Price History](https://my.apps.factset.com/workstation/navigator/company-security/price-history/NVDA-US)

[Link to S&P 500 FactSet Price History](https://my.apps.factset.com/workstation/navigator/company-security/price-history/SP50)

3.  Data Types:
       - Numerical: Cvol, % Change, Open, Close, Price
       - Catagorical: Date 
4.  Columns

Many columns in the datasets overlap, so it is important to select the correct ones and get rid of duplicate columns. Once data is collected combine datasets in an excel file or merge columns in python on Date  
From Fatset:
    - Date: The date of the recorded stock market data.
    - Price: The closing price of NVDA/S&P 500 on that date.
    - CVol (Volume): The trading volume of the NVDA/S&P 500 on that date.
    - % Change: The percentage change in NVDA/S&P 500 closing price from the previous trading day.
From Yahoo Finance
    - Open: The opening price of NVDA/S&P 500 index on that date.
    - High: The highest trading price NVDA/S&P 500 during the day.
    - Low: The lowest trading price of NVDA/S&P 500 during the day.

## Interperting Visualizations


### Figure 1 NVDA & S&P % Change per Month
[Link to Figure 1]()
1. 
```
monthly_changes = filtered_data_percent_change.groupby("Month, Day, Year").agg({
        "S&P % Change": "sum",
        "NVDA % Change": "sum"
    }).reset_index()
    monthly_changes["Month, Day, Year"] = monthly_changes["Month, Day, Year"].astype(str)

fig_percent_change = px.bar(monthly_changes, x="Month, Day, Year", y=["S&P % Change", "NVDA % Change"],
                                barmode="group", title="Monthly % Change Comparison: S&P 500 vs. NVIDIA", 
                                color_discrete_sequence=['blue', 'red'])
```
### Figure 2 Monthly Trading Volume Per Stock
[Link to Figure 2]()
1. 
```
y_data = f"{selected_stock_volume} CVol"
fig_trading_volume = px.bar(data, x="Year", y=y_data,
                                title=f"Monthly Trading Volume: {selected_stock_volume}",
                                color_discrete_sequence=['blue'])
```
### Figure 3 S&P 500 Candlestick Chart
[Link to Figure 3]()
1.
```
fig_sp500 = go.Figure(data=[go.Candlestick(x=filtered_data_sp500["Date"],
                open=filtered_data_sp500["S&P Open"], high=filtered_data_sp500["S&P High"],
                low=filtered_data_sp500["S&P Low"], close=filtered_data_sp500["S&P Price"])])

fig_sp500.update_layout(title="S&P 500 Stock Price Over Time",
                            xaxis_title="Date",
                            yaxis_title="Price",
                            xaxis_rangeslider_visible=False)
```
### Figure 4 NVDA Candlestick Chart
[Link to Figure 4]()
1.
```
fig_nvda = go.Figure(data=[go.Candlestick(x=filtered_data_nvda["Date"],
                open=filtered_data_nvda["NVDA Open"], high=filtered_data_nvda["NVDA High"],
                low=filtered_data_nvda["NVDA Low"], close=filtered_data_nvda["NVDA Price"])])
fig_nvda.update_layout(title="NVDA Stock Price Over Time",
                           xaxis_title="Date",
                           yaxis_title="Price",
                           xaxis_rangeslider_visible=False)
```

## Discussion & Summary
Find an artcle related to your questons and summarize the artcle.
1. Ask your questons to generatve AI. Include generatve AI’s response with your
query (Ask as many as possible for proper responses; Menton that the response
is generated from which generatve AI. For example, ChatGPT)
2. Discuss whether your visualizatons align well with the artcle and generatve AI’s
response
