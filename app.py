import streamlit as st
import pandas as pd
import joblib


model = joblib.load("disease_prediction_model.pkl")


st.set_page_config(
    page_title="Disease Prediction System",
    page_icon="🏥",
    layout="centered"
)
st.title("🏥 Disease Prediction System")
st.subheader("Machine Learning Based Health Prediction")

st.write("Enter Patient Details")
st.divider()


name = st.text_input("Patient Name")


age = st.number_input(
    "Age",
    min_value=0,
    max_value=100,
    value=21,
    step=1
)


gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)


bmi = st.number_input(
    "BMI",
    min_value=0.0,
    max_value=100.0,
    value=25.0,
    step=0.1
)


bp = st.number_input(
    "Blood Pressure (mmHg)",
    min_value=50,
    max_value=250,
    value=120,
    step=1
)


cholesterol = st.number_input(
    "Cholesterol (mg/dL)",
    min_value=50,
    max_value=500,
    value=200,
    step=1
)


glucose = st.number_input(
    "Glucose (mg/dL)",
    min_value=40,
    max_value=300,
    value=100,
    step=1
)


heart_rate = st.number_input(
    "Heart Rate (bpm)",
    min_value=30,
    max_value=220,
    value=75,
    step=1
)

smoking = st.selectbox(
    "Smoking",
    ["No", "Yes"]
)


exercise = st.selectbox(
    "Exercise Level",
    ["Low", "Moderate", "High"]
)

st.divider()


if st.button("🔍 Predict Disease", use_container_width=True):

    if name.strip() == "":
        st.warning("Please enter Patient Name.")

    else:

    
        gender_value = 1 if gender == "Male" else 0
        smoking_value = 1 if smoking == "Yes" else 0

        if exercise == "Low":
            exercise_value = 0
        elif exercise == "Moderate":
            exercise_value = 1
        else:
            exercise_value = 2

    
        new_patient = pd.DataFrame({
            "Age": [age],
            "Gender": [gender_value],
            "BMI": [bmi],
            "Blood_Pressure_mmHg": [bp],
            "Cholesterol_mg_dL": [cholesterol],
            "Glucose_mg_dL": [glucose],
            "Heart_Rate_bpm": [heart_rate],
            "Smoking": [smoking_value],
            "Exercise_Level": [exercise_value]
        })

    
        prediction = model.predict(new_patient)[0]

        st.divider()
        st.subheader("Prediction Result")

        st.write("**Patient Name:**", name)

        if prediction == 1:
            st.error("⚠️ Disease")
        else:
            st.success("✅ No Disease")
