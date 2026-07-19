import streamlit as st

from api.api_client import APIClient
from components.response_view import render_line_chart, render_metrics, show_api_error
from components.sidebar import render_sidebar
from utils.formatters import integer, percentage

render_sidebar()
st.title("📋 Claims Analytics")

summary = APIClient.get("/claims/summary")
if not show_api_error(summary):
    st.subheader("Claim Summary")
    render_metrics([
        ("Total Claims", integer(summary.get("total_claims"))),
        ("Approved", integer(summary.get("approved_claims"))),
        ("Denied", integer(summary.get("denied_claims"))),
        ("Pending", integer(summary.get("pending_claims"))),
        ("Paid", integer(summary.get("paid_claims"))),
    ])
    st.divider()
    st.subheader("Claim Approval & Denial Rates")
    render_metrics([
        ("Approval Rate", percentage(summary.get("approval_rate"))),
        ("Denial Rate", percentage(summary.get("denial_rate"))),
    ])

trend = APIClient.get("/claims/monthly")
render_line_chart(trend, x="service_date", y="claim_count", title="Monthly Claims")
