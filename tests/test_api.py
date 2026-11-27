
import pytest

from fastapi.testclient import TestClient
from api.main import app


@pytest.fixture
def client():

    with TestClient(app) as test_client:

        yield test_client


def test_health(client):

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"


def test_prediction(client):

    payload = {
        "tenure": 12,
        "MonthlyCharges": 85.0,
        "TotalCharges": 1020.0,
        "Contract": "Month-to-month",
        "InternetService": "Fiber optic",
        "TechSupport": "No"
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200

    result = response.json()

    assert result["prediction"] in [0, 1]

    assert 0 <= result["churn_probability"] <= 1


def test_invalid_input(client):

    response = client.post(
        "/predict",
        json={"tenure": -10}
    )

    assert response.status_code == 422


def test_model_info(client):

    response = client.get("/model-info")

    assert response.status_code == 200

    assert "version" in response.json()
