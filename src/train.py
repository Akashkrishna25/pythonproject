
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import (
    StandardScaler,
    OneHotEncoder
)
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from sklearn.model_selection import (
    train_test_split,
    StratifiedKFold,
    cross_val_score
)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    classification_report,
    roc_auc_score,
    average_precision_score,
    precision_recall_curve
)

ROOT = Path(__file__).resolve().parents[1]

FEATURES = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
    "Contract",
    "InternetService",
    "TechSupport"
]

NUMERIC = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges"
]

CATEGORICAL = [
    "Contract",
    "InternetService",
    "TechSupport"
]


def load_data():

    df = pd.read_csv(
        ROOT / "data" / "customers.csv"
    )

    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    df = df.drop_duplicates(
        subset=["customerID"]
    )

    X = df[FEATURES]

    y = df["Churn"].map({
        "Yes": 1,
        "No": 0
    })

    return X, y


def create_preprocessor():

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(
            strategy="median"
        )),
        ("scaler", StandardScaler())
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(
            strategy="most_frequent"
        )),
        ("encoder", OneHotEncoder(
            handle_unknown="ignore"
        ))
    ])

    return ColumnTransformer([
        ("numeric", numeric_pipeline, NUMERIC),
        ("categorical", categorical_pipeline,
         CATEGORICAL)
    ])


def train():

    X, y = load_data()

    X_dev, X_test, y_dev, y_test = train_test_split(
        X, y,
        test_size=0.2,
        stratify=y,
        random_state=42
    )

    X_train, X_val, y_train, y_val = train_test_split(
        X_dev, y_dev,
        test_size=0.25,
        stratify=y_dev,
        random_state=42
    )

    candidates = {

        "Logistic Regression":
            LogisticRegression(
                max_iter=2000,
                random_state=42
            ),

        "Random Forest":
            RandomForestClassifier(
                n_estimators=200,
                max_depth=10,
                random_state=42
            )
    }

    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )

    best_score = -np.inf
    best_model = None
    best_name = None

    for name, estimator in candidates.items():

        pipeline = Pipeline([
            ("preprocessor", create_preprocessor()),
            ("model", estimator)
        ])

        scores = cross_val_score(
            pipeline,
            X_train,
            y_train,
            cv=cv,
            scoring="roc_auc",
            n_jobs=-1
        )

        score = scores.mean()

        print(name, "CV ROC-AUC:", score)

        if score > best_score:

            best_score = score
            best_model = pipeline
            best_name = name

    best_model.fit(X_train, y_train)

    val_probs = best_model.predict_proba(
        X_val
    )[:, 1]

    precision, recall, thresholds = (
        precision_recall_curve(y_val, val_probs)
    )

    f1 = (
        2 * precision[:-1] * recall[:-1] /
        (precision[:-1] + recall[:-1] + 1e-12)
    )

    threshold = float(
        thresholds[np.argmax(f1)]
    )

    test_probs = best_model.predict_proba(
        X_test
    )[:, 1]

    predictions = (
        test_probs >= threshold
    ).astype(int)

    print("Best Model:", best_name)
    print("Threshold:", threshold)

    print("Test ROC-AUC:",
          roc_auc_score(y_test, test_probs))

    print("Average Precision:",
          average_precision_score(
              y_test, test_probs
          ))

    print(classification_report(
        y_test,
        predictions,
        zero_division=0
    ))

    artifact = {
        "model": best_model,
        "model_name": best_name,
        "threshold": threshold,
        "features": FEATURES,
        "version": "1.0.0"
    }

    model_dir = ROOT / "models"

    model_dir.mkdir(exist_ok=True)

    joblib.dump(
        artifact,
        model_dir / "churn_model.joblib"
    )

    print("Model saved successfully")


if __name__ == "__main__":
    train()
