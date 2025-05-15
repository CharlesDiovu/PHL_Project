import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("post-harvest-loss-app\data\merged_crop_climate_data.csv")
    
    # Convert risk score to numerical value
    risk_map = {"Low": 1, "Medium": 2, "High": 3}
    df["Risk_Num"] = df["Risk Score"].map(risk_map)
    
    return df

df = load_data()

st.set_page_config(layout="wide")
st.title("🔮 PHL Prediction Tool")

# Train model
@st.cache_resource
def train_model():
    X = df[["Avg Rainfall", "Avg Humidity", "Avg Temp", "Risk_Num"]]
    y = df["AVERAGE PHL (%)"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    
    return model, mae

model, mae = train_model()

st.write(f"Model MAE: {mae:.2f}%")

# Prediction form
st.header("Predict PHL for Your Farm")

col1, col2 = st.columns(2)

with col1:
    state = st.selectbox("State", options=df["State"].unique())
    crop = st.selectbox("Crop", options=df["Crop"].unique())
    
with col2:
    rainfall = st.slider("Average Rainfall (mm)", min_value=0, max_value=300, value=100)
    temp = st.slider("Average Temperature (°C)", min_value=20, max_value=35, value=25)

humidity = st.slider("Average Humidity (%)", min_value=30, max_value=100, value=70)
risk_level = st.selectbox("Risk Level", options=["Low", "Medium", "High"])

# Map risk level to numerical value
risk_map = {"Low": 1, "Medium": 2, "High": 3}
risk_num = risk_map[risk_level]

# Make prediction
if st.button("Predict PHL"):
    input_data = [[rainfall, humidity, temp, risk_num]]
    prediction = model.predict(input_data)[0]
    
    st.success(f"Predicted Post-Harvest Loss: {prediction:.1f}%")
    
    # Recommendations based on prediction
    st.subheader("Recommendations to Reduce Losses")
    
    if prediction > 40:
        st.warning("High Risk Detected! Consider these urgent actions:")
        st.markdown("""
        - Invest in cold storage facilities
        - Use improved packaging materials
        - Arrange for immediate transportation to markets
        - Consider processing into shelf-stable products
        """)
    elif prediction > 25:
        st.info("Moderate Risk Detected. Recommended actions:")
        st.markdown("""
        - Improve storage conditions
        - Coordinate with buyers before harvest
        - Use proper harvesting techniques
        - Monitor climate conditions closely
        """)
    else:
        st.success("Low Risk Detected. Maintain these best practices:")
        st.markdown("""
        - Continue current good practices
        - Regularly inspect storage facilities
        - Maintain relationships with buyers
        - Stay informed about market conditions
        """)
