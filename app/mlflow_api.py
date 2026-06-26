"""Thin HTTP client for the MLflow /invocations endpoint."""

import json
import os

import requests

MLFLOW_SERVE_URL = os.getenv("MLFLOW_SERVE_URL", "http://127.0.0.1:5001/invocations")

FEATURE_COLUMNS = [
    "credit_score",
    "country",
    "gender",
    "age",
    "tenure",
    "balance",
    "products_number",
    "credit_card",
    "active_member",
    "estimated_salary",
]


def predict_churn_via_api(**fields) -> int:
    """POST one row to the model server, return 0 or 1."""
    row = [fields[col] for col in FEATURE_COLUMNS]
    payload = {
        "dataframe_split": {
            "columns": FEATURE_COLUMNS,
            "data": [row],
        }
    }

    response = requests.post(
        MLFLOW_SERVE_URL,
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload),
        timeout=30,
    )

    response.raise_for_status()
    result = response.json()

    # Response shape varies a bit by MLflow version.
    if isinstance(result, dict) and "predictions" in result:
        return int(result["predictions"][0])
    return int(result[0] if isinstance(result, list) else result)
