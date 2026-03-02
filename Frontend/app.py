import streamlit as st
import requests
import datetime
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Inventory Dashboard", layout="wide")

st.title("📦 Smart Inventory Demand Planner")

# Sidebar for inputs
st.sidebar.header("User Inputs")
store_id = st.sidebar.number_input("Store ID", min_value=1, value=1)
item_id = st.sidebar.number_input("Item ID", min_value=1, value=1)
target_date = st.sidebar.date_input("Forecast Date", datetime.date(2026, 3, 1))

# Memory inputs in the main area
col1, col2, col3 = st.columns(3)
with col1:
    lag_7 = st.number_input("Sales 7 Days Ago", value=20.0)
with col2:
    lag_30 = st.number_input("Sales 30 Days Ago", value=22.0)
with col3:
    roll_7 = st.number_input("7-Day Avg", value=19.5)

if st.button("Generate Forecast", width="stretch"):
    payload = {
        "store": store_id, "item": item_id, 
        "dayofweek": target_date.weekday(), "month": target_date.month, "year": target_date.year,
        "sales_lag_7": lag_7, "sales_lag_14": 18.0, "sales_lag_30": lag_30, "rolling_mean_7": roll_7
    }
    
    try:
        # Connect to the Backend running on port 8001
        response = requests.post("http://127.0.0.1:8001/predict", json=payload)
        
        if response.status_code == 200:
            prediction = response.json()['forecasted_sales']
            
            # --- ASSIGNING VALUES TO THE INVENTORY PLAN ---
            st.divider()
            col_a, col_b = st.columns(2)
            
            with col_a:
                st.metric(label="📊 Predicted Demand", value=f"{prediction:.2f} Units")
            
            with col_b:
                # Calculating suggested stock based on 20% safety buffer
                suggested_stock = prediction * 1.20
                st.metric(label="🛒 Suggested Inventory Level", value=f"{int(suggested_stock)} Units")

            # Add a visual trend
            chart_data = pd.DataFrame({
                'Day': ['7 Days Ago', 'Today (Estimated)', 'Forecast'],
                'Sales': [lag_7, roll_7, prediction]
            })
            fig = px.line(chart_data, x='Day', y='Sales', title="Demand Trend Analysis", markers=True)
            st.plotly_chart(fig, width="stretch")
            
            # Actionable Plan
            st.info(f"**Inventory Plan:** Based on a forecast of {prediction:.2f} units, your optimal order quantity is {int(suggested_stock)} units to maintain a 20% safety buffer.")
            
        else:
            st.error(f"Backend returned an error: {response.text}")
            
    except Exception as e:
        st.error(f"Backend Connection Failed: {e}")