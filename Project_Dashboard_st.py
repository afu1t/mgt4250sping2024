import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title("Stock Performance Dashboard")  # Set the title of the dashboard

data = pd.read_excel("Updated SP500 & NVDA.xlsx")
data["Date"] = pd.to_datetime(data["Date"])
data["Month, Day, Year"] = data["Date"].dt.to_period("M")
data["Year"] = data['Month, Day, Year'].astype(str)  # Added for dropdown filter use

# Options with "All Dates" included for the percentage change dropdown
options = ["All Dates"] + sorted(data['Year'].unique().tolist())

# Dropdown for filtering by month for percentage change
selected_month_percent_change = st.sidebar.selectbox(
    'Select Month for % Change',
    options=options,
    index=0  # default to "All Dates"
)

# Dropdown for selecting S&P or NVDA for trading volume
selected_stock_volume = st.sidebar.selectbox(
    'Select Stock for Trading Volume',
    options=['S&P', 'NVDA']
)

# Dropdown for filtering by month for S&P 500 candlestick chart
selected_month_sp500 = st.sidebar.selectbox(
    'Select Month for S&P 500 Candlestick Chart',
    options=data['Year'].unique(),
    index=len(data['Year'].unique())-1  # default to the most recent month
)

# Dropdown for filtering by month for NVDA candlestick chart
selected_month_nvda = st.sidebar.selectbox(
    'Select Month for NVDA Candlestick Chart',
    options=data['Year'].unique(),
    index=len(data['Year'].unique())-1  # default to the most recent month
)

# Filter the data based on selected months
filtered_data_percent_change = data if selected_month_percent_change == "All Dates" else data[data['Year'] == selected_month_percent_change]
filtered_data_sp500 = data[data['Year'] == selected_month_sp500]
filtered_data_nvda = data[data['Year'] == selected_month_nvda]

col1, col2 = st.columns([7, 3])
with col1:
    monthly_changes = filtered_data_percent_change.groupby("Month, Day, Year").agg({
        "S&P % Change": "sum",
        "NVDA % Change": "sum"
    }).reset_index()
    monthly_changes["Month, Day, Year"] = monthly_changes["Month, Day, Year"].astype(str)
    fig_percent_change = px.bar(monthly_changes, x="Month, Day, Year", y=["S&P % Change", "NVDA % Change"],
                                barmode="group", title="Monthly % Change Comparison: S&P 500 vs. NVIDIA", 
                                color_discrete_sequence=['blue', 'red'])
    st.plotly_chart(fig_percent_change, use_container_width=True)

with col2:
    y_data = f"{selected_stock_volume} CVol"
    fig_trading_volume = px.bar(data, x="Year", y=y_data,
                                title=f"Monthly Trading Volume: {selected_stock_volume}",
                                color_discrete_sequence=['blue'])
    st.plotly_chart(fig_trading_volume, use_container_width=True)

col3, col4 = st.columns([5, 5])
with col3:
    fig_sp500 = go.Figure(data=[go.Candlestick(x=filtered_data_sp500["Date"],
                open=filtered_data_sp500["S&P Open"], high=filtered_data_sp500["S&P High"],
                low=filtered_data_sp500["S&P Low"], close=filtered_data_sp500["S&P Price"])])
    fig_sp500.update_layout(title="S&P 500 Stock Price Over Time",
                            xaxis_title="Date",
                            yaxis_title="Price",
                            xaxis_rangeslider_visible=False)
    st.plotly_chart(fig_sp500, use_container_width=True)

with col4:
    fig_nvda = go.Figure(data=[go.Candlestick(x=filtered_data_nvda["Date"],
                open=filtered_data_nvda["NVDA Open"], high=filtered_data_nvda["NVDA High"],
                low=filtered_data_nvda["NVDA Low"], close=filtered_data_nvda["NVDA Price"])])
    fig_nvda.update_layout(title="NVDA Stock Price Over Time",
                           xaxis_title="Date",
                           yaxis_title="Price",
                           xaxis_rangeslider_visible=False)
    st.plotly_chart(fig_nvda, use_container_width=True)
