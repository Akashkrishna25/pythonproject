
from pathlib import Path
from contextlib import asynccontextmanager

import joblib
import pandas as pd

from fastapi import FastAPI, HTTPException

from api.schemas import (
    CustomerInput,
    PredictionOutput
)

ROOT = Path(__file__).resolve().parents[1]

MODEL_PATH = (
    ROOT / "models" / "churn_model.joblib"
)


@asynccontextmanager
async def lifespan(app: FastAPI):

    app.state.artifact = (
        joblib.load(MODEL_PATH)
    )

    yield


app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/")
def home():

    return {
        "message": "Customer Churn Prediction API"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.get("/model-info")
def model_info():

    artifact = app.state.artifact

    return {
        "model": artifact["model_name"],
        "version": artifact["version"],
        "features": artifact["features"],
        "threshold": artifact["threshold"]
    }


@app.post(
    "/predict",
    response_model=PredictionOutput
)
def predict(customer: CustomerInput):

    artifact = app.state.artifact

    model = artifact["model"]

    threshold = artifact["threshold"]

    data = pd.DataFrame([
        customer.model_dump()
    ])

    data = data[artifact["features"]]

    try:

        probability = float(
            model.predict_proba(data)[0, 1]
        )

        prediction = int(
            probability >= threshold
        )

        return PredictionOutput(
            prediction=prediction,
            churn_probability=probability,
            threshold=threshold,
            model_version=artifact["version"]
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Prediction failed"
        )
