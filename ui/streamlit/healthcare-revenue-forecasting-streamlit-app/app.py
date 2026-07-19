import streamlit as st

from components.sidebar import render_sidebar

st.set_page_config(
    page_title="Healthcare Revenue Forecasting",
    page_icon="🏥",
    layout="wide",
)

render_sidebar()

st.title("🏥 Healthcare Revenue Forecasting")
st.markdown(
    """
    ### Executive Healthcare Forecasting Platform

    Use the application pages to explore:

    - Revenue Analytics
    - Claims Analytics
    - Payments Analytics
    - Denials Analytics
    - AR Aging Analytics
    - Patient Billing Analytics
    - Forecasting Analytics
    """
)
