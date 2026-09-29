import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/student_data.csv")

# Load trained model
model = joblib.load("models/logistic_regression_model.pkl")

# Create encoders
internet_encoder = LabelEncoder()
parental_encoder = LabelEncoder()

internet_encoder.fit(df["internet_access"])
parental_encoder.fit(df["parental_education"])

print("======================================")
print(" Student Academic Performance Predictor")
print("======================================")

# Get student information
study_hours = float(input("Enter study hours per day: "))
attendance_percent = float(input("Enter attendance percentage: "))
previous_score = float(input("Enter previous score: "))
sleep_hours = float(input("Enter average sleep hours: "))
assignment_score = float(input("Enter assignment score: "))
extracurricular_hours = float(
    input("Enter extracurricular hours per day: ")
)

internet_access = input(
    "Internet access (Yes/No): "
).strip().title()

parental_education = input(
    "Parental education (Diploma/Graduate/High School/Postgraduate): "
).strip().title()

# Encode categorical values
internet_access_encoded = internet_encoder.transform(
    [internet_access]
)[0]

parental_education_encoded = parental_encoder.transform(
    [parental_education]
)[0]

# Prepare input data
student_data = [[
    study_hours,
    attendance_percent,
    previous_score,
    sleep_hours,
    assignment_score,
    extracurricular_hours,
    internet_access_encoded,
    parental_education_encoded
]]

# Make prediction
prediction = model.predict(student_data)

print("\n======================================")
print("Predicted Performance:", prediction[0])
print("======================================")