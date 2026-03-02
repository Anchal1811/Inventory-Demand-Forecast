import sys
import os
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# --- PATH AUTO-FIX ---
# This ensures 'api' can see 'src' and 'models'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# Now we can import from src
from src.features import generate_features

app = FastAPI(title="Inventory Demand API")

MODEL_PATH = os.path.join(BASE_DIR, 'models', 'inventory_model.pkl')

class PredictionInput(BaseModel):
    store: int
    item: int
    dayofweek: int
    month: int
    year: int
    sales_lag_7: float
    sales_lag_14: float
    sales_lag_30: float
    rolling_mean_7: float

@app.get("/")
def home():
    return {"status": "Backend is Running"}

@app.post("/predict")
def predict_demand(data: PredictionInput):
    if not os.path.exists(MODEL_PATH):
        raise HTTPException(status_code=500, detail=f"Model file not found at {MODEL_PATH}")
    
    model = joblib.load(MODEL_PATH)
    input_df = pd.DataFrame([data.dict()])
    
    # Ensure columns match what the model expects
    prediction = model.predict(input_df)
    return {"forecasted_sales": round(float(prediction[0]), 2)}