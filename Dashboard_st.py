import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
st.set_page_config(layout="wide")
data = pd.read_excel("Updated SP500 & NVDA.xlsx")
data["Date"] = pd.to_datetime(data["Date"])
data["YearMonth"] = data["Date"].dt.to_period("M")

col1,col2 = st.columns([7,3])
with col1:
    monthly_changes = data.groupby("YearMonth").agg({
    "S&P % Change": "sum",
    "NVDA % Change": "sum"
    }).reset_index()
    monthly_changes["YearMonth"] = monthly_changes["YearMonth"].astype(str)
    fig_percent_change = px.bar(monthly_changes, x="YearMonth", y=["S&P % Change", "NVDA % Change"],
                            barmode="group", title="Monthly % Change Comparison: S&P 500 vs. NVIDIA")
    st.plotly_chart(fig_percent_change,use_container_width=True)
with col2:
    monthly_volumes = data.groupby("YearMonth").agg({
    "S&P CVol": "sum",
    "NVDA CVol": "sum"
    }).reset_index()
    monthly_volumes["YearMonth"] = monthly_volumes["YearMonth"].astype(str)
    fig_trading_volume = px.bar(monthly_volumes, x="YearMonth", y=["S&P CVol", "NVDA CVol"],
                            barmode="group", title="Monthly Trading Volume: S&P 500 vs. NVIDIA")
    st.plotly_chart(fig_trading_volume,use_container_width=True)

col3,col4 = st.columns([5,5])
with col3:
    fig_sp500 = go.Figure(data=[go.Candlestick(x=data["Date"],
                open=data["S&P Open"], high=data["S&P High"],
                low=data["S&P Low"], close=data["S&P Price"])])
    fig_sp500.update_layout(title="S&P 500 Stock Price Over Time",
                        xaxis_title="Date",
                        yaxis_title="Price",
                        xaxis_rangeslider_visible=False)
    st.plotly_chart(fig_sp500,use_container_width=True)
with col4:
    fig_nvda = go.Figure(data=[go.Candlestick(x=data["Date"],
                open=data["NVDA Open"], high=data["NVDA High"],
                low=data["NVDA Low"], close=data["NVDA Price"])])
    fig_nvda.update_layout(title="NVDA Stock Price Over Time",
                        xaxis_title="Date",
                        yaxis_title="Price",
                        xaxis_rangeslider_visible=False)
    st.plotly_chart(fig_nvda,use_container_width=True)
