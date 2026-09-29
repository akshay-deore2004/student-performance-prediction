Student Performance Prediction
📌 Project Overview

Student Performance Prediction is a Machine Learning project that predicts a student's academic performance based on different academic, lifestyle, and background factors.

The project uses Logistic Regression to classify student performance from the provided input features.

🎯 Objective

The main objective of this project is to use Machine Learning to predict student academic performance and understand how different factors such as study hours, attendance, previous scores, sleep, assignments, extracurricular activities, internet access, and parental education can be associated with academic outcomes.

✨ Features
Predicts student academic performance
Takes student information as input
Uses a trained Machine Learning model
Handles categorical features using Label Encoding
Provides predictions through a Python script
Stores the trained model for future predictions
📊 Input Features

The prediction system uses the following features:

Feature	Description
Study Hours	Average study hours per day
Attendance	Student attendance percentage
Previous Score	Previous academic score
Sleep Hours	Average sleep hours per day
Assignment Score	Assignment performance score
Extracurricular Hours	Time spent on extracurricular activities
Internet Access	Whether the student has internet access
Parental Education	Educational background of the parents
🤖 Machine Learning Model

The project uses:

Logistic Regression

Logistic Regression is a supervised Machine Learning classification algorithm used to predict the class/category of a target variable.

🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Joblib
Jupyter Notebook
Git & GitHub
📁 Project Structure
student-performance-prediction/
│
├── data/
│   └── student_data.csv
│
├── model/
│   └── logistic_regression_model.pkl
│
├── notebooks/
│
├── src/
│   └── predict_student.py
│
├── visualizations/
│
├── venv/
│
├── student-performance-prediction.ipynb
├── predict-student.py
├── README.md
└── requirements.txt
▶️ How to Run the Project
1. Open the project in VS Code

Open the student-performance-prediction folder in Visual Studio Code.

2. Install the required libraries

Open the terminal and run:

pip install -r requirements.txt
3. Run the prediction program

You can run the program using:

python src/predict_student.py

If the virtual environment is not activated in PowerShell, you can run:

.\venv\Scripts\python.exe src\predict_student.py
4. Enter student information

The program will ask for:

Enter study hours per day:
Enter attendance percentage:
Enter previous score:
Enter average sleep hours:
Enter assignment score:
Enter extracurricular hours per day:
Internet access (Yes/No):
Parental education:

After entering the information, the model will display the predicted performance.

🧪 Example

Example input:

Study hours per day: 8
Attendance percentage: 90
Previous score: 85
Average sleep hours: 7
Assignment score: 90
Extracurricular hours per day: 2
Internet access: Yes
Parental education: Graduate

Example output:

Predicted Performance: High
📈 Future Improvements

The project can be further improved by:

Adding more Machine Learning algorithms
Comparing model performance
Adding model evaluation metrics
Creating a graphical user interface
Developing a web application using Streamlit
Adding interactive data visualizations
Improving input validation
Deploying the prediction application online