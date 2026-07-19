import streamlit as st

from api.api_client import APIClient
from components.response_view import render_bar_chart, render_metrics, show_api_error
from components.sidebar import render_sidebar
from utils.formatters import currency, currency_millions, number, percentage

render_sidebar()
st.title("💳 Payments Analytics")

summary = APIClient.get("/payments/summary")
if not show_api_error(summary):
    render_metrics([
        ("Total Payments", currency_millions(summary.get("total_payments"))),
        ("Insurance Payments", currency_millions(summary.get("insurance_payments"))),
        ("Patient Payments", currency_millions(summary.get("patient_payments"))),
        ("Average Payment", currency(summary.get("average_payment"))),
        ("Average Days To Payment", number(summary.get("average_days_to_payment"))),
    ])

monthly = APIClient.get("/payments/monthly")
render_bar_chart(monthly, x="payment_date", y="total_payment", title="Monthly Payments")
