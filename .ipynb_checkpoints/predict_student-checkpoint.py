import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

# Number of students
n = 1000

# Generate student-related data
study_hours = np.clip(np.random.normal(5.5, 2.0, n), 0.5, 10)

attendance = np.clip(
    np.random.normal(78, 12, n),
    40,
    100
)

previous_score = np.clip(
    np.random.normal(68, 14, n),
    30,
    100
)

sleep_hours = np.clip(
    np.random.normal(7, 1.2, n),
    4,
    10
)

assignment_score = np.clip(
    np.random.normal(72, 15, n),
    20,
    100
)

extracurricular_hours = np.clip(
    np.random.normal(3, 2, n),
    0,
    10
)

internet_access = np.random.choice(
    ["Yes", "No"],
    n,
    p=[0.9, 0.1]
)

parental_education = np.random.choice(
    ["High School", "Diploma", "Graduate", "Postgraduate"],
    n,
    p=[0.25, 0.20, 0.40, 0.15]
)

# Convert parental education into a numerical contribution
parental_bonus = pd.Series(parental_education).map({
    "High School": 0,
    "Diploma": 1,
    "Graduate": 2,
    "Postgraduate": 3
}).values

internet_bonus = (internet_access == "Yes") * 2

# Random variation
noise = np.random.normal(0, 6, n)

# Generate final score
final_score = (
    0.18 * study_hours * 10
    + 0.28 * attendance
    + 0.22 * previous_score
    + 0.10 * sleep_hours * 10
    + 0.20 * assignment_score
    + 0.05 * extracurricular_hours * 10
    + internet_bonus
    + parental_bonus
    + noise
)

final_score = np.clip(final_score, 0, 100)

# Create performance categories
performance_category = pd.cut(
    final_score,
    bins=[-np.inf, 55, 75, np.inf],
    labels=["Low", "Medium", "High"]
)

# Create DataFrame
df = pd.DataFrame({
    "study_hours": np.round(study_hours, 2),
    "attendance_percent": np.round(attendance, 1),
    "previous_score": np.round(previous_score, 1),
    "sleep_hours": np.round(sleep_hours, 1),
    "assignment_score": np.round(assignment_score, 1),
    "extracurricular_hours": np.round(extracurricular_hours, 1),
    "internet_access": internet_access,
    "parental_education": parental_education,
    "final_score": np.round(final_score, 1),
    "performance_category": performance_category
})

# Save dataset
df.to_csv("data/student_data.csv", index=False)

print("Dataset created successfully!")
print("Number of records:", len(df))
print("Dataset saved to: data/student_data.csv")