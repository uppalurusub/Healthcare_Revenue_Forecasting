from typing import Any, Iterable

import pandas as pd
import plotly.express as px
import streamlit as st


def show_api_error(data: Any) -> bool:
    """Display an API error and return True when the payload contains one."""
    if isinstance(data, dict) and data.get("error"):
        st.error(f"API request failed: {data['error']}")
        return True
    return False


def render_metrics(metrics: Iterable[tuple[str, str]], columns: int | None = None) -> None:
    items = list(metrics)
    if not items:
        return
    cols = st.columns(columns or len(items))
    for index, (label, value) in enumerate(items):
        cols[index % len(cols)].metric(label, value)


def render_line_chart(
    data: Any,
    x: str,
    y: str,
    title: str,
    *,
    markers: bool = False,
) -> None:
    if show_api_error(data):
        return
    df = pd.DataFrame(data)
    if df.empty:
        st.info("No data available.")
        return
    fig = px.line(df, x=x, y=y, markers=markers, title=title)
    st.plotly_chart(fig, width="stretch")


def render_bar_chart(data: Any, x: str, y: str, title: str | None = None) -> None:
    if show_api_error(data):
        return
    df = pd.DataFrame(data)
    if df.empty:
        st.info("No data available.")
        return
    fig = px.bar(df, x=x, y=y, title=title)
    st.plotly_chart(fig, width="stretch")


def render_pie_chart(data: Any, names: str, values: str, title: str | None = None) -> None:
    if show_api_error(data):
        return
    df = pd.DataFrame(data)
    if df.empty:
        st.info("No data available.")
        return
    fig = px.pie(df, names=names, values=values, title=title)
    st.plotly_chart(fig, width="stretch")


def render_dataframe(data: Any) -> None:
    if show_api_error(data):
        return
    df = pd.DataFrame(data)
    if df.empty:
        st.info("No data available.")
        return
    st.dataframe(df, width="stretch")
