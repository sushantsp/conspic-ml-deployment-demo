# test_api.py

import requests

BASE_URL = "http://127.0.0.1:8000"

# ✅ Valid input (from sklearn diabetes dataset)
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

# ❌ Invalid input (missing fields + wrong type)
invalid_input = {
    "age": "not_a_number",
    "sex": 1
}

def test_valid():
    print("\n--- Testing VALID request ---")
    response = requests.post(f"{BASE_URL}/predict", json=valid_input)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

def test_invalid():
    print("\n--- Testing INVALID request ---")
    response = requests.post(f"{BASE_URL}/predict", json=invalid_input)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

if __name__ == "__main__":
    test_valid()
    test_invalid()
