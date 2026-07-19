import streamlit as st

from api.api_client import APIClient
from components.response_view import render_line_chart, render_metrics, show_api_error
from components.sidebar import render_sidebar
from utils.formatters import currency_millions, percentage

render_sidebar()
st.title("💰 Revenue Analytics")

kpis = APIClient.get("/revenue/kpis")
if not show_api_error(kpis):
    render_metrics([
        ("Total Revenue", currency_millions(kpis.get("total_revenue"))),
        ("Collection Rate", percentage(kpis.get("collection_rate"))),
        ("Reimbursement Rate", percentage(kpis.get("reimbursement_rate"))),
    ])

monthly = APIClient.get("/revenue/monthly")
render_line_chart(
    monthly,
    x="service_date",
    y="gross_revenue",
    title="Monthly Revenue Trend",
    markers=True,
)
