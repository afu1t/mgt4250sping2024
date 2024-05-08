# MGT4250 Course Project
Author: Aidan Fulton (afulton7@elon.edu)

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

*for tableau go to tableau public, sign up, click create, go to web offering, load data and create model, then click publish as and name workbook,
onece saved use share button to get link for github*

[Elon University](https://www.elon.edu)
![Untitled](https://github.com/afu1t/mgt4250sping2024/assets/168783406/116a8a0c-f796-43ee-8ced-96f2dad113fb)

## Data Description
```python required packages
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
```
## Interperting Visualizations
[Streamlit Dashboard](https://mgt4250sping2024-msv4h2cqbdprhvbrweqbqv.streamlit.app)
## Discussion & Summary
# Figure 1 NVDA & S&P % Change per Month
```
from datetime import datetime
data["Date"] = pd.to_datetime(data["Date"])
data["YearMonth"] = data["Date"].dt.to_period("M")
monthly_changes = data.groupby("YearMonth").agg({
    "S&P % Change": "sum",
    "NVDA % Change": "sum"
}).reset_index()
monthly_changes["YearMonth"] = monthly_changes["YearMonth"].astype(str)

fig_percent_change = px.bar(monthly_changes, x="YearMonth", y=["S&P % Change", "NVDA % Change"],
                            barmode="group", title="Monthly % Change Comparison: S&P 500 vs. NVIDIA")
```
# Figure 2 Monthly Trading Volume Per Stock
```
monthly_volumes = data.groupby("YearMonth").agg({
    "S&P CVol": "sum",
    "NVDA CVol": "sum"
}).reset_index()
monthly_volumes["YearMonth"] = monthly_volumes["YearMonth"].astype(str)

fig_trading_volume = px.bar(monthly_volumes, x="YearMonth", y=["S&P CVol", "NVDA CVol"],
                            barmode="group", title="Monthly Trading Volume: S&P 500 vs. NVIDIA")
```
# Figure 3 S&P 500 Candlestick Chart
```
fig_sp500 = go.Figure(data=[go.Candlestick(x=data["Date"],
                open=data["S&P Open"], high=data["S&P High"],
                low=data["S&P Low"], close=data["S&P Price"])])

fig_sp500.update_layout(title="S&P 500 Stock Price Over Time",
                        xaxis_title="Date",
                        yaxis_title="Price",
                        xaxis_rangeslider_visible=False)
```
# Figure 4 NVDA Candlestick Chart
```
fig_nvda = go.Figure(data=[go.Candlestick(x=data["Date"],
                open=data["NVDA Open"], high=data["NVDA High"],
                low=data["NVDA Low"], close=data["NVDA Price"])])

fig_nvda.update_layout(title="NVDA Stock Price Over Time",
                        xaxis_title="Date",
                        yaxis_title="Price",
                        xaxis_rangeslider_visible=False)
```
