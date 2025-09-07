import streamlit as st
import joblib
import numpy as np
import os

# Load model
MODEL_PATH = os.path.join("models", "diabetes_model.pkl")
model = joblib.load(MODEL_PATH)

st.title("🩺 Diabetes Progression Prediction")
st.write("Enter patient health details to predict disease progression score.")

# Input fields
age = st.number_input("Age (standardized)", -0.2, 0.2, 0.0, step=0.01)
sex = st.selectbox("Sex", [0, 1])
bmi = st.slider("BMI (standardized)", -0.2, 0.2, 0.0, step=0.01)
bp = st.slider("Blood Pressure (standardized)", -0.2, 0.2, 0.0, step=0.01)
s1 = st.number_input("S1 (Cholesterol)", -0.2, 0.2, 0.0, step=0.01)
s2 = st.number_input("S2 (LDL)", -0.2, 0.2, 0.0, step=0.01)
s3 = st.number_input("S3 (HDL)", -0.2, 0.2, 0.0, step=0.01)
s4 = st.number_input("S4 (Cholesterol/HDL ratio)", -0.2, 0.2, 0.0, step=0.01)
s5 = st.number_input("S5 (log triglycerides)", -0.2, 0.2, 0.0, step=0.01)
s6 = st.number_input("S6 (blood sugar)", -0.2, 0.2, 0.0, step=0.01)

# Prediction
if st.button("Predict"):
    features = np.array([[age, sex, bmi, bp, s1, s2, s3, s4, s5, s6]])
    prediction = model.predict(features)[0]
    st.success(f"Predicted diabetes progression score: **{prediction:.2f}**")
