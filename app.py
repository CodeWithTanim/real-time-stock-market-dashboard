import streamlit as st
import plotly.graph_objs as go
import pandas as pd

from utils.stock_api import get_stock_data
from utils.indicators import calculate_moving_average, calculate_rsi
import config

st.set_page_config(page_title="📈 Stock Dashboard", layout="wide")

st.title("📈 Real-Time Stock Market Dashboard")

symbol = st.text_input("Enter Stock Symbol (e.g. AAPL, MSFT, TSLA):", "AAPL")

if symbol:
    df = get_stock_data(symbol, config.API_KEY)

    if df is not None:
        ma = calculate_moving_average(df)
        rsi = calculate_rsi(df)

        st.subheader(f"Stock Price Chart for {symbol.upper()}")

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df.index, y=df["Close"], name='Close Price'))
        fig.add_trace(go.Scatter(x=ma.index, y=ma, name='Moving Average (10)'))
        fig.update_layout(title=f"{symbol.upper()} Stock Price", xaxis_title="Time", yaxis_title="Price")

        st.plotly_chart(fig, use_container_width=True)

        st.subheader("📊 RSI Indicator")
        st.line_chart(rsi)

        st.success("✅ Data loaded successfully.")
    else:
        st.error("❌ Failed to fetch data. Check symbol or API usage limit.")
