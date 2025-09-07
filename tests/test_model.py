import os
import joblib
import numpy as np

def test_model_loads_and_predicts():
    """
        This test uses a zero-vector sample; it only checks the model runs and returns something numeric/array-like.

        If your model file is located elsewhere adjust model_path.
    """
    model_path = os.path.join(os.path.dirname(__file__), "..", "models", "diabetes_model.pkl")
    model_path = os.path.abspath(model_path)
    assert os.path.exists(model_path), f"Model file not found at {model_path}"

    model = joblib.load(model_path)

    # Sample input (10 features)
    sample = np.zeros((1, 10))
    pred = model.predict(sample)
    assert hasattr(pred, "__len__") or isinstance(pred, (float, int, np.floating)), "Prediction has unexpected type"
