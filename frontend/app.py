
import os
import requests
import streamlit as st

API_URL = os.getenv(
    "API_URL",
    "http://localhost:8000"
)

st.set_page_config(
    page_title="Customer Churn Intelligence",
    layout="wide"
)

st.title("Customer Churn Intelligence")

st.write(
    "Machine Learning-powered customer "
    "retention dashboard"
)

with st.form("customer_form"):

    col1, col2 = st.columns(2)

    with col1:

        tenure = st.slider(
            "Tenure in months",
            0, 72, 12
        )

        monthly_charges = st.number_input(
            "Monthly Charges",
            min_value=0.0,
            value=85.0
        )

        total_charges = st.number_input(
            "Total Charges",
            min_value=0.0,
            value=1020.0
        )

    with col2:

        contract = st.selectbox(
            "Contract",
            [
                "Month-to-month",
                "One year",
                "Two year"
            ]
        )

        internet = st.selectbox(
            "Internet Service",
            [
                "DSL",
                "Fiber optic",
                "No"
            ]
        )

        support = st.selectbox(
            "Technical Support",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

    submitted = st.form_submit_button(
        "Predict Customer Churn"
    )

if submitted:

    payload = {
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "Contract": contract,
        "InternetService": internet,
        "TechSupport": support
    }

    try:

        response = requests.post(
            f"{API_URL}/predict",
            json=payload,
            timeout=10
        )

        response.raise_for_status()

        result = response.json()

        probability = result[
            "churn_probability"
        ]

        col1, col2 = st.columns(2)

        col1.metric(
            "Estimated Churn Probability",
            f"{probability:.2%}"
        )

        col2.metric(
            "Model Version",
            result["model_version"]
        )

        st.progress(
            float(probability)
        )

        if result["prediction"] == 1:

            st.warning(
                "Customer flagged for "
                "retention review"
            )

        else:

            st.success(
                "Customer not flagged"
            )

    except requests.RequestException:

        st.error(
            "Unable to connect to the prediction API"
        )
