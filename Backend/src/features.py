import pandas as pd
import numpy as np

def generate_features(df):
    """
    Standardizes feature engineering for both training and inference.
    """
    df = df.copy()
    # Convert date and sort
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values(['store', 'item', 'date'])

        # Time-based features
        df['dayofweek'] = df['date'].dt.dayofweek
        df['month'] = df['date'].dt.month
        df['year'] = df['date'].dt.year

    # Lag Features (Past performance)
    for lag in [7, 14, 30]:
        df[f'sales_lag_{lag}'] = df.groupby(['store', 'item'])['sales'].shift(lag)

    # Rolling Mean (Recent trend)
    df['rolling_mean_7'] = (df.groupby(['store', 'item'])['sales_lag_7']
                            .transform(lambda x: x.rolling(window=7).mean()))

    return df.dropna()