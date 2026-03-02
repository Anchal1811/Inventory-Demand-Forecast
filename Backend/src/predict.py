import joblib
import os
import pandas as pd

def test_single_prediction():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MODEL_PATH = os.path.join(BASE_DIR, 'models', 'inventory_model.pkl')

    if not os.path.exists(MODEL_PATH):
        print("Model file missing.")
        return

    model = joblib.load(MODEL_PATH)
    
    # Dummy data for Store 1, Item 1
    test_data = pd.DataFrame([{
        "store": 1, "item": 1, "dayofweek": 1, "month": 3, "year": 2026,
        "sales_lag_7": 20.0, "sales_lag_14": 18.0, "sales_lag_30": 22.0, "rolling_mean_7": 19.5
    }])
    
    pred = model.predict(test_data)
    print(f"Test Prediction for Store 1, Item 1: {pred[0]} units")

if __name__ == "__main__":
    test_single_prediction()