# Purpose: smoke-test FastAPI endpoint using TestClient (no server run required).

# This imports your FastAPI app directly and uses TestClient — no running server required in CI.

# Make sure app/fastapi_app.py imports models/diabetes_model.pkl using a relative path as in the earlier code (so tests can import the module).

import json
import os
import sys
import pytest

from fastapi.testclient import TestClient

# import app from your fastapi module
from app.fastapi_app import app

client = TestClient(app)

valid_input = {
    "age": 0.0381,
    "sex": 0.0507,
    "bmi": 0.0617,
    "bp": 0.0219,
    "s1": -0.0442,
    "s2": -0.0348,
    "s3": -0.0434,
    "s4": -0.0026,
    "s5": 0.0199,
    "s6": -0.0176
}

def test_root():
    res = client.get("/")
    assert res.status_code == 200
    assert "message" in res.json()

def test_predict_valid():
    res = client.post("/predict", json=valid_input)
    assert res.status_code == 200
    data = res.json()
    assert "prediction" in data
    assert isinstance(data["prediction"], (int, float))

def test_predict_invalid():
    res = client.post("/predict", json={"age": "bad"})
    assert res.status_code in (422, 400)
