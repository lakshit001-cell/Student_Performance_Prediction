🎓 Student Performance Prediction
Machine Learning Regression Pipeline (June 2025 – July 2025)
This project predicts a student's final academic grade (G3) based on a variety of personal, social, and economic indicators. It features a complete pipeline from exploratory data analysis and regression modeling to a live interactive web dashboard.

📌 Project Overview
Academic success is influenced by more than just study hours. This project analyzes the impact of parental education, health, internet access, and past failures on final grades. By using regression techniques, we can identify "at-risk" students early and understand the primary drivers of academic success.

🛠️ Tech Stack
Language: Python 3.12

Data Science: pandas, numpy, scikit-learn

Modeling: Linear Regression, Random Forest Regressor

Deployment: Streamlit (Web UI), joblib (Model Serialization)

📊 Data Features
The model trained on the UCI Student Alcohol Consumption dataset, focusing on the following key features:

Study Time: Weekly study hours (1 to 4).

Absences: Number of school absences (0 to 93).

Parent Education: Combined metric of Mother's and Father's education levels.

Health: Current health status (1 to 5).

Failures: Number of past class failures.

Internet Access: Binary indicator of home internet access.

🚀 The Pipeline
1. Data Analysis (analysis.py)
Feature Engineering: Created a composite parent_edu feature to simplify the model and encoded categorical internet data.

Modeling: * Linear Regression: Baseline model for identifying linear trends.

Random Forest Regressor: Used for capturing non-linear interactions between social factors and grades.

Evaluation: Utilized K-Fold Cross-Validation and RMSE (Root Mean Squared Error) to ensure model stability and accuracy.

2. Live Prediction Dashboard (app.py)
A user-friendly Streamlit application that allows users to:

Input student data via interactive sliders and select-boxes.

Get instant grade predictions using the serialized Random Forest model.

Visualize the impact of different lifestyle choices on the predicted outcome.

📈 Performance & Results
Based on testing, the Random Forest Regressor outperformed simple Linear Regression due to its ability to handle complex feature dependencies.

Key Finding: Feature Importance analysis revealed that Past Failures and Absences were the strongest negative predictors of final academic performance, while Parental Education showed a significant positive correlation.

📂 File Structure
⚙️ How to Run
Install Dependencies:

Train the Model:

Launch the Dashboard: