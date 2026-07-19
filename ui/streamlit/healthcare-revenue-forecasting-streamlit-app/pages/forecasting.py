import pandas as pd
import plotly.express as px
import streamlit as st

from api.api_client import APIClient
from components.request_form import render_forecasting_form
from components.response_view import show_api_error
from components.sidebar import render_sidebar

render_sidebar()
st.title("📈 Revenue Forecasting")

months = render_forecasting_form()
forecast = APIClient.get("/forecasting/revenue", params={"periods": months})

if not show_api_error(forecast):
    df = pd.DataFrame(forecast)
    if df.empty:
        st.info("No forecast data available.")
    else:
        df["forecast_month"] = pd.to_datetime(df["forecast_month"])
        fig = px.line(
            df,
            x="forecast_month",
            y="forecast_revenue",
            markers=True,
            title=f"{months}-Month Revenue Forecast",
        )
        st.plotly_chart(fig, width="stretch")
