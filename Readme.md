# 🎓 Student Performance Prediction

A machine learning regression pipeline designed to predict a student’s final academic grade (**G3**) based on personal, social, and economic factors.  

This project covers the complete workflow—from **data analysis and modeling** to a **live interactive web dashboard**.

- **Project Duration**: June 2025 – July 2025  

---

## 📌 Project Overview

Academic performance is influenced by multiple factors beyond study time. This project analyzes how variables like:

- Parental education  
- Health  
- Internet access  
- Past failures  

impact final grades.

Using regression models, the system helps:
- Identify **at-risk students early**  
- Understand key drivers of academic success  

---

## 🛠️ Tech Stack

- **Language**: Python 3.12  

- **Data Science**:
  - `pandas`, `numpy`, `scikit-learn`  

- **Modeling**:
  - Linear Regression  
  - Random Forest Regressor  

- **Deployment**:
  - Streamlit (Web Dashboard)  
  - joblib (Model Serialization)  

---

## 📊 Data Features

The model is trained on the **UCI Student Alcohol Consumption dataset**.

### Key Features:

- **Study Time** → Weekly study hours (1–4)  
- **Absences** → Number of school absences (0–93)  
- **Parent Education** → Combined metric of parents’ education levels  
- **Health** → Scale from 1 (low) to 5 (high)  
- **Failures** → Number of past class failures  
- **Internet Access** → Binary (Yes/No)  

---

## 🚀 The Pipeline

### 1️⃣ Data Analysis & Modeling (`analysis.py`)

#### 🔹 Feature Engineering
- Created `parent_edu` as a combined metric  
- Encoded categorical features (e.g., internet access)  

#### 🔹 Models Used
- **Linear Regression**  
  - Baseline model for identifying linear relationships  

- **Random Forest Regressor**  
  - Captures non-linear interactions between features  

#### 🔹 Evaluation
- **K-Fold Cross Validation** → Ensures model stability  
- **RMSE (Root Mean Squared Error)** → Measures prediction accuracy  

---

### 2️⃣ Live Prediction Dashboard (`app.py`)

A **Streamlit-based web application** that allows:

- Interactive input via sliders and dropdowns  
- Instant prediction of student grades  
- Visualization of how different factors influence outcomes  

---

## 📈 Performance & Results

- **Random Forest Regressor** outperformed Linear Regression  
  - Better at capturing complex dependencies  

### 🔍 Key Insights

- **Past Failures** → Strongest negative predictor  
- **Absences** → Significant negative impact  
- **Parental Education** → Positive correlation with performance  

---

## 📂 File Structure

```
├── analysis.py           # Data analysis & model training
├── app.py                # Streamlit dashboard
├── model.pkl             # Saved trained model (joblib)
├── data/                 # Dataset files
└── README.md
```

---

## ⚙️ How to Run

### 1. Install Dependencies
```bash
pip install pandas numpy scikit-learn streamlit joblib
```

---

### 2. Train the Model
```bash
python analysis.py
```

---

### 3. Launch the Dashboard
```bash
streamlit run app.py
```

---

## 🧠 Summary

This project demonstrates:

- End-to-end regression pipeline  
- Feature engineering and model comparison  
- Model evaluation using cross-validation  
- Deployment using an interactive web interface  
- Real-world application of ML in education analytics  

---

## 📌 Note

This project highlights how machine learning can be used to **predict academic outcomes** and provide actionable insights for improving student performance.