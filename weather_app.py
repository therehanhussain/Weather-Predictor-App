import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
import random

st.set_page_config(page_title="☁️ Weather Predictor", layout="centered")

cloudy_bg = """
<style>
body {
    background: linear-gradient(to top, #d7e1ec, #f0f4f8);
    font-family: 'Segoe UI', sans-serif;
}
.stApp {
    background: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80');
    background-size: cover;
    background-attachment: fixed;
}
h1, h2, h3 {
    color: #2c3e50;
}
.stSidebar {
    background-color: rgba(255, 255, 255, 0.85);
}
</style>
"""
st.markdown(cloudy_bg, unsafe_allow_html=True)

st.title("☁️ Cloudy Weather Predictor")
st.markdown("Welcome to your **mock weather forecast app**, designed with a soft cloudy aesthetic ☁️✨")

st.sidebar.header("📍 Location & Date")
city = st.sidebar.selectbox("Select City", ["New York", "London", "Tokyo", "Mumbai", "Sydney"])
date = st.sidebar.date_input("Select Date", value=datetime.today())

random.seed(hash(city + str(date)))
temp = round(random.uniform(15, 35), 1)
humidity = round(random.uniform(30, 90), 1)
condition = random.choice(["☀️ Sunny", "⛅ Partly Cloudy", "☁️ Cloudy", "🌧️ Rainy", "⛈️ Stormy"])

st.markdown(f"### 📅 Forecast for **{city}** on **{date.strftime('%A, %B %d, %Y')}**")
col1, col2, col3 = st.columns(3)
col1.metric("🌡️ Temperature", f"{temp} °C")
col2.metric("💧 Humidity", f"{humidity} %")
col3.metric("🌤️ Condition", condition)

st.markdown("### 📈 Last Week Temperature Trends (Mock)")
dates = pd.date_range(end=date, periods=7)
temps = [round(temp + random.uniform(-3, 3), 1) for _ in range(7)]
df = pd.DataFrame({'Date': dates, 'Temperature (°C)': temps})
df.set_index('Date', inplace=True)
st.line_chart(df)

st.markdown("---")
st.caption("🔍 Note: This is a **demo app** using randomly generated data. Designed for UI showcase and fun!")

