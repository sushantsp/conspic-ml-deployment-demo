 
import os
import joblib
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Paths
MODEL_DIR = os.path.join("models")
MODEL_PATH = os.path.join(MODEL_DIR, "diabetes_model.pkl")

def main():
    # Load dataset
    diabetes = load_diabetes(as_frame=True)
    X = diabetes.data
    y = diabetes.target

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    score = r2_score(y_test, y_pred)
    print(f"Model R² score: {score:.4f}")

    # Ensure models/ directory exists
    os.makedirs(MODEL_DIR, exist_ok=True)

    # Save model
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved at {MODEL_PATH}")

if __name__ == "__main__":
    main()
