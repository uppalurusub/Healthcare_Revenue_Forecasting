import streamlit as st

from api.api_client import APIClient
from components.response_view import render_bar_chart
from components.sidebar import render_sidebar

render_sidebar()
st.title("❌ Denials Analytics")

reasons = APIClient.get("/denials/reasons")
render_bar_chart(reasons, x="denial_reason", y="count", title="Denial Reasons")
