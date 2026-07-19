from typing import Any


def currency_millions(value: Any, decimals: int = 2) -> str:
    return f"${float(value or 0) / 1_000_000:,.{decimals}f}M"


def currency(value: Any, decimals: int = 0) -> str:
    return f"${float(value or 0):,.{decimals}f}"


def percentage(value: Any, decimals: int = 2) -> str:
    return f"{float(value or 0):,.{decimals}f}%"


def integer(value: Any) -> str:
    return f"{int(value or 0):,}"


def number(value: Any, decimals: int = 0) -> str:
    return f"{float(value or 0):,.{decimals}f}"
