import streamlit as st

from api.api_client import APIClient
from components.response_view import render_dataframe, render_metrics, show_api_error
from components.sidebar import render_sidebar
from utils.formatters import currency_millions, percentage

render_sidebar()
st.title("👨‍⚕️ Patient Billing")

summary = APIClient.get("/patient-billing/summary")
if not show_api_error(summary):
    render_metrics([
        ("Total Charges", currency_millions(summary.get("total_chargess"))),
        ("Insurance Responsibility", currency_millions(summary.get("insurance_responsibility"))),
        ("Patient Responsibility", currency_millions(summary.get("patient_responsibility"))),
        ("Patient Payment", currency_millions(summary.get("patient_payment"))),
        ("Remaining Balance", currency_millions(summary.get("remaining_balance"))),
    ])

balances = APIClient.get("/patient-billing/outstanding-balances")
render_dataframe(balances)
