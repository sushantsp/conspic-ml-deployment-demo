# app/fastapi_app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
import joblib
import numpy as np
import os

# Load the trained model
MODEL_PATH = os.path.join("models", "diabetes_model.pkl")
model = joblib.load(MODEL_PATH)

# Define the request body schema
class DiabetesFeatures(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float

# Initialize FastAPI app
app = FastAPI(title="Diabetes Prediction API")

@app.get("/")
def read_root():
    return {"message": "Diabetes Prediction API is running!"}

@app.post("/predict")
def predict(features: DiabetesFeatures):
    try:
        # Convert input to numpy array
        data = np.array([
            [
                features.age,
                features.sex,
                features.bmi,
                features.bp,
                features.s1,
                features.s2,
                features.s3,
                features.s4,
                features.s5,
                features.s6
            ]
        ])

        # Make prediction
        prediction = model.predict(data)[0]

        return {"prediction": float(prediction)}

    except ValidationError as e:
        raise HTTPException(status_code=422, detail=f"Validation error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")