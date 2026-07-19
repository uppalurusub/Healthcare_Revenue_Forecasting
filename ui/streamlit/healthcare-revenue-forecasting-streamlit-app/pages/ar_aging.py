import streamlit as st

from api.api_client import APIClient
from components.response_view import render_pie_chart
from components.sidebar import render_sidebar

render_sidebar()
st.title("📅 AR Aging Analytics")

aging = APIClient.get("/ar-aging/aging-buckets")
render_pie_chart(aging, names="aging_bucket", values="outstanding_balance", title="AR Aging Buckets")
