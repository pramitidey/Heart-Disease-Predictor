import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('heart_model.pkl')

st.set_page_config(page_title="Heart Disease Predictor", layout="centered")
st.title("❤️ Heart Disease Prediction App")
st.markdown("Predict whether someone has heart disease based on medical input data.")

# Input fields
age = st.number_input("Age", 1, 120)

# Sex input as dropdown
sex = st.selectbox("Sex", ["Female", "Male"])  # display options
sex_val = 1 if sex == "Male" else 0            # convert to numeric
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", 80, 400)
chol = st.number_input("Serum Cholesterol in mg/dl (chol)", 100, 600)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
restecg = st.selectbox("Resting ECG (restecg)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved (thalach)", 60, 250)
exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.number_input("ST depression (oldpeak)", 0.0, 6.0, step=0.1)
slope = st.selectbox("Slope of ST segment (slope)", [0, 1, 2])
ca = st.selectbox("Major vessels colored (ca)", [0, 1, 2, 3])
thal = st.selectbox("Thal", [0, 1, 2, 3])

# Convert categorical input
sex_val = 1 if sex == "Male" else 0

# Prepare input array
input_data = np.array([[age, sex_val, cp, trestbps, chol, fbs, restecg,
                        thalach, exang, oldpeak, slope, ca, thal]])

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("🚨 High Risk: Likely to have Heart Disease.")
    else:
        st.success("✅ Low Risk: Unlikely to have Heart Disease.")
