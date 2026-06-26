"""Serve entry point implementation for MLproject.

You don't run this file yourself. From the repo root, after notebook 02:

    mlflow run . -e serve

Tweak the defaults if you need to:

    mlflow run . -e serve -P port=5002 -P alias=champion

MLproject calls this script under the hood. Gradio (app/gradio_ui.py) expects the
server on http://127.0.0.1:5001/invocations unless you set MLFLOW_SERVE_URL.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from mlflow.models.flavor_backend_registry import get_flavor_backend
from mlflow.utils import env_manager as EnvManager

DEMO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(DEMO_ROOT))

from src.config import CHAMPION_ALIAS, MODEL_NAME, build_model_uri


def main():
    parser = argparse.ArgumentParser(description="Start MLflow model server for a registered model.")
    parser.add_argument("--model-name", default=MODEL_NAME)
    parser.add_argument("--alias", default=None)
    parser.add_argument("--version", type=int, default=None)
    parser.add_argument("--port", type=int, default=5001)
    parser.add_argument("--host", default="127.0.0.1")
    args = parser.parse_args()

    model_uri = build_model_uri(
        args.model_name,
        args.alias or CHAMPION_ALIAS,
        args.version,
    )
    print(f"Starting MLflow model server for {model_uri} on {args.host}:{args.port}")
    get_flavor_backend(model_uri, env_manager=EnvManager.LOCAL).serve(
        model_uri=model_uri,
        port=args.port,
        host=args.host,
        timeout=60,
    )


if __name__ == "__main__":
    main()
