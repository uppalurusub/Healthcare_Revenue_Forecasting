import streamlit as st

from api.api_client import APIClient
from components.response_view import render_metrics, show_api_error
from components.sidebar import render_sidebar
from utils.formatters import currency_millions, integer, number, percentage

render_sidebar()
st.title("🏥 Executive Dashboard")

dashboard = APIClient.get("/dashboard")
if show_api_error(dashboard):
    st.stop()

revenue = dashboard.get("revenue", {})
claims = dashboard.get("claims", {})
payments = dashboard.get("payments", {})
denials = dashboard.get("denials", {})
ar = dashboard.get("ar_aging", {})
billing = dashboard.get("patient_billing", {})
forecast = dashboard.get("forecast", {})

tab1, tab2, tab3, tab4 = st.tabs(
    ["📊 Executive Summary", "💰 Revenue Cycle", "🏥 Operations", "📈 Forecasting"]
)

with tab1:
    st.subheader("Executive KPIs")
    render_metrics([
        ("Revenue", currency_millions(revenue.get("total_revenue"))),
        ("Claims", integer(claims.get("total_claims"))),
        ("Payments", currency_millions(payments.get("total_payments"))),
        ("AR Balance", currency_millions(ar.get("total_ar_balance"))),
    ])

with tab2:
    st.subheader("Revenue Analytics")
    render_metrics([
        ("Total Revenue", currency_millions(revenue.get("total_revenue"))),
        ("Collection Rate", percentage(revenue.get("collection_rate"))),
        ("Reimbursement Rate", percentage(revenue.get("reimbursement_rate"))),
        ("Revenue Leakage", currency_millions(revenue.get("revenue_leakage"))),
    ])
    st.divider()
    st.subheader("Claims")
    render_metrics([
        ("Total Claims", integer(claims.get("total_claims"))),
        ("Approved", integer(claims.get("approved_claims"))),
        ("Denied", integer(claims.get("denied_claims"))),
        ("Approval Rate", percentage(claims.get("approval_rate"))),
    ])
    st.divider()
    st.subheader("Payments")
    render_metrics([
        ("Total Payments", currency_millions(payments.get("total_payments"))),
        ("Insurance", currency_millions(payments.get("insurance_payments"))),
        ("Patient", currency_millions(payments.get("patient_payments"))),
        ("Success Rate", percentage(payments.get("payment_success_rate"))),
    ])

with tab3:
    st.subheader("AR Aging")
    render_metrics([
        ("AR Balance", currency_millions(ar.get("total_ar_balance"))),
        ("Expected Collection", currency_millions(ar.get("expected_collection"))),
        ("Days in AR", number(ar.get("average_days_in_ar"))),
        ("High Risk Accounts", integer(ar.get("high_risk_accounts"))),
    ])
    st.divider()
    st.subheader("Denials")
    render_metrics([
        ("Denials", integer(denials.get("total_denials"))),
        ("Denied Amount", currency_millions(denials.get("total_denied_amount"))),
        ("Recovered", currency_millions(denials.get("recovered_amount"))),
        ("Recovery Rate", percentage(denials.get("recovery_rate"))),
    ])
    st.divider()
    st.subheader("Patient Billing")
    render_metrics([
        ("Charges", currency_millions(billing.get("total_chargess"))),
        ("Patient Responsibility", currency_millions(billing.get("patient_responsibility"))),
        ("Patient Payments", currency_millions(billing.get("patient_payment"))),
        ("Collection Rate", percentage(billing.get("collection_rate"))),
    ])

with tab4:
    st.subheader("Forecast KPIs")
    render_metrics([
        ("Projected Revenue", currency_millions(forecast.get("projected_revenue"))),
        ("Projected Collections", currency_millions(forecast.get("projected_collections"))),
        ("Projected AR", currency_millions(forecast.get("projected_ar"))),
        ("Forecast Accuracy", percentage(forecast.get("forecast_accuracy"))),
    ])
    st.success(f"Best Forecast Model: {forecast.get('best_model', 'N/A')}")
