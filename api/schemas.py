
from typing import Literal
from pydantic import BaseModel, Field


class CustomerInput(BaseModel):

    tenure: int = Field(
        ge=0,
        le=120
    )

    MonthlyCharges: float = Field(
        ge=0,
        allow_inf_nan=False
    )

    TotalCharges: float = Field(
        ge=0,
        allow_inf_nan=False
    )

    Contract: Literal[
        "Month-to-month",
        "One year",
        "Two year"
    ]

    InternetService: Literal[
        "DSL",
        "Fiber optic",
        "No"
    ]

    TechSupport: Literal[
        "Yes",
        "No",
        "No internet service"
    ]


class PredictionOutput(BaseModel):

    prediction: int

    churn_probability: float

    threshold: float

    model_version: str
