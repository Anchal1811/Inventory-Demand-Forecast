# 📦 SmartStock AI
### Intelligent Inventory Demand Forecasting


### Main Interface
![Inventory Dashboard](./screenshots/inventory.png)

### Demand Forecast Analysis
![Forecast Chart](./screenshots/forecast.png)

## 🚀 Features
* **Real-time Predictions:** Uses a trained XGBoost model to forecast sales.
* **Interactive Dashboard:** Built with Streamlit for easy data input and visualization.
* **FastAPI Backend:** A robust API that serves model predictions on port 8001.
* **Trend Analysis:** Visualizes historical vs. forecasted data using Plotly.

## 🛠️ Installation & Setup
1. **Clone the repo:** `git clone https://github.com/YOUR_USERNAME/SmartStock-AI.git`
2. **Backend:** - `cd Backend`
   - `uvicorn api.main:app --port 8001`
3. **Frontend:**
   - `cd Frontend`
   - `streamlit run app.py --server.port 8502`
