# Student Academic Performance Prediction & Analysis

## Project Overview

This project analyzes student academic factors and uses Machine Learning
to predict student performance categories.

The project demonstrates an end-to-end Data Science workflow including:

- Data generation
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Data visualization
- Machine Learning model training
- Model evaluation
- Feature importance analysis
- Model saving and loading
- Student performance prediction

> **Dataset Note:** The dataset used in this project is synthetically
> generated for educational and demonstration purposes. It does not
> represent real student records.

---

## Objectives

The main objectives of this project are:

1. Analyze factors related to student academic performance.
2. Visualize relationships between academic variables.
3. Train multiple Machine Learning classification models.
4. Compare model performance.
5. Identify important predictive features.
6. Build a reusable student performance prediction system.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Joblib
- Git & GitHub

---

## Dataset

The project contains 1,000 synthetically generated student records.

### Features

| Feature | Description |
|---|---|
| study_hours | Average study hours per day |
| attendance_percent | Student attendance percentage |
| previous_score | Previous academic score |
| sleep_hours | Average sleep hours |
| assignment_score | Assignment performance score |
| extracurricular_hours | Extracurricular activity hours |
| internet_access | Availability of internet access |
| parental_education | Parent's education level |
| final_score | Final academic score |
| performance_category | Low, Medium, or High |

---

## Exploratory Data Analysis

The project includes analysis of:

- Student performance categories
- Study hours vs final score
- Attendance vs final score
- Correlation between numerical features

Visualizations are stored in the `visualizations/` directory.

---

## Machine Learning Models

Three classification algorithms were trained and evaluated:

1. Logistic Regression
2. Decision Tree
3. Random Forest

### Model Accuracy

| Model | Accuracy |
|---|---:|
| Logistic Regression | 77.50% |
| Decision Tree | 64.50% |
| Random Forest | 74.50% |

The reported accuracy values are based on the project's 80/20 train-test split
with `random_state=42`.

The Logistic Regression model achieved the highest test accuracy among the
three models in this experiment and was saved for the prediction system.

---

## Feature Importance

Random Forest feature importance was used to examine which input variables
contributed most strongly to the model's predictions.

The feature importance visualization is available in:

`visualizations/feature_importance.png`

---

## Prediction System

A standalone Python script is included to make predictions for a new student.

Run:

```bash
python src\predict_student.py