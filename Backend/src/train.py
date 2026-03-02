import os
import pandas as pd
import joblib
from xgboost import XGBRegressor
from features import generate_features

# Get absolute path to Backend folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run_training():
    data_path = os.path.join(BASE_DIR, 'Data', 'train (1).csv')
    model_path = os.path.join(BASE_DIR, 'models', 'inventory_model.pkl')

    print(f"Loading data from: {data_path}")
    df = pd.read_csv(data_path)
    
    print("Preprocessing...")
    df_processed = generate_features(df)
    
    X = df_processed.drop(['sales', 'date'], axis=1)
    y = df_processed['sales']
    
    print("Training XGBoost...")
    model = XGBRegressor(n_estimators=100)
    model.fit(X, y)
    
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print(f"Done! Model saved at {model_path}")

if __name__ == "__main__":
    run_training()