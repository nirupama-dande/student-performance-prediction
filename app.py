
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Student Performance Prediction")

st.title("🎓 Student Performance Prediction")
st.write("Enter student details to predict the final grade.")

model = joblib.load("student_performance_model.pkl")

student_id = st.number_input("Student ID", min_value=0, value=1)
age = st.number_input("Age", min_value=10, max_value=30, value=18)
gender = st.selectbox("Gender", ["Option 0", "Option 1", "Option 2"])
school_type = st.selectbox("School Type", ["Option 0", "Option 1"])
parent_education = st.selectbox(
    "Parent Education",
    ["Option 0", "Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
)
study_hours = st.number_input("Study Hours", min_value=0.0, max_value=24.0, value=5.0)
attendance_percentage = st.number_input(
    "Attendance Percentage", min_value=0.0, max_value=100.0, value=80.0
)
internet_access = st.selectbox("Internet Access", ["Option 0", "Option 1"])
travel_time = st.selectbox(
    "Travel Time", ["Option 0", "Option 1", "Option 2", "Option 3"]
)
extra_activities = st.selectbox("Extra Activities", ["Option 0", "Option 1"])
study_method = st.selectbox(
    "Study Method",
    ["Option 0", "Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
)
math_score = st.number_input("Math Score", 0.0, 100.0, 70.0)
science_score = st.number_input("Science Score", 0.0, 100.0, 70.0)
english_score = st.number_input("English Score", 0.0, 100.0, 70.0)

if st.button("Predict Final Grade"):

    input_data = pd.DataFrame([{
        "student_id": student_id,
        "age": age,
        "gender": int(gender.split()[-1]),
        "school_type": int(school_type.split()[-1]),
        "parent_education": int(parent_education.split()[-1]),
        "study_hours": study_hours,
        "attendance_percentage": attendance_percentage,
        "internet_access": int(internet_access.split()[-1]),
        "travel_time": int(travel_time.split()[-1]),
        "extra_activities": int(extra_activities.split()[-1]),
        "study_method": int(study_method.split()[-1]),
        "math_score": math_score,
        "science_score": science_score,
        "english_score": english_score
    }])

    prediction = model.predict(input_data)

    st.success(f"🎯 Predicted Final Grade: {prediction[0]}")
