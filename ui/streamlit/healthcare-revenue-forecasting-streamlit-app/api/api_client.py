from typing import Any

import requests

BASE_URL = "http://localhost:8000/api"
DEFAULT_TIMEOUT = 30


class APIClient:
    """HTTP client for the Healthcare Revenue Forecasting API."""

    @staticmethod
    def get(endpoint: str, params: dict | None = None) -> Any:
        try:
            response = requests.get(
                f"{BASE_URL}{endpoint}",
                params=params,
                timeout=DEFAULT_TIMEOUT,
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as exc:
            return {"error": str(exc)}
