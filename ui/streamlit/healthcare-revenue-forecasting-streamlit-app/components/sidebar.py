import streamlit as st


def render_sidebar() -> None:
    """Render common application information in the sidebar."""
    with st.sidebar:
        st.title("🏥 Revenue Forecasting")
        st.caption("Healthcare Revenue Cycle Analytics")
        st.divider()
        st.markdown(
            """
            **Analytics Modules**
            - Executive Dashboard
            - Revenue
            - Claims
            - Payments
            - Denials
            - AR Aging
            - Patient Billing
            - Forecasting
            """
        )
        st.divider()
        st.caption("API: http://localhost:8000/api")
