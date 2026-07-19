import streamlit as st


def render_forecasting_form() -> int:
    """Collect revenue forecasting request parameters."""
    with st.form("forecasting_request_form"):
        periods = st.slider("Forecast Period (Months)", 3, 36, 12)
        submitted = st.form_submit_button("Generate Forecast", type="primary")

    if submitted:
        st.session_state["forecast_periods"] = periods

    return st.session_state.get("forecast_periods", periods)
