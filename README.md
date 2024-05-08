# MGT4250 Course Project
Author: Aidan Fulton (afulton7@elon.edu)

[Link to Streamlit Dashboard](https://mgt4250sping2024-msv4h2cqbdprhvbrweqbqv.streamlit.app)

## Project Description: 
### Questions of interest
- Q1
- Q2
- Q3
### Important Statement
These questions are *especially* **important** because
1. Reason 1
2. Reason 2
3. Reason 3

## Data Description
```python required packages
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
1. In your README file] Provide instructons about how to access and download
your data correctly.
2.  [In your README file] Explain the data types and descriptons of the columns
used in visualizatons.
```
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
