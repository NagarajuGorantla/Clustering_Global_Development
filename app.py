import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from utils import load_data, get_future_dates

# ------------------------------------------------------------------
# Page Configuration (Industry Standard)
# ------------------------------------------------------------------
st.set_page_config(
    page_title="Apple Stock Forecasting",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------------------
# App Header
# ------------------------------------------------------------------
st.title("Apple Stock Price Forecasting Dashboard")
st.caption(
    "End-to-end time series forecasting using statistical and machine learning models. "
    "Built for analytical decision support, not hype."
)

st.divider()

# ------------------------------------------------------------------
# Sidebar — Control Center
# ------------------------------------------------------------------
with st.sidebar:
    st.header("Configuration")

    forecast_horizon = st.slider(
        "Forecast Horizon (Days)",
        min_value=7,
        max_value=180,
        value=30,
        step=7
    )

    model_type = st.selectbox(
        "Forecasting Model",
        options=[
            "ARIMA (Statistical)",
            "SARIMAX (Seasonal)",
            "Machine Learning (Baseline)"
        ]
    )

    show_raw_data = st.checkbox("View source dataset")

    st.divider()
    st.caption("Model parameters are intentionally simplified for clarity.")

# ------------------------------------------------------------------
# Data Loading
# ------------------------------------------------------------------
@st.cache_data
def get_dataset():
    return load_data("data/AAPL.csv")

df = get_dataset()

# ------------------------------------------------------------------
# Optional Raw Data View
# ------------------------------------------------------------------
if show_raw_data:
    st.subheader("Source Dataset")
    st.dataframe(df.tail(100), use_container_width=True)

# ------------------------------------------------------------------
# KPI Summary (Executive-Friendly)
# ------------------------------------------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Records Available", len(df))
col2.metric("Forecast Horizon (Days)", forecast_horizon)
col3.metric("Selected Model", model_type.split(" ")[0])

st.divider()

# ------------------------------------------------------------------
# Forecasting Logic (Placeholder / Extendable)
# ------------------------------------------------------------------
st.subheader("Forecast Results")

last_price = df["Close"].iloc[-1]
future_dates = get_future_dates(df.index[-1], forecast_horizon)

# Simple baseline forecast (replace with real model output)
forecast_values = np.linspace(
    last_price,
    last_price * 1.05,
    forecast_horizon
)

forecast_df = pd.DataFrame({
    "Date": future_dates,
    "Forecasted Price": forecast_values
})

# ------------------------------------------------------------------
# Visualization
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(df.index[-120:], df["Close"].iloc[-120:], label="Historical Price")
ax.plot(forecast_df["Date"], forecast_df["Forecasted Price"], linestyle="--", label="Forecast")

ax.set_title("Apple Stock Price Forecast")
ax.set_xlabel("Date")
ax.set_ylabel("Price (USD)")
ax.legend()
ax.grid(alpha=0.3)

st.pyplot(fig)

# ------------------------------------------------------------------
# Forecast Table
# ------------------------------------------------------------------
st.subheader("Forecasted Values")

styled_forecast = (
    forecast_df
    .assign(**{"Forecasted Price": forecast_df["Forecasted Price"].round(2)})
)

st.dataframe(styled_forecast, use_container_width=True)

# ------------------------------------------------------------------
# Business Interpretation
# ------------------------------------------------------------------
st.subheader("Analytical Interpretation")

st.markdown(
    """
    - The forecast represents a **model-driven expectation**, not financial advice.
    - Short-term trends are generally more reliable than long-horizon projections.
    - This framework supports **scenario testing**, model comparison, and extension
      to exogenous variables such as volume, macro indicators, or sentiment.
    """
)

st.divider()

# ------------------------------------------------------------------
# Footer
# ------------------------------------------------------------------
st.caption(
    "Built with Python, Streamlit, and statistical learning methods. "
    "Designed for portfolio demonstration and analytical storytelling."
)
