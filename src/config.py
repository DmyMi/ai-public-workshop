"""Paths and names shared across notebooks, the serve entry point, and the Gradio client."""

from pathlib import Path

DEMO_ROOT = Path(__file__).resolve().parent.parent
MLFLOW_DB = DEMO_ROOT / "mlflow.db"
DATA_PATH = DEMO_ROOT / "data" / "bank_customers.csv"

MODEL_NAME = "BankChurnModel"
CHAMPION_ALIAS = "champion"
TARGET = "churn"

# Same column order as training and the /invocations payload.
FEATURE_COLS = [
    "country",
    "gender",
    "credit_score",
    "age",
    "tenure",
    "balance",
    "products_number",
    "credit_card",
    "active_member",
    "estimated_salary",
]


def build_model_uri(model_name: str, alias: str | None, version: int | None) -> str:
    """Return an MLflow model URI. Version wins over alias if both are set."""
    if version is not None:
        return f"models:/{model_name}/{version}"
    return f"models:/{model_name}@{alias or CHAMPION_ALIAS}"
