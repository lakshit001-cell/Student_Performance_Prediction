import pandas as pd
import streamlit as st
import joblib


@st.cache_resource
def load_model():
    return joblib.load("student_model.pkl")

model=load_model()
st.title("STUDENT GRADE PREDICTOR")
study_time=st.slider("study time",1,4)
absences=st.slider("absences",0,30)
medu=st.slider("mother education",0,4)
fedu=st.slider("father education",0,4)
failures=st.slider("failures",0,4)
Health=st.slider("Health",1,5)
Ic=st.selectbox("Internet access",['yes','no'])
if Ic=="yes":
    insc=1
else:
    insc=0
pedu=medu+fedu

if st.button("Calculate grade"):
    features=[study_time,absences,pedu,Health,failures,insc]
    ff=[features]
    grade=model.predict(ff)
    st.write(grade[0])





