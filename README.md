# MGT4250 Course Project
Author: Aidan Fulton (afulton7@elon.edu)

This is my Senior course Project for MGT4250 at Elon University

[Streamlit Visualizations](https://mgt4250sping2024-yqhrxyeegsqphtr2ae38dp.streamlit.app/)

## Project Description: 
### Questions of interest
1. Is there a correlation between NVDA's price increase and overall market performance
2. What are the trends in trading volume for S&P 500 and NVIDIA, and how do they correlate with stock price movements?
3. How has the stock price of NVDA evolved over time, and are there specific months with notable price fluctuations?
### Importance Statement
These questions are relevant because:
1. Unicorn stocks are becoming more prevalent as tech start-ups are breaking the $1B dollar barrier. It is important to identify trends, and with the correct data predictive model, unicorn companies can be identified before their $1B dollar valuation.
2. Nvidia's breakout in 2023 quickly propelled them to a market leader in the tech industry, stock data should be studied to see if NVDA's earnings can be sustainable over the next few years
3. Visualizing long term stock data can reveal unseen trends and can provide insights if the stock is over or undervalued

[Investopedia Unicorn Stocks Article](https://www.investopedia.com/terms/u/unicorn.asp)

[Investor's Business Daily](https://www.investors.com/research/swing-trading/nvidia-stock-earnings-report-swing-trade-success/)

[Investopedia Stock Valuation](https://www.investopedia.com/articles/fundamental-analysis/09/five-must-have-metrics-value-investors.asp)
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
   - Numerical: Cvol, % Change, Open, Low, High, Price
   - Categorical: Date 
4.  Columns:

Many columns in the datasets overlap, so it is important to select the correct ones and get rid of duplicate columns. Once data is collected combine datasets in an excel file or merge columns in python on Date, remove all columns that are not listed below.

From Fatset:

 - Date: The date of the recorded stock market data.
 - Price: The closing price of NVDA/S&P 500 on that date.
 - CVol (Volume): The trading volume of the NVDA/S&P 500 on that date.
 - % Change: The percentage change in NVDA/S&P 500 closing price from the previous trading day.

From Yahoo Finance:
- Open: The opening price of NVDA/S&P 500 index on that date.
- Low: The lowest trading price of NVDA/S&P 500 during the day.
- High: The highest trading price NVDA/S&P 500 during the day.
## Interpreting  Visualizations


### Figure 1 NVDA & S&P % Change per Month
![Link to Figure 1 Image](https://github.com/afu1t/mgt4250sping2024/assets/168783406/688a1e7f-436a-4726-93f6-73f44ea56b07)

1. The Monthly % change bar chart shows the fluctuations  in both the S&P 500 and Nvidia per month. When analyzing the chart, the % change for NVDA is much more drastic than the S&P 500. This could be attributed to the S&P 500 being an index fund that includes a diversified portfolio of stocks versus NVDA being one company and more sensitive to change. Overall this model does a good job of visualizing NVDA's performance compared to the general stock market, and with datasets from YahooFinance and FactSet, any stock can be compared to the S&P 500.
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
![Link to Figure 2 NVDA Trading Volume](https://github.com/afu1t/mgt4250sping2024/assets/168783406/904b3c21-a3c6-49d5-a7f5-eebc68618775)![Link to Figure 2 S&P Trading Volume](https://github.com/afu1t/mgt4250sping2024/assets/168783406/b00a0eff-6f59-4049-9e1c-6768c99028ff)


1. The second figure shows trading volume per stock. Contrary to what I originally thought, trading volume does not have a major impact on stock performance. The S&P 500 had a much higher trading volume than NVDA but its overall percent change was lower than NVDA. In turn, trading volume can be ruled out as a major factor for identifying high-value stocks.
```
y_data = f"{selected_stock_volume} CVol"
fig_trading_volume = px.bar(data, x="Year", y=y_data,
                                title=f"Monthly Trading Volume: {selected_stock_volume}",
                                color_discrete_sequence=['blue'])
```
### Figure 3 S&P 500 Candlestick Chart
![Link to Figure S&P 500 Candlestick](https://github.com/afu1t/mgt4250sping2024/assets/168783406/47a04118-de5b-42e3-9edd-9e98ca1820b8)

1. Candlestick charts are often used by financial analysts and are a good tool for analyzing a stock's performance over time. The S&P 500 has had consistent growth aside from 2020 (Covid-19), and overall provides solid returns for investors. Candlestick charts do a good job of visualizing the peaks and troughs on a graph, highlighting good and bad time periods for the stock market.
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

![Figure 4 NVDA Candlestick](https://github.com/afu1t/mgt4250sping2024/assets/168783406/78150f99-fa39-460a-b74f-95072ff23e0b)

1. Similar to figure 3, a candlestick chart was deployed to analyze NVDA's stock performance over the past 5 years. From 2019-2022 NVDA's stock price grew slowly, but skyrocketed in 2023 and 2024. Comparing NVDA's candlestick graph to the S&P 500 candlestick graph, NVDA performed significantly better than the S&P 500 in 2023 and early 2024.
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
### Discussion Article: Nvidia briefly joins $1 trillion valuation club
[Reuters NVDA surpasses 1 Trillion article](https://www.reuters.com/technology/nvidia-sets-eye-1-trillion-market-value-2023-05-30/)
1. In May 2023, NVDA surpassed 1 trillion in market value. NVDA surged roughly 200% since October, outperforming countless companies in the S&P 500 due to rapid advancements in generative AI. Nvidia's chips are crucial for AI applications and dominate the market with the company controlling 80% of GPU production. Despite high valuations, analysts see further growth potential as AI technology continues to evolve. 

2. Asking ChatGTP 4 Questions of interest:
 - Typically, a positive correlation indicates that NVDA's stock price tends to move in the same direction as the market index. This requires statistical analysis of historical price data to compute the correlation coefficient. 
 - Trading volume trends can reveal how actively a stock is being traded and can sometimes predict future price movements. An increase in trading volume can indicate heightened interest in the stock, often preceding either a price increase if the volume is buying-heavy, or a decrease if the volume is selling-heavy.
 - NVIDIA's stock price history shows substantial fluctuations over time, which can be analyzed to identify specific patterns or trends. For instance, looking at monthly or yearly highs and lows, as well as any notable spikes or drops around specific events or during certain months, can provide insights into seasonal impacts or market reactions to company news and global events. According to historical data, NVIDIA has experienced significant price changes, often correlating with product launches, market trends, or financial reports.
3. Visualizations vs. Generative AI
 - Although generative AI is an extremely powerful tool, ChatGTP4 did not do a good job of interpreting the data and identifying trends. For example, trading volume can suggest a heightened interest in a stock, but in the case of NVDA it was not a major driver for the increase in price. More likely, the emergence of AI Nvidia's GPU and CPU's were the best available product. 
 - Similarly, the AI was not good at identifying trends in stock performance over time. NVDA's stock price did not seem to fluctuate down as much as the S&P 500, especially during Covid-19. Instead, NVDA had a dramatic price increase over a short period of time, while the S&P 500's price climbed at a slower rate.
