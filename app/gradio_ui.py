"""Gradio form for the churn demo. Run in a second terminal while `mlflow run . -e serve` is up.

    python app/gradio_ui.py

http://localhost:7861
"""

import sys
from pathlib import Path

DEMO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(DEMO_ROOT))

import gradio as gr

from app.mlflow_api import MLFLOW_SERVE_URL, predict_churn_via_api


def predict_via_api(
    credit_score: int,
    country: str,
    gender: str,
    age: int,
    tenure: int,
    balance: float,
    products_number: int,
    credit_card: int,
    active_member: int,
    estimated_salary: float,
) -> str:
    pred = predict_churn_via_api(
        credit_score=credit_score,
        country=country,
        gender=gender,
        age=age,
        tenure=tenure,
        balance=balance,
        products_number=products_number,
        credit_card=credit_card,
        active_member=active_member,
        estimated_salary=estimated_salary,
    )

    churn_label = "Churn" if pred == 1 else "No churn"
    return (
        f"Prediction: **{churn_label}** (class={pred})\n\n"
        f"Served from `{MLFLOW_SERVE_URL}`"
    )


def main():
    with gr.Blocks(title="Bank Churn API Demo") as demo:
        gr.Markdown(
            "# Bank Churn: MLflow Serve Demo\n"
            "Fill in customer details. Predictions come from `mlflow models serve`."
        )
        with gr.Row():
            credit_score = gr.Number(label="Credit score", value=650)
            country = gr.Dropdown(["France", "Spain", "Germany"], label="Country", value="France")
            gender = gr.Dropdown(["Female", "Male"], label="Gender", value="Female")
        with gr.Row():
            age = gr.Number(label="Age", value=42)
            tenure = gr.Number(label="Tenure (years)", value=3)
            balance = gr.Number(label="Balance", value=50000)
        with gr.Row():
            products_number = gr.Number(label="Products", value=2, precision=0)
            credit_card = gr.Radio([0, 1], label="Credit card", value=1)
            active_member = gr.Radio([0, 1], label="Active member", value=1)
        estimated_salary = gr.Number(label="Estimated salary", value=100000)
        output = gr.Markdown()
        btn = gr.Button("Predict churn", variant="primary")
        btn.click(
            predict_via_api,
            inputs=[
                credit_score,
                country,
                gender,
                age,
                tenure,
                balance,
                products_number,
                credit_card,
                active_member,
                estimated_salary,
            ],
            outputs=output,
        )
    demo.launch(server_name="0.0.0.0", server_port=7861)


if __name__ == "__main__":
    main()
